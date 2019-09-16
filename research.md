---
layout: page
title: Research
permalink: /research/
---

# Astrophysics
## Inside-out quenching galaxies with H$$\alpha$$ ring-like structures
### Advisor: [**Yingjie Peng**](http://kiaa.pku.edu.cn/people/yingjie-peng)

{% include image.html url="/images/Ha-ring.png" caption="H-alpha ring galaxies in MaNGA" width=400 align="right" %}

We investigated galaxies with H$$\alpha$$ emission ring-like structures in Mapping Nearby Galaxies at APO (MaNGA) survey, with stellar mass in the range $$9 <\log(M/M_\odot) < 12$$. These galaxies are almost
located in the green valley on SFR-stellar mass plane. The radius of H$$\alpha$$ rings are measured and good
linear relations between bar length and H$$\alpha$$ ring radius are found. We reveal that the appearance of H$$\alpha$$ star-forming ring-like structure has a strong correlation with bar-induced activities, but not with active galactic nuclei (AGN). The majority of our H$$\alpha$$ ring galaxy sample are galaxies which are classified as LINER with EW(H$$\alpha)< 3$$Å. Low luminosity AGN possibly plays a role in inside-out quenching accompanying with H$$\alpha$$ ring-like structure. Morphological quenching and bulge show less relation with H$$\alpha$$ ring galaxies.

# Physics
## Quantifying Faraday Pattern and Onset Amplitude of Fluid with NMF and 2PCF Algorithms
### Author: Jiaxuan Li & Xiaoyi Ouyang

{% include image.html url="/images/Faraday1.png" caption="Faraday patterns" width=400 align="right" %}


We reviewed theories on weakly nonlinear region of Faraday pattern, arriving at an approximate expression for dispersion relation and a rough explanation for hysteresis. A common predicament concerning experiments of surface wave originates from quantification of physical quantities, e.g. wavelength. We intend to apply two algorithms (i.e. NMF and 2PCF) to quantify experimental data given their unique features. In order to test the algorithms' efficacy, we further investigate the _dipole_ oscillation pattern of milk under weak forcing and weak damping condition. Since dispersion relation is well-characterized in this case, we can compare dispersion relation obtained from NMF and 2PCF with theorical one.

{% include image.html url="/images/Faraday2.png" caption="Acceleration-driven frequency relation" width=300 align="left" %}
<br>
<br>
 The fitted $$T/\rho$$ coincides with literature quite well. Then we focus on onset amplitude of Faraday waves and discuss on the source of unexpected hysteresis. The theoretical $$\Omega$$-$$k$$ relation and acceleration-$$\Omega$$ relation fit the experiment data well and parameters are in appropriate range.

<br>
<br>
<br>
<br>
<br>
<br>

# Software Development
- [**mrf**](https://mrfiltering.readthedocs.io/en/latest/): Multi-Resolution Filtering is a method for isolating faint, extended emission in Dragonfly data and other low resolution images, developed by [Pieter van Dokkum](http://pietervandokkum.com) and [Jiaxuan Li](http://astrojacobli.github.io).

- [**unagi**](https://github.com/dr-guangtou/unagi): Search and download data from Hyper Suprime-Cam (HSC) Subaru Strategic Survey (SSP), developed by [Song Huang](http://dr-guangtou.github.io), [Jiaxuan Li](http://astrojacobli.github.io) and contributors.

- [**kungpao**](https://github.com/dr-guangtou/kungpao): Photometric analysis library for Hyper Suprime Camera (HSC) images, developed by [Song Huang](http://dr-guangtou.github.io) and [Jiaxuan Li](http://astrojacobli.github.io).

- [**lvhuo**](https://github.com/dr-guangtou/lvhuo): Image stacking analysis for Hyper Suprime-Cam data, developed by [Jiaxuan Li](http://astrojacobli.github.io) and [Song Huang](http://dr-guangtou.github.io).

- [**slug**](https://github.com/AstroJacobLi/slug): Integrated tool for calculating 1-D surface brightness profile of massive galaxies, developed by [Jiaxuan Li](http://astrojacobli.github.io).

- Some of my works can be found on Github: [**@AstroJacobLi**](https://github.com/AstroJacobLi). Please star if you like them!

<!-- https://ionicabizau.github.io/github-calendar/example/ -->
<!-- Include the library. -->
<script
  src="https://unpkg.com/github-calendar@latest/dist/github-calendar.min.js"
></script>

<!-- Optionally, include the theme (if you don't want to struggle to write the CSS) -->
<link
   rel="stylesheet"
   href="https://unpkg.com/github-calendar@latest/dist/github-calendar-responsive.css"
/>

<!-- Prepare a container for your calendar. -->
<div class="calendar">
    <!-- Loading stuff -->
    Loading the data just for you.
</div>

<script>
    GitHubCalendar(".calendar", "astrojacobli");
    // or enable responsive functionality
    GitHubCalendar(".calendar", "astrojacobli", { responsive: true });
</script>