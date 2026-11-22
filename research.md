---
layout: page
title: Research
permalink: /research/
---

<div class="res-page" id="res-app">
  <div class="res-subbar">
    <span>Dwarf galaxies, dark matter on small scales, low-surface-brightness surveys, and statistical methods.</span>
    <span class="res-subbar__links">
      <a href="{{ '/publications/' | relative_url }}">Publications &rarr;</a>
      <span class="res-sep">&middot;</span>
      <a href="{{ '/software/' | relative_url }}">Software &rarr;</a>
    </span>
  </div>

  <!-- Topic Filter Tabs -->
  <div class="res-tabs" role="tablist" aria-label="Filter research projects by topic">
    <button type="button" class="res-tab is-active" data-topic="all" role="tab" aria-selected="true">
      All <span class="res-tab__count">(8)</span>
    </button>
    <button type="button" class="res-tab" data-topic="dwarfs" role="tab" aria-selected="false">
      Dwarf Galaxies <span class="res-tab__count">(4)</span>
    </button>
    <button type="button" class="res-tab" data-topic="lsb" role="tab" aria-selected="false">
      LSB &amp; Outskirts <span class="res-tab__count">(2)</span>
    </button>
    <button type="button" class="res-tab" data-topic="methods" role="tab" aria-selected="false">
      Methods &amp; Inference <span class="res-tab__count">(2)</span>
    </button>
    <button type="button" class="res-tab" data-topic="solar" role="tab" aria-selected="false">
      Outer Solar System <span class="res-tab__count">(1)</span>
    </button>
  </div>

  <!-- Flagship Survey Hero -->
  <section class="res-hero" data-res-item data-topic="dwarfs">
    <div>
      <div class="res-hero__kicker">Flagship Survey</div>
      <h2 class="res-hero__title">
        <a href="https://elves-surveys.github.io/elves-dwarf/" target="_blank" rel="noopener">ELVES-Dwarf Survey: Satellites of Isolated Dwarf Galaxies in the Local Volume</a>
      </h2>
      <p class="res-hero__desc">
        I lead the <strong>E</strong>xploration of <strong>L</strong>ocal <strong>V</strong>olum<strong>E</strong> <strong>S</strong>atellites of <strong>Dwarf</strong> galaxies (<strong>ELVES-Dwarf</strong>) survey — building the first large, homogeneous, distance-confirmed census of satellites around isolated dwarf hosts (10<sup>8</sup> &lt; M<sub>&lowast;</sub> &lt; 10<sup>10</sup> M<sub>&odot;</sub>). Across 39 hosts, we confirm 39 satellites out of 207 candidates via surface brightness fluctuation distances from HSC and Magellan.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="https://elves-surveys.github.io/elves-dwarf/" target="_blank" rel="noopener">Survey Website &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://scixplorer.org/abs/2026ApJ..1002...75L/abstract" target="_blank" rel="noopener">Paper I (ApJ 2026) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://arxiv.org/abs/2609.00283" target="_blank" rel="noopener">Paper II (arXiv 2026) &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="elves" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-elves">
        <p>Satellite candidates are identified in integrated light using the Legacy Surveys (complete down to M<sub>g</sub> &approx; &minus;9 mag) and confirmed via SBF distances from deep Hyper Suprime-Cam and Magellan imaging. The satellite systems are strikingly diverse: 21 hosts have no confirmed satellites, 10 have one, six have two, and two have four.</p>
        <p>Overall satellite abundances and stellar mass functions broadly agree with TNG50 and Milky Way-calibrated galaxy&ndash;halo connection models, though strong outliers exist. The quenched fraction of satellites around dwarf hosts is substantially lower than around Milky Way-mass hosts, showing that environmental quenching is far less efficient in dwarf halos.</p>
      </div>
    </div>

    <figure class="res-hero__figure">
      <img src="/images/elves-dwarf-status.png" data-zoom-src="/images/elves-dwarf-status.png" data-zoom-caption="ELVES-Dwarf survey: 39 dwarf hosts across the Local Volume, with 39 distance-confirmed satellites out of 207 candidates." alt="ELVES-Dwarf survey overview showing 39 dwarf hosts and 39 confirmed satellites">
      <figcaption>39 dwarf hosts across the Local Volume, with 39 distance-confirmed satellites out of 207 candidates.</figcaption>
    </figure>
  </section>

  <!-- 2-Column Visual Portfolio Grid -->
  <div class="res-grid">

    <!-- DDO 161 -->
    <article class="res-project" data-res-item data-topic="dwarfs">
      <div class="res-project__thumb res-project__thumb--light">
        <img src="/images/DDO161.png" data-zoom-src="/images/DDO161.png" data-zoom-caption="DDO 161 hosts four confirmed satellites, lying at the 0.04% extreme of TNG50 cosmological simulation predictions." alt="DDO 161 satellite abundance compared with TNG50 predictions">
      </div>
      <h3 class="res-project__title">
        <a href="https://scixplorer.org/abs/2026ApJ...998L..24L/abstract" target="_blank" rel="noopener">DDO 161: A Possible &ldquo;Too-Many-Satellites&rdquo; Problem</a>
      </h3>
      <p class="res-project__summary">
        With four Magellan-confirmed satellites above M<sub>&lowast;</sub> &gt; 10<sup>5.4</sup> M<sub>&odot;</sub>, the isolated dwarf galaxy DDO 161 (at 6 Mpc) is the most satellite-rich dwarf known — lying at the 0.04% tail of TNG50 predictions.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="https://scixplorer.org/abs/2026ApJ...998L..24L/abstract" target="_blank" rel="noopener">ApJL (2026) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://arxiv.org/abs/2511.01733" target="_blank" rel="noopener">arXiv &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="ddo161" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-ddo161">
        <p>We identified eight satellite candidates within the projected virial radius of DDO 161 (M<sub>&lowast;</sub> &approx; 10<sup>8.4</sup> M<sub>&odot;</sub>) and confirmed four satellites through surface brightness fluctuation distances from deep Magellan imaging. Its unusually rich satellite system exceeds expectations from Milky Way-calibrated galaxy&ndash;halo models and offers a direct small-scale test of &Lambda;CDM and dark matter physics.</p>
      </div>
    </article>

    <!-- 2017 OF201 -->
    <article class="res-project" data-res-item data-topic="solar">
      <div class="res-project__thumb res-project__thumb--dark-contain">
        <img src="/images/TNO/orbits_press_release.jpeg" data-zoom-src="/images/TNO/orbits_press_release.jpeg" data-zoom-caption="Orbits and current locations of Neptune, Pluto, and 2017 OF201. Figure credit: Jiaxuan Li (Princeton), Sihao Cheng (IAS)." alt="Orbits of Neptune, Pluto, and 2017 OF201">
      </div>
      <h3 class="res-project__title">
        <a href="https://scixplorer.org/abs/2026ApJ...998L...6C/abstract" target="_blank" rel="noopener">2017 OF201: Dwarf Planet Candidate in an Extremely Wide Orbit</a>
      </h3>
      <p class="res-project__summary">
        With Sihao Cheng (IAS) and Eritas Yang (Princeton), we discovered a ~700 km trans-Neptunian object on a 25,000-year orbit (a &approx; 840 au, e &approx; 0.946) that challenges the Planet Nine apsidal-clustering hypothesis.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="https://scixplorer.org/abs/2026ApJ...998L...6C/abstract" target="_blank" rel="noopener">ApJL (2026) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://en.wikipedia.org/wiki/2017_OF201" target="_blank" rel="noopener">Wikipedia &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://www.nytimes.com/2025/05/29/science/dwarf-planet-nine-discovery.html" target="_blank" rel="noopener">NYT &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="tno" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-tno">
        <p>Spotted in archival DECaLS (DECam) and CFHT data spanning over 7 years, 2017 OF201 is currently ~90 au from the Sun and sits outside the apsidal clustering of other extreme TNOs. Because it is detectable by DECaLS-depth surveys for only ~0.5% of its orbital period, it implies a substantial hidden outer Solar System population awaiting Rubin LSST.</p>
        <p><strong>Press:</strong> <a href="https://www.ias.edu/news/extreme-cousin-pluto-possible-dwarf-planet-discovered-solar-systems-edge" target="_blank" rel="noopener">IAS</a> &middot; <a href="https://web.astro.princeton.edu/news/princeton-astronomers-discover-extraordinary-distant-object-solar-systems-edge" target="_blank" rel="noopener">Princeton</a> &middot; <a href="https://skyandtelescope.org/astronomy-news/another-dwarf-planet-in-our-solar-system/" target="_blank" rel="noopener">Sky &amp; Telescope</a> &middot; <a href="https://phys.org/news/2025-05-extreme-cousin-pluto-dwarf-planet.html" target="_blank" rel="noopener">Phys.org</a> &middot; <a href="https://www.newscientist.com/article/2481477-new-dwarf-planet-spotted-at-the-edge-of-the-solar-system/" target="_blank" rel="noopener">New Scientist</a></p>
        <img src="/images/TNO/ETNO_orbits_apsidal.jpeg" data-zoom-src="/images/TNO/ETNO_orbits_apsidal.jpeg" data-zoom-caption="Plan view of extreme TNO orbits showing 2017 OF201 as an outlier to apsidal clustering." alt="Extreme TNO apsidal clustering plot">
        <div class="res-drawer__caption">Plan view of extreme TNO orbits showing 2017 OF201 outside the apsidal clustering.</div>
      </div>
    </article>

    <!-- Hedgehog -->
    <article class="res-project" data-res-item data-topic="dwarfs">
      <div class="res-project__thumb res-project__thumb--light">
        <img src="/images/research_thumbs/hedgehog_fig1.png" data-zoom-src="/images/research_thumbs/hedgehog_fig1.png" data-zoom-caption="Hedgehog (dw1322m2053) in Legacy Survey DR10 griz, Magellan/IMACS i-band (resolved stars &amp; SBF), and GALEX UV (quiescent, no UV emission)." alt="Three-panel discovery image of Hedgehog in Legacy Survey, IMACS, and GALEX">
      </div>
      <h3 class="res-project__title">
        <a href="https://scixplorer.org/abs/2024ApJ...975L..23L/abstract" target="_blank" rel="noopener">Hedgehog: An Isolated Quiescent Dwarf Galaxy at 2.4 Mpc</a>
      </h3>
      <p class="res-project__summary">
        Discovery of dw1322m2053 (&ldquo;Hedgehog&rdquo;), a quiescent dwarf galaxy with no neighbors within 1 Mpc and 1.7 Mpc from Centaurus A — one of the most isolated quenched dwarfs known at its stellar mass.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="{{ '/research/Hedgehog/' | relative_url }}">3D Map &rarr;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://scixplorer.org/abs/2024ApJ...975L..23L/abstract" target="_blank" rel="noopener">ApJL (2024) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://aasnova.org/2024/11/06/discovery-of-a-lonely-galactic-hedgehog/" target="_blank" rel="noopener">AAS Nova &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://www.youtube.com/watch?v=-cpowWCC2-M" target="_blank" rel="noopener">Video &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="hedgehog" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-hedgehog">
        <p>Measured via surface brightness fluctuations from Legacy Surveys and deep Magellan/IMACS imaging, Hedgehog exhibits a red optical color, early-type morphology, and no UV emission. It may be a backsplash galaxy ejected from the Centaurus A group, or quenched in the field by cosmic-web ram pressure, reionization, or internal stellar feedback.</p>
      </div>
    </article>

    <!-- PopSED -->
    <article class="res-project" data-res-item data-topic="methods">
      <div class="res-project__thumb res-project__thumb--light">
        <img src="/images/research_thumbs/popsed_fig1.jpg" data-zoom-src="/images/PopSED_ICML_poster.jpeg" data-zoom-caption="PopSED framework schematic (click shows the full ICML 2023 MLxAstro poster)." alt="PopSED normalizing-flow population inference schematic">
      </div>
      <h3 class="res-project__title">
        <a href="https://scixplorer.org/abs/2024AJ....167...16L/abstract" target="_blank" rel="noopener">PopSED: Population-Level Inference from Broadband Photometry</a>
      </h3>
      <p class="res-project__summary">
        A normalizing-flow framework that infers galaxy population distributions directly from photometry by minimizing Wasserstein distance — recovering 100k galaxies in 1 GPU-hour (10<sup>6</sup>&times; faster than per-galaxy SED fitting).
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="https://scixplorer.org/abs/2024AJ....167...16L/abstract" target="_blank" rel="noopener">AJ (2024) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://github.com/AstroJacobLi/popsed" target="_blank" rel="noopener">GitHub &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://aas243-aas.ipostersessions.com/default.aspx?s=17-8B-BF-EA-85-AA-3F-8F-05-B7-9F-FD-F4-22-2F-BA&guestview=true" target="_blank" rel="noopener">AAS Poster &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="popsed" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-popsed">
        <p>Validated on mock observations and applied to GAMA galaxies at z &lt; 0.1, PopSED reliably recovers redshift, stellar mass distributions, and the star-forming main sequence directly at the population level. Our AAS 243 poster won the <a href="https://aas.org/posts/news/2023/01/congratulations-aas-243-chambliss-student-award-winners" target="_blank" rel="noopener">Chambliss Astronomy Achievement Student Award</a>.</p>
      </div>
    </article>

    <!-- Beyond UDG I & II -->
    <article class="res-project" data-res-item data-topic="dwarfs lsb">
      <div class="res-project__thumb res-project__thumb--light">
        <img src="/images/upg_images.png" data-zoom-src="/images/upg_images.png" data-zoom-caption="Ultra-puffy and ultra-diffuse galaxies around Milky Way analogs in Subaru HSC-SSP data." alt="Ultra-puffy and ultra-diffuse galaxies in HSC data">
      </div>
      <h3 class="res-project__title">
        <a href="{{ '/research/BeyondUDG/' | relative_url }}">Beyond Ultra-Diffuse Galaxies I &amp; II (Ultra-Puffy Galaxies)</a>
      </h3>
      <p class="res-project__summary">
        Using Subaru HSC-SSP, we defined &ldquo;ultra-puffy&rdquo; galaxies (UPGs) as 1.5&sigma; outliers above the mass&ndash;size relation around Milky Way analogs and showed that environmental quenching is not tied to being a mass&ndash;size outlier.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="{{ '/research/BeyondUDG/' | relative_url }}">Data Products &rarr;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://scixplorer.org/abs/2023ApJ...955....1L/abstract" target="_blank" rel="noopener">Paper I (2023) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://scixplorer.org/abs/2023ApJ...955....2L/abstract" target="_blank" rel="noopener">Paper II (2023) &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="upg" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-upg">
        <p>Defining UPGs via the mass&ndash;size relation avoids the stellar-population bias of fixed surface-brightness cuts. Across Milky Way analogs at 0.01 &lt; z &lt; 0.04, each host contains N<sub>UPG</sub> = 0.31 &plusmn; 0.05 (5% of satellites) and N<sub>UDG</sub> = 0.44 &plusmn; 0.05 (7% of satellites). Paper II shows UPGs share the same quenched fraction as normal-sized satellites, suggesting they form puffy prior to infall and quench via ram-pressure stripping.</p>
        <img src="/images/upg_quench.png" data-zoom-src="/images/upg_quench.png" data-zoom-caption="Quenched fractions of UDGs (gray), UPGs (green), and normal-sized satellites (orange) as a function of stellar mass." alt="Quenched fractions of UDGs, UPGs, and normal satellites">
        <div class="res-drawer__caption">Quenched fractions of UDGs, UPGs, and normal-sized satellites vs. stellar mass.</div>
      </div>
    </article>

    <!-- Reaching for the Edge -->
    <article class="res-project" data-res-item data-topic="lsb">
      <div class="res-project__thumb res-project__thumb--dark-contain">
        <img src="/images/research_thumbs/outskirts_thumb.jpg" data-zoom-src="/images/low-z-postage.jpg" data-zoom-caption="Five low-redshift massive galaxies compared across SDSS, DECaLS, HSC, and Dragonfly." alt="Five low-redshift massive galaxies in HSC and Dragonfly">
      </div>
      <h3 class="res-project__title">
        <a href="https://scixplorer.org/abs/2022MNRAS.515.5335L/abstract" target="_blank" rel="noopener">Reaching for the Edge: Outskirts of Massive Galaxies Across Surveys</a>
      </h3>
      <p class="res-project__summary">
        Systematic cross-survey benchmark of stellar halos in HSC, DECaLS, SDSS, and the Dragonfly Telephoto Array — reaching 30 mag/arcsec<sup>2</sup> with Dragonfly and 150&ndash;200 kpc with HSC.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="https://scixplorer.org/abs/2022MNRAS.515.5335L/abstract" target="_blank" rel="noopener">MNRAS (2022) &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="edge" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-edge">
        <p>HSC and DECaLS surface-brightness profiles of intermediate-redshift massive galaxies agree down to 28 mag/arcsec<sup>2</sup> (~100 kpc), with DECaLS recovering stellar mass within 100 kpc to 0.05 dex relative to HSC — providing a practical calibration benchmark for wide-field low-surface-brightness science.</p>
      </div>
    </article>

    <!-- Multi-Resolution Filtering -->
    <article class="res-project" data-res-item data-topic="methods">
      <div class="res-project__thumb res-project__thumb--light">
        <img src="/images/MRF-cirrus.jpg" data-zoom-src="/images/MRF-cirrus.jpg" data-zoom-caption="Multi-Resolution Filtering (MRF) isolating Galactic cirrus in Dragonfly Telephoto Array data." alt="Galactic cirrus isolated in Dragonfly data using Multi-Resolution Filtering">
      </div>
      <h3 class="res-project__title">
        <a href="https://scixplorer.org/abs/2020PASP..132g4503V/abstract" target="_blank" rel="noopener">Multi-Resolution Filtering for Faint Extended Emission</a>
      </h3>
      <p class="res-project__summary">
        An empirical, self-contained method (<code>mrf</code>) developed for the Dragonfly Telephoto Array to subtract compact sources using higher-resolution imaging and isolate faint, diffuse emission.
      </p>
      <div class="res-project__footer">
        <span class="res-links">
          <a href="https://scixplorer.org/abs/2020PASP..132g4503V/abstract" target="_blank" rel="noopener">PASP (2020) &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://github.com/AstroJacobLi/mrf" target="_blank" rel="noopener">GitHub &#8599;</a>
          <span class="res-sep">&middot;</span>
          <a href="https://mrfiltering.readthedocs.io/en/latest/" target="_blank" rel="noopener">Docs &#8599;</a>
        </span>
        <button type="button" class="res-details-btn" data-res-toggle="mrf" aria-expanded="false">Details</button>
      </div>
      <div class="res-drawer" id="drawer-mrf">
        <p>Developed with Pieter van Dokkum, <code>mrf</code> removes stars and bright galaxies down to a predefined surface-brightness threshold in low-spatial-resolution, ultra-deep imaging, while also providing a calibrated method for measuring scale-dependent surface-brightness detection limits.</p>
      </div>
    </article>

  </div>
