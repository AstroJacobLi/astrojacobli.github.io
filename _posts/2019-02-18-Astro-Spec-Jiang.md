---
layout: post
title:  "Astronomical Spectroscopy"
date:   2019-02-18 21:38:00
author: Jiaxuan Li
categories: paper
---
# [天体光谱学 — 江林华](http://kiaa.pku.edu.cn/~jiang/teaching.html#teach=class3)

## 第一讲

### 热动平衡下的热力学和统计物理

一个热力学系统，$$N, E, V$$ are fixed. We assume energy levels $$\epsilon_1, \epsilon_2…$$ , and corresponding degeneracy $$g_1, g_2, …$$ There are $n_1, n_2, ...$ particles on each energy levels. Thus $$\sum_i n_i = N, \sum_i n_i \epsilon_i = E$$ constrain this system.

- **Boltzmann Distribution**

  Particles are Discriminable. 

  Differentiate $$\Omega_{M.B.} = \frac{N!}{\Pi_i n_i}\Pi_i g_i^{n_i}$$ and use the constrain above, we get Boltzmann Distribution. $$n_i = g_i e^{- \alpha - \beta\epsilon_i}$$.

- **Bose-Einstein Distribution**

  Particles are indistinguishable. And no Pauli law.
  $$
  n_i = \frac{g_i}{e^{\alpha + \beta\epsilon_i} - 1}.
  $$

- **Fermi-Dirac Distribution**
  $$
  n_i = \frac{g_i}{e^{\alpha + \beta\epsilon_i} + 1}.
  $$
  Under classical limit, FD and BE distribution go back to Boltzmann.

- Boltzmann Equation (so-called)

  $$n_i = g_i e^{- \alpha - \beta\epsilon_i}$$, thus $$N = e^{-\alpha} \sum_i g_i e^{-\beta \epsilon_i} = e^{-\alpha} G$$. We define partition function $$G$$. 
  $$
  \frac{n_i}{N} = \frac{g_i}{G} e^{-\epsilon_i/k_BT}, \frac{n_i}{n_j} = \frac{g_i}{g_j} e^{-(\epsilon_j-\epsilon_i)/k_BT} .
  $$

- **Maxwell Distribution**
  $$
  f_M(\vec{v}) = \left(\frac{m}{2\pi k_B T}\right)^{3/2} \exp\left(-\frac{mv^2}{2k_B T}\right) = f(v_x) f(v_y) f(v_z).
  $$
  This is $$dP = f_M(\vec{v}) dv_x dv_y dv_z$$.
  $$
  F_M(v) = 4\pi v^2 \left(\frac{m}{2\pi k_B T}\right)^{3/2} \exp\left(-\frac{mv^2}{2k_B T}\right)
  $$
  This is $$dP = F_M(v) dv$$.

### 原子跃迁和电离

- An atom jumps from $$j$$ to $$i$$, we have ​$$\frac{n_i}{n_j} = \frac{g_i}{g_j} e^{-(\epsilon_i-\epsilon_j)/k_BT} .$$

  Recall [Einstein coefficients](https://en.wikipedia.org/wiki/Einstein_coefficients). See "Detailed Balancing". 

  I once calculated the occupation of Cobalt in a radiation field for Ping, see this [notebook](https://nbviewer.jupyter.org/github/astroJacobLi/astro-ph/blob/master/Ping/Cobalt.ipynb), and this [folder](https://github.com/AstroJacobLi/astro-ph/tree/master/Ping).  

- Blackbody Radiation: 
  $$
  r_B(\nu) = \frac{2\pi h \nu^3}{c^2} \frac{1}{e^{h\nu^/k_BT - 1}}.
  $$
  This is the energy emitted in unit time unit area unit frequency, and has nothing to do with radiation direction.

- Ionization

  $$\chi_{0, 1}$$ Is not excited neutral atom. Former number is about ionization, latter number is about excitation.

  Photo-electric: $$h\nu = \chi_{r, k} + \frac{1}{2} m_e v^2$$.

  For $$r$$-time ionization: $$\frac{n_{r, j}}{n_{r, i}} = \frac{g_{r, j}}{g_{r, i}} e^{-(\epsilon_i-\epsilon_j)/k_BT} .$$

  For HI: $r=0, j=2, i=1$: $$T(\text{K}) = 6000, 10000, 20000$$, the corresponding $$\frac{n_{0,2}}{n_{0,1}} = 10^{-8}, 3\times10^{-5}, 10^{-2}$$.

  So excitation is only significant when temperature is about 20000 K. (Blue stars)

  For $$r$$-time ionization, Boltzmann Equation still holds for a fixed $$r$$.



## 第二讲 氢原子光谱

电子分布率 

电子离中间最近