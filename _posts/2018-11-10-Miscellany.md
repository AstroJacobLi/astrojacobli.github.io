---
layout: post
title:  "Miscellany"
date:   2018-11-10 00:40:00
author: Jiaxuan Li
categories: Coding
---

## [Set up a Macbook for Astronomy](https://github.com/AstroJacobLi/astro-ph/wiki/Macbook-for-Astronomy)

# IFU surveys
## MaNGA survey
The current data release is v2_1_2, containing ~2700 galaxies with $$0<z<0.15$$.

- [MaNGA survey overview](https://www.sdss.org/dr13/manga/)

- [Summary information about MaNGA objects (`fits` file)](https://data.sdss.org/sas/dr14/manga/spectro/redux/v2_1_2/drpall-v2_1_2.fits). You can search in this file whether your objects are contained in current MaNGA data release. You can also using SDSS `navigate` and `explore` tool to see whether your objects are contained in MaNGA.

- [MaNGA Pipe3D Value-Added-Catalogue](https://www.sdss.org/dr14/data_access/
value-added-catalogs/?vac_id=manga-pipe3d-value-added-catalog-spatially-resolved-and-integrated-properties-of-galaxies) by Sanchez et al. This is what I use in my research. This VAC catalog contains the physical properties and also information of gas emission lines. _Note: The SFR in this catalog is calculated by summing up H⍺ SFR of every spaxel in the FOV. So the genuine SFR must be larger. The IMF used here is Salpeter, while the most prevalent IMF is Kroupa IMF.

- [MaNGA cube files](https://data.sdss.org/sas/dr14/manga/spectro/pipe3d/v2_1_2/2.1.2/), if you want to study the properties of specific galaxies.

## SAMI survey
- [SAMI survey overview](https://sami-survey.org)
- [SAMI objects list](https://sami-survey.org/system/files/attachments/403/sami_sel_20140413_v1.9_publiclist): can be opened with `.txt` using TOPCAT. 
- [SAMI single object viewer](https://datacentral.org.au/services/sov/): better GUI than MaNGA. After finding your objects in the SAMI objects list, you can just input the `CATID`, then related files can be downloaded.
- [SAMI data query using SQL](https://datacentral.org.au/services/query/)

## CALIFA survey
- [CALIFA overview](http://califa.caha.es)
- [CALIFA DR3 search tool](http://www.caha.es/CALIFA/public_html/?q=content/califa-3rd-data-release-searching-tool-mac-users)


***


XKCD style of Mathematica plot: [https://mathematica.stackexchange.com/questions/11350/xkcd-style-plots](https://mathematica.stackexchange.com/questions/11350/xkcd-style-plots)

XKCD style of Matplotlib (bug for line labels): [http://jakevdp.github.io/blog/2012/10/07/xkcd-style-plots-in-matplotlib/#The-Code:-XKCDify](http://jakevdp.github.io/blog/2012/10/07/xkcd-style-plots-in-matplotlib/#The-Code:-XKCDify). This code must run under python2 environment.

A good example of 2D Histogram using astroML: [http://www.astroml.org/examples/datasets/plot_SDSS_SSPP.html](http://www.astroml.org/examples/datasets/plot_SDSS_SSPP.html)

Convert Jupyter Notebook to `html`: `jupyter nbconvert --to html low-z-galaxy-survey.ipynb `

Convert LaTeX to html gif picture: [https://www.codecogs.com/latex/eqneditor.php](https://www.codecogs.com/latex/eqneditor.php)

***

Mac录屏的同时录制声音：[https://www.jianshu.com/p/a8ff665285de](https://www.jianshu.com/p/a8ff665285de)

A good website to check visibility for a given RA and DEC: [http://catserver.ing.iac.es/staralt/](http://catserver.ing.iac.es/staralt/)

**Convert figure to data points**: [http://markummitchell.github.io/engauge-digitizer/](http://markummitchell.github.io/engauge-digitizer/)


#### How to use latex in jekyll?
- gem install kramdown
- Change the markdown line in _config.yml to markdown: kramdown
- And add something like

```javascript
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```
to `_layouts/default.html`. Now you can simply mark any mathematics in your posts with `$$`

***

Princeton Program: [https://international.princeton.edu/international-students-and-scholars/International-Student-Internship-Program](https://international.princeton.edu/international-students-and-scholars/International-Student-Internship-Program)