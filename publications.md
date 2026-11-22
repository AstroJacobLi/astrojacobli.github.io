---
layout: page
title: Publications
permalink: /publications/
---

<div class="pub-page" id="pub-app">
  <div class="pub-subbar">
    <div>
      <a href="{{ '/cv/' | relative_url }}">&larr; Back to CV</a>
      <span class="pub-sep">&middot;</span>
      <a href="{{ site.data.publications.library_url }}" target="_blank" rel="noopener">Full library on SciX &#8599;</a>
    </div>
    <div>Updated {{ site.data.publications.updated_at }}</div>
  </div>

  <!-- Compact Stats + Publications per Year -->
  <div class="pub-overview">
    <div class="pub-stats-panel" aria-label="Publication summary metrics">
      <div class="pub-stat">
        <span class="pub-stat__label">Publications</span>
        <div class="pub-stat__right">
          <span class="pub-stat__num" id="stat-pubs">{{ site.data.publications.summary.total_papers }}</span>
          <span class="pub-stat__note" id="stat-pubs-note">{{ site.data.publications.summary.refereed_papers }} refereed</span>
        </div>
      </div>

      <div class="pub-stat">
        <span class="pub-stat__label">Citations</span>
        <div class="pub-stat__right">
          <span class="pub-stat__num" id="stat-cites">{{ site.data.publications.summary.total_citations }}</span>
          <span class="pub-stat__note" id="stat-cites-note">{{ site.data.publications.summary.refereed_citations }} refereed</span>
        </div>
      </div>

      <div class="pub-stat">
        <span class="pub-stat__label">h-index</span>
        <div class="pub-stat__right">
          <span class="pub-stat__num" id="stat-hindex">{{ site.data.publications.summary.h_index }}</span>
          <span class="pub-stat__note" id="stat-hindex-note">{{ site.data.publications.summary.h_index_refereed }} refereed</span>
        </div>
      </div>
    </div>

    <div class="pub-chart-panel">
      <div class="pub-chart-panel__top">
        <span class="pub-chart-panel__title">Publications per year</span>
        <div class="pub-chart-legend" id="pub-year-legend">
          <span><i style="background:#94070a;"></i>First</span>
          <span><i style="background:#3b6e8c;"></i>Major (2nd&ndash;3rd)</span>
          <span><i style="background:#c4d3df;"></i>Other</span>
        </div>
      </div>
      <div class="pub-chart-svg-wrap" id="pub-year-chart"></div>
    </div>
  </div>

  <!-- Authorship Filter Tabs -->
  <div class="pub-tabs" role="tablist" aria-label="Filter by authorship">
    <button type="button" class="pub-tab is-active" data-role="all" role="tab" aria-selected="true">
      All <span class="pub-tab__count" data-role-count="all">({{ site.data.publications.summary.total_papers }})</span>
    </button>
    <button type="button" class="pub-tab" data-role="first" role="tab" aria-selected="false">
      First author <span class="pub-tab__count" data-role-count="first">({{ site.data.publications.summary.first_author_count }})</span>
    </button>
    <button type="button" class="pub-tab" data-role="major" role="tab" aria-selected="false">
      Major author (2nd&ndash;3rd) <span class="pub-tab__count" data-role-count="major">({{ site.data.publications.summary.major_author_count }})</span>
    </button>
    <button type="button" class="pub-tab" data-role="other" role="tab" aria-selected="false">
      Other <span class="pub-tab__count" data-role-count="other">({{ site.data.publications.summary.other_author_count }})</span>
    </button>
  </div>

  <!-- Quiet Filter, Search, and Sort Controls -->
  <div class="pub-controls">
    <div class="pub-controls__left">
      <label for="pub-type">Type:</label>
      <select id="pub-type" class="pub-select">
        <option value="all">All entries</option>
        <option value="papers">Papers (refereed + arXiv)</option>
        <option value="refereed">Refereed only</option>
        <option value="preprint">arXiv preprints</option>
        <option value="misc">Software, proposals &amp; misc</option>
      </select>

      <label for="pub-sort">Sort:</label>
      <select id="pub-sort" class="pub-select">
        <option value="date-desc">Newest first</option>
        <option value="cites-desc">Most cited</option>
        <option value="date-asc">Oldest first</option>
      </select>
    </div>

    <div class="pub-controls__right">
      <div class="pub-search-wrap">
        <input type="text" id="pub-search" placeholder="Filter by keyword, author, journal..." aria-label="Search publications" autocomplete="off">
        <button type="button" class="pub-search-clear" id="pub-search-clear" aria-label="Clear search">&times;</button>
      </div>
    </div>
  </div>

  <div class="pub-filter-note" id="pub-filter-note" style="display:none;"></div>

  <!-- Publication List -->
  <div id="pub-list-container"></div>

  <div class="pub-footnote">
    Data synced from <a href="{{ site.data.publications.library_url }}" target="_blank" rel="noopener">NASA SciX / ADS</a>. Click any title or <em>SciX</em> link to open its SciX abstract page.
  </div>
