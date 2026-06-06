---
aliases: [Multiple Regression, Multiple Linear Regression, ANOVA Table, Adjusted R-squared, F-test, Joint Hypothesis Test, AIC, BIC, Dummy Variables, Influence Analysis, Studentized Residuals, Partial Slope Coefficient]
tags: [CFA-L2, quant, concept, regression]
date: 2026-06-04
status: evergreen
source: Schweser Book 1, Reading 1 (Modules 1.1, 1.2, 1.4), LOS 1.a–1.f, 1.k, 1.l
---

# Multiple Regression (Basics, Model Fit, Dummies, Influence)

> Hub note for Reading 1. Assumption **violations** (heteroskedasticity / serial correlation / multicollinearity) live in [[Regression_Assumption_Violations]]; **misspecification** in [[Model_Misspecification]]; **logistic** (qualitative dependent variable) in [[Logistic_Regression]].

## Overview (LOS 1.a–1.b)

The general model: `Yᵢ = b₀ + b₁X₁ᵢ + b₂X₂ᵢ + … + bₖXₖᵢ + εᵢ`. OLS estimates the intercept and slopes to **minimize the sum of squared residuals** `Σ(Yᵢ − Ŷᵢ)²`. Multiple regression is used to **(1) identify relationships, (2) forecast, (3) test theories**.

**Interpreting coefficients:**
- **Intercept b₀** = value of Y when *all* X = 0.
- **Slope bⱼ** = expected change in Y for a 1-unit change in Xⱼ, **holding all other X constant** → called a **partial slope coefficient**. Adding a correlated variable typically *changes* the other slopes (e.g. X₁ slope shifts 4.5 → 2.5 once X₂ enters).

**Significance via p-value:** the p-value is the smallest significance level at which H₀ (bⱼ = 0) can be rejected. **p-value < α → reject** (coefficient significant); p-value > α → fail to reject.

## Five Assumptions (LOS 1.c)

1. **Linear** relationship between Y and each X.
2. Residuals are **normally distributed**.
3. **Constant variance** of errors (homoskedasticity).
4. Residuals are **independent** (uncorrelated across observations).
5. Independent variables are **not random**, and there is **no exact linear relationship** between two or more X's (else perfect multicollinearity).

**Residual-plot diagnostics (preliminary, not formal tests):**
- *Residuals vs. predicted Ŷ* and *residuals vs. each X*: should scatter randomly around a horizontal line at 0 (no pattern, constant spread). A fan/funnel shape ⇒ heteroskedasticity.
- **Normal Q-Q plot**: standardized residuals should lie on the diagonal. Departures (fat tails, skew) ⇒ non-normal residuals. (Recall 5% of normal observations lie below −1.65 SD.)

## Model Fit — ANOVA, R², Adjusted R², AIC/BIC (LOS 1.d)

**ANOVA decomposition:** `SST = RSS + SSE` (Total = Regression/explained + Error/unexplained).

**Full ANOVA table (memorize the df and mean-square columns):**

| Source | df | Sum of squares | Mean square |
|---|---|---|---|
| Regression | **k** | RSS | **MSR = RSS / k** |
| Error (residual) | **n − k − 1** | SSE | **MSE = SSE / (n − k − 1)** |
| Total | **n − 1** | SST | — |

- **Overall F = MSR / MSE**, df = **k (numerator), n − k − 1 (denominator)** — same value as the `(RSS/k)/(SSE/(n−k−1))` form below. Always **one-tailed, right side**.
- **Standard error of the estimate (SEE)** = `√MSE = √[SSE/(n−k−1)]` — the standard deviation of the residuals; **smaller SEE = better fit**. (Same root quantity MSE drives both the F-test and the SEE.)

| Quantity | Formula |
|---|---|
| **R²** | `RSS / SST = 1 − SSE/SST` — % of Y variation explained by all X's together |
| **Adjusted R²** | `1 − [(n−1)/(n−k−1)] × (SSE/SST) = 1 − (1−R²)(n−1)/(n−k−1)` |

- **R² almost always rises** when you add a variable (even a useless one) → rewards **overfitting**.
- **Adjusted R² ≤ R²**; it *can fall* when a weak variable is added. Rule of thumb: adding a variable raises adjusted R² only if that coefficient's |t| > 1. Use adjusted R² to compare models with **different numbers** of regressors.

**AIC and BIC** (compare competing models for the **same dependent variable**; **lower = better**):
- `AIC = n·ln(SSE/n) + 2(k+1)` — preferred when the goal is **forecasting**.
- `BIC = n·ln(SSE/n) + ln(n)·(k+1)` — preferred when the goal is **best goodness of fit**.
- `k` is a **penalty** for added parameters. Since `ln(n) > 2` for n ≥ 8, **BIC penalizes overfitting more harshly** than AIC → BIC favors smaller models.

## Joint Hypothesis Test — Nested-Model F-test (LOS 1.e)

Tests whether a group of `q` excluded variables jointly add explanatory power. **Unrestricted** (full, k variables) vs. **restricted** (subset). H₀: the q excluded coefficients are all 0.

`F = [(SSE_R − SSE_U) / q] / [SSE_U / (n − k − 1)]`

- `SSE_R` = restricted SSE, `SSE_U` = unrestricted SSE, `q` = # excluded variables, `k` = # variables in the unrestricted model. df = **q (numerator), n − k − 1 (denominator)**.
- **Reject if F > F_critical.** The F-test is **ALWAYS one-tailed** (despite the "=" in H₀) — classic L2 trap.
- **Overall model F-test** (H₀: b₁=…=bₖ=0, i.e. q = k, all variables excluded): then `SSE_R = SST`, so `F = (RSS/k) / (SSE/(n−k−1))`.

