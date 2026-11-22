#!/usr/bin/env python3
"""Fetch publication metadata and metrics from the NASA ADS / SciX API.

Reads SCIX_API_TOKEN (or ADS_DEV_KEY / ADS_API_TOKEN) from the environment,
~/.env, or ~/.ads/dev_key, queries the configured SciX library, and writes
structured JSON to _data/publications.json for Jekyll.
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

LIBRARY_ID = "hymVHtQ2TveZ5t3VzwQYzg"
ORCID_ID = "0000-0001-9592-4190"
API_BASE = "https://api.adsabs.harvard.edu/v1"
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "_data" / "publications.json"


def load_token() -> str:
    env_names = ("SCIX_API_TOKEN", "ADS_DEV_KEY", "ADS_API_TOKEN", "SCIX_TOKEN")
    for name in env_names:
        val = os.environ.get(name, "").strip()
        if val:
            return val

    for dotenv_path in (REPO_ROOT / ".env", Path.home() / ".env"):
        if dotenv_path.is_file():
            for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                if k in env_names:
                    v = v.strip().strip('"').strip("'")
                    if v:
                        return v

    ads_key = Path.home() / ".ads" / "dev_key"
    if ads_key.is_file():
        val = ads_key.read_text(encoding="utf-8").strip()
        if val:
            return val

    raise RuntimeError(
        "No SciX/ADS API token found. Set SCIX_API_TOKEN in ~/.env or the environment."
    )


def api_request(
    method: str,
    path: str,
    token: str,
    params: dict[str, Any] | None = None,
    body: bytes | None = None,
    content_type: str = "application/json",
) -> dict[str, Any]:
    url = f"{API_BASE}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if body is not None:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"ADS/SciX API HTTP {exc.code} on {path}: {detail}") from exc


def fetch_library(token: str, library_id: str) -> tuple[dict[str, Any], list[str]]:
    bibcodes: list[str] = []
    metadata: dict[str, Any] = {}
    start = 0
    rows = 500
    while True:
        data = api_request(
            "GET",
            f"/biblib/libraries/{library_id}",
            token,
            params={"start": start, "rows": rows},
        )
        if not metadata:
            metadata = data.get("metadata", {})
        batch = data.get("documents", [])
        bibcodes.extend(batch)
        total = int(metadata.get("num_documents", len(bibcodes)))
        if not batch or len(bibcodes) >= total:
            break
        start += len(batch)
    seen: set[str] = set()
    unique_bibcodes = []
    for b in bibcodes:
        if b not in seen:
            seen.add(b)
            unique_bibcodes.append(b)
    return metadata, unique_bibcodes


def fetch_documents(token: str, bibcodes: list[str]) -> list[dict[str, Any]]:
    fields = [
        "bibcode",
        "title",
        "author",
        "orcid_pub",
        "orcid_user",
        "orcid_other",
        "year",
        "pubdate",
        "pub",
        "bibstem",
        "volume",
        "issue",
        "page",
        "citation_count",
        "read_count",
        "property",
        "doctype",
        "arxiv_class",
        "identifier",
        "doi",
        "abstract",
        "keyword",
    ]
    payload = ("bibcode\n" + "\n".join(bibcodes)).encode("utf-8")
    data = api_request(
        "POST",
        "/search/bigquery",
        token,
        params={
            "q": "*:*",
            "fq": "{!bitset}",
            "rows": max(len(bibcodes) + 10, 500),
            "fl": ",".join(fields),
        },
        body=payload,
        content_type="big-query/csv",
    )
    return data.get("response", {}).get("docs", [])


def fetch_metrics(token: str, bibcodes: list[str]) -> dict[str, Any]:
    if not bibcodes:
        return {}
    body = json.dumps(
        {
            "bibcodes": bibcodes,
            "types": ["basic", "citations", "indicators", "histograms"],
        }
    ).encode("utf-8")
    return api_request("POST", "/metrics", token, body=body)


def find_author_position(doc: dict[str, Any]) -> tuple[int | None, str]:
    """Return (1-based author position, match_method) for Jiaxuan Li."""
    authors: list[str] = doc.get("author", []) or []

    for field in ("orcid_pub", "orcid_user", "orcid_other"):
        orcids = doc.get(field) or []
        for idx, oid in enumerate(orcids):
            if oid and oid.strip() == ORCID_ID:
                return idx + 1, f"orcid:{field}"

    for idx, name in enumerate(authors):
        norm = re.sub(r"\s+", " ", name.strip()).lower()
        if norm.startswith("li, jiaxuan") or norm == "jiaxuan li":
            return idx + 1, "name:exact"

    li_j_matches = []
    for idx, name in enumerate(authors):
        norm = re.sub(r"\s+", " ", name.strip()).lower()
        if re.match(r"^li,\s*j\.?(\s|$)", norm):
            li_j_matches.append(idx + 1)
    if len(li_j_matches) == 1:
        return li_j_matches[0], "name:initial"

    return None, "unmatched"


def extract_arxiv_id(doc: dict[str, Any]) -> str | None:
    for ident in doc.get("identifier") or []:
        if ident.lower().startswith("arxiv:"):
            return ident.split(":", 1)[1]
    bibcode = doc.get("bibcode", "")
    if "arXiv" in bibcode:
        m = re.search(r"arXiv(\d{4})(\d{5})", bibcode)
        if m:
            return f"{m.group(1)}.{m.group(2)}"
    return None


def clean_journal(doc: dict[str, Any]) -> str:
    bibstems = doc.get("bibstem") or []
    stem = bibstems[0] if bibstems else ""
    pub = doc.get("pub") or ""
    abbrev_map = {
        "ApJ": "ApJ",
        "ApJL": "ApJL",
        "ApJS": "ApJS",
        "AJ": "AJ",
        "MNRAS": "MNRAS",
        "A&A": "A&A",
        "Natur": "Nature",
        "NatAs": "Nature Astronomy",
        "Sci": "Science",
        "PASP": "PASP",
        "PASJ": "PASJ",
        "RNAAS": "RNAAS",
        "OJAp": "Open Journal of Astrophysics",
        "arXiv": "arXiv e-prints",
        "PhRvD": "Phys. Rev. D",
        "PhRvL": "Phys. Rev. Lett.",
        "JCAP": "JCAP",
        "A&ARv": "A&ARv",
        "ARA&A": "ARA&A",
        "BAAS": "BAAS",
        "AAS": "AAS Meeting",
        "PhDT": "Ph.D. Thesis",
        "MPEC": "MPEC",
        "zndo": "Zenodo",
    }
    if stem in abbrev_map:
        return abbrev_map[stem]
    return pub or stem or ""


def format_inline_latex(expr: str) -> str:
    """Convert common astrophysics inline LaTeX snippets to safe HTML."""
    replacements = {
        r"\alpha": "α",
        r"\beta": "β",
        r"\gamma": "γ",
        r"\delta": "δ",
        r"\lambda": "λ",
        r"\mu": "μ",
        r"\sigma": "σ",
        r"\odot": "⊙",
        r"\star": "★",
        r"\ast": "∗",
        r"\sim": "∼",
        r"\approx": "≈",
        r"\lesssim": "≲",
        r"\gtrsim": "≳",
        r"\pm": "±",
        r"\times": "×",
        r"\cdot": "·",
        r"\deg": "°",
        r"\circ": "°",
    }
    out = expr
    for src, dst in replacements.items():
        out = out.replace(src, dst)
    out = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", out)
    out = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", out)
    out = re.sub(r"\^([A-Za-z0-9+\-−*∗⊙])", r"<sup>\1</sup>", out)
    out = re.sub(r"_([A-Za-z0-9+\-−*∗⊙])", r"<sub>\1</sub>", out)
    return out


def _mml_to_html(elem: ET.Element) -> str:
    tag = elem.tag.split("}")[-1].lower()
    children = list(elem)
    if tag == "mspace":
        return " "
    if tag == "msub" and len(children) >= 2:
        return f"{_mml_to_html(children[0])}<sub>{_mml_to_html(children[1])}</sub>"
    if tag == "msup" and len(children) >= 2:
        return f"{_mml_to_html(children[0])}<sup>{_mml_to_html(children[1])}</sup>"
    if tag == "msubsup" and len(children) >= 3:
        return (
            f"{_mml_to_html(children[0])}"
            f"<sub>{_mml_to_html(children[1])}</sub>"
            f"<sup>{_mml_to_html(children[2])}</sup>"
        )
    if tag == "mover" and len(children) >= 1:
        return _mml_to_html(children[0])
    if tag == "mfrac" and len(children) >= 2:
        return f"({_mml_to_html(children[0])}/{_mml_to_html(children[1])})"
    parts = [html.escape((elem.text or "").strip(), quote=False)]
    for ch in children:
        parts.append(_mml_to_html(ch))
        if ch.tail and ch.tail.strip():
            parts.append(html.escape(ch.tail.strip(), quote=False))
    joined = "".join(parts)
    if tag == "mo" and joined in ("=", "<", ">", "≤", "≥", "∼", "≈", "±", "×", "+", "-", "−", "≍"):
        return f" {joined} "
    return joined


def _convert_inline_formula(match: re.Match[str]) -> str:
    block = match.group(0)
    # Remove XML namespaces so ElementTree parses <mml:...> cleanly
    cleaned = re.sub(r"<(/?)mml:", r"<\1", block)
    cleaned = re.sub(r'\s+xmlns(?::\w+)?="[^"]*"', "", cleaned)
    try:
        root = ET.fromstring(cleaned)
        rendered = _mml_to_html(root)
        return re.sub(r"\s+", " ", rendered).strip()
    except ET.ParseError:
        text = re.sub(r"<[^>]+>", " ", block)
        return html.escape(re.sub(r"\s+", " ", text).strip(), quote=False)


def format_abstract_html(raw_abstract: str) -> str:
    """Convert ADS/SciX abstract (with MathML, <SUB>/<SUP>, LaTeX) into clean safe HTML."""
    s = re.sub(r"\s+", " ", raw_abstract or "").strip()
    if not s:
        return ""
    s = s.replace("``", "“").replace("''", "”")

    tokens: list[tuple[str, str]] = []

    def stash(html_snippet: str) -> str:
        key = f"@@ABS{len(tokens)}@@"
        tokens.append((key, html_snippet))
        return key

    # 1. Convert <inline-formula>...</inline-formula> MathML blocks
    s = re.sub(
        r"<inline-formula>.*?</inline-formula>",
        lambda m: stash(_convert_inline_formula(m)),
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 2. Preserve safe inline HTML tags (<SUB>, <SUP>, <I>, <EM>)
    s = re.sub(
        r"<(/?)(sub|sup|i|em)>",
        lambda m: stash(f"<{m.group(1) or ''}{m.group(2).lower()}>"),
        s,
        flags=re.IGNORECASE,
    )

    s = html.unescape(s)
    escaped = html.escape(s, quote=False)

    # 3. Convert simple inline $...$ LaTeX expressions
    escaped = re.sub(r"\$([^$]+)\$", lambda m: format_inline_latex(m.group(1)), escaped)

    for key, snippet in tokens:
        escaped = escaped.replace(key, snippet)

    return re.sub(r"\s+", " ", escaped).strip()


def format_title(raw_title: str) -> tuple[str, str]:
    """Return (plain_text_title, safe_html_title) from an ADS title string."""
    s = re.sub(r"\s+", " ", raw_title).strip()
    # Preserve safe inline ADS tags before unescaping entities
    tag_tokens: list[tuple[str, str]] = []

    def stash_tag(match: re.Match[str]) -> str:
        slash = match.group(1) or ""
        tag = match.group(2).lower()
        key = f"@@TAG{len(tag_tokens)}@@"
        tag_tokens.append((key, f"<{slash}{tag}>"))
        return key

    s = re.sub(r"<(/?)(sub|sup|i|em)>", stash_tag, s, flags=re.IGNORECASE)
    s = html.unescape(s)
    escaped = html.escape(s, quote=False)

    # Convert simple inline $...$ LaTeX expressions to safe HTML
    def replace_math(match: re.Match[str]) -> str:
        return format_inline_latex(match.group(1))

    escaped = re.sub(r"\$([^$]+)\$", replace_math, escaped)

    for key, tag_html in tag_tokens:
        escaped = escaped.replace(key, tag_html)

    plain = re.sub(r"<[^>]+>", "", escaped)
    plain = html.unescape(plain)
    return plain, escaped


def compute_h_index(citations: list[int]) -> int:
    ordered = sorted(citations, reverse=True)
    h = 0
    for idx, c in enumerate(ordered, start=1):
        if c >= idx:
            h = idx
        else:
            break
    return h


def parse_sort_date(pubdate: str, year: int) -> str:
    parts = (pubdate or f"{year}-00-00").split("-")
    y = parts[0] if len(parts) > 0 and parts[0].isdigit() else f"{year:04d}"
    m = parts[1] if len(parts) > 1 and parts[1].isdigit() else "00"
    d = parts[2] if len(parts) > 2 and parts[2].isdigit() else "00"
    return f"{y}-{m}-{d}"


def format_month_year(pubdate: str, year: int) -> str:
    months = [
        "",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    parts = (pubdate or "").split("-")
    if len(parts) >= 2 and parts[1].isdigit():
        m = int(parts[1])
        if 1 <= m <= 12:
            return f"{months[m]} {year}"
    return str(year) if year else ""


def build_yearly_citations(metrics: dict[str, Any]) -> list[dict[str, int]]:
    hist = metrics.get("histograms", {}).get("citations", {})
    ref_to_ref = hist.get("refereed to refereed", {})
    non_to_ref = hist.get("nonrefereed to refereed", {})
    ref_to_non = hist.get("refereed to nonrefereed", {})
    non_to_non = hist.get("nonrefereed to nonrefereed", {})

    years = sorted(
        {
            int(y)
            for d in (ref_to_ref, non_to_ref, ref_to_non, non_to_non)
            for y in d.keys()
            if str(y).isdigit()
        }
    )
    series = []
    cumulative = 0
    for y in years:
        ys = str(y)
        ref = int(ref_to_ref.get(ys, 0)) + int(non_to_ref.get(ys, 0))
        nonref = int(ref_to_non.get(ys, 0)) + int(non_to_non.get(ys, 0))
        total = ref + nonref
        cumulative += total
        series.append(
            {
                "year": y,
                "refereed": ref,
                "nonrefereed": nonref,
                "total": total,
                "cumulative": cumulative,
            }
        )
    while series and series[0]["total"] == 0:
        series.pop(0)
    return series


def classify_doc_group(refereed: bool, doctype: str) -> str:
    if refereed:
        return "refereed"
    if doctype == "eprint":
        return "preprint"
    return "misc"


def main() -> int:
    token = load_token()
    print(f"Fetching SciX library {LIBRARY_ID}...")
    lib_meta, bibcodes = fetch_library(token, LIBRARY_ID)
    print(f"Library '{lib_meta.get('name', '')}': {len(bibcodes)} documents")

    docs = fetch_documents(token, bibcodes)
    print(f"Fetched metadata for {len(docs)} documents")

    papers = []
    unmatched = []
    for doc in docs:
        bibcode = doc["bibcode"]
        authors = doc.get("author") or []
        pos, match_method = find_author_position(doc)
        if pos is None:
            unmatched.append((bibcode, (doc.get("title") or [""])[0]))
            category = "other"
        elif pos == 1:
            category = "first"
        elif pos in (2, 3):
            category = "major"
        else:
            category = "other"

        props = set(doc.get("property") or [])
        refereed = "REFEREED" in props
        doctype = doc.get("doctype") or ""
        doc_group = classify_doc_group(refereed, doctype)
        year = int(doc.get("year") or 0)
        pubdate = doc.get("pubdate") or f"{year}-00-00"
        raw_title = (doc.get("title") or ["Untitled"])[0]
        title_plain, title_html = format_title(raw_title)
        doi_list = doc.get("doi") or []
        doi = doi_list[0] if doi_list else None
        arxiv_id = extract_arxiv_id(doc)
        citations = int(doc.get("citation_count") or 0)
        reads = int(doc.get("read_count") or 0)

        page_val = doc.get("page") or ""
        if isinstance(page_val, list):
            page_val = page_val[0] if page_val else ""

        papers.append(
            {
                "bibcode": bibcode,
                "title": title_plain,
                "title_html": title_html,
                "authors": authors,
                "author_count": len(authors),
                "author_position": pos,
                "author_match": match_method,
                "category": category,
                "doc_group": doc_group,
                "year": year,
                "pubdate": pubdate,
                "date_display": format_month_year(pubdate, year),
                "sort_date": parse_sort_date(pubdate, year),
                "journal": clean_journal(doc),
                "pub_full": doc.get("pub") or "",
                "volume": doc.get("volume") or "",
                "page": page_val,
                "refereed": refereed,
                "doctype": doctype,
                "citations": citations,
                "reads": reads,
                "doi": doi,
                "arxiv_id": arxiv_id,
                "scix_url": f"https://scixplorer.org/abs/{urllib.parse.quote(bibcode, safe='')}/abstract",
                "abstract": re.sub(r"<[^>]+>", " ", html.unescape(doc.get("abstract") or "")).strip(),
                "abstract_html": format_abstract_html(doc.get("abstract") or ""),
            }
        )

    papers.sort(key=lambda p: (p["sort_date"], p["citations"]), reverse=True)

    # Fetch yearly citation histograms for all + each authorship category + refereed
    print("Fetching ADS/SciX citation histograms by category...")
    hist_groups = {
        "all": [p["bibcode"] for p in papers],
        "first": [p["bibcode"] for p in papers if p["category"] == "first"],
        "major": [p["bibcode"] for p in papers if p["category"] == "major"],
        "other": [p["bibcode"] for p in papers if p["category"] == "other"],
        "refereed": [p["bibcode"] for p in papers if p["refereed"]],
        "first_refereed": [
            p["bibcode"] for p in papers if p["category"] == "first" and p["refereed"]
        ],
        "major_refereed": [
            p["bibcode"] for p in papers if p["category"] == "major" and p["refereed"]
        ],
        "other_refereed": [
            p["bibcode"] for p in papers if p["category"] == "other" and p["refereed"]
        ],
    }

    metrics_all = fetch_metrics(token, hist_groups["all"])
    citations_by_year = {"all": build_yearly_citations(metrics_all)}
    for key, subset in hist_groups.items():
        if key == "all":
            continue
        m = fetch_metrics(token, subset)
        citations_by_year[key] = build_yearly_citations(m)

    all_cites = [p["citations"] for p in papers]
    ref_cites = [p["citations"] for p in papers if p["refereed"]]
    first_papers = [p for p in papers if p["category"] == "first"]
    major_papers = [p for p in papers if p["category"] == "major"]
    other_papers = [p for p in papers if p["category"] == "other"]

    indicators = metrics_all.get("indicators", {})
    indicators_ref = metrics_all.get("indicators refereed", {})

    summary = {
        "total_papers": len(papers),
        "refereed_papers": sum(1 for p in papers if p["refereed"]),
        "preprint_papers": sum(1 for p in papers if p["doc_group"] == "preprint"),
        "misc_items": sum(1 for p in papers if p["doc_group"] == "misc"),
        "total_citations": sum(all_cites),
        "refereed_citations": sum(ref_cites),
        "h_index": int(indicators.get("h", compute_h_index(all_cites))),
        "h_index_refereed": int(indicators_ref.get("h", compute_h_index(ref_cites))),
        "i10_index": int(indicators.get("i10", sum(1 for c in all_cites if c >= 10))),
        "first_author_count": len(first_papers),
        "first_author_refereed": sum(1 for p in first_papers if p["refereed"]),
        "first_author_citations": sum(p["citations"] for p in first_papers),
        "major_author_count": len(major_papers),
        "major_author_refereed": sum(1 for p in major_papers if p["refereed"]),
        "major_author_citations": sum(p["citations"] for p in major_papers),
        "other_author_count": len(other_papers),
        "other_author_refereed": sum(1 for p in other_papers if p["refereed"]),
        "other_author_citations": sum(p["citations"] for p in other_papers),
    }

    output = {
        "library_id": LIBRARY_ID,
        "library_name": lib_meta.get("name", ""),
        "library_url": f"https://scixplorer.org/user/libraries/{LIBRARY_ID}",
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "summary": summary,
        "citations_by_year": citations_by_year,
        "papers": papers,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(
        f"Summary: {summary['total_papers']} total ({summary['refereed_papers']} refereed, "
        f"{summary['preprint_papers']} preprints, {summary['misc_items']} misc), "
        f"{summary['total_citations']} citations, h-index={summary['h_index']}"
    )
    if unmatched:
        print(f"Note: {len(unmatched)} item(s) had no author match (classified as other):")
        for b, t in unmatched:
            print(f"  - {b}: {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
