---
aliases: [Breusch-Pagan Test, BP Test, Heteroskedasticity Test]
tags: [CFA-L2, quant, test, regression]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 1.3, LOS 1.h
---

# Breusch-Pagan (BP) Test

Detects **conditional heteroskedasticity** — whether residual variance is related to the level of the independent variables. Core idea: **if the size of the residuals can be explained by the regressors, heteroskedasticity is present.**

## Construction Steps

1. **Run the original regression, save residuals.** `Yᵢ = b₀ + b₁X₁ᵢ + ... + bₖXₖᵢ + εᵢ` → obtain `ε̂ᵢ`.
2. **Auxiliary regression: regress the SQUARED residuals on the original regressors.** `ε̂ᵢ² = a₀ + a₁X₁ᵢ + ... + aₖXₖᵢ + uᵢ` If the regressors significantly explain the squared residuals, variance is tied to X → heteroskedasticity.
3. **Test statistic** (R² from the auxiliary regression): `BP = n × R²`
4. **Compare to χ² critical value.**

## Test Specification

| Item | Value |
|------|-------|
| Distribution | **χ² (chi-square)** |
| Degrees of freedom | **k** (number of independent variables) |
| Tail | **One-tailed** (only large R² / BP signals a problem) |
| H₀ | No conditional heteroskedasticity |
| Hₐ | Conditional heteroskedasticity present |
| Decision | BP > critical → **reject H₀** → heteroskedasticity present |

## Worked Example (curriculum)

5 years of monthly data → n = 60; auxiliary-regression R² = 8%.
- `BP = 60 × 0.08 = 4.8`
- χ² critical, 1 df, 5% = **3.841**
- 4.8 > 3.841 → **reject H₀** → conditional heteroskedasticity confirmed.

## Correction

Use **White-corrected (robust / heteroskedasticity-consistent) standard errors**, then recompute t-stats with the original coefficients → see [[Regression_Assumption_Violations]].

## Exam Traps
- Dependent variable in the auxiliary regression is the **squared** residual, not the residual.
- Statistic is `n × R²`, χ² with **k** df, **one-tailed**.
- Don't confuse with **Breusch-Godfrey (BG)** = serial correlation (F-distribution), or **Durbin-Watson** = single-lag serial correlation. Side-by-side comparison: [[Statistical_Tests_Master_Table]].
- BP's auxiliary regression uses the **squared** residuals; BG's uses the **residuals themselves plus their lags**.

## Q&A

### 2026-06-03 — How do you construct the BP test?
**Q:** How is the BP test built?
**A:** Regress the squared OLS residuals on the original independent variables; statistic `BP = n × R²`, χ² with k df, one-tailed; BP > critical → conditional heteroskedasticity. Example: n=60, R²=8% → 4.8 > 3.841 → reject H₀. Correct with White standard errors.
Related: [[Regression_Assumption_Violations]]
