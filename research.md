---
layout: page
title: Research
permalink: /research/
---

## Astrophysics

### Multi-resolution filtering: an empirical method for isolating faint, extended emission in Dragonfly data and other low resolution images
#### Advisor: [Pieter van Dokkum (Yale)](http://pietervandokkum.com)
We developed an empirical, self-contained method "Multi-resolution filtering" (MRF) to isolate and study faint, large-scale emission in imaging data of low spatial resolution. The method was developed for the Dragonfly Telephoto Array, which produces images that have excellent low surface brightness sensitivity but poor spatial resolution. The resulting image only contains emission fainter than a pre-defined surface brightness limit. The method is implemented in [$$\texttt{mrf}$$](https://github.com/AstroJacobLi/mrf), an open-source MIT licensed Python package. It also contains an well-defined method to determine the surface brightness detection limit on a certain scale. This work is crucial for the future sciences of Dragonfly surveys. Please see [van Dokkum et al. 2019](https://ui.adsabs.harvard.edu/abs/2019arXiv191012867V/abstract) for more details. 
{% include image.html url="/images/MRF-cirrus.png" caption="MRF reveals Galactic cirrus clearly in Dragonfly data (Danieli et al. 2019)" width=720 align="center" %}
<br>

### Reaching for the Edge I: Probing the Outskirts of Massive Galaxies with HSC, DECaLS, SDSS and Dragonfly
{% include image.html url="/images/low-z-postage.jpg" caption="Images of five low redshift massive galaxies in four different surveys" width=420 align="right" %}
#### Advisors: [Alexie Leauthaud (UCSC)](http://alexie.sites.ucsc.edu), [Song Huang (Princeton)](http://dr-guangtou.github.io)
We compared the abilities to detect massive galaxy outskirts and related systematics for Hyper Suprime-Cam (HSC), Dark Energy Camera Legacy Survey (DECaLS), Dragonfly Telephoto Array and SDSS. Dragonfly shows outstanding ability on recovering outskirts of low-$$z$$ bright galaxies to $$30\ \mathrm{mag/arcsec^2}$$. HSC could reach farther than 150 kpc for individual galaxy and 200 kpc for a galaxy ensemble. Good agreements are achieved between HSC and DECaLS profiles of intermediate-$$z$$ galaxies down to $$28\ \mathrm{mag/arcsec^2}\ (\sim100\ \mathrm{kpc})$$. DECaLS is able to recover the stellar mass within 100 kpc from HSC by only 0.05 dex. This work serves as a good reference for low surface brightness studies using different datasets and benefits future sky surveys. 

🔗[**Paper Draft**](https://astrojacobli.github.io/publications/JLi_et_al_Galaxy_Outskirts.pdf)

<br>

### Inside-out quenching galaxies with H$$\alpha$$ ring-like structures
#### Advisor: [Yingjie Peng (KIAA)](http://kiaa.pku.edu.cn/people/yingjie-peng)

{% include image.html url="/images/Ha-ring.png" caption="H-alpha ring galaxies in MaNGA" width=400 align="right" %}

We investigated galaxies with H$$\alpha$$ emission ring-like structures in Mapping Nearby Galaxies at APO (MaNGA) survey, with the stellar mass in the range of $$10.0<\log(M/M_\odot)<11.5$$. They are located in the "green valley" and experiencing the inside-out quenching process. We measure the radii of H$$\alpha$$ rings and find that bars are just stuck in the H$$\alpha$$ rings. High bar fraction, high AGN (Seyfert/LINER) fraction and high bulge-to-total ratio support that the joint effects of bar, bulge and AGN could quench the massive disk galaxies efficiently by the inside-out quenching mode and form the H$$\alpha$$ ring-like structure.

🔗<a class="tosu" href="https://astrojacobli.github.io/publications/JLi_et_al_inside_out_quenching_H_alpha_ring.pdf">Paper Draft</a>

<br>

## Physics
### Quantifying Faraday Pattern and Onset Amplitude of Fluid with NMF and 2PCF Algorithms
#### Author: Jiaxuan Li (PKU) & Xiaoyi Ouyang (PKU)

{% include image.html url="/images/Faraday1.png" caption="Faraday patterns" width=400 align="right" %}
We reviewed theories on weakly nonlinear region of Faraday pattern, arriving at an approximate expression for dispersion relation and a rough explanation for hysteresis. A common predicament concerning experiments of surface wave originates from quantification of physical quantities, e.g. wavelength. We intend to apply two algorithms (i.e. NMF and 2PCF) to quantify experimental data given their unique features. In order to test the algorithms' efficacy, we further investigate the _dipole_ oscillation pattern of milk under weak forcing and weak damping condition. Since dispersion relation is well-characterized in this case, we can compare dispersion relation obtained from NMF and 2PCF with the theoretical one. The fitted $$T/\rho$$ coincides with literature quite well. Then we focus on onset amplitude of Faraday waves and discuss on the source of unexpected hysteresis. The theoretical $$\Omega$$-$$k$$ relation and acceleration-$$\Omega$$ relation fit the experiment data well and parameters are in appropriate range.

<br>
<br>

## Software Development
- [**mrf**](https://mrfiltering.readthedocs.io/en/latest/): Multi-Resolution Filtering is a method for isolating faint, extended emission in Dragonfly data and other low resolution images, developed by [Pieter van Dokkum](http://pietervandokkum.com) and [Jiaxuan Li](http://astrojacobli.github.io).

- [**unagi**](https://github.com/dr-guangtou/unagi): Search and download data from Hyper Suprime-Cam (HSC) Subaru Strategic Survey (SSP), developed by [Song Huang](http://dr-guangtou.github.io), [Jiaxuan Li](http://astrojacobli.github.io) and contributors.

- [**kungpao**](https://github.com/dr-guangtou/kungpao): Photometric analysis library for Hyper Suprime Camera (HSC) images, developed by [Song Huang](http://dr-guangtou.github.io) and [Jiaxuan Li](http://astrojacobli.github.io).

- [**lvhuo**](https://github.com/dr-guangtou/lvhuo): Image stacking analysis for Hyper Suprime-Cam data, developed by [Jiaxuan Li](http://astrojacobli.github.io) and [Song Huang](http://dr-guangtou.github.io).

- [**slug**](https://github.com/AstroJacobLi/slug): Integrated tool for calculating 1-D surface brightness profile of massive galaxies, developed by [Jiaxuan Li](http://astrojacobli.github.io).

- More works can be found on Github: [**@AstroJacobLi**](https://github.com/AstroJacobLi). Please star if you like them!

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