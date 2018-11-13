---
layout: post
title:  "IFU Surveys"
date:   2018-11-13 00:40:00
author: Jiaxuan Li
categories: Astrophysics
---

# IFU surveys
## MaNGA survey
The current data release is v2_1_2, containing ~2700 galaxies with 0<z<0.15.
- [MaNGA survey overview](https://www.sdss.org/dr13/manga/)
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