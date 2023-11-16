---
layout: page
title: Research
permalink: /research/
---

#### [Link to my publications in ADS](https://ui.adsabs.harvard.edu/public-libraries/hymVHtQ2TveZ5t3VzwQYzg)

### PopSED: Population-Level Inference for Galaxy Properties from Broadband Photometry with Neural Density Estimation

{% include image.html url="/images/PopSED_ICML_poster.jpeg" caption="Poster of PopSED for the [MLxAstro workshop](https://ml4astro.github.io/icml2023/assets/29.pdf) in 2023 ICML" width=450 align="right"%}

In [Li et al. (2023c)](https://ui.adsabs.harvard.edu/abs/2023arXiv230916958L/abstract), we present PopSED, a framework for population-level inference of galaxy properties from photometric data. Unlike the traditional approach of first analyzing individual galaxies and then combining the results to determine the physical properties of the entire galaxy population, we directly make the population distribution the inference objective. We train **normalizing flows** to approximate the population distribution by minimizing the Wasserstein distance between the synthetic photometry of the galaxy population and the observed data. We validate our method using mock observations and apply it to galaxies from the GAMA survey. PopSED reliably recovers the redshift and stellar mass distribution of 100K galaxies using broadband photometry within 1 GPU-hour, being **1 million times faster** than the traditional SED modeling method. From the population posterior we also recover the star-forming main sequence for GAMA galaxies at $z<0.1$. With the unprecedented number of galaxies in upcoming surveys, our method offers an efficient tool for studying galaxy evolution and deriving redshift distributions for cosmological analyses.

The code <tt>[popsed](https://github.com/AstroJacobLi/popsed)</tt> is available on <a href="https://github.com/AstroJacobLi/popsed"><font color="FF00CC">GitHub</font></a>. If you have any questions, please feel free to open an issue on GitHub or contact me via email.

<br><br><br>

### Beyond Ultra-Diffuse Galaxies II: Environmental Quenching of Mass-Size Outliers Among the Satellites of Milky Way Analogs

{% include image.html url="/images/upg_quench.png" caption="The quenched fractions of UDGs (gray), UPGs (green), normal-sized satellites (orange) as a function of stellar mass." width=450 align="right" %}

In [Paper I (Li et al. 2023a)](https://arxiv.org/abs/2210.14994), we present a sample of large diffuse galaxies (i.e., ultra-diffuse and ultra-puffy galaxies) around Milky-Way analogs using the exquisitely deep and wide Hyper Suprime-Cam Strategic Survey images. As a follow-up study, in this [Paper II (Li et al. 2023b)](https://arxiv.org/abs/2302.14108), we explore the statistical characteristics of these mass-size outliers, including their size distribution, spatial distribution, and most importantly, their star formation status. By comparing these distributions with normal satellites of MW analogs, we learn about how mass-size outliers form, and how their star formation is tied to their exotic sizes. We find that, once using the appropriate way to construct the mass-size outlier sample (i.e., selecting then based on the mass-size relation, instead of hard cuts on size or surface brightness), the quenched fraction (the fraction of galaxies that are quiescent in star formation) of mass-size outliers is very similar to normal-sized satellites. This hints that **quenching is not tied to being a mass-size outlier**. We discuss the possibility where mass-size outliers are formed prior to falling into the current host, and are quenched together with normal-sized dwarfs via ram pressure stripping. The next step is to find ultra-puffy galaxies in simulations, where we can study their formation and evolution in detail.



### Beyond Ultra-Diffuse Galaxies I: Mass-Size Outliers Among the Satellites of Milky Way Analogs

{% include image.html url="/images/upg_images.png" caption="Ultra-puffy and ultra-diffuse galaxies in HSC data" width=620 align="center" %}

Large diffuse galaxies are hard to find, but understanding the environments where they live, their numbers, and ultimately their origins, is of intense interest and importance for galaxy formation and evolution. In [Paper I (Li et al. 2023a)](https://arxiv.org/abs/2210.14994), we propose a new concept of "ultra-puffy" galaxies (UPGs), defined to be $$1.5\sigma$$ above the average mass-size relation. We argue that our definition for ultra-puffy galaxies, based on the mass-size relation, better represent the tail of the satellite size distribution. It is also more physically-motivated than the common definition of ultra-diffuse galaxies (UDGs), which depends on surface brightness and size cuts and thus yields different surface mass density cuts for quenched and star-forming galaxies.

Using Subaru's Hyper Suprime-Cam Strategic Survey Program, we perform a systematic search for low surface brightness galaxies, and present samples of UPGs and UDGs associated with Milky-Way analogs at $$0.01 < z < 0.04$$. The data products are available [here](http://jiaxuanli.me/research/BeyondUDG/). We find that each MW analog hosts $$N_{\rm UPG}=0.31±0.05$$ ultra-puffy galaxies on average, which is consistent with but slightly lower than the observed abundance at this halo mass in the Local Volume. The UDG abundance $$N_{\rm UDG}=0.44±0.05$$ agrees with local measurements quite well. On average, 7% of the satellites in MW analogs are UDGs, and 5% of the satellites are UPGs. In [Paper II (Li et al. 2023b)](https://arxiv.org/abs/2302.14108), we present the size and spatial distributions of UPGs and their star formation status.

<br>

### Reaching for the Edge I: Probing the Outskirts of Massive Galaxies with HSC, DECaLS, SDSS, and Dragonfly
In [Li et al. (2022a)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.515.5335L/abstract), we compared the abilities to detect massive galaxy outskirts and related systematics for Hyper Suprime-Cam (HSC), Dark Energy Camera Legacy Survey (DECaLS), Dragonfly Telephoto Array and SDSS. Dragonfly shows outstanding ability on recovering outskirts of low-$$z$$ bright galaxies to $$30\ \mathrm{mag/arcsec^2}$$. HSC could reach farther than 150 kpc for individual galaxy and 200 kpc for a galaxy ensemble. Good agreements are achieved between HSC and DECaLS profiles of intermediate-$$z$$ galaxies down to $$28\ \mathrm{mag/arcsec^2}\ (\sim100\ \mathrm{kpc})$$. DECaLS is able to recover the stellar mass within 100 kpc from HSC by only 0.05 dex. This work serves as a good reference for low surface brightness studies using different datasets and benefits future sky surveys.

{% include image.html url="/images/low-z-postage.jpg" caption="Images of five low redshift massive galaxies in four different surveys" width=720 align="center" %}



### Multi-resolution filtering: an empirical method for isolating faint, extended emission in Dragonfly data and other low resolution images
We developed an empirical, self-contained method "Multi-resolution filtering" (MRF) to isolate and study faint, large-scale emission in imaging data of low spatial resolution. The method was developed for the Dragonfly Telephoto Array, which produces images that have excellent low surface brightness sensitivity but poor spatial resolution. The resulting image only contains emission fainter than a pre-defined surface brightness limit. The method is implemented in [$$\texttt{mrf}$$](https://github.com/AstroJacobLi/mrf), an open-source MIT licensed Python package. It also contains an well-defined method to determine the surface brightness detection limit on a certain scale. This work is crucial for the future sciences of Dragonfly surveys. Please see [van Dokkum et al. 2019](https://ui.adsabs.harvard.edu/abs/2019arXiv191012867V/abstract) for more details. 
{% include image.html url="/images/MRF-cirrus.jpg" caption="MRF reveals Galactic cirrus clearly in Dragonfly data (Danieli et al. 2019)" width=720 align="center" %}
<br>
<br>

### Inside-out quenching galaxies with H$$\alpha$$ ring-like structures
{% include image.html url="/images/Ha-ring.png" caption="H-alpha ring galaxies in MaNGA" width=400 align="right" %}
We investigated galaxies with H$$\alpha$$ emission ring-like structures in Mapping Nearby Galaxies at APO (MaNGA) survey, with the stellar mass in the range of $$10.0<\log(M/M_\odot)<11.5$$. They are located in the "green valley" and experiencing the inside-out quenching process. We measure the radii of H$$\alpha$$ rings and find that bars are just stuck in the H$$\alpha$$ rings. High bar fraction, high AGN (Seyfert/LINER) fraction and high bulge-to-total ratio support that the joint effects of bar, bulge and AGN could quench the massive disk galaxies efficiently by the inside-out quenching mode and form the H$$\alpha$$ ring-like structure.
🔗<a class="tosu" href="https://astrojacobli.github.io/publications/JLi_et_al_inside_out_quenching_H_alpha_ring.pdf">Paper Draft</a>

<br>

## Software Development
- [**smplotlib**](https://github.com/AstroJacobLi/smplotlib): Matplotlib template for SuperMongo style. Just one line of code to make your plot look like SuperMongo! [Also see a thread on Twitter](https://twitter.com/AstroJacobLi/status/1646724338723192832)

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