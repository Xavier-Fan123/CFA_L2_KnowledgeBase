---
aliases: [Regression Assumption Violations, Heteroskedasticity, Serial Correlation, Multicollinearity, BP Test, White Standard Errors, Newey-West]
tags: [CFA-L2, quant, concept, regression]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 1.3, LOS 1.h / 1.i / 1.j
---

# Regression Assumption Violations

The three primary assumption violations: **(1) heteroskedasticity, (2) serial correlation
(autocorrelation), (3) multicollinearity.**

---

## 1. Heteroskedasticity (LOS 1.h)

Residual variance is **not constant** across observations (some subsamples are more spread out).

| Type | Related to level of X? | Problem? |
|------|------|------|
| **Unconditional** | No | Violates equal-variance, but usually no major problem |
| **Conditional** | Yes (variance rises/falls with X) | **Serious** — invalidates inference |

**Effects of conditional heteroskedasticity:**
- Standard errors are unreliable (for financial data usually **underestimated** → too many **Type I errors**).
- The overall F-test is unreliable.
- Coefficient estimates remain **consistent and unbiased**.

**Detection:** ① residual scatter plots (fan shape); ② **Breusch-Pagan (BP) test** → see [[Breusch_Pagan_Test]].

**Correction:** compute **robust standard errors** (a.k.a. **White-corrected** / heteroskedasticity-
consistent standard errors), then recompute t-stats using the **original coefficients**.

### White correction — the principle (beyond-scope add-on)
> Curriculum only says "use White standard errors, coefficients unchanged." The mechanism below is
> added reasoning, not curriculum text.

- OLS coefficients stay unbiased/consistent under heteroskedasticity; only `Var(β̂)` is computed wrong.
- OLS assumes homoskedasticity: `Var(β̂) = σ²(X'X)⁻¹`. The true ("sandwich") form is
  `Var(β̂) = (X'X)⁻¹ [Σ σ²ᵢ xᵢxᵢ'] (X'X)⁻¹`.
- The middle term has n unknown `σ²ᵢ` — can't estimate each. **White's insight:** you don't need each
  `σ²ᵢ`, only the sum; replace `σ²ᵢ` with the squared OLS residual `ê²ᵢ`:
  `V̂_White = (X'X)⁻¹ (Σ ê²ᵢ xᵢxᵢ') (X'X)⁻¹` — the heteroskedasticity-consistent estimator.
- Square-root the diagonal → robust SE. Coefficients unchanged; SEs (usually larger) → more
  conservative, valid t-tests. It is a **large-sample (asymptotic)** result.

---

## 2. Serial Correlation / Autocorrelation (LOS 1.i)

Residuals are correlated across observations: `Cov(εₜ, εₜ₋₁) ≠ 0`. Common in time series.

**Effects:** standard errors wrong (positive serial correlation → SE underestimated → Type I errors);
coefficient estimates remain consistent (unless a lagged dependent variable is a regressor).

**Detection:**
- **Durbin-Watson (DW)** — single-lag serial correlation only.
- **Breusch-Godfrey (BG) test** — more general, handles multiple lags. Regresses the residuals on the
  original regressors **plus** lagged residual(s); BG statistic has an **F-distribution** with `p` and
  `n − p − k − 1` df (`p` = lags tested). BG stat > critical → reject "no serial correlation."

**Correction:** **Newey-West** corrected standard errors (robust to both serial correlation AND
heteroskedasticity), then recompute t-stats on original coefficients.

> Intuition: Newey-West generalizes White — its "sandwich" filling adds the cross-period residual
> products `êᵢêᵢ₋ⱼ` (serial-correlation terms) on top of `ê²ᵢ` (heteroskedasticity term).

---

## 3. Multicollinearity (LOS 1.j)

Two or more independent variables are **highly correlated** with each other.

**Effects:** coefficients still consistent/unbiased, but **standard errors inflated** → t-stats too
small → variables look insignificant (high R² / significant F, yet few significant t-stats = classic
multicollinearity signature).

**Detection — Variance Inflation Factor (VIF):**
`VIFⱼ = 1 / (1 − R²ⱼ)`, where `R²ⱼ` is from regressing `Xⱼ` on the other regressors.
- VIF = 1 (R²=0): not correlated with others.
- VIF > 5 (R² > 80%): investigate.
- VIF > 10 (R² > 90%): **severe** multicollinearity.

**Correction:** omit one or more correlated variables; use a different proxy; or increase sample size.

---

## Master Comparison Table

| | Heteroskedasticity | Serial Correlation | Multicollinearity |
|---|---|---|---|
| What breaks | Residual variance not constant | Residuals correlated over time | X's correlated with each other |
| Coefficients | Unbiased, consistent | Unbiased, consistent* | Unbiased, consistent |
| Standard errors | Usually **under**estimated | Usually **under**estimated (positive SC) | **Inflated** |
| Detect | BP test, residual plot | DW (1 lag), BG (multi-lag) | VIF |
| Correct | White (robust) SE | Newey-West SE | Drop variable / new proxy / more data |

\* unless a lagged dependent variable is used as a regressor.

## Exam Traps
- Conditional (not unconditional) heteroskedasticity is the dangerous one.
- BP test is **one-tailed**; White corrects it. DW vs BG: DW = one lag, BG = multiple lags; both detect serial correlation.
- Multicollinearity's tell: **high R² + significant F but insignificant t-stats**.
- All three corrections (White, Newey-West) change only the **standard errors**, never the coefficients.

## Q&A

### 2026-06-03 — How do you construct the Breusch-Pagan test?
**Q:** How is the BP test built?
**A:** ① Run the original regression, save residuals. ② Regress the **squared residuals** on the
original independent variables (auxiliary regression). ③ Test statistic `BP = n × R²` (R² from the
auxiliary regression), distributed **χ² with k df** (k = number of independent variables), **one-tailed**.
④ BP > critical → reject H₀ (no heteroskedasticity) → conditional heteroskedasticity present.
Curriculum example: n=60, R²=8% → BP = 60×0.08 = 4.8 > 3.841 → reject. Fix with White standard errors.
Full detail: [[Breusch_Pagan_Test]].

### 2026-06-03 — How does the White method correct heteroskedasticity (the principle)?
**Q:** How does White's method correct it, and what's the underlying principle?
**A:** Curriculum: keep the original coefficients, replace the standard errors with robust
(White-corrected / heteroskedasticity-consistent) SEs, then recompute t-stats. Principle (beyond
scope): OLS coefficients stay unbiased, but `Var(β̂)=σ²(X'X)⁻¹` is wrong under heteroskedasticity. The
true form is a "sandwich" `(X'X)⁻¹[Σσ²ᵢxᵢxᵢ'](X'X)⁻¹`; White estimates the unknown middle by replacing
each `σ²ᵢ` with the squared residual `ê²ᵢ`, giving a consistent (large-sample) variance estimate. SEs
usually grow → more conservative, valid inference.
Related: [[Model_Misspecification]]
