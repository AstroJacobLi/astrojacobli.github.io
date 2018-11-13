---
layout: post
title:  "Statistics and Python"
date:   2018-10-18 00:40:00
author: Jiaxuan Li
categories: Coding
---

# David Hogg's paper on Statistics

### [Data analysis recipes: Fitting a model to data](https://arxiv.org/abs/1008.4686)
### [Data analysis recipes: Probability calculus for inference](https://arxiv.org/abs/1205.4446v1)

***
### Useful python packages:
- [`healpy`](https://healpy.readthedocs.io/en/latest/install.html): It is a package dealing with data on a sphere. It can map every direction to a pixel position, and vice versa. It can also calculate power spectrum of things like CMB. Although it's super useful, its python documentation is really unfriendly for beginners.
- [`starry`](https://rodluger.github.io/starry/tutorials/hd189.html): very cool package that can calculate light curves of transits and secondary eclipses of exoplanets, light curves of eclipsing binaries, rotational phase curves of exoplanets, light curves of planet-planet and planet-moon occultations, and more. A very cool tutorial:
https://rodluger.github.io/starry/tutorials/hd189.html.
***
# [Plot with Python](https://github.com/AstroJacobLi/astro-ph/wiki/Plot-with-Python)

# Using Python to do Data Analysis
- Very good tutorial of using python and Jupiter to analyze data, by Jake VanderPlas: [Reproducible Data Analysis in Jupyter](http://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)
- Various ways to [draw a histogram](https://realpython.com/python-histograms/#a-fancy-alternative-with-seaborn), with NumPy, Matplotlib, Pandas and seaborn, by Brad Solomon.

# Bayesian Statistics
## [Akaike Information Criterion](https://en.wikipedia.org/wiki/Akaike_information_criterion)
## `emcee`: Seriously Kick-Ass MCMC tool
- `emcee` is a python module that implements a very cool MCMC sampling algorithm cample an ensemble sampler. In order to more efficiently sample the parameter space, many samplers (called walkers) run in parallel and periodically exchange states. emcee is available from this website:
http://dan.iel.fm/emcee/current/. And some examples for EMCEE: http://dfm.io/emcee/current/user/line/
- The most up-to-date documents of `emcee` is https://emcee.readthedocs.io/en/latest/tutorials/line/. It's much prettier and understandable than before. You can install newest version by clone its GitHub, then `pip uninstall emcee`, and using `python setup.py install` to install new version.
- If you google `emcee example`, you can already find a lot of good tutorials and examples.  But if you need an example for complex astrophysical application, my personal recommendation is the `prospector` SED fitting code by Ben Johnson:  https://github.com/bd-j/prospector
- `emcee` employs _Affine Invariant Markov chain Monte Carlo (MCMC) Ensemble sampler._ But Metropolis-Hastings sampler and The Parallel-Tempered Ensemble Sampler (PTMCMC) can also be found in `emcee`. The PTMCMC is useful if you expect your distribution to be multi-modal.

> Related to today’s discussion on MCMC:
1.  About autocorrelation time in emcee: https://emcee.readthedocs.io/en/latest/tutorials/autocorr/ In `emcee` the `autocorr.py` deals with this, and more here on how to use it to check convergence in real application: https://emcee.readthedocs.io/en/latest/tutorials/monitor/
2. The `dynesty` Dynamic Nested Sampling code is here: https://dynesty.readthedocs.io/en/latest/ ; `prospector` has an example of its application here: https://github.com/bd-j/prospector/blob/master/prospect/fitting/nested.py
3. About the `pickle` issue, the general description of “pickleable” objects can be found here: https://docs.python.org/3/library/pickle.html#pickle-picklable  Although in real application, this can get tricky.
4. About the time spent on each realization of the likelihood, if you think there might be room for improvement, I always use `cProfile` to profile the time spent on each functional call.  It is very easy to use.

### `corner`: A package of drawing corner diagrams of MCMC and 2d histogram.
You can find everything about `corner` on https://corner.readthedocs.io/en/latest/. It's very easy to use and has many options. Good tool! You can find some examples in the `SN cosmology.ipynb`.
***

- [Ford 2005](http://adsabs.harvard.edu/abs/2005AJ....129.1706F)

- [Ford 2005](https://arxiv.org/abs/astro-ph/0512634)

- A mcmc tool developed by astronomers: [emcee](http://dfm.io/emcee/current/user/quickstart/)

- Astrobite on [fitting (Hogg paper)](https://astrobites.org/2011/07/26/astrostatistics-how-to-fit-a-model-to-data/)

- Astrobite on correlated [errors](https://astrobites.org/2014/07/01/beyond-chi-squared-an-introduction-to-correlated-noise/)

- [Gaussian Process](http://www.gaussianprocess.org)

- [pymc tutorials](https://healthyalgorithms.com/tag/pymc/)

- [Data analysis using Jupyter](http://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)