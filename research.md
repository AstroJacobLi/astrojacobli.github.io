---
layout: page
title: Research
permalink: /research/
---

#### [Link to my publications in ADS](https://ui.adsabs.harvard.edu/public-libraries/hymVHtQ2TveZ5t3VzwQYzg)


## Astrophysics

### Beyond Ultra-Diffuse Galaxies: Mass-Size Outliers Among the Satellites of Milky Way Analogs

Large diffuse galaxies are hard to find, but understanding the environments where they live, their numbers, and ultimately their origins, is of intense interest and importance for galaxy formation and evolution. In [Paper I (Li et al. 2022b)](https://arxiv.org/abs/2210.14994), we propose a new concept of "ultra-puffy" galaxies (UPGs), defined to be $$1.5\sigma$$ above the average mass-size relation. We argue that our definition for ultra-puffy galaxies, based on the mass-size relation, better represent the tail of the satellite size distribution. It is also more physically-motivated than the common definition of ultra-diffuse galaxies (UDGs), which depends on surface brightness and size cuts and thus yields different surface mass density cuts for quenched and star-forming galaxies.

Using Subaru's Hyper Suprime-Cam Strategic Survey Program, we perform a systematic search for low surface brightness galaxies, and present samples of UPGs and UDGs associated with Milky-Way analogs at $$0.01 < z < 0.04$$. The data products are available [here](http://jiaxuanli.me/research/BeyondUDG/). We find that each MW analog hosts $$N_{\rm UPG}=0.31±0.05$$ ultra-puffy galaxies on average, which is consistent with but slightly lower than the observed abundance at this halo mass in the Local Volume. The UDG abundance $$N_{\rm UDG}=0.44±0.05$$ agrees with local measurements quite well. On average, 7% of the satellites in MW analogs are UDGs, and 5% of the satellites are UPGs. In the upcoming Paper II (to be submitted), we will present the size and spatial distributions of UPGs and their star formation status.

{% include image.html url="/images/upg_images.png" caption="Ultra-puffy and ultra-diffuse galaxies in HSC data" width=620 align="center" %}


<br>

### Reaching for the Edge I: Probing the Outskirts of Massive Galaxies with HSC, DECaLS, SDSS and Dragonfly
{% include image.html url="/images/low-z-postage.jpg" caption="Images of five low redshift massive galaxies in four different surveys" width=420 align="right" %}
#### Advisors: [Alexie Leauthaud (UCSC)](http://alexie.sites.ucsc.edu), [Song Huang (Princeton)](http://dr-guangtou.github.io)
In [Li et al. (2022a)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.515.5335L/abstract), we compared the abilities to detect massive galaxy outskirts and related systematics for Hyper Suprime-Cam (HSC), Dark Energy Camera Legacy Survey (DECaLS), Dragonfly Telephoto Array and SDSS. Dragonfly shows outstanding ability on recovering outskirts of low-$$z$$ bright galaxies to $$30\ \mathrm{mag/arcsec^2}$$. HSC could reach farther than 150 kpc for individual galaxy and 200 kpc for a galaxy ensemble. Good agreements are achieved between HSC and DECaLS profiles of intermediate-$$z$$ galaxies down to $$28\ \mathrm{mag/arcsec^2}\ (\sim100\ \mathrm{kpc})$$. DECaLS is able to recover the stellar mass within 100 kpc from HSC by only 0.05 dex. This work serves as a good reference for low surface brightness studies using different datasets and benefits future sky surveys. 



### Multi-resolution filtering: an empirical method for isolating faint, extended emission in Dragonfly data and other low resolution images
#### Advisor: [Pieter van Dokkum (Yale)](http://pietervandokkum.com)
We developed an empirical, self-contained method "Multi-resolution filtering" (MRF) to isolate and study faint, large-scale emission in imaging data of low spatial resolution. The method was developed for the Dragonfly Telephoto Array, which produces images that have excellent low surface brightness sensitivity but poor spatial resolution. The resulting image only contains emission fainter than a pre-defined surface brightness limit. The method is implemented in [$$\texttt{mrf}$$](https://github.com/AstroJacobLi/mrf), an open-source MIT licensed Python package. It also contains an well-defined method to determine the surface brightness detection limit on a certain scale. This work is crucial for the future sciences of Dragonfly surveys. Please see [van Dokkum et al. 2019](https://ui.adsabs.harvard.edu/abs/2019arXiv191012867V/abstract) for more details. 
{% include image.html url="/images/MRF-cirrus.jpg" caption="MRF reveals Galactic cirrus clearly in Dragonfly data (Danieli et al. 2019)" width=720 align="center" %}
<br>
<br>

### Inside-out quenching galaxies with H$$\alpha$$ ring-like structures
#### Advisor: [Yingjie Peng (KIAA)](http://kiaa.pku.edu.cn/people/yingjie-peng)

{% include image.html url="/images/Ha-ring.png" caption="H-alpha ring galaxies in MaNGA" width=400 align="right" %}

We investigated galaxies with H$$\alpha$$ emission ring-like structures in Mapping Nearby Galaxies at APO (MaNGA) survey, with the stellar mass in the range of $$10.0<\log(M/M_\odot)<11.5$$. They are located in the "green valley" and experiencing the inside-out quenching process. We measure the radii of H$$\alpha$$ rings and find that bars are just stuck in the H$$\alpha$$ rings. High bar fraction, high AGN (Seyfert/LINER) fraction and high bulge-to-total ratio support that the joint effects of bar, bulge and AGN could quench the massive disk galaxies efficiently by the inside-out quenching mode and form the H$$\alpha$$ ring-like structure.

🔗<a class="tosu" href="https://astrojacobli.github.io/publications/JLi_et_al_inside_out_quenching_H_alpha_ring.pdf">Paper Draft</a>

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