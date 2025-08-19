---
layout: post
title:  "Miscellany"
date:   2018-12-16 13:40:00
author: Jiaxuan Li
categories: Coding
---


[Weber–Fechner law](https://en.wikipedia.org/wiki/Weber–Fechner_law)

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