---
aliases: [Regression Assumption Violations, Heteroskedasticity, Serial Correlation, Multicollinearity, BP Test, White Standard Errors, Newey-West]
tags: [CFA-L2, quant, concept, regression]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 1.3, LOS 1.h / 1.i / 1.j
---

# Regression Assumption Violations

The three primary assumption violations: **(1) heteroskedasticity, (2) serial correlation (autocorrelation), (3) multicollinearity.**

> All test statistics, df, tails, and decision rules side by side: [[Statistical_Tests_Master_Table]].

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

**Correction:** compute **robust standard errors** (a.k.a. **White-corrected** / heteroskedasticity-consistent standard errors), then recompute t-stats using the **original coefficients**.

### White correction — the principle (beyond-scope add-on)
> Curriculum only says "use White standard errors, coefficients unchanged." The mechanism below is added reasoning, not curriculum text.

- OLS coefficients stay unbiased/consistent under heteroskedasticity; only `Var(β̂)` is computed wrong.
- OLS assumes homoskedasticity: `Var(β̂) = σ²(X'X)⁻¹`. The true ("sandwich") form is `Var(β̂) = (X'X)⁻¹ [Σ σ²ᵢ xᵢxᵢ'] (X'X)⁻¹`.
- The middle term has n unknown `σ²ᵢ` — can't estimate each. **White's insight:** you don't need each `σ²ᵢ`, only the sum; replace `σ²ᵢ` with the squared OLS residual `ê²ᵢ`: `V̂_White = (X'X)⁻¹ (Σ ê²ᵢ xᵢxᵢ') (X'X)⁻¹` — the heteroskedasticity-consistent estimator.
- Square-root the diagonal → robust SE. Coefficients unchanged; SEs (usually larger) → more conservative, valid t-tests. It is a **large-sample (asymptotic)** result.

---

## 2. Serial Correlation / Autocorrelation (LOS 1.i)

Residuals are correlated across observations: `Cov(εₜ, εₜ₋₁) ≠ 0`. Common in time series.

**Effects:** standard errors wrong (positive serial correlation → SE underestimated → Type I errors); coefficient estimates remain consistent (unless a lagged dependent variable is a regressor).

**Detection:**
- **Durbin-Watson (DW)** — single-lag serial correlation only.
- **Breusch-Godfrey (BG) test** — more general, handles multiple lags. Regresses the residuals on the original regressors **plus** lagged residual(s); BG statistic has an **F-distribution** with `p` and `n − p − k − 1` df (`p` = lags tested). BG stat > critical → reject "no serial correlation."

### Durbin-Watson: reading the scale

`DW = Σₜ₌₂ⁿ(êₜ − êₜ₋₁)² / Σₜ₌₁ⁿ êₜ²` and, for large samples, **`DW ≈ 2(1 − r)`** where `r` = correlation of adjacent residuals.

| r | DW | Meaning |
|---|---|---|
| **+1** | **0** | perfect **positive** serial correlation |
| 0 | 2 | no serial correlation |
| **−1** | **4** | perfect **negative** serial correlation |

**Why (the memory anchor):** the numerator is the sum of squared **gaps between neighbouring residuals**.
- Positive SC → residuals persist (+ follows +), neighbours look alike → gaps ≈ 0 → **DW ≈ 0**.
- Negative SC → residuals alternate `+, −, +, −` → every gap is ~double the residual → numerator maximal → **DW ≈ 4**.

Mnemonic: **"Positive = Pals"** — they stick together, no gap → 0. Negative = flip-flop, maximum gap → 4.
Fallback: write `2(1 − r)`, set `r = +1` → 0.

*Derivation (beyond curriculum, my reasoning):* numerator `= Σêₜ² + Σêₜ₋₁² − 2Σêₜêₜ₋₁ ≈ 2Σê² − 2rΣê² = 2Σê²(1 − r)`; divide by `Σê²` → `2(1 − r)`.

**Decision rule (symmetric about 2):**

| DW range | Conclusion |
|---|---|
| 0 → d_l | reject H₀ → **positive** serial correlation |
| d_l → d_u | inconclusive |
| d_u → 4 − d_u | fail to reject → no serial correlation |
| 4 − d_u → 4 − d_l | inconclusive |
| 4 − d_l → 4 | reject H₀ → **negative** serial correlation |

The **inconclusive region** is DW's fatal weakness — which is why the 2026 curriculum only names DW as "the single-lag test" and makes **BG** the workhorse. (Schweser Book 1 gives no d_l/d_u table in Module 1.3; the "DW ≈ 2.0" benchmark reappears in the trend-model section of Module 3.)

**Correction:** **Newey-West** corrected standard errors (robust to both serial correlation AND heteroskedasticity), then recompute t-stats on original coefficients.

> Intuition: Newey-West generalizes White — its "sandwich" filling adds the cross-period residual products `êᵢêᵢ₋ⱼ` (serial-correlation terms) on top of `ê²ᵢ` (heteroskedasticity term).

---

## 3. Multicollinearity (LOS 1.j)

Two or more independent variables are **highly correlated** with each other.

**Effects:** coefficients still consistent/unbiased, but **standard errors inflated** → t-stats too small → variables look insignificant (high R² / significant F, yet few significant t-stats = classic multicollinearity signature).

**Full consequence list (what breaks vs. what survives):**

| Affected | Not affected |
|---|---|
| SEs of slope coefficients **inflated** | R² and adjusted R² |
| t-stats deflated → **Type II error** (fail to reject H₀: bⱼ=0 for variables that do matter) | F-test of overall significance (still significant) |
| Coefficients **unstable** — signs flip / magnitudes swing when one observation or variable is added or dropped; implausible signs appear | Unbiasedness & consistency of the coefficients |
| Individual-effect interpretation ("holding others constant") breaks down — the data never hold them constant | Forecasting / Ŷ, *provided* the collinearity structure persists and you stay in-sample |

**Detection — Variance Inflation Factor (VIF):** `VIFⱼ = 1 / (1 − R²ⱼ)`, where `R²ⱼ` is from regressing `Xⱼ` on the other regressors.
- VIF = 1 (R²=0): not correlated with others.
- VIF > 5 (R² > 80%): investigate.
- VIF > 10 (R² > 90%): **severe** multicollinearity.

**Correction:** omit one or more correlated variables; use a different proxy; or increase sample size.
No robust-SE patch exists here — unlike White / Newey-West, you must change the **model or the data**.

**Perfect (exact) multicollinearity** is a separate case: the model **cannot be estimated at all** (software drops a regressor). Classic cause = the dummy-variable trap (including all n categories instead of n−1). See [[Multiple_Regression]] assumption 5.

---

## Master Comparison Table

| Dimension | Heteroskedasticity | Serial Correlation | Multicollinearity |
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
- **DW → 0 = positive SC, DW → 4 = negative SC** (`DW ≈ 2(1−r)`). Mnemonic: "positive = pals, no gap → 0."
- **DW is invalid when a lagged dependent variable is a regressor** (i.e. in any AR model) — use the t-test on residual autocorrelations, `t = ρ̂ / (1/√T)`. See [[Time_Series_Analysis]].
- Direction confusion: *positive* SC (DW near 0) → SEs **under**estimated → t-stats too big → **Type I** error. Opposite of multicollinearity, which causes Type II.
- Multicollinearity's tell: **high R² + significant F but insignificant t-stats**.
- All three corrections (White, Newey-West) change only the **standard errors**, never the coefficients.
- Multicollinearity does **not** bias coefficients — only inflates their SEs. **Omitted-variable bias (misspecification) is the one that biases coefficients.** Don't mix them up.
- Low pairwise correlations do **not** rule out multicollinearity: three or more variables can be jointly collinear with modest pairwise correlations. Correlation alone is diagnostic only in a two-variable regression — use VIF.

## Q&A

### 2026-07-26 — Why is DW near 0 positive serial correlation and near 4 negative? How to remember?
**Q:** Why does a DW statistic close to 0 mean positive serial correlation and close to 4 mean negative, and how do you memorize which is which?
**A:** Anchor on **`DW ≈ 2(1 − r)`**: `r = +1 → DW = 0`; `r = 0 → DW = 2`; `r = −1 → DW = 4`. The reason is that DW's numerator `Σ(êₜ − êₜ₋₁)²` measures the **squared gaps between neighbouring residuals** — under positive SC residuals persist so neighbours look alike (gap ≈ 0 → DW ≈ 0); under negative SC they alternate sign so each gap is ~double the residual (numerator maximal → DW ≈ 4). Mnemonic: **"positive = pals, they stick together, no gap → 0."** Decision scale is symmetric about 2: `<d_l` positive SC, `>4−d_l` negative SC, `d_u` to `4−d_u` clean, two inconclusive bands in between. Traps: DW is invalid with a lagged dependent variable (AR models — use the residual-autocorrelation t-test); and positive SC understates SEs → **Type I** error.
Related: [[Time_Series_Analysis]], [[Multiple_Regression]]

### 2026-07-26 — What are the consequences of multicollinearity?
**Q:** When a model has multicollinearity, what does it cause?
**A:** It destroys **precision**, not unbiasedness. (1) SEs of the slope coefficients are **inflated**; (2) t-stats deflate → **Type II error**, real variables look insignificant; (3) the exam signature is **high R² + significant F but insignificant t-stats**; (4) coefficients become **unstable** — signs flip and magnitudes swing when one observation or variable changes; (5) the "holding others constant" interpretation of bⱼ breaks down. **Unaffected:** R²/adj-R², the F-test, coefficient unbiasedness/consistency, and forecasting (if the collinearity structure persists and you stay in-sample). Detect with `VIFⱼ = 1/(1−R²ⱼ)` (>5 investigate, >10 severe); fix by dropping a variable, changing proxy, or enlarging the sample — there is **no robust-SE patch** as there is for heteroskedasticity (White) or serial correlation (Newey-West). Contrast: omitted-variable bias **does** bias coefficients.
Related: [[Multiple_Regression]], [[Model_Misspecification]]

### 2026-06-03 — How do you construct the Breusch-Pagan test?
**Q:** How is the BP test built?
**A:** ① Run the original regression, save residuals. ② Regress the **squared residuals** on the original independent variables (auxiliary regression). ③ Test statistic `BP = n × R²` (R² from the auxiliary regression), distributed **χ² with k df** (k = number of independent variables), **one-tailed**. ④ BP > critical → reject H₀ (no heteroskedasticity) → conditional heteroskedasticity present. Curriculum example: n=60, R²=8% → BP = 60×0.08 = 4.8 > 3.841 → reject. Fix with White standard errors. Full detail: [[Breusch_Pagan_Test]].

### 2026-06-03 — How does the White method correct heteroskedasticity (the principle)?
**Q:** How does White's method correct it, and what's the underlying principle?
**A:** Curriculum: keep the original coefficients, replace the standard errors with robust (White-corrected / heteroskedasticity-consistent) SEs, then recompute t-stats. Principle (beyond scope): OLS coefficients stay unbiased, but `Var(β̂)=σ²(X'X)⁻¹` is wrong under heteroskedasticity. The true form is a "sandwich" `(X'X)⁻¹[Σσ²ᵢxᵢxᵢ'](X'X)⁻¹`; White estimates the unknown middle by replacing each `σ²ᵢ` with the squared residual `ê²ᵢ`, giving a consistent (large-sample) variance estimate. SEs usually grow → more conservative, valid inference.
Related: [[Model_Misspecification]]
