---
layout: post
title:  "Statistics and Python"
date:   2018-12-18 21:40:00
author: Jiaxuan Li
categories: Coding
---
# 普通统计学

## 第一章

调查的两种方法：实验和观察。观察到的信息无法做casual的判断，只能给出correlation。但是实验室做实验可以做出因果关系来。天文观测没法给出casaul link，这需要注意。天文观测没法控制变量。我们只能知道结果，但是可以通过贝叶斯方法来推断是什么原因产生了这些结果（通过一定的概率模型）。

普查有time-delay。给定一个概率抽样，那么就可以算出抽样误差。

整群抽样能够减小调查的成本，但是需要注意群与群之间差异要较小。

非概率抽样很难做统计推断，很难推广到总体。

一个个体被调查到的概率是$$p$$， 则其代表性是$$1/p$$.



SImpson悖论：如果忘记了一些混淆因素，那么结论很可能完全不可信。



如果是概率抽样，那么抽样误差可以算出来。在$$N$$个样本中抽样，那么一个标准差一定小于$$1/\sqrt{N}$$.

未响应样本：给人打电话有人不接。这样可以算出来总统支持率的上下限。

数据挖掘里的EM算法（Expectation & Maximization）：通过迭代，把未响应数据填入列联表。这个算法成立要求“随机不相应”。

响应误差：注意措辞。调查时有可能强加给人一个观点，这对中立的人/不了解情况的人不公平。访员对结果也有影响。

**试验是检验变量间因果关系的一种方法。**做调查没法得到因果关系，只能得到相关信息。相关关系可以做预测，但是没法做决策。给定一个巧克力消耗量，我可以预测诺贝尔奖量。但是没法让说让一个国家猛吃巧克力，然后这个国家诺贝尔奖量就猛的上升了。决策靠的是因果，预测靠的是相关。在做实验时，一定要控制其他变量相同（或者完全随机，随机选择实验对象），然后控制一个变量不同。要考虑到各种因素，不要带来Simpson悖论。

**随机化实验方法：**随机选取病人，从而各种因素在两组内分布都是相近的。随机化对照是**金标准**。随机对照和历史对照可以完全不一样，衡量药品的药效一定要做**随机化对照**。对人做实验是有ethical committee来判断是否合乎伦理。

[Median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation): $$\text{MAD} = \text{median}(|X_i - \text{median}(X)|)$$.



# Gaussian Process

[Gaussian Process for Machine Learning](http://www.gaussianprocess.org/gpml/chapters/RW.pdf)

# David Hogg's paper on Statistics

### [Data analysis recipes: Fitting a model to data](https://arxiv.org/abs/1008.4686)
### [Data analysis recipes: Probability calculus for inference](https://arxiv.org/abs/1205.4446v1)

***

# [Plot with Python](https://github.com/AstroJacobLi/astro-ph/wiki/Plot-with-Python)

# Using Python to do Data Analysis
- Very good tutorial of using python and Jupiter to analyze data, by Jake VanderPlas: [Reproducible Data Analysis in Jupyter](http://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)
- Various ways to [draw a histogram](https://realpython.com/python-histograms/#a-fancy-alternative-with-seaborn), with NumPy, Matplotlib, Pandas and seaborn, by Brad Solomon.
- [Introduction of PyData community, by Jake VanderPlas](https://www.youtube.com/watch?v=DifMYH3iuFw)

# Bayesian Statistics
## [Frequentism v.s. Bayesianism, by Jake VanderPlas](https://www.youtube.com/watch?v=KhAUfqhLakw)
## [Akaike Information Criterion](https://en.wikipedia.org/wiki/Akaike_information_criterion)
## `emcee`: Seriously Kick-Ass MCMC tool
- `emcee` is a python module that implements a very cool MCMC sampling algorithm cample an ensemble sampler. In order to more efficiently sample the parameter space, many samplers (called walkers) run in parallel and periodically exchange states. emcee is available from this website:
http://dan.iel.fm/emcee/current/. And some examples for EMCEE: http://dfm.io/emcee/current/user/line/
- The most up-to-date documents of `emcee` is https://emcee.readthedocs.io/en/latest/tutorials/line/. It's much prettier and understandable than before. You can install newest version by clone its GitHub, then `pip uninstall emcee`, and using `python setup.py install` to install new version.
- If you google `emcee example`, you can already find a lot of good tutorials and examples.  But if you need an example for complex astrophysical application, my personal recommendation is the `prospector` SED fitting code by Ben Johnson:  https://github.com/bd-j/prospector
- `emcee` employs _Affine Invariant Markov chain Monte Carlo (MCMC) Ensemble sampler._ But Metropolis-Hastings sampler and The Parallel-Tempered Ensemble Sampler (PTMCMC) can also be found in `emcee`. The PTMCMC is useful if you expect your distribution to be multi-modal.

> Related to today’s discussion on MCMC:
>
> 1.  About autocorrelation time in emcee: https://emcee.readthedocs.io/en/latest/tutorials/autocorr/ In `emcee` the `autocorr.py` deals with this, and more here on how to use it to check convergence in real application: https://emcee.readthedocs.io/en/latest/tutorials/monitor/
2. The `dynesty` Dynamic Nested Sampling code is here: https://dynesty.readthedocs.io/en/latest/ ; `prospector` has an example of its application here: https://github.com/bd-j/prospector/blob/master/prospect/fitting/nested.py
3. About the `pickle` issue, the general description of “pickleable” objects can be found here: https://docs.python.org/3/library/pickle.html#pickle-picklable  Although in real application, this can get tricky.
4. About the time spent on each realization of the likelihood, if you think there might be room for improvement, I always use `cProfile` to profile the time spent on each functional call.  It is very easy to use.

***

- [Ford 2005](http://adsabs.harvard.edu/abs/2005AJ....129.1706F)

- [Ford 2005](https://arxiv.org/abs/astro-ph/0512634)

- A mcmc tool developed by astronomers: [emcee](http://dfm.io/emcee/current/user/quickstart/)

- Astrobite on [fitting (Hogg paper)](https://astrobites.org/2011/07/26/astrostatistics-how-to-fit-a-model-to-data/)

- Astrobite on correlated [errors](https://astrobites.org/2014/07/01/beyond-chi-squared-an-introduction-to-correlated-noise/)

- [Gaussian Process](http://www.gaussianprocess.org)

- [pymc tutorials](https://healthyalgorithms.com/tag/pymc/)

- [Data analysis using Jupyter](http://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)