</div>

<!-- Click-to-zoom figure modal -->
<div class="res-zoom-modal" id="res-zoom-modal" role="dialog" aria-modal="true" aria-label="Expanded figure view">
  <div class="res-zoom-modal__inner">
    <button type="button" class="res-zoom-modal__close" id="res-zoom-close" aria-label="Close figure">&times;</button>
    <img id="res-zoom-img" src="" alt="">
    <div class="res-zoom-modal__caption" id="res-zoom-caption"></div>
  </div>
</div>

<script>
(function () {
  'use strict';

  var app = document.getElementById('res-app');
  if (!app) return;

  var tabs = app.querySelectorAll('.res-tab');
  var items = app.querySelectorAll('[data-res-item]');

  function setTopic(topic) {
    tabs.forEach(function (tab) {
      var active = tab.getAttribute('data-topic') === topic;
      tab.classList.toggle('is-active', active);
      tab.setAttribute('aria-selected', active ? 'true' : 'false');
    });
    items.forEach(function (el) {
      var topics = (el.getAttribute('data-topic') || '').split(/\s+/);
      var match = (topic === 'all' || topics.indexOf(topic) !== -1);
      el.classList.toggle('is-hidden', !match);
    });
  }

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      setTopic(tab.getAttribute('data-topic'));
    });
  });

  app.querySelectorAll('[data-res-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var id = btn.getAttribute('data-res-toggle');
      var drawer = document.getElementById('drawer-' + id);
      if (!drawer) return;
      var open = drawer.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Less' : 'Details';
    });
  });

  // Click-to-zoom for figures
  var modal = document.getElementById('res-zoom-modal');
  var modalImg = document.getElementById('res-zoom-img');
  var modalCap = document.getElementById('res-zoom-caption');
  var modalClose = document.getElementById('res-zoom-close');

  app.querySelectorAll('[data-zoom-src]').forEach(function (img) {
    img.addEventListener('click', function () {
      modalImg.src = img.getAttribute('data-zoom-src');
      modalImg.alt = img.alt || '';
      modalCap.textContent = img.getAttribute('data-zoom-caption') || '';
      modal.classList.add('is-open');
    });
  });

  function closeModal() {
    modal.classList.remove('is-open');
  }

  modalClose.addEventListener('click', closeModal);
  modal.addEventListener('click', function (e) {
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
  });
})();
</script>
