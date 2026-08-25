---
aliases: [Time Series Analysis, Covariance Stationary, Unit Root, Dickey-Fuller Test, Random Walk, First Differencing, AR Model, Mean Reversion, Trend Model, Log-Linear Trend, Seasonality, Seasonal Lag, Chain Rule of Forecasting, RMSE, Cointegration, Engle-Granger, ARCH]
tags: [CFA-L2, quant, concept, time-series]
date: 2026-08-25
status: evergreen
source: Schweser Book 1, Reading 2 (Modules 2.1–2.5), LOS 2.a–2.o
---

# Time Series Analysis

> DF / DF-EG / ARCH / residual-autocorrelation tests compared against every other L2 test: [[Statistical_Tests_Master_Table]].

## Trend Models (LOS 2.a–2.b)

| Model | Equation | Use when… |
|---|---|---|
| **Linear trend** | `yₜ = b₀ + b₁t + εₜ` | variable changes by a **constant amount** each period (data plots on a straight line; e.g. inflation) |
| **Log-linear trend** | `ln(yₜ) = b₀ + b₁t + εₜ` | variable grows at a **constant rate** / exponential growth (convex curve; e.g. stock prices, sales) |

- The independent variable is **time t = 1, 2, …, T**. For log-linear, the forecast comes out as **ln(y)** — take `eˣ` (BA II Plus `[2nd] LN`) to get the level. Example: ln-forecast 8.41 → e^8.41 = $4,492M.
- **Choosing**: plot the data. Equally scattered around the line → linear. Curved / residuals persistently positive then negative (serially correlated) → log-linear.
- **Limitation**: trend models assume **uncorrelated residuals**. If the **Durbin-Watson** stat is far from **2.0**, residuals are serially correlated → trend model inadequate → switch to an **AR model**.

## Covariance Stationary (LOS 2.c)

In an autoregressive (AR) model, past values predict the current value. OLS-based inference on an AR model **may be invalid unless the series is covariance stationary**. A series is covariance stationary if it meets **three conditions**:

| # | Condition | Meaning |
|---|------|------|
| 1 | **Constant & finite expected value** | Mean is constant over time (= the mean-reverting level) |
| 2 | **Constant & finite variance** | Volatility around the mean is constant over time |
| 3 | **Constant & finite covariance at any lag** | Autocovariance depends only on the lag, not on time |

Mnemonic: **mean, variance, and all autocovariances — each "constant and finite."**

## Mean Reversion (LOS 2.f)

For AR(1) `xₜ = b₀ + b₁xₜ₋₁`, the **mean-reverting level** is `b₀ / (1 − b₁)`. The series tends back toward this level. An AR(1) has a **finite** mean-reverting level only when **|b₁| < 1**. All covariance-stationary series have a finite mean-reverting level.

## AR(p) Model Structure & Detecting Correlated Residuals (LOS 2.d–2.e)

An **autoregressive model of order p, AR(p)**, regresses the variable on its own `p` most recent lags: `xₜ = b₀ + b₁xₜ₋₁ + b₂xₜ₋₂ + … + bₚxₜ₋ₚ + εₜ`. AR(1) uses only the first lag. OLS estimation of an AR model is valid only when the series is **covariance stationary** and the **residuals are uncorrelated**.

**Why not Durbin-Watson here:** the DW statistic is **invalid** when a lagged dependent variable is a regressor (which is exactly the AR setup). Use the **residual-autocorrelation t-test** instead.

**Three-step test that an AR model fits (LOS 2.e):**
1. Estimate the AR model (e.g. AR(1)) and obtain the residuals.
2. Compute the **autocorrelations of the residuals** at each lag `k`.
3. For each lag, test H₀: residual autocorrelation = 0 with a t-test. The **standard error of a residual autocorrelation is `1/√T`** (T = number of observations), so

   `t = ρ̂(ε,k) / (1/√T) = ρ̂(ε,k) × √T`

   Compare |t| to the critical t (df ≈ T − 2). **Any significant residual autocorrelation ⇒ the AR model is misspecified** — add more lags (including a seasonal lag) and re-test until all residual autocorrelations are insignificant. **No significant autocorrelations ⇒ the model is well specified.**