</div>

<div class="pub-chart-tooltip" id="pub-tooltip" role="tooltip"></div>

<script id="publications-data" type="application/json">
{{ site.data.publications | jsonify | replace: '</script>', '<\/script>' }}
</script>

<script>
(function () {
  'use strict';

  var rawEl = document.getElementById('publications-data');
  if (!rawEl) return;
  var DATA = JSON.parse(rawEl.textContent);
  var PAPERS = DATA.papers || [];

  var ROLE_COLORS = {
    first: '#94070a',
    major: '#3b6e8c',
    other: '#c4d3df'
  };

  var ROLE_LABELS = {
    all: 'All',
    first: 'First author',
    major: 'Major author (2nd\u20133rd)',
    other: 'Other'
  };

  var state = {
    role: 'all',
    type: 'all',
    search: '',
    sort: 'date-desc',
    year: null
  };

  try {
    var params = new URLSearchParams(window.location.search);
    var r = params.get('role');
    var t = params.get('type');
    var y = params.get('year');
    var s = params.get('sort');
    var q = params.get('q');
    if (r && ['all', 'first', 'major', 'other'].indexOf(r) !== -1) state.role = r;
    if (t && ['all', 'papers', 'refereed', 'preprint', 'misc'].indexOf(t) !== -1) state.type = t;
    if (y && /^\d{4}$/.test(y)) state.year = parseInt(y, 10);
    if (s && ['date-desc', 'cites-desc', 'date-asc'].indexOf(s) !== -1) state.sort = s;
    if (q) state.search = q;
  } catch (e) {}

  var tooltipEl = document.getElementById('pub-tooltip');

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function formatAuthorName(name) {
    if (!name) return '';
    var idx = name.indexOf(',');
    if (idx === -1) return name.trim();
    var last = name.slice(0, idx).trim();
    var first = name.slice(idx + 1).trim();
    return first ? (first + ' ' + last) : last;
  }

  function computeHIndex(items) {
    var cites = items.map(function (p) { return p.citations || 0; }).sort(function (a, b) { return b - a; });
    var h = 0;
    for (var i = 0; i < cites.length; i++) {
      if (cites[i] >= i + 1) h = i + 1;
      else break;
    }
    return h;
  }

  function matchesType(p, typeFilter) {
    if (typeFilter === 'all') return true;
    if (typeFilter === 'papers') return p.doc_group === 'refereed' || p.doc_group === 'preprint';
    return p.doc_group === typeFilter;
  }

  function matchesSearch(p, query) {
    if (!query) return true;
    var q = query.trim().toLowerCase();
    if (!q) return true;
    var hay = [
      p.title || '',
      (p.authors || []).join(' '),
      p.journal || '',
      p.pub_full || '',
      String(p.year || ''),
      p.bibcode || '',
      p.arxiv_id || '',
      p.abstract || ''
    ].join(' ').toLowerCase();
    return hay.indexOf(q) !== -1;
  }

  function getFilteredPapers(opts) {
    opts = opts || {};
    var role = opts.ignoreRole ? 'all' : state.role;
    var year = opts.ignoreYear ? null : state.year;
    return PAPERS.filter(function (p) {
      if (role !== 'all' && p.category !== role) return false;
      if (!matchesType(p, state.type)) return false;
      if (year !== null && p.year !== year) return false;
      if (!matchesSearch(p, state.search)) return false;
      return true;
    });
  }

  function sortPapers(list) {
    var arr = list.slice();
    if (state.sort === 'cites-desc') {
      arr.sort(function (a, b) {
        return (b.citations - a.citations) || (b.sort_date || '').localeCompare(a.sort_date || '');
      });
    } else if (state.sort === 'date-asc') {
      arr.sort(function (a, b) {
        return (a.sort_date || '').localeCompare(b.sort_date || '') || (b.citations - a.citations);
      });
    } else {
      arr.sort(function (a, b) {
        return (b.sort_date || '').localeCompare(a.sort_date || '') || (b.citations - a.citations);
      });
    }
    return arr;
  }

  function showTooltip(evt, html) {
    tooltipEl.innerHTML = html;
    tooltipEl.classList.add('is-visible');
    moveTooltip(evt);
  }

  function moveTooltip(evt) {
    var pad = 10;
    var x = evt.clientX + pad;
    var y = evt.clientY - pad - tooltipEl.offsetHeight;
    if (x + tooltipEl.offsetWidth > window.innerWidth - 8) {
      x = evt.clientX - tooltipEl.offsetWidth - pad;
    }
    if (y < 8) y = evt.clientY + pad + 8;
    tooltipEl.style.left = x + 'px';
    tooltipEl.style.top = y + 'px';
  }

  function hideTooltip() {
    tooltipEl.classList.remove('is-visible');
  }

  function updateRoleCounts() {
    var base = getFilteredPapers({ ignoreRole: true, ignoreYear: false });
    var counts = { all: base.length, first: 0, major: 0, other: 0 };
    base.forEach(function (p) {
      if (counts[p.category] !== undefined) counts[p.category]++;
    });
    ['all', 'first', 'major', 'other'].forEach(function (r) {
      var el = document.querySelector('[data-role-count="' + r + '"]');
      if (el) el.textContent = '(' + counts[r] + ')';
    });
  }

  function updateStats(filtered) {
    var total = filtered.length;
    var refList = filtered.filter(function (p) { return p.refereed; });
    var totalCites = filtered.reduce(function (s, p) { return s + (p.citations || 0); }, 0);
    var refCites = refList.reduce(function (s, p) { return s + (p.citations || 0); }, 0);
    var h = computeHIndex(filtered);
    var hRef = computeHIndex(refList);

    document.getElementById('stat-pubs').textContent = total;
    document.getElementById('stat-pubs-note').textContent = refList.length + ' refereed';

    document.getElementById('stat-cites').textContent = totalCites.toLocaleString();
    document.getElementById('stat-cites-note').textContent = refCites.toLocaleString() + ' refereed';

    document.getElementById('stat-hindex').textContent = h;
    document.getElementById('stat-hindex-note').textContent = hRef + ' refereed';
  }

  function renderPubYearChart() {
    var container = document.getElementById('pub-year-chart');
    var legend = document.getElementById('pub-year-legend');
    var subset = getFilteredPapers({ ignoreYear: true });

    var allYears = PAPERS.map(function (p) { return p.year; }).filter(Boolean);
    var minY = Math.min.apply(null, allYears);
    var maxY = Math.max.apply(null, allYears);

    var byYear = {};
    for (var y = minY; y <= maxY; y++) {
      byYear[y] = { year: y, first: 0, major: 0, other: 0, total: 0 };
    }
    subset.forEach(function (p) {
      if (byYear[p.year]) {
        byYear[p.year][p.category]++;
        byYear[p.year].total++;
      }
    });

    var series = [];
    for (var yr = minY; yr <= maxY; yr++) series.push(byYear[yr]);

    if (state.role === 'all') {
      legend.innerHTML =
        '<span><i style="background:' + ROLE_COLORS.first + ';"></i>First</span>' +
        '<span><i style="background:' + ROLE_COLORS.major + ';"></i>Major (2nd\u20133rd)</span>' +
        '<span><i style="background:' + ROLE_COLORS.other + ';"></i>Other</span>';
    } else {
      legend.innerHTML =
        '<span><i style="background:' + ROLE_COLORS[state.role] + ';"></i>' + escapeHtml(ROLE_LABELS[state.role]) + '</span>';
    }

    var W = 560, H = 138;
    var padL = 28, padR = 8, padT = 16, padB = 22;
    var chartW = W - padL - padR;
    var chartH = H - padT - padB;
    var maxVal = Math.max(4, Math.max.apply(null, series.map(function (d) { return d.total; })));
    var tickStep = maxVal <= 8 ? 2 : (maxVal <= 20 ? 5 : 10);
    var yMax = Math.ceil(maxVal / tickStep) * tickStep;

    var slotW = chartW / series.length;
    var barW = Math.min(36, Math.max(16, slotW * 0.56));

    var svg = [];
    svg.push('<svg viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="Publications per year">');

    for (var v = 0; v <= yMax; v += tickStep) {
      var gy = padT + chartH - (v / yMax) * chartH;
      svg.push('<line x1="' + padL + '" y1="' + gy.toFixed(1) + '" x2="' + (W - padR) + '" y2="' + gy.toFixed(1) + '" stroke="' + (v === 0 ? '#bdbdbd' : '#eeeeee') + '" stroke-width="1"/>');
      svg.push('<text x="' + (padL - 6) + '" y="' + (gy + 3.5).toFixed(1) + '" text-anchor="end" font-size="10" fill="#777">' + v + '</text>');
    }

    series.forEach(function (d, idx) {
      var cx = padL + idx * slotW + slotW / 2;
      var x = cx - barW / 2;
      var isDimmed = state.year !== null && state.year !== d.year;
      var cls = 'pub-chart-bar-group' + (isDimmed ? ' is-dimmed' : '');

      svg.push('<g class="' + cls + '" data-pub-year="' + d.year + '">');
      svg.push('<rect x="' + (padL + idx * slotW).toFixed(1) + '" y="' + padT + '" width="' + slotW.toFixed(1) + '" height="' + (chartH + padB) + '" fill="transparent"/>');

      var curY = padT + chartH;
      var segs = [
        { val: d.first, color: ROLE_COLORS.first },
        { val: d.major, color: ROLE_COLORS.major },
        { val: d.other, color: ROLE_COLORS.other }
      ];
      segs.forEach(function (seg) {
        if (!seg.val) return;
        var h = (seg.val / yMax) * chartH;
        curY -= h;
        svg.push('<rect x="' + x.toFixed(1) + '" y="' + curY.toFixed(1) + '" width="' + barW.toFixed(1) + '" height="' + Math.max(1, h).toFixed(1) + '" fill="' + seg.color + '"/>');
      });

      if (d.total > 0) {
        svg.push('<text x="' + cx.toFixed(1) + '" y="' + (curY - 4).toFixed(1) + '" text-anchor="middle" font-size="10" fill="#444">' + d.total + '</text>');
      }
      var yearFill = (state.year === d.year) ? '#94070a' : '#555';
      var yearWeight = (state.year === d.year) ? '700' : '400';
      svg.push('<text x="' + cx.toFixed(1) + '" y="' + (H - 5) + '" text-anchor="middle" font-size="10.5" font-weight="' + yearWeight + '" fill="' + yearFill + '">' + d.year + '</text>');
      svg.push('</g>');
    });

    svg.push('</svg>');
    container.innerHTML = svg.join('');

    container.querySelectorAll('[data-pub-year]').forEach(function (g) {
      var yrVal = parseInt(g.getAttribute('data-pub-year'), 10);
      var row = byYear[yrVal];
      g.addEventListener('click', function () {
        state.year = (state.year === yrVal) ? null : yrVal;
        render();
      });
      g.addEventListener('mouseenter', function (evt) {
        var html = '<strong>' + yrVal + '</strong>: ' + row.total;
        if (state.role === 'all') {
          html += ' (First: ' + row.first + ', Major: ' + row.major + ', Other: ' + row.other + ')';
        }
        showTooltip(evt, html);
      });
      g.addEventListener('mousemove', moveTooltip);
      g.addEventListener('mouseleave', hideTooltip);
    });
  }

  function renderAuthorsHtml(paper, expanded) {
    var authors = paper.authors || [];
    if (!authors.length) return '';
    var posIdx = (paper.author_position != null) ? (paper.author_position - 1) : -1;

    function fmtOne(idx) {
      var label = escapeHtml(formatAuthorName(authors[idx]));
      if (idx === posIdx) {
        return '<span class="pub-author-self">' + label + '</span>';
      }
      return label;
    }

    var MAX_INLINE = 7;
    if (expanded || authors.length <= MAX_INLINE) {
      var full = [];
      for (var i = 0; i < authors.length; i++) full.push(fmtOne(i));
      var out = full.join(', ');
      if (expanded && authors.length > MAX_INLINE) {
        out += ' <button type="button" class="pub-authors-toggle" data-toggle-authors="' + escapeHtml(paper.bibcode) + '">[less]</button>';
      }
      return out;
    }

    var shown = [];
    for (var j = 0; j < 5; j++) shown.push(fmtOne(j));
    var html = shown.join(', ');
    var remaining = authors.length - 5;

    if (posIdx >= 5) {
      html += ', &hellip;, ' + fmtOne(posIdx);
      remaining = authors.length - 6;
    }
    html += ' <button type="button" class="pub-authors-toggle" data-toggle-authors="' + escapeHtml(paper.bibcode) + '">(+' + remaining + ' more)</button>';
    return html;
  }

  function formatNonRefTag(paper) {
    if (paper.refereed) return '';
    if (paper.doc_group === 'preprint') return '';
    var labels = {
      software: 'Software',
      proposal: 'Proposal',
      abstract: 'AAS Abstract',
      inproceedings: 'Proceedings',
      circular: 'MPEC'
    };
    var txt = labels[paper.doctype];
    return txt ? ' <span class="pub-entry__tag">[' + escapeHtml(txt) + ']</span>' : '';
  }

  function formatVenueAndLinks(paper) {
    var venueParts = [];
    if (paper.journal) {
      var j = '<span class="pub-entry__journal">' + escapeHtml(paper.journal) + '</span>';
      if (paper.volume) j += ', ' + escapeHtml(paper.volume);
      if (paper.page && !/^arXiv:/i.test(paper.page)) j += ', ' + escapeHtml(paper.page);
      venueParts.push(j);
    }
    if (paper.date_display) {
      venueParts.push(escapeHtml(paper.date_display));
    }

    var links = [];
    links.push('<a href="' + escapeHtml(paper.scix_url) + '" target="_blank" rel="noopener">SciX</a>');
    if (paper.arxiv_id) {
      links.push('<a href="https://arxiv.org/abs/' + encodeURIComponent(paper.arxiv_id) + '" target="_blank" rel="noopener">arXiv:' + escapeHtml(paper.arxiv_id) + '</a>');
    }
    if (paper.doi) {
      links.push('<a href="https://doi.org/' + encodeURI(paper.doi) + '" target="_blank" rel="noopener">DOI</a>');
    }
    if (paper.abstract) {
      links.push('<button type="button" data-toggle-abstract="' + escapeHtml(paper.bibcode) + '" aria-expanded="false">Abstract</button>');
    }

    return venueParts.join(' &middot; ') + formatNonRefTag(paper) +
      ' <span class="pub-sep">&mdash;</span> <span class="pub-entry__links">' + links.join(' &middot; ') + '</span>';
  }

  function buildPaperRowHtml(paper) {
    var cites = paper.citations || 0;
    var citeText = cites > 0
      ? ('<strong>' + cites + '</strong> ' + (cites === 1 ? 'citation' : 'citations'))
      : '0 citations';

    return (
      '<li class="pub-entry" data-bibcode="' + escapeHtml(paper.bibcode) + '">' +
        '<div class="pub-entry__body">' +
          '<div class="pub-entry__title">' +
            '<a href="' + escapeHtml(paper.scix_url) + '" target="_blank" rel="noopener">' + (paper.title_html || escapeHtml(paper.title)) + '</a>' +
          '</div>' +
          '<div class="pub-entry__authors" data-authors-for="' + escapeHtml(paper.bibcode) + '">' +
            renderAuthorsHtml(paper, false) +
          '</div>' +
          '<div class="pub-entry__meta">' + formatVenueAndLinks(paper) + '</div>' +
          (paper.abstract
            ? '<div class="pub-abstract" data-abstract-for="' + escapeHtml(paper.bibcode) + '">' + (paper.abstract_html || escapeHtml(paper.abstract)) + '</div>'
            : '') +
        '</div>' +
        '<div class="pub-entry__cites">' + citeText + '</div>' +
      '</li>'
    );
  }

  function renderFilterNote(filtered) {
    var el = document.getElementById('pub-filter-note');
    var pieces = [];
    if (state.year !== null) {
      pieces.push('Filtered to year <strong>' + state.year + '</strong> <button type="button" class="pub-year-clear" id="pub-clear-year">Clear &times;</button>');
    }
    if (state.search.trim()) {
      pieces.push('Matching &ldquo;' + escapeHtml(state.search.trim()) + '&rdquo; (' + filtered.length + ' found)');
    }
    if (!pieces.length) {
      el.style.display = 'none';
      el.innerHTML = '';
      return;
    }
    el.style.display = 'flex';
    el.innerHTML = pieces.join('<span class="pub-sep">&middot;</span>');
    var clearYr = document.getElementById('pub-clear-year');
    if (clearYr) {
      clearYr.addEventListener('click', function () {
        state.year = null;
        render();
      });
    }
  }

  function renderList(filtered) {
    var container = document.getElementById('pub-list-container');
    var sorted = sortPapers(filtered);

    if (!sorted.length) {
      container.innerHTML =
        '<div class="pub-empty">No matching publications.' +
          '<button type="button" id="pub-reset-all">Reset filters</button>' +
        '</div>';
      var resetBtn = document.getElementById('pub-reset-all');
      if (resetBtn) {
        resetBtn.addEventListener('click', function () {
          state.role = 'all';
          state.type = 'all';
          state.search = '';
          state.year = null;
          document.getElementById('pub-search').value = '';
          render();
        });
      }
      return;
    }

    var groupByYear = (state.sort === 'date-desc' || state.sort === 'date-asc');
    if (groupByYear) {
      var groups = [];
      var map = {};
      sorted.forEach(function (p) {
        if (!map[p.year]) {
          map[p.year] = { year: p.year, items: [] };
          groups.push(map[p.year]);
        }
        map[p.year].items.push(p);
      });
      container.innerHTML = groups.map(function (g) {
        return (
          '<section class="pub-year-group">' +
            '<h2 class="pub-year-heading">' + g.year +
              '<span class="pub-year-heading__count">(' + g.items.length + ')</span>' +
            '</h2>' +
            '<ul class="pub-list">' +
              g.items.map(buildPaperRowHtml).join('') +
            '</ul>' +
          '</section>'
        );
      }).join('');
    } else {
      container.innerHTML = '<ul class="pub-list">' + sorted.map(buildPaperRowHtml).join('') + '</ul>';
    }
  }

  function syncControlsUI() {
    document.querySelectorAll('.pub-tab').forEach(function (btn) {
      var active = btn.getAttribute('data-role') === state.role;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-selected', active ? 'true' : 'false');
    });
    document.getElementById('pub-type').value = state.type;
    document.getElementById('pub-sort').value = state.sort;
    var searchInput = document.getElementById('pub-search');
    if (searchInput.value !== state.search) searchInput.value = state.search;
    document.getElementById('pub-search-clear').classList.toggle('is-visible', !!state.search.trim());
  }

  var paperByBibcode = {};
  PAPERS.forEach(function (p) { paperByBibcode[p.bibcode] = p; });
  var expandedAuthors = {};

  function render() {
    syncControlsUI();
    updateRoleCounts();
    var filtered = getFilteredPapers();
    updateStats(filtered);
    renderPubYearChart();
    renderFilterNote(filtered);
    renderList(filtered);
  }

  document.querySelectorAll('.pub-tab').forEach(function (btn) {
    btn.addEventListener('click', function () {
      state.role = btn.getAttribute('data-role');
      render();
    });
  });

  document.getElementById('pub-type').addEventListener('change', function (e) {
    state.type = e.target.value;
    render();
  });

  document.getElementById('pub-sort').addEventListener('change', function (e) {
    state.sort = e.target.value;
    render();
  });

  var searchInput = document.getElementById('pub-search');
  searchInput.addEventListener('input', function () {
    state.search = searchInput.value;
    render();
  });

  document.getElementById('pub-search-clear').addEventListener('click', function () {
    state.search = '';
    searchInput.value = '';
    searchInput.focus();
    render();
  });

  document.getElementById('pub-list-container').addEventListener('click', function (evt) {
    var absBtn = evt.target.closest('[data-toggle-abstract]');
    if (absBtn) {
      var bc = absBtn.getAttribute('data-toggle-abstract');
      var drawer = document.querySelector('[data-abstract-for="' + CSS.escape(bc) + '"]');
      if (drawer) {
        var open = drawer.classList.toggle('is-open');
        absBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        absBtn.textContent = open ? 'Hide abstract' : 'Abstract';
      }
      return;
    }

    var authBtn = evt.target.closest('[data-toggle-authors]');
    if (authBtn) {
      var bc2 = authBtn.getAttribute('data-toggle-authors');
      expandedAuthors[bc2] = !expandedAuthors[bc2];
      var wrap = document.querySelector('[data-authors-for="' + CSS.escape(bc2) + '"]');
      if (wrap && paperByBibcode[bc2]) {
        wrap.innerHTML = renderAuthorsHtml(paperByBibcode[bc2], !!expandedAuthors[bc2]);
      }
    }
  });

  render();
})();
</script>
