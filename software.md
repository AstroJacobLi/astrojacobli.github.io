---
layout: page
title: Software
permalink: /software/
---

<div class="sw-page">
  <div class="sw-subbar">
    <span>Open-source tools for astronomical simulations, plotting, and research workflows.</span>
    <a href="https://github.com/AstroJacobLi" target="_blank" rel="noopener">GitHub (@AstroJacobLi) &#8599;</a>
  </div>

  <div class="sw-list">
    <article class="sw-item">
      <div class="sw-item__body">
        <div class="sw-item__head">
          <a class="sw-item__name" href="https://github.com/AstroJacobLi/Rosesim" target="_blank" rel="noopener">Rosesim</a>
          <span class="sw-item__meta-tag">&middot; Python</span>
        </div>
        <p class="sw-item__desc">
          A forward-modeling simulator for the Nancy Grace Roman Space Telescope. Rosesim generates realistic synthetic observations by injecting artificial sources into Roman exposures, enabling tests of source detection, photometry pipelines, and survey completeness for faint and low-surface-brightness galaxies.
        </p>
        <div class="sw-item__links">
          <a href="https://github.com/AstroJacobLi/Rosesim" target="_blank" rel="noopener">GitHub &#8599;</a>
        </div>
      </div>
      <figure class="sw-item__figure">
        <img src="/images/symphony_test.jpg" alt="Simulated Roman deep-field image from Rosesim">
        <figcaption>Simulated Roman deep-field image</figcaption>
      </figure>
    </article>

    <article class="sw-item">
      <div class="sw-item__body">
        <div class="sw-item__head">
          <a class="sw-item__name" href="https://github.com/AstroJacobLi/smplotlib" target="_blank" rel="noopener">smplotlib</a>
          <span class="sw-item__meta-tag">&middot; Python</span>
        </div>
        <p class="sw-item__desc">
          A Matplotlib style library inspired by the classic <em>SuperMongo</em> aesthetic. <code>smplotlib</code> provides clean, publication-ready plot styles with a single import, matching the traditional look of astronomical journals without manual tweaking of <code>rcParams</code>.
        </p>
        <div class="sw-item__links">
          <a href="https://github.com/AstroJacobLi/smplotlib" target="_blank" rel="noopener">GitHub &#8599;</a>
          <span class="sw-sep">&middot;</span>
          <a href="https://pypi.org/project/smplotlib/" target="_blank" rel="noopener">PyPI &#8599;</a>
          <span class="sw-sep">&middot;</span>
          <code>pip install smplotlib</code>
        </div>
      </div>
      <figure class="sw-item__figure">
        <img src="/images/two_phase.png" alt="Example plot generated with smplotlib">
        <figcaption>Example figure styled with smplotlib</figcaption>
      </figure>
    </article>
  </div>

  <h2 class="sw-section-heading">BibTeX &amp; CV Utilities</h2>

  <div class="sw-util-grid">
    <article class="sw-util">
      <div class="sw-item__head">
        <a class="sw-item__name" href="https://github.com/AstroJacobLi/bib2cv" target="_blank" rel="noopener">bib2cv</a>
        <span class="sw-item__meta-tag">&middot; Python</span>
      </div>
      <p class="sw-item__desc">
        A command-line tool that converts a BibTeX <code>.bib</code> file into a formatted publication list for your CV. Automatically sorts entries, highlights author names, and outputs clean LaTeX or plain-text lists.
      </p>
      <div class="sw-item__links">
        <a href="https://github.com/AstroJacobLi/bib2cv" target="_blank" rel="noopener">GitHub &#8599;</a>
      </div>
    </article>

    <article class="sw-util">
      <div class="sw-item__head">
        <a class="sw-item__name" href="https://github.com/AstroJacobLi/bib_arxiv_to_published" target="_blank" rel="noopener">bib_arxiv_to_published</a>
        <span class="sw-item__meta-tag">&middot; Python</span>
      </div>
      <p class="sw-item__desc">
        Automatically updates arXiv preprint entries in a BibTeX file to their final published journal references by querying the NASA ADS API and replacing journal, volume, page, and DOI metadata in place.
      </p>
      <div class="sw-item__links">
        <a href="https://github.com/AstroJacobLi/bib_arxiv_to_published" target="_blank" rel="noopener">GitHub &#8599;</a>
      </div>
    </article>
  </div>
</div>