**Worked example (residual-autocorrelation test):** AR(1) estimated on **T = 102** observations. SE = `1/√102 = 0.099`. The lag-2 residual autocorrelation is 0.0843 → `t = 0.0843/0.099 = 0.85`. The critical two-tail t at 5% with 100 df is **1.98**; 0.85 < 1.98 ⇒ fail to reject ⇒ that autocorrelation is **not** significant. If every lag is insignificant, the AR(1) errors are not serially correlated → model OK. (Source: Schweser Book 1, Module 2.1; official LM5 uses the same `1/√T` SE — e.g. 1/√40 = 0.1581.)

## Forecasting AR Models — Chain Rule & RMSE (LOS 2.d / 2.g)

- **One- and two-period-ahead forecasts (chain rule of forecasting)**: because the regressor is a *lagged* value, multi-step forecasts must be built sequentially. For AR(1):
  - one-step: `x̂ₜ₊₁ = b₀ + b₁xₜ` (uses the **actual** current value `xₜ`)
  - two-step: `x̂ₜ₊₂ = b₀ + b₁x̂ₜ₊₁` (plugs in the **forecast** `x̂ₜ₊₁`, not an actual value)

  Each forecast feeds the next, so **multiperiod forecasts are more uncertain** than single-period ones (uncertainty compounds at every step).

**Worked example (one- & two-period AR(1) forecast):** estimated AR(1) `x̂ₜ = 1.2 + 0.45xₜ₋₁`, current `xₜ = 5.0`.
- One-step: `x̂ₜ₊₁ = 1.2 + 0.45(5.0) = 3.45`.
- Two-step: `x̂ₜ₊₂ = 1.2 + 0.45(3.45) = 2.7525` (note: feeds the **forecast** 3.45, not 5.0).
- These converge toward the mean-reverting level `1.2/(1−0.45) = 2.18`. (Source: Schweser Book 1, Module 2.1.)
- **In-sample vs. out-of-sample**: in-sample forecasts fall inside the estimation data; out-of-sample fall outside it. Out-of-sample accuracy is the real test of forecasting power.
- **RMSE (root mean squared error)** = √(average squared out-of-sample error). To choose between two models that both fit (e.g. AR(1) vs. AR(2)), pick the one with the **lower out-of-sample RMSE** → smaller forecast error, better predictive power.

## Random Walk & Unit Root (LOS 2.i)

- **Random walk**: `xₜ = xₜ₋₁ + εₜ` (b₁ = 1). With or without drift, a random walk is **NOT covariance stationary** — its mean-reverting level is `b₀/(1−1) = b₀/0`, undefined (infinite).
- `b₁ = 1` means a **unit root**. A series with a unit root follows a random walk and is non-stationary; modeling it directly in an AR model gives **incorrect inferences**.

## Testing for Stationarity / Unit Root (LOS 2.k)

**Method 1 — examine autocorrelations:** estimate an AR model; a stationary process has residual autocorrelations insignificant at all lags, or decaying to zero as lags increase.

**Method 2 — Dickey-Fuller (DF) test** (more definitive):
- You **cannot** directly test whether the AR coefficient = 1. DF transform: subtract `xₜ₋₁` from both sides of AR(1): `xₜ − xₜ₋₁ = b₀ + (b₁ − 1)xₜ₋₁ + εₜ`.
- Let `g = b₁ − 1` and test `g = 0` with a **modified t-test**.

| Item | Value |
|------|------|
| H₀ | `g = 0` (i.e. b₁ = 1) → **series has a unit root (non-stationary)** |
| Hₐ | `g < 0` (b₁ < 1) → no unit root (stationary) |
| Test | **Modified t-test** (not standard t critical values) |

