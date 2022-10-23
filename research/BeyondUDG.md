---
layout: page
# title: Research
permalink: /research/BeyondUDG/
---
<head>
    <link rel="stylesheet" type="text/css" href="../../css/display.css">
    <style>
    .galaxies {
      padding: 10px;
      }
    </style>
</head>

## Beyond Ultra-Diffuse Galaxies I: Mass-Size Outliers Among the Satellites of Milky Way Analogs

### Cutout Images of UPGs and UDGs
You can enjoy the beautiful cutout images of UDGs and UPGs using the image visualization tool developed by Yao-Yuan Mao. Click the link below!!! 
- Mosaic of <a class="pku_style" href="http://jiaxuanli.me/galary/BeyondUDG/UPG.html">UPGs</a>
- Mosaic of <a class="pku_style" href="http://jiaxuanli.me/galary/BeyondUDG/UDG.html">UDGs</a>

Users can click "--> Choose image source <--" and select the desired image source. ``HSC-SSP PDR2`` is recommended to see the low surface brightness outskirts of these galaxies. Hovering over the image will display the coordinates and ID of the galaxy. It takes several minutes to load all the images for the first time. When clicking on the individual image, the user will be redirected to the corresponding coordinate in the Legacy Survey Viewer. Here we show several UPGs and UDGs as eye candies :) 

<h4>Ultra-puffy galaxies (UPGs)</h4>
<div class='galaxies'>
    <ul class="small-block-grid-5">
        <li>
        <img class="pic  " title="viz-id = 14681
ra = 18.949017
dec = -0.7763651" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=18.949017&amp;dec=-0.7763651&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
        </li>
        <li>
      <img class="pic  " title="viz-id = 44907
ra = 217.3622571
dec = -0.1367947" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=217.3622571&amp;dec=-0.1367947&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
      <li>
      <img class="pic  " title="viz-id = 85963
ra = 37.683083
dec = -4.6020238" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=37.683083&amp;dec=-4.6020238&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
      <li>
      <img class="pic  " title="viz-id = 44517
ra = 18.3238671
dec = -0.2380388" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=18.3238671&amp;dec=-0.2380388&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
      <li>
       <img class="pic  " title="viz-id = 19656
ra = 220.7369959
dec = 0.2805017" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=220.7369959&amp;dec=0.2805017&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
	</ul>
</div>


<h4>Ultra-diffuse galaxies (UDGs)</h4>
<div class='galaxies'>
    <ul class="small-block-grid-5">
        <li>
        <img class="pic  " title="viz-id = 1984
ra = 189.9153345
dec = 0.8239197" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=189.9153345&amp;dec=0.8239197&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
        </li>
        <li>
     <img class="pic  " title="viz-id = 73112
ra = 151.3453846
dec = 0.5119705" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=151.3453846&amp;dec=0.5119705&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
      <li>
       <img class="pic  " title="viz-id = 69381
ra = 29.1199043
dec = -4.5306946" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=29.1199043&amp;dec=-4.5306946&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
      <li>
      <img class="pic  " title="viz-id = 55342
ra = 179.7553824
dec = -1.8056669" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=179.7553824&amp;dec=-1.8056669&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
      <li>
      <img class="pic  " title="viz-id = 11065
ra = 237.7386258
dec = 42.6750964" src="https://www.legacysurvey.org/viewer/cutout.jpg?ra=237.7386258&amp;dec=42.6750964&amp;pixscale=0.1666667&amp;layer=hsc-dr2&amp;size=180" width="180" height="180">
      </li>
	</ul>
</div>


### Catalogs and Data
We make the following catalogs and data available for public use. The catalogs are in the CDS format. One can load the data following the instruction of [``astropy``](https://docs.astropy.org/en/stable/api/astropy.io.ascii.Cds.html). A detailed description of the catalog can be found in Table 3 of Paper I. Note that we haven't done any background contamination correction in the following catalogs.
- [Catalog of ultra-puffy galaxies (UPGs)](https://github.com/AstroJacobLi/kuaizi/blob/master/data/BeyondUDG/upg_cds.dat)
- [Catalog of ultra-diffuse galaxies (UDGs)](https://github.com/AstroJacobLi/kuaizi/blob/master/data/BeyondUDG/udg_cds.dat)

As described in Section 3.4, we apply a bias correction to the measurements of size, total magnitude, surface brightness, and color. The bias has already been corrected in the above catalog. For transparency and reproducibility, here we provide the bias terms in the following files. The bias is defined as ``bias = truth - measurement`` and is consistent with Figure 4. One can derive the original measurements by subtracting the bias term from the catalogued values.
- [Bias terms of UPGS](https://github.com/AstroJacobLi/kuaizi/blob/master/data/BeyondUDG/upg_bias.fits)
- [Bias terms of UDGs](https://github.com/AstroJacobLi/kuaizi/blob/master/data/BeyondUDG/udg_bias.fits)

We also provide the catalogs of "fake" UDGs and UPGs. They are used to derive the background contamination fraction in Section 4.3. 
- [Catalog of fake UPGs](https://github.com/AstroJacobLi/kuaizi/blob/master/data/BeyondUDG/fake_upg_cat_1.5sigma_220726.fits)
- [Catalog of fake UDGs](https://github.com/AstroJacobLi/kuaizi/blob/master/data/BeyondUDG/fake_udg_cat_220726.fits)


