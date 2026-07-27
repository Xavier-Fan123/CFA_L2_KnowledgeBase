---
aliases: [Statistical Tests Master Table, Test Statistics Summary, Hypothesis Test Reference, Which Test Do I Use, Critical Values, Degrees of Freedom Reference]
tags: [CFA-L2, atlas, quant, cheatsheet, test]
date: 2026-07-26
status: evergreen
source: Aggregated from KB quant notes; verified against Schweser Book 1 (Modules 1.1-1.4, 2.1-2.5)
---

# Statistical Tests — Master Table

Every hypothesis test in CFA L2 Quantitative Methods in one place: **statistic → distribution → df → tails → decision rule**. All L2 statistical tests live in Quant (Readings 1-2 + logistic); no other topic area introduces one.

Detail notes: [[Multiple_Regression]] · [[Regression_Assumption_Violations]] · [[Breusch_Pagan_Test]] · [[Time_Series_Analysis]] · [[Logistic_Regression]] · [[Model_Misspecification]]

---

## The Master Table

| # | Test | H₀ (what you're assuming) | Statistic | Dist. | df | Tails | Reject when |
|---|---|---|---|---|---|---|---|
| 1 | **Coefficient t-test** | `bⱼ = 0` (variable irrelevant) | `t = (b̂ⱼ − bⱼ,H₀) / SE(b̂ⱼ)` | **t** | **n − k − 1** | **2** | \|t\| > t_c |
| 2 | **Overall F-test** | `b₁ = b₂ = … = bₖ = 0` (model worthless) | `F = MSR/MSE = (RSS/k) / (SSE/(n−k−1))` | **F** | **k**, **n − k − 1** | **1** (right) | F > F_c |
| 3 | **Nested / partial F-test** | the `q` excluded coefficients are all 0 | `F = [(SSE_R − SSE_U)/q] / [SSE_U/(n−k−1)]` | **F** | **q**, **n − k − 1** | **1** (right) | F > F_c |
| 4 | **Studentized residual** (outlier) | observation is not an outlier | deleted residual ÷ its SD | **t** | **n − k − 2** | **2** | \|t\| > t_c |
| 5 | **Breusch-Pagan (BP)** | no conditional heteroskedasticity | `BP = n × R²_aux` (aux: regress **ê²** on the X's) | **χ²** | **k** | **1** (right) | BP > χ²_c |
| 6 | **Breusch-Godfrey (BG)** | no serial correlation up to `p` lags | regress **ê** on X's **+ lagged ê's**; test lag coefficients | **F** | **p**, **n − p − k − 1** | **1** (right) | BG > F_c |
| 7 | **Durbin-Watson (DW)** | no serial correlation (**1 lag only**) | `DW = Σ(êₜ − êₜ₋₁)² / Σêₜ² ≈ 2(1 − r)` | **DW table** | d_l, d_u by n & k | **2** (w/ inconclusive bands) | `< d_l` → **positive** SC; `> 4 − d_l` → **negative** SC |
| 8 | **Residual autocorrelation t-test** (AR models) | `ρ(ε, lag k) = 0` | `t = ρ̂ / (1/√T) = ρ̂ · √T` | **t** | ≈ **T − 2** | **2** | \|t\| > t_c → AR misspecified, add lags |
| 9 | **Dickey-Fuller (DF)** | `g = b₁ − 1 = 0` → **unit root present** | transform AR(1) to `xₜ − xₜ₋₁ = b₀ + g·xₜ₋₁ + εₜ`, test `g` | **modified t** (DF critical values) | — | **1** (left; Hₐ: g < 0) | reject → **stationary** (no unit root) |
| 10 | **DF-EG** (cointegration) | regression **residuals** have a unit root → **not** cointegrated | DF test on the residuals, **Engle-Granger** critical values | **modified t** (EG values) | — | **1** (left) | reject → **cointegrated** → regression valid |
| 11 | **ARCH(1) test** | `a₁ = 0` → no ARCH | regress `ê²ₜ = a₀ + a₁ê²ₜ₋₁ + uₜ`, test `a₁` | **t** | — | **2** (Hₐ: a₁ ≠ 0) | `a₁` significant → **ARCH** → SEs wrong → use **GLS** |
| 12 | **Likelihood Ratio (LR)** (logit nested) | the `q` dropped coefficients are all 0 | `LR = −2(LL_R − LL_U) = 2(LL_U − LL_R)` | **χ²** | **q** | **1** (right) | LR > χ²_c |

**Not hypothesis tests** — thresholds/diagnostics, no distribution or df:

| Diagnostic | Rule |
|---|---|
| **VIF** (multicollinearity) | `VIFⱼ = 1/(1 − R²ⱼ)`; **> 5** investigate, **> 10** severe |
| **Leverage** (high-leverage point) | `Lᵢ ∈ [0,1]`, `ΣLᵢ = k + 1`; potentially influential if `Lᵢ > 3(k+1)/n` |
| **Adjusted R² / AIC / BIC** | model selection, not significance. Lower AIC/BIC = better (AIC forecasting, BIC goodness of fit) |
| **RMSE** | out-of-sample forecast accuracy; lower = better |
| **Chi-square in Big Data** | ⚠️ ranks **tokens** by association with a class in text feature selection — **not** the BP χ² test. See [[Big_Data_Projects]] |

---

## Rule 1 — Tails: one clean generalization

> **Every F and χ² test is one-tailed right. Every t-test is two-tailed — except Dickey-Fuller.**

That single sentence covers all 12 rows. Why it works:
- **F and χ² are already squared/ratio quantities** — they can't go negative, and only *large* values signal a problem. There is no "too small" side to test. This is why the F-test is one-tailed **despite the "=" in H₀** — the classic L2 trap.
- **t is symmetric**, so a "≠ 0" alternative naturally uses both tails.
- **Dickey-Fuller is the lone exception** because its Hₐ is directional (`g < 0`): a unit root sits at the *boundary* `b₁ = 1`, and the only economically meaningful departure is `b₁ < 1`. Left tail only.

## Rule 2 — Critical values (z; large-sample limit of t)

| Confidence | α | **Two-tailed** | **One-tailed** |
|---|---|---|---|
| 90% | 0.10 | ± **1.645** | **1.28** |
| 95% | 0.05 | ± **1.96** | **1.645** |
| 99% | 0.01 | ± **2.58** | **2.33** |

Five numbers total: **1.28 · 1.645 · 1.96 · 2.33 · 2.58**. **1.645 appears in both columns** — one-tailed 95% = two-tailed 90% (both leave 0.05 in the right tail), so the one-tailed column is the two-tailed column **shifted down one row**. General rule: **one-tailed at α = two-tailed at 2α**.

Confidence interval for a coefficient: `b̂ⱼ ± t_c × SE(b̂ⱼ)`, **always two-tailed**, df = n − k − 1.

## Rule 3 — Degrees of freedom, decoded

`n` = observations · `k` = independent variables · `q` = variables excluded/dropped · `p` = lags tested · `T` = time-series observations

| df | Used by | Logic |
|---|---|---|
| **n − k − 1** | coefficient t-test, F denominators, SEE, MSE | you estimated `k` slopes **+ 1 intercept** = k+1 parameters |
| **n − k − 2** | studentized residual (#4) | same, **minus one more** — the observation was deleted, so you're on n−1 data points |
| **k** | overall F numerator, BP | one per independent variable |
| **q** | nested F numerator, LR | one per **restriction** (variable dropped) |
| **p**, **n − p − k − 1** | BG | `p` lags tested; denominator loses the k regressors, p lagged residuals, and the intercept |

Anchor: **n − k − 1 is the default.** Only #4 (n−k−2), BP (k), the numerators (k / q / p), and BG's denominator deviate.

---

## "Which test do I use?" — decision flow

```
WHAT AM I TESTING?

├─ Does ONE variable matter?          → coefficient t-test  (t, n−k−1, 2-tail)
├─ Does the WHOLE model matter?       → overall F-test      (F, k & n−k−1, 1-tail)
├─ Do SEVERAL variables jointly matter?
│     ├─ OLS / continuous Y           → nested F-test       (F, q & n−k−1, 1-tail)
│     └─ Logit / binary Y             → LR test             (χ², q, 1-tail)   ← NOT F
│
├─ ASSUMPTION VIOLATIONS
│     ├─ Heteroskedasticity           → BP                  (χ², k, 1-tail)  → fix: White SE
│     ├─ Serial correlation, 1 lag    → DW  (0 = +SC, 4 = −SC) → fix: Newey-West SE
│     ├─ Serial correlation, p lags   → BG  (F, p & n−p−k−1)   → fix: Newey-West SE
│     └─ Multicollinearity            → VIF (no test)          → fix: drop variable / new proxy / more data
│
├─ DATA PROBLEMS
│     ├─ Extreme Y (outlier)          → studentized residual (t, n−k−2, 2-tail)
│     └─ Extreme X (high leverage)    → leverage > 3(k+1)/n  (no test)
│
└─ TIME SERIES
      ├─ Is it stationary?            → Dickey-Fuller  (modified t, 1-tail LEFT)
      ├─ AR residuals correlated?     → residual autocorr t-test, t = ρ̂√T   ← DW is INVALID here
      ├─ Seasonality?                 → same t-test at the SEASONAL lag (4 quarterly / 12 monthly)
      ├─ Volatility clustering?       → ARCH(1): regress ê²ₜ on ê²ₜ₋₁      → fix: GLS
      └─ Can I regress series A on B? → DF on each; if both have unit roots → DF-EG for cointegration
```

---

## Direction table — what each violation does to your inference

| Violation | Coefficients | Standard errors | Error you make |
|---|---|---|---|
| **Conditional heteroskedasticity** | unbiased, consistent | **under**estimated | **Type I** (false positives) |
| **Positive serial correlation** | unbiased, consistent* | **under**estimated | **Type I** (false positives) |
| **Multicollinearity** | unbiased, consistent | **over**estimated (inflated) | **Type II** (false negatives) |
| **Omitted variable (correlated w/ X)** | **BIASED + inconsistent** | unreliable | inference invalid at the root |
| **ARCH** | still usable | incorrect | inference unreliable → **GLS** |

\* unless a lagged dependent variable is a regressor.

**The one asymmetry worth memorizing:** heteroskedasticity and serial correlation **shrink** SEs → t-stats too big → you *wrongly find significance* (**Type I**). Multicollinearity **inflates** SEs → t-stats too small → you *wrongly miss significance* (**Type II**). Only **misspecification** touches the coefficients themselves.

---

## Exam Traps

- **F-test is one-tailed** despite the "=" in H₀. Same for BP (χ²) and BG (F). Squared statistics have no left tail.
- **Dickey-Fuller reads backwards:** "cannot reject H₀" = **has a unit root** = non-stationary. Do not reverse this.
- **DF cannot test `b₁ = 1` directly** — it tests the transformed `g = b₁ − 1 = 0` with **modified** (not standard) t critical values.
- **DW is invalid in AR models** (lagged dependent variable as regressor). Use the residual-autocorrelation t-test, `t = ρ̂√T`.
- **DW → 0 = positive SC, DW → 4 = negative SC.** Mnemonic: "positive = pals, they stick together, no gap → 0."
- **DW's inconclusive bands** are its fatal flaw — which is why the 2026 curriculum makes **BG** the workhorse and only names DW as the single-lag test.
- **Logit nested test is LR (χ², q df), NOT F.** Log-likelihood is always negative; **closer to 0 = better fit**.
- **BP's auxiliary regression uses SQUARED residuals** (`ê²`); BG's uses the **residuals themselves** plus their lags. Don't swap them.
- **Studentized residual uses n − k − 2**, not n − k − 1 — the observation was deleted first.
- **Adding a seasonal lag to AR(1) keeps it AR(1) with a seasonal term — NOT AR(2).**
- **ARCH ≠ unit root**: ARCH is about error *variance*; a unit root is about the series *level*.
- **Chi-square appears twice in Quant with unrelated meanings**: BP's heteroskedasticity statistic and LR's logit statistic are hypothesis tests; Big Data's "chi-square" is a **token-ranking feature-selection score**.

## Q&A

### 2026-07-26 — Is there a single rule for which tests are one-tailed vs two-tailed?
**Q:** Across all the L2 quant tests, how do I know which are one-tailed and which are two-tailed?
**A:** **Every F and χ² test is one-tailed right; every t-test is two-tailed — except Dickey-Fuller (one-tailed left).** That covers all 12 tests. F and χ² are squared/ratio quantities that cannot be negative, so only large values signal a problem and there is no left side to test — this is why the F-test is one-tailed **despite the "=" in H₀**, the classic trap. t is symmetric, so a "≠ 0" alternative uses both tails. DF is the sole exception because its Hₐ is directional (`g = b₁ − 1 < 0`): the unit root sits at the boundary `b₁ = 1` and only `b₁ < 1` is meaningful. Confidence intervals are always two-tailed.
Related: [[Multiple_Regression]], [[Regression_Assumption_Violations]]
