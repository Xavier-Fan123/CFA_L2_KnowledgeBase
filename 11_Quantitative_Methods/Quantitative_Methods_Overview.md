---
aliases: [Quantitative Methods Overview, Quant Overview]
tags: [CFA-L2, quant, overview]
date: 2026-06-03
status: evergreen
source: Schweser Book 1 (Readings 1-4)
---

# Quantitative Methods — Overview

Entry point for the Quant topic area. **Four readings:** multiple regression, time series, machine learning, big data projects. **Full reading-level coverage.**

## Reading 1 — Multiple Regression
- [[Multiple_Regression]] — basics, 5 assumptions, ANOVA, R²/adjusted R²/AIC/BIC, nested F-test, prediction, influence analysis, dummy variables
- [[Model_Misspecification]] — functional-form errors (omit / transform / scale / pool)
- [[Regression_Assumption_Violations]] — heteroskedasticity, serial correlation, multicollinearity
- [[Breusch_Pagan_Test]] — detecting conditional heteroskedasticity
- [[Logistic_Regression]] — qualitative dependent variable, logit, LR test

## Reading 2 — Time-Series Analysis
- [[Time_Series_Analysis]] — trend (linear/log-linear), covariance stationary, AR, unit root, Dickey-Fuller, first differencing, chain rule, RMSE, seasonality, ARCH, cointegration (DF-EG)

## Reading 3 — Machine Learning
- [[Machine_Learning]] — supervised/unsupervised/deep learning; overfitting & bias-variance; LASSO, SVM, KNN, CART, random forest; PCA, k-means/hierarchical clustering; neural nets, DLN, RL

## Reading 4 — Big Data Projects
- [[Big_Data_Projects]] — data wrangling & scaling; text processing (BOW, DTM, N-grams); model evaluation (confusion matrix, precision/recall/F1, ROC/AUC); bias-variance tuning, grid search

## Exam Traps (cross-cutting)
- Robust SE corrections (White, Newey-West) change SEs only, never coefficients.
- "Cannot reject H₀" in Dickey-Fuller = unit root = non-stationary.
- Logit nested test = LR test (χ²), not F-test; the nested-model and overall regression F-tests are one-tailed.
- ML: hyperparameters are set by the researcher; bias error = in-sample/underfit, variance error = out-of-sample/overfit.
