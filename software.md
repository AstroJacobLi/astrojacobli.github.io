---
layout: page
title: Software
permalink: /software/
---
<link rel="stylesheet" href="/css/display.css">

<style>
.software-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
    gap: 1.6em;
    margin-top: 1.5em;
}
.software-card {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.09);
    padding: 1.4em 1.6em 1.2em;
    display: flex;
    flex-direction: column;
    transition: box-shadow 0.2s;
    border-top: 4px solid #94070a;
}
.software-card:hover {
    box-shadow: 0 6px 22px rgba(0,0,0,0.14);
}
/* Featured card: full-width, two-column with image */
.software-card-featured {
    grid-column: 1 / -1;
    flex-direction: row;
    gap: 0;
    padding: 0;
    overflow: hidden;
    align-items: stretch;
}
.software-card-featured .software-card-body {
    flex: 1;
    padding: 1.4em 1.6em 1.2em;
    display: flex;
    flex-direction: column;
    min-width: 0;
}
.software-card-preview {
    width: 320px;
    flex-shrink: 0;
    position: relative;
    overflow: hidden;
    background: #0a0a0a;
}
.software-card-preview img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.35s ease;
}
.software-card-featured:hover .software-card-preview img {
    transform: scale(1.03);
}
.software-card-preview .preview-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.65));
    color: #eee;
    font-size: 0.78em;
    padding: 1.2em 0.8em 0.5em;
    text-align: center;
    font-style: italic;
}
/* Plot preview: white background */
.software-card-preview.preview-light {
    background: #f8f8f8;
    border-left: 1px solid #e8e8e8;
}
.software-card-preview.preview-light img {
    object-fit: contain;
    padding: 0.5em;
}
.software-card-preview.preview-light .preview-caption {
    background: linear-gradient(transparent, rgba(240,240,240,0.85));
    color: #555;
}
.software-card-header {
    display: flex;
    align-items: center;
    gap: 0.7em;
    margin-bottom: 0.5em;
}
.software-icon {
    font-size: 1.7em;
    line-height: 1;
}
.software-name {
    font-size: 1.25em;
    font-weight: 700;
    color: #94070a;
    text-decoration: none;
}
.software-name:hover {
    text-decoration: underline;
}
.software-lang {
    display: inline-block;
    font-size: 0.78em;
    font-weight: 600;
    color: #555;
    background: #f0f0f0;
    border-radius: 4px;
    padding: 1px 7px;
    margin-left: 0.3em;
    vertical-align: middle;
}
.software-desc {
    color: #333;
    font-size: 1em;
    line-height: 1.55;
    margin-bottom: 0.9em;
    flex-grow: 1;
}
.software-card-footer {
    display: flex;
    align-items: center;
    gap: 0.7em;
    flex-wrap: wrap;
}
.software-badge img {
    height: 20px;
    vertical-align: middle;
}
.software-gh-link {
    font-size: 0.88em;
    color: #0056b3;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.3em;
}
.software-gh-link:hover {
    text-decoration: underline;
}
@media (max-width: 680px) {
    .software-grid {
        grid-template-columns: 1fr;
    }
    .software-card-featured {
        flex-direction: column;
    }
    .software-card-preview {
        width: 100%;
        height: 200px;
    }
    .software-card-preview.preview-light {
        height: 220px;
    }
}
</style>

<font size="+1"><h1 style="color: #94070a; font-weight: 300;">Software</h1></font>

I develop open-source tools for astronomy and research productivity. All packages are freely available on GitHub.

<div class="software-grid">

<div class="software-card software-card-featured">
  <div class="software-card-body">
    <div class="software-card-header">
      <span class="software-icon">🌹</span>
      <a class="software-name" href="https://github.com/AstroJacobLi/Rosesim" target="_blank" rel="noopener">Rosesim</a>
      <span class="software-lang">Python</span>
    </div>
    <p class="software-desc">
      A forward-modeling simulator for the Nancy Grace Roman Space Telescope. Rosesim generates realistic synthetic observations by injecting artificial sources into Roman exposures, enabling robust tests of source detection, photometry pipelines, and survey completeness for faint and low-surface-brightness objects.
    </p>
    <div class="software-card-footer">
      <a class="software-badge" href="https://github.com/AstroJacobLi/Rosesim" target="_blank" rel="noopener">
        <img src="https://img.shields.io/github/stars/AstroJacobLi/Rosesim?style=flat&color=94070a" alt="GitHub stars">
      </a>
      <a class="software-gh-link" href="https://github.com/AstroJacobLi/Rosesim" target="_blank" rel="noopener">
        &#128279; GitHub
      </a>
    </div>
  </div>
  <div class="software-card-preview">
    <img src="/images/symphony_test.jpg" alt="Simulated Roman deep-field image from Rosesim">
    <span class="preview-caption">Simulated Roman deep-field image</span>
  </div>
