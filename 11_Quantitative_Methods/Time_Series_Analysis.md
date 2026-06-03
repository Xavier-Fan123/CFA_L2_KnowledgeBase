---
aliases: [Time Series Analysis, Covariance Stationary, Unit Root, Dickey-Fuller Test, Random Walk, First Differencing, AR Model, Mean Reversion]
tags: [CFA-L2, quant, concept, time-series]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 2, LOS 2.c / 2.f / 2.i / 2.k
---

# Time Series Analysis

## Covariance Stationary (LOS 2.c)

In an autoregressive (AR) model, past values predict the current value. OLS-based inference on an AR
model **may be invalid unless the series is covariance stationary**. A series is covariance stationary
if it meets **three conditions**:

| # | Condition | Meaning |
|---|------|------|
| 1 | **Constant & finite expected value** | Mean is constant over time (= the mean-reverting level) |
| 2 | **Constant & finite variance** | Volatility around the mean is constant over time |
| 3 | **Constant & finite covariance at any lag** | Autocovariance depends only on the lag, not on time |

Mnemonic: **mean, variance, and all autocovariances — each "constant and finite."**

## Mean Reversion (LOS 2.f)

For AR(1) `xₜ = b₀ + b₁xₜ₋₁`, the **mean-reverting level** is `b₀ / (1 − b₁)`. The series tends back
toward this level. An AR(1) has a **finite** mean-reverting level only when **|b₁| < 1**. All covariance-
stationary series have a finite mean-reverting level.

## Random Walk & Unit Root (LOS 2.i)

- **Random walk**: `xₜ = xₜ₋₁ + εₜ` (b₁ = 1). With or without drift, a random walk is **NOT covariance
  stationary** — its mean-reverting level is `b₀/(1−1) = b₀/0`, undefined (infinite).
- `b₁ = 1` means a **unit root**. A series with a unit root follows a random walk and is non-stationary;
  modeling it directly in an AR model gives **incorrect inferences**.

## Testing for Stationarity / Unit Root (LOS 2.k)

**Method 1 — examine autocorrelations:** estimate an AR model; a stationary process has residual
autocorrelations insignificant at all lags, or decaying to zero as lags increase.

**Method 2 — Dickey-Fuller (DF) test** (more definitive):
- You **cannot** directly test whether the AR coefficient = 1. DF transform: subtract `xₜ₋₁` from both sides
  of AR(1): `xₜ − xₜ₋₁ = b₀ + (b₁ − 1)xₜ₋₁ + εₜ`.
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

If a series is a random walk (has a unit root), transform to covariance stationary by **first
differencing**: define `yₜ = xₜ − xₜ₋₁` (model the **change**, not the level). Then fit an AR(1) on the
differenced series `yₜ = b₀ + b₁yₜ₋₁ + εₜ`. The differenced series has a finite mean-reverting level and
is therefore covariance stationary.

**Worked example (capacity utilization):** AR(1) on the level suggests a unit root → not stationary →
take first differences (period-over-period change) → re-estimate AR(1) on the differenced series; the
lag coefficient is now significant → usable.

## Logic Map

```
Build AR model
   ├─ Test stationarity → (1) autocorrelations decay to 0?  (2) Dickey-Fuller (H0: g=0 → unit root)
   ├─ Reject H0 → no unit root → covariance stationary → use AR directly ✓
   └─ Cannot reject H0 → unit root → random walk → non-stationary
                                        └─► first differencing → stationary → re-fit AR(1) on differences ✓
```

## Exam Traps
- DF test cannot test `b₁ = 1` directly; it tests the transformed `g = b₁ − 1 = 0` with a **modified** t.
- **"Cannot reject H₀" = has unit root = non-stationary** (do not reverse this).
- Random walk (with or without drift) is non-stationary; the fix is **first differencing**, not adding
  variables or changing proxies.
- Only a covariance-stationary series is guaranteed a **finite mean-reverting level**.

## Q&A

### 2026-06-03 — What is covariance stationary?
**Q:** What does covariance stationary mean?
**A:** A time series is covariance stationary if it meets three conditions: (1) constant and finite
expected value (mean), (2) constant and finite variance, (3) constant and finite covariance with itself
at any given lag. It is the prerequisite for valid AR-model inference. A random walk (unit root, b₁=1)
is not covariance stationary because its mean-reverting level `b₀/(1−b₁)` is undefined; fix via first
differencing.

### 2026-06-03 — Unit root / Dickey-Fuller test / first differencing
**Q:** Explain the unit root, the Dickey-Fuller test steps, and first differencing.
**A:** b₁=1 → unit root → random walk → non-stationary → AR inference invalid. You can't test b₁=1
directly, so DF subtracts xₜ₋₁ from both sides of AR(1) and tests `g = b₁−1 = 0` with a modified t-test.
H₀: g=0 = unit root present. "Cannot reject H₀" → has a unit root (non-stationary); "reject" → stationary.
Fix non-stationarity with **first differencing** `yₜ = xₜ − xₜ₋₁`, then fit AR(1) on the differenced
series (now has a finite mean-reverting level → covariance stationary). Capacity-utilization example
demonstrates the full flow.
Related: [[Model_Misspecification]]
