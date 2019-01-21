---
layout: post
title:  "ARAA notes"
date:   2019-01-19 21:38:00
author: Jiaxuan Li
categories: paper
---
# ARAA notes
Feel very ashamed for the decadence in the past year 2018. I will try to read as many paper as possible and do my best in 2019.

## [Weak Lensing for Precision Cosmology, by Rachel Mandelbaum](https://www.annualreviews.org/doi/abs/10.1146/annurev-astro-081817-051928)

### Moments of images
The moment of a 2-D distribution about the point $$(c_x, c_y)$$ is defined as a kind of average (this definition is straightforward):
\\[M_{m, n} = \frac{\int \rho(x, y) (x-c_x)^m (y-c_y)^n \md x\md y}{\int \rho(x, y)\md x\md y}.\\]

The moment can be generalized with a weighting function:
\\[M_{m, n} = \frac{\int I(x, y)W(x, y)( x-c_x)^m (y-c_y)^n \md x\md y}{\int I(x, y)W(x, y)\md x\md y},\\]
where $$I(x, y)$$ is the intensity map and $$W(x, y)$$ is a weighting function.

Since the images are discrete instead of continuous, we write the integral to summation:
\\[M_{m, n} = \frac{\sum_x \sum_y I(x, y)W(x, y)( x-c_x)^m (y-c_y)^n \md x\md y}{\sum_x \sum_y  I(x, y)W(x, y)\md x\md y}.\\]

The order of moment is defined as $$m+n$$. Here after we usually assume a unity weighting function.

- Zero order moment: $$M_{0, 0} = \sum_x \sum_y I(x, y)$$ is the total brightness of an image. We ignore the denominator here otherwise it will yield trivial result.
- First order moment: $$M_{1, 0} = \frac{\sum_x \sum_y I(x, y) x}{\sum_x \sum_y I(x, y)}$$ is the $$x$$ centroid of the image with an arbitrary coordinate origin. The centroid of image is $$(M_{1, 0}, M_{0, 1})$$. Given the centroid, we can remove the origin of image to the centroid, and calculate higher order moments.
{% include image.html url="/images/ellipse-moment.png" caption="Second order moments of ellipse" width=280 align="right" %}
- Second order moments: Here we discuss the second order moment of an ellipse with constance surface brightness $$\mu$$ (not in magnitude). Assume we have correct the coordinate origin to the center of this ellipse. The the horizontal aligned ellipse (black one in the right figure), it's straightforward to calculate its second order moments as:
\\[M_{2, 0} = \frac{1}{4}a^2,\ M_{0, 2} = \frac{1}{4}b^2,\ M_{1, 1} = 0.\\]
We already see that the second order moments contain information about the shape, size and orientation of an ellipse. Then we study a non-trivial case by rotating the ellipse by $$\theta$$ (pink ellipse). We are very familiar with the coordinate transformation between $$(x, y)$$ and $$(x', y')$$, which is written as
\\[x' = x\cos\theta - y\sin\theta,\ y' = x\sin\theta + y\cos\theta.\\]
Plug in these transformation and express $$M_{2, 0}'$$ using $$M_{2, 0},\ M_{0, 2},\ M_{1,1}$$, also noticing the Jacobian of this transformation is unity, we have:
\\[M_{2, 0}' = \frac{1}{4}(a^2\cos^2\theta + b^2\sin^2\theta),\\]
\\[M_{0, 2}' = \frac{1}{4}(a^2\sin^2\theta + b^2\cos^2\theta),\\]
\\[M_{1, 1}' = \frac{1}{4}(a^2 - b^2)\sin\theta\cos\theta.\\]
Then we can define a complex ellipticity which goes like
\\[\tilde{e} = \frac{M_{2, 0} - M_{0, 2} + 2i M_{1, 1}}{M_{2, 0} + M_{0, 2}}.\\]
And it turns out to be
\\[\tilde{e} = \frac{1-q^2}{1+q^2}(\cos 2\theta + i\sin 2\theta),\\]
where $$q$$ is the axis ratio $$b/a$$, and $$ (1-q^2) / (1+q^2) = e$$ is the ellipticity of the ellipse. Thus
\\[\tilde{e} = e_1 + i e_2 = e(\cos 2\theta + i\sin 2\theta).\\]
Hence we have many combinations to express the shape (ellipticity and position angle) and size: $$(\theta, e)$$, $$(e_1, e_2)$$, etc.

## [The Connection Between Galaxies and Their Dark Matter Halos, by Risa Wechsler and Jeremy Tinker](https://www.annualreviews.org/doi/abs/10.1146/annurev-astro-081817-051756)

## [The Faintest Dwarf Galaxies](https://arxiv.org/abs/1901.05465)

## [The Most Luminous Supernovae](https://arxiv.org/abs/1812.01428v1)

## [Gaussian Process in Machine Learning](http://www.gaussianprocess.org/gpml/chapters/RW.pdf)
