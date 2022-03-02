---
layout: post
title:  "Scikit-learn"
date:   2018-12-10 10:18:00
author: Jiaxuan Li
categories: coding
---

# Quick Start

## Machine learning
- Supervised learning: Classification, Regression. (Learn the map $$X\to y$$)
- Unsupervised learning: Clustering, density estimation.
- Dimensionality reduction.
{% include image.html url="/images/ml_map.png" caption="Scikit-learn Cheat Sheet" width=500 align="right" %}

## Scikit-learn
- Data is constructed by the format: (n_samples, n_features)
- Datasets Examples: iris, diabetes, digits, etc.
- Every `estimator` class has `.fit(X_train, y_train)` and `.predict(X_test, y_test)`.
- Export the `estimator` into a file:
```python
from joblib import jump, load
dump(clf, 'filename.joblib')
clf = load('filename.joblib')
```
- You can change the parameters of an `estimator` after construct it by using `.set_params()` method.
- In classification, `y` can have multi-labels (like in iris). You can use `sklearn.preprocessing.LabelBinarizer` or `sklearn.preprocessing.MultiLabelBinarizer`, and classify using `sklearn.multiclass.OneVsRestClassifier`.

# [Supervised learning: predicting an output variable from high-dimensional observations](https://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html)

## Nearest Neighbor Classification
- kNN (k-th nearest neighbor classification): `sklearn.neighbors.KNeighborsClassifier` is also an estimator.
- [Curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality): if your sample is small and dimension is high, then your sample will be very sparse. Also it's very interesting that in high dimensions, the high-dimensional unit hypercube can be said to consist almost entirely of the "corners" of the hypercube, with almost no "middle".

## Linear model: Regression
- Linear models: $$y = X \beta + \epsilon$$, in which $$y$$ and $$\epsilon$$ are $$(n\times 1)$$, $$X$$ is $$(n\times m)$$ and $$\beta$$ is $$(m\times 1)$$. Here $$X$$ is data, $$y$$ is target, $$\beta$$ is coefficients and $$\epsilon$$ is observation noise.
- Linear Regression estimator: `sklearn.linear_model.LinearRegression`. 
- Shrinkage: `sklearn.linear_model.Ridge` and `sklearn.linear_model.Lasso`. 
- If we use linear model to do classification, remember using 'logistic' or 'sigmoid' function: `sklearn.linear_model.LogisticRegression`.

## Support Vector Machines (SVMs)
- SVMs has regularization parameter $$C$$, smaller $$C$$ means more regularization. `sklearn.svm.SVC` is the estimator.
- Different kernels give different results.

# [Model selection and cross-validation](https://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html)
Since an estimator has some parameters, we need to choose the best values for these parameters to get the best behavior. So we use `score` and 'cross-validation'. 
- CV generators: `sklearn.model_selection.KFold` can be used as `kfold = KFold(n_splits=5)`, `for train, test in kfold.split(X):`. This can generate 5 groups of training samples and test samples. Then we can calculate scores for each set.
- Another way is `sklearn.model_selection.cross_val_score(svc, X, y, cv=5, n_jobs=-1)`.
- Another way is grid-search the parameter space using `sklearn.model_selection.GridSearchCV(svc, param_grid=dict(C=Cs))`.
- Some estimator can automatically give the best values of some parameters. For example constructing an estimator `estimator = sklearn.linear_model.LassoCV(cv=5)` and fit it with data. Then we can retrieve the best parameter 'alpha' by `estimator.alpha_`. But we should note, this may not be reliable. We'd better estimate the best parameter by ourselves.



`pca.fit_transform` = first `fit`, then `transform`.