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