**Exam result reading (Professor's Note):**
- "Cannot reject H₀ (g=0)" → **series HAS a unit root (non-stationary)**.
- "Reject H₀" → series does NOT have a unit root (stationary).

## Fix: First Differencing

If a series is a random walk (has a unit root), transform to covariance stationary by **first differencing**: define `yₜ = xₜ − xₜ₋₁` (model the **change**, not the level). Then fit an AR(1) on the differenced series `yₜ = b₀ + b₁yₜ₋₁ + εₜ`. The differenced series has a finite mean-reverting level and is therefore covariance stationary.

**Worked example (capacity utilization):** AR(1) on the level suggests a unit root → not stationary → take first differences (period-over-period change) → re-estimate AR(1) on the differenced series; the lag coefficient is now significant → usable.

## ARCH (2.m) — Autoregressive Conditional Heteroskedasticity

A series has **ARCH** when the **variance of the error in one period depends on the variance of the error in prior periods** — the error variance is *conditional* (time-varying) and *autoregressive* (driven by its own past). The error term is then **conditionally heteroskedastic**.

**ARCH(1) test** — regress squared residuals on their own first lag:

```
ε̂ₜ² = a₀ + a₁ε̂ₜ₋₁² + uₜ
```

| Item | Reading |
|------|---------|
| H₀ | `a₁ = 0` → **no ARCH** (constant / homoskedastic error variance) |
| Hₐ | `a₁ ≠ 0` → **ARCH present** |
| Decision | `a₁` **statistically significant** → series **has ARCH** |

**Consequences & fix:**
- Standard errors of the regression coefficients become **incorrect** → t-stats / inference unreliable (coefficients themselves still usable). Fix with **generalized least squares (GLS)**.

**Constructive use — forecast next-period variance.** If ARCH(1) holds:

```
σ̂ₜ₊₁² = â₀ + â₁ε̂ₜ²
```

useful for volatility / VaR forecasting.

## Seasonality (LOS 2.l)

Seasonality = a pattern that repeats **year to year** (e.g. retail sales spike each December). It makes an AR model **misspecified** unless a seasonal lag is added.

- **Detect**: examine the **residual autocorrelations**. A statistically significant autocorrelation at the **seasonal lag** signals seasonality — **lag 4** for quarterly data, **lag 12** for monthly. (Hotel example: lag-4 residual autocorrelation t-stat 5.45 > 2.026 → seasonality present.)
- **Correct**: add a **seasonal lag** of the dependent variable as an extra regressor. Quarterly AR(1) with seasonal lag: `ln xₜ = b₀ + b₁ ln xₜ₋₁ + b₂ ln xₜ₋₄ + εₜ`. ⚠️ This is **still an AR(1) model with a seasonal term — NOT an AR(2)**. After correcting, the seasonal-lag residual autocorrelation becomes insignificant and R² jumps (hotel example: 79.3% → 94.9%).
- **Forecast**: plug both the prior-period and prior-year values into the seasonal equation; the answer is in ln units → apply `eˣ`.

## Multiple Time Series & Cointegration (LOS 2.n)

When regressing one time series on another (e.g. market model: stock returns yₜ on market returns xₜ), **either series may have a unit root**. Run separate **Dickey-Fuller** tests first → **five scenarios**:

| Scenario | yₜ | xₜ | Linear regression valid? |
|---|---|---|---|
| 1 | stationary | stationary | ✅ Yes — reliable |
| 2 | stationary | unit root | ❌ No |
| 3 | unit root | stationary | ❌ No |
| 4 | unit root | unit root, **not** cointegrated | ❌ No |
| 5 | unit root | unit root, **cointegrated** | ✅ Yes — reliable |

**Cointegration** = two series are economically linked / share a common trend that is not expected to change, so the **error from regressing one on the other is covariance stationary** → t-tests are reliable. **Test**: regress one on the other, then run a **Dickey-Fuller test on the residuals using Engle-Granger critical values (DF-EG test)**. Reject the unit-root null → residuals stationary → series **cointegrated** → regression usable (Scenario 5).

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- Commodity **price levels** often behave like non-stationary series, while spreads, returns, or inventory-adjusted basis may be closer to stationary. Regressing one price level on another without testing unit roots can produce a high R-squared and meaningless inference.
- Cointegration is useful when there is a durable economic link, such as spot vs. nearby futures, related grades, substitute fuels, or regional prices connected by freight and quality differentials. The tradeable idea is usually the stationary residual, not the two outright price levels.
- Seasonality is structural for many commodities. Heating demand, refinery maintenance, harvest cycles, monsoons, storage injection/withdrawal, and shipping seasons can create predictable lags; ignoring them can make an AR model look falsely misspecified.
- ARCH/volatility clustering is common around inventory reports, weather shocks, policy announcements, delivery squeezes, and geopolitical events. A mean forecast and a volatility forecast should be treated as separate outputs.
- Structural breaks matter more than elegant in-sample fit. Pipeline reversals, new export capacity, benchmark reform, contract-specification changes, sanctions, and storage constraints can invalidate a previously stable basis or cointegration relationship.
- Model outputs must be tied back to execution. A statistically stationary spread is not automatically tradable if the convergence horizon is longer than credit tenor, margin capacity, storage availability, or mandate limits.

## Logic Map — Full Model-Selection Flow (LOS 2.o)

```
1. Goal? relate variables (cross-section / cointegration) vs. model over time (time series)
2. Plot the series → look for non-constant variance, non-constant mean, seasonality, STRUCTURAL SHIFT
       └─ structural shift → split into 2 models (before/after the break)
3. No seasonality/shift → TREND model:  straight line → linear ;  curved → log-linear
4. Test residuals with Durbin-Watson:  ≈2 → use trend model ✓ ;  serial correlation → go AR
5. Before AR, check stationarity:  linear trend → first-difference ;  exponential → first-difference ln
6. Run AR(1) on (differenced) series → test residual autocorrelations
       └─ serial correlation remains → add lags (incl. seasonal lag, e.g. 12 for monthly)
7. Test ARCH: regress ê²ₜ on ê²ₜ₋₁ ;  a₁ significant → ARCH → correct with GLS
8. Two good models? choose the one with lower out-of-sample RMSE
```

## Exam Traps
- **Durbin-Watson is invalid for AR models** (lagged dependent variable as regressor). Detect serial correlation of AR residuals with the **t-test on residual autocorrelations**, SE = **`1/√T`**, `t = ρ̂·√T`. Any significant residual autocorrelation ⇒ add lags / re-specify.
- **Two-period AR(1) forecast feeds the one-period FORECAST, not the actual value**: `x̂ₜ₊₂ = b₀ + b₁x̂ₜ₊₁` (a classic trap is to reuse `xₜ`). Multiperiod forecasts are more uncertain.
- DF test cannot test `b₁ = 1` directly; it tests the transformed `g = b₁ − 1 = 0` with a **modified** t.
- **"Cannot reject H₀" = has unit root = non-stationary** (do not reverse this).
- Random walk (with or without drift) is non-stationary; the fix is **first differencing**, not adding variables or changing proxies.
- Only a covariance-stationary series is guaranteed a **finite mean-reverting level**.
- **ARCH ≠ unit root**: ARCH concerns the error *variance*; a unit root concerns the series *level*.
- Test ARCH by regressing **squared residuals on lagged squared residuals**; significant `a₁` → ARCH → SEs wrong → use **GLS**. If ARCH exists you **can** forecast next-period variance.
- **Linear vs. log-linear**: constant *amount* of change → linear; constant *rate* (exponential) → log-linear. Serially correlated trend residuals (DW ≠ 2) → abandon the trend model for AR.
- A **seasonal lag** added to AR(1) keeps it an **AR(1) with a seasonal term, not AR(2)**. Detect seasonality via a significant residual autocorrelation at lag 4 (quarterly) / 12 (monthly).
- Two time series: regression is valid **only** if (a) neither has a unit root, or (b) both have unit roots **and are cointegrated** (DF-EG test). One-has-one-doesn't → invalid.
- Out-of-sample **RMSE** (lower = better) chooses between competing forecasting models.

## Q&A

### 2026-06-03 — What is covariance stationary?
**Q:** What does covariance stationary mean?
**A:** A time series is covariance stationary if it meets three conditions: (1) constant and finite expected value (mean), (2) constant and finite variance, (3) constant and finite covariance with itself at any given lag. It is the prerequisite for valid AR-model inference. A random walk (unit root, b₁=1) is not covariance stationary because its mean-reverting level `b₀/(1−b₁)` is undefined; fix via first differencing.

### 2026-06-03 — Unit root / Dickey-Fuller test / first differencing
**Q:** Explain the unit root, the Dickey-Fuller test steps, and first differencing.
**A:** b₁=1 → unit root → random walk → non-stationary → AR inference invalid. You can't test b₁=1 directly, so DF subtracts xₜ₋₁ from both sides of AR(1) and tests `g = b₁−1 = 0` with a modified t-test. H₀: g=0 = unit root present. "Cannot reject H₀" → has a unit root (non-stationary); "reject" → stationary. Fix non-stationarity with **first differencing** `yₜ = xₜ − xₜ₋₁`, then fit AR(1) on the differenced series (now has a finite mean-reverting level → covariance stationary). Capacity-utilization example demonstrates the full flow.
Related: [[Model_Misspecification]]

### 2026-06-04 — How do you test and correct for seasonality?
**Q:** How is seasonality detected and corrected in a time-series model, and does it make the model AR(2)?
**A:** Detect by examining the **residual autocorrelations** of the fitted AR model: a statistically significant autocorrelation at the **seasonal lag** (4 for quarterly, 12 for monthly data) signals seasonality, which makes the model misspecified. Correct by **adding a seasonal lag** of the dependent variable as an extra regressor, e.g. quarterly `ln xₜ = b₀ + b₁ ln xₜ₋₁ + b₂ ln xₜ₋₄ + εₜ`. This remains an **AR(1) model with a seasonal term — NOT an AR(2)**. After correction the seasonal-lag autocorrelation becomes insignificant and R² improves.
Related: [[Multiple_Regression]]

### 2026-06-04 — When can you regress one time series on another (cointegration)?
**Q:** Two time series may each have a unit root — when is linear regression between them valid?
**A:** Run a **Dickey-Fuller test on each** series. Five scenarios: (1) both stationary → valid; (2) only y stationary → invalid; (3) only x stationary → invalid; (4) both unit roots, **not** cointegrated → invalid; (5) both unit roots **and cointegrated** → valid. **Cointegration** means the two series share a stable long-run relationship so the **regression residuals are covariance stationary**; test it with a **Dickey-Fuller test on the residuals using Engle-Granger critical values (DF-EG)** — reject the unit-root null → cointegrated → regression reliable.
Related: [[Multiple_Regression]]

### 2026-06-04 — How do you compute one- and two-period AR(1) forecasts, and test the AR model's fit?
**Q:** Given an estimated AR(1) model, how do you make one- and two-period-ahead forecasts, and how do you check the model is correctly specified?
**A:** **Forecasts (chain rule):** one-step `x̂ₜ₊₁ = b₀ + b₁xₜ` uses the **actual** current value; two-step `x̂ₜ₊₂ = b₀ + b₁x̂ₜ₊₁` plugs in the **forecast** (not the actual), so multiperiod forecasts are more uncertain. Example `x̂ₜ = 1.2 + 0.45xₜ₋₁`, xₜ=5.0 → one-step 3.45, two-step 1.2 + 0.45(3.45) = 2.7525. **Model-fit test (LOS 2.e):** Durbin-Watson is **invalid** for AR models (lagged dependent variable), so test the **residual autocorrelations**: SE = **`1/√T`**, `t = ρ̂·√T`, compared to critical t (df ≈ T−2). Any significant residual autocorrelation ⇒ misspecified ⇒ add lags and re-test until all are insignificant. Example: T=102 → SE = 1/√102 = 0.099; lag-2 autocorr 0.0843 → t = 0.85 < 1.98 → not significant → AR(1) errors not serially correlated.
Related: [[Multiple_Regression]]

### 2026-06-04 — What is ARCH?
**Q:** What is ARCH?
**A:** ARCH (autoregressive conditional heteroskedasticity) means the **variance of the regression error in one period depends on the variance of the error in previous periods** — the error is conditionally heteroskedastic. Test ARCH(1) by regressing squared residuals on their first lag: `ε̂ₜ² = a₀ + a₁ε̂ₜ₋₁² + uₜ`; if `a₁` is statistically significant the series has ARCH. Consequence: the regression's **standard errors are incorrect** → use **generalized least squares (GLS)**. Bonus: with ARCH you can forecast next-period variance via `σ̂ₜ₊₁² = â₀ + â₁ε̂ₜ²`. Don't confuse ARCH (error variance) with a unit root (series level).
Related: [[Model_Misspecification]]
