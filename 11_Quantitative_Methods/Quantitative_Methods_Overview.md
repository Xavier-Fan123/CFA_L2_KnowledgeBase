---
aliases: [Quantitative Methods Overview, Quant Overview]
tags: [CFA-L2, quant, overview]
date: 2026-06-03
status: incubating
source: Schweser Book 1
---

# Quantitative Methods — Overview

Entry point for the Quant topic area. Two big modules: multiple regression and time series.

## Module 1 — Multiple Regression
- [[Model_Misspecification]] — functional-form errors (omit / transform / scale / pool)
- [[Regression_Assumption_Violations]] — heteroskedasticity, serial correlation, multicollinearity
- [[Breusch_Pagan_Test]] — detecting conditional heteroskedasticity
- [[Logistic_Regression]] — qualitative dependent variable, logit, LR test
- (to add) F-test for nested models, R²/adjusted R²/AIC/BIC, influence analysis, dummy variables

## Module 2 — Time-Series Analysis
- [[Time_Series_Analysis]] — covariance stationary, AR, unit root, Dickey-Fuller, first differencing
- (to add) trend models, mean reversion forecasting, RMSE, seasonality, ARCH, cointegration

## Exam Traps (cross-cutting)
- Robust SE corrections (White, Newey-West) change SEs only, never coefficients.
- "Cannot reject H₀" in Dickey-Fuller = unit root = non-stationary.
- Logit nested test = LR test (χ²), not F-test.