</div>

<div class="software-card software-card-featured">
  <div class="software-card-body">
    <div class="software-card-header">
      <span class="software-icon">📊</span>
      <a class="software-name" href="https://github.com/AstroJacobLi/smplotlib" target="_blank" rel="noopener">smplotlib</a>
      <span class="software-lang">Python</span>
    </div>
    <p class="software-desc">
      A Matplotlib style library inspired by the classic <em>SuperMongo</em> aesthetic. smplotlib provides clean, publication-ready plot styles with a single import, making it easy to produce figures that match the traditional look of astronomical journals without manual tweaking of rcParams.
    </p>
    <div class="software-card-footer">
      <a class="software-badge" href="https://github.com/AstroJacobLi/smplotlib" target="_blank" rel="noopener">
        <img src="https://img.shields.io/github/stars/AstroJacobLi/smplotlib?style=flat&color=94070a" alt="GitHub stars">
      </a>
      <a class="software-badge" href="https://pypi.org/project/smplotlib/" target="_blank" rel="noopener">
        <img src="https://img.shields.io/pypi/dm/smplotlib?style=flat&color=F58025" alt="PyPI downloads">
      </a>
      <a class="software-gh-link" href="https://github.com/AstroJacobLi/smplotlib" target="_blank" rel="noopener">
        &#128279; GitHub
      </a>
    </div>
  </div>
  <div class="software-card-preview preview-light">
    <img src="/images/two_phase.png" alt="Example plot generated with smplotlib">
    <span class="preview-caption">Example publication-ready figure</span>
  </div>
</div>

<div class="software-card">
  <div class="software-card-header">
    <span class="software-icon">📄</span>
    <a class="software-name" href="https://github.com/AstroJacobLi/bib2cv" target="_blank" rel="noopener">bib2cv</a>
    <span class="software-lang">Python</span>
  </div>
  <p class="software-desc">
    A command-line tool that converts a BibTeX <code>.bib</code> file into a formatted publication list for your CV. bib2cv automatically sorts entries, highlights author names, and outputs clean LaTeX or plain-text lists — saving the tedious manual work of maintaining a publications section every time a new paper is accepted.
  </p>
  <div class="software-card-footer">
    <a class="software-badge" href="https://github.com/AstroJacobLi/bib2cv" target="_blank" rel="noopener">
      <img src="https://img.shields.io/github/stars/AstroJacobLi/bib2cv?style=flat&color=94070a" alt="GitHub stars">
    </a>
    <a class="software-gh-link" href="https://github.com/AstroJacobLi/bib2cv" target="_blank" rel="noopener">
      &#128279; GitHub
    </a>
  </div>
</div>

<div class="software-card">
  <div class="software-card-header">
    <span class="software-icon">🔄</span>
    <a class="software-name" href="https://github.com/AstroJacobLi/bib_arxiv_to_published" target="_blank" rel="noopener">bib_arxiv_to_published</a>
    <span class="software-lang">Python</span>
  </div>
  <p class="software-desc">
    A utility that automatically updates arXiv preprint entries in a BibTeX file to their final published journal references. It queries the NASA ADS API to find the peer-reviewed version of each arXiv paper and replaces the preprint metadata — journal, volume, pages, DOI — in place, keeping your bibliography always up to date.
  </p>
  <div class="software-card-footer">
    <a class="software-badge" href="https://github.com/AstroJacobLi/bib_arxiv_to_published" target="_blank" rel="noopener">
      <img src="https://img.shields.io/github/stars/AstroJacobLi/bib_arxiv_to_published?style=flat&color=94070a" alt="GitHub stars">
    </a>
    <a class="software-gh-link" href="https://github.com/AstroJacobLi/bib_arxiv_to_published" target="_blank" rel="noopener">
      &#128279; GitHub
    </a>
  </div>
</div>

</div>