The joint F-test is more meaningful than separate t-tests when regressors are correlated.

## Predicting Y (LOS 1.f)

Plug forecasted X's into the **full estimated equation**, using **all** coefficients — even ones that are statistically insignificant. (Dropping an insignificant X and re-estimating will generally change the remaining coefficients.) Example: `EG10 = −11.6 + 0.25·PR + 0.14·YCS`; PR=50, YCS=4 → `−11.6 + 12.5 + 0.56 = 1.46%`.

## Influence Analysis (LOS 1.k)

- **Outlier** = extreme **Y** value; **high-leverage point** = extreme **X** value.
- **Leverage (Lᵢ)** ∈ [0,1]; Σ leverages = k + 1. A point is **potentially influential** if its leverage exceeds **3(k+1)/n**.
- **Studentized residuals** detect outliers: delete one observation, re-fit on n−1, compare actual Yᵢ to its predicted value, divide by its SD. Compare to t with **n − k − 2 df**. |studentized residual| > t_critical ⇒ outlier.
- **Influential** = excluding it materially changes the coefficients. Not all outliers/high-leverage points are influential. Remedies: fix input errors, delete bad data, add omitted variables, or **winsorize**.

## Dummy (Qualitative) Independent Variables (LOS 1.l)

A **dummy** is 0/1 (on/off). To distinguish **n classes use (n − 1) dummies** — otherwise you create an exact linear relationship among regressors (the **dummy-variable trap**). The omitted class is the **reference point**.

| Type | Effect |
|---|---|
| **Intercept dummy** | shifts the intercept: `Y = (b₀ + d₀D) + b₁X` → intercept becomes b₀+d₀ when D=1 |
| **Slope dummy** (interaction term) | changes the slope: `Y = b₀ + b₁X + d₁(D·X)` |
| **Both** | shifts intercept *and* slope |

**Interpretation:** each dummy coefficient = the difference in Y between that category and the **omitted reference category**, holding other variables constant. Quarterly-EPS example with Q4 omitted: `EPS = 1.25 + 0.75·Q1 − 0.20·Q2 + 0.10·Q3`. Intercept 1.25 = average Q4 EPS; Q1 average = 1.25+0.75 = 2.00; Q2 = 1.05; Q3 = 1.35. These are also next-year quarterly forecasts.

## Worked Example — full model fit pass

Monthly returns on 5 X's, n = 60, SST = 460, SSE = 170.
- `R² = 1 − 170/460 = 63.0%`.
- `Adjusted R² = 1 − (1 − 0.63)(59/54) = 1 − 0.37×1.0926 = 59.6%`.
- Add 4 more X's (k=9), R² rises to 65.0% but adjusted R² **falls** to 58.7% → **prefer the 5-variable model** (higher adjusted R², fewer variables, and it would have lower BIC).

## Exam Traps
- The nested/overall **F-test is one-tailed** even though H₀ contains "=".
- **R² always rises** with more variables; judge added variables by **adjusted R², AIC, or BIC**, not R².
- **BIC penalizes complexity more than AIC**; AIC → forecasting, BIC → goodness of fit; lower is better for both, and only comparable across models with the **same dependent variable**.
- Predict Y using **all** coefficients, including insignificant ones.
- Use **(n − 1)** dummies for n categories; the dropped category is the reference.
- Slope coefficients are **partial** — they hold other X's constant and change as regressors are added.

## Q&A

### 2026-06-04 — How do R², adjusted R², AIC and BIC differ for model selection?
**Q:** When comparing multiple regression models, how do R², adjusted R², AIC, and BIC differ?
**A:** **R²** = RSS/SST, the fraction of Y's variation explained, but it almost always **increases** when any variable is added, so it rewards overfitting. **Adjusted R²** `= 1 − (1−R²)(n−1)/(n−k−1)` penalizes extra variables and can decrease (it rises only if the new coefficient's |t| > 1). **AIC** `= n·ln(SSE/n) + 2(k+1)` and **BIC** `= n·ln(SSE/n) + ln(n)(k+1)` both reward fit and penalize parameters — **lower is better**, comparable only across models with the **same dependent variable**. AIC is for **forecasting**, BIC for **goodness of fit**, and BIC penalizes complexity more (ln n > 2).
Related: [[Regression_Assumption_Violations]]

### 2026-06-04 — How is the nested-model joint F-test constructed?
**Q:** How do you test whether a group of excluded variables jointly matters?
**A:** Use the partial **F-test** comparing a restricted model (subset) to the unrestricted (full) model: `F = [(SSE_R − SSE_U)/q] / [SSE_U/(n−k−1)]`, with **q** = number of excluded variables (numerator df) and **n−k−1** denominator df. Reject H₀ (all q excluded coefficients = 0) if **F > F_critical**; the test is **always one-tailed**. For the overall-significance F-test, q = k and SSE_R = SST, giving `F = (RSS/k)/(SSE/(n−k−1))`. The joint test beats separate t-tests when regressors are correlated.
Related: [[Logistic_Regression]]

### 2026-06-04 — How do you interpret a dummy-variable regression?
**Q:** How are dummy-variable coefficients interpreted, and how many dummies do you need?
**A:** Use **(n − 1)** dummies for **n** categories (else you hit the dummy-variable trap — perfect multicollinearity). The omitted category is the **reference**: the intercept equals the reference category's mean, and each dummy's coefficient is the **difference** between its category and the reference, holding other variables constant. An **intercept dummy** shifts the intercept; a **slope dummy** (interaction term D·X) shifts the slope. Quarterly EPS with Q4 omitted: `EPS = 1.25 + 0.75Q1 − 0.20Q2 + 0.10Q3` → Q4 avg = 1.25, Q1 = 2.00, etc.
Related: [[Model_Misspecification]]
