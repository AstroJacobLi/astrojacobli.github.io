---
layout: post
title:  "Sky Surveys"
date:   2018-12-17 10:40:00
author: Jiaxuan Li
categories: Astrophysics
---

# Optical Surveys

## SDSS
The Sloan Digital Sky Survey has created the most detailed three-dimensional maps of the Universe ever made, with deep multi-color images of one third of the sky, and spectra for more than three million astronomical objects. Learn and explore all phases and surveys—past, present, and future—of the SDSS.

It's just 20 years old. See <a href="https://www.sdss.org/press-releases/sdss20/">
[The first high-z quasar of SDSS](https://twitter.com/sdssurveys/status/994412430167040000?s=21) was observed by Xiaohui Fan and Micheal Strauss on the Thanksgiving morning, 1998. 

- [DR 14 site](http://skyserver.sdss.org/dr14/en/home.aspx)
- [Navigate](http://skyserver.sdss.org/dr14/en/tools/chart/navi.aspx)
- [Search](http://skyserver.sdss.org/dr14/en/tools/search/searchhome.aspx)
- [Overview of Tutorial](https://www.sdss.org/dr12/tutorials/)
- [SDSS Image Analysis](http://shuang-astronomy.wikia.com/wiki/SDSS_Image_Analysis)
- [MPA-JHU DR7 catalogs](https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/#derived)

## DES
The [Dark Energy Survey](http://www.darkenergysurvey.org/) (DES) is a visible and near-infrared survey that aims to probe the dynamics of the expansion of the Universe and the growth of large-scale structure. The survey uses the 4-meter Victor M. Blanco Telescope located at Cerro Tololo Inter-American Observatory (CTIO) in Chile. It uses g, r, i, z, and Y bands. DECam has one of the widest fields of view (2.2-degree diameter) available for ground-based optical and infrared imaging.

It can do: [supernovae cosmology](https://arxiv.org/abs/1811.02376v1), BAO, galaxy cluster finder, [weak lensing](https://arxiv.org/abs/1708.01530), etc.

I uses [DECaLS](http://legacysurvey.org/decamls/) (DECam Legacy Survey). Dustin Lang made a wonderful [skyview map](http://legacysurvey.org/viewer#IC%20968). Currently DES is only a photometric survey.

## HSC
The [Hyper Suprime-Cam Subaru Strategic Program](https://hsc.mtk.nao.ac.jp/ssp/) (HSC-SSP) is led by the astronomical communities of Japan and Taiwan, and Princeton University. It's a photometric survey for 1400 square degrees using Hyper Suprime-Cam mounted on 8.2m [Subaru Telescope](https://subarutelescope.org). It is now the seriously kicking-ass survey for galaxies and cosmology.

The main science goals contain: [weak lensing cosmology](https://arxiv.org/abs/1809.09148v1), high-z galaxies, general galaxy formation and evolution (like [stellar-halo connection](https://arxiv.org/abs/1811.01139v1)), etc. 

HSC data entrance: [https://hscdata.mtk.nao.ac.jp/hsc_ssp/](https://hscdata.mtk.nao.ac.jp/hsc_ssp/)

SQL: [https://hscdata.mtk.nao.ac.jp/datasearch/](https://hscdata.mtk.nao.ac.jp/datasearch/)

Image cutout: [https://hscdata.mtk.nao.ac.jp/das_quarry/dr2.1/](https://hscdata.mtk.nao.ac.jp/das_quarry/dr2.1/)

PSF model: [https://hscdata.mtk.nao.ac.jp/psf/6/](https://hscdata.mtk.nao.ac.jp/das_quarry/dr2.1/)

SkyMap: [https://hscdata.mtk.nao.ac.jp/hsc_ssp/dr2/s18a/hscMap](https://hscdata.mtk.nao.ac.jp/hsc_ssp/dr2/s18a/hscMap)

HSC Public DR2: [https://hsc-release.mtk.nao.ac.jp/doc/](https://hsc-release.mtk.nao.ac.jp/doc/)

1. Header: `ra`, `dec`, `layer` (such as `s18a-wide`), `z_spec`, `z_phot`, etc.
2. `i-band`: 
   - `image`
   - `image_header`
   - `hsc_mask` (This is the binary mask produced by HSC pipeline)
   - `hsc_mask_header`
   - `variance`
   - `variance_header`
   - `mask` (This is the mask used for ELLIPSE)
   - `ell_free`
   - `ell_fix`
   - `info`
     - `img_size`: size in pix, such as [1000, 1000]
     - `m10` or `m100`
     - `bad_mask`: if the center of galaxy is obscured by mask
     - `mean_interval`: such as 20 kpc - 50 kpc
     - `mean_e`: mean ellipticity within `mean_interval`
     - `mean_pa`: mean PA within `mean_interval`
     - `global_bkg`: the background measured by `sep` after masking out satellittes
     - `global_rms`: the `rms` measured by `sep`
     - `mean_skyobj`: the mean value of `skyobj` within [1 arcmin, 3 arcmin] and 8.4 arcsec.
3. `r-band`
4. `g-band`

## Dragonfly

<a href="http://iopscience.iop.org/article/10.1086/674875/pdf">

- Canon 400mm f/2.8 IS II lens + SBIG STF-8300M CCD
- Aperture: D = 134 mm
- CCD: 3326 × 2504 pixels, 43% efficiency in R and G, 2.8"/pixel, 2.6 deg*1.9 deg FOV.
- Read noise: 10 electrons. Gain: 0.37 electrons/ADU. 
- Dark noise: 0.04 electrons/s.
- Tracking error: rms = 1.5".

## Redshift surveys

[2MASS](https://ui.adsabs.harvard.edu/#abs/2012yCat..21990026H/abstract)
[6dF](https://ui.adsabs.harvard.edu/#abs/2010yCat..73990683J/abstract)

# Transient Surveys
## Pan-STARRS
Panoramic Survey Telescope and Rapid Response System (Pan-STARRS) is a well calibrated telescope for transient surveys.

# IFU Surveys
## MaNGA survey
The current data release is v2_1_2, containing ~2700 galaxies with redshift ranges from 0 to 0.15.
- [MaNGA survey overview](https://www.sdss.org/dr13/manga/)
- [Marvin: a tool specifically designed to visualise and analyse MaNGA data.](https://dr15.sdss.org/marvin/)
- [Summary information about MaNGA objects (`fits` file)](https://data.sdss.org/sas/dr14/manga/spectro/redux/v2_1_2/drpall-v2_1_2.fits). You can search in this file whether your objects are contained in current MaNGA data release. You can also using SDSS `navigate` and `explore` tool to see whether your objects are contained in MaNGA.
- [MaNGA Pipe3D Value-Added-Catalogue](https://www.sdss.org/dr14/data_access/value-added-catalogs/?vac_id=manga-pipe3d-value-added-catalog-spatially-resolved-and-integrated-properties-of-galaxies) by Sanchez et al. This is what I use in my research. This VAC catalog contains the physical properties and also information of gas emission lines. _Note: The SFR in this catalog is calculated by summing up H⍺ SFR of every spaxel in the FOV. So the genuine SFR must be larger. The IMF used here is Salpeter, while the most prevalent IMF is Kroupa IMF.
- [MaNGA cube files](https://data.sdss.org/sas/dr14/manga/spectro/pipe3d/v2_1_2/2.1.2/), if you want to study the properties of specific galaxies.

## SAMI survey
- [SAMI survey overview](https://sami-survey.org)
- [SAMI objects list](https://sami-survey.org/system/files/attachments/403/sami_sel_20140413_v1.9_publiclist): can be opened with `.txt` using TOPCAT. 
- [SAMI single object viewer](https://datacentral.org.au/services/sov/): better GUI than MaNGA. After finding your objects in the SAMI objects list, you can just input the `CATID`, then related files can be downloaded.
- [SAMI data query using SQL](https://datacentral.org.au/services/query/)

## CALIFA survey
- [CALIFA overview](http://califa.caha.es)
- [CALIFA DR3 search tool](http://www.caha.es/CALIFA/public_html/?q=content/califa-3rd-data-release-searching-tool-mac-users)
- [PyCASSO database: spatially resolved stellar population properties for CALIFA galaxies](https://academic.oup.com/mnras/article-abstract/471/3/3727/3979019)