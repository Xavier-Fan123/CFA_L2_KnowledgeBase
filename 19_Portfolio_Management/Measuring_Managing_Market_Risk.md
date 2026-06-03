---
aliases: [Measuring and Managing Market Risk, Value at Risk, VaR, Expected Shortfall, Sensitivity Risk, Scenario Risk, Risk Budgeting]
tags: [CFA-L2, pm, concept, risk]
date: 2026-06-03
status: evergreen
source: Schweser Book 5, Module 38, LOS 38.a-38.l
---

# Measuring and Managing Market Risk

## Value at Risk (38.a)
- **VaR** = the **minimum loss** expected over a given period at a given confidence level (e.g., "5% 1-day
  VaR = $1m" → at least $1m loss is expected 5% of the time / on ~1 in 20 days).
- Three elements: a **loss amount**, a **time period**, and a **probability**.
- **Worked example (Schweser):** "There is a 5% probability of a loss of **$25,000 or more** in any given
  month" = a **monthly 5% VaR of $25,000**. Equivalently: "5% of the time, the **minimum** monthly loss
  is $25,000." The $25,000 is a **minimum** (not maximum) loss at that confidence.

## Estimation Methods (38.b, 38.c)
| Method | How | Pros / Cons |
|------|------|------|
| **Parametric (variance-covariance)** | Assume normal returns; VaR from mean, σ, and z-score | Simple, fast; **poor for options/non-normal** (fat tails, skew) |
| **Historical simulation** | Reprice the current portfolio over actual past returns; read the percentile | No distribution assumption, handles options; but **assumes the past repeats**, limited by sample |
| **Monte Carlo simulation** | Simulate many returns from assumed distributions | Flexible, handles complex portfolios; **computationally heavy**, model-dependent |

## Advantages & Limitations (38.d)
- **+**: single, comparable number; widely used; aggregates across positions.
- **−**: says nothing about the **size of losses beyond VaR**; sensitive to assumptions/look-back;
  can understate tail risk; not subadditive in general (historical/parametric).

## Extensions (38.e)
- **Conditional VaR (CVaR) / expected shortfall**: average loss **given** that loss exceeds VaR (tail).
- **Incremental VaR**: change in VaR from adding/removing a position. **Marginal VaR**: sensitivity to a
  small change. **Relative (ex-ante tracking) VaR**: VaR of active return vs benchmark.

## Sensitivity & Scenario Measures (38.f-38.i)
- **Sensitivity**: equity **beta**; fixed-income **duration & convexity**; option **Greeks (delta,
  gamma, vega)**. Measure exposure to a single risk factor, but **not probability** of loss.
- **Scenario risk**: **historical** scenarios (replay a past crisis) and **hypothetical/stress** tests
  (extreme but plausible). Capture non-normal, multi-factor stress that VaR may miss.

## Constraints & Users (38.j, 38.k, 38.l)
- **Constraints**: **risk budgeting** (allocate a total risk limit across units), **position limits**,
  **scenario limits**, **stop-loss limits**.
- Different users emphasize different measures: **banks** (regulatory VaR, liquidity, leverage),
  **asset managers** (active risk / relative VaR), **pensions** (surplus-at-risk, liability-relative),
  **insurers** (economic capital, scenario/stress).

## Exam Traps
- VaR is a **minimum** loss at a confidence level, not the maximum; it ignores **how bad** the tail is —
  use **CVaR/expected shortfall** for that.
- **Parametric VaR is poor for option-heavy portfolios** (non-normal); historical/Monte Carlo handle them.
- Sensitivity measures give **exposure**, not loss probability; scenario analysis covers tail/multi-factor stress.

## Q&A

### 2026-06-03 — What exactly does "5% VaR = $25,000/month" mean?
**Q:** State the correct interpretation and what VaR fails to tell you.
**A:** It means there is a **5% probability of losing $25,000 or more** in a month — i.e., 5% of the time
the loss is **at least** $25,000. VaR is a **minimum** loss at that confidence, **not** a maximum, and it
says **nothing about how large** the loss is once you're in the tail. For the average loss beyond VaR,
use **conditional VaR / expected shortfall**. Other extensions: incremental VaR (Δ from adding a
position), marginal VaR (sensitivity), relative/ex-ante tracking VaR (active return vs benchmark).
Related: [[Backtesting_and_Simulation]]

### 2026-06-03 — Which VaR method for an options-heavy book?
**Q:** Compare parametric, historical, and Monte Carlo VaR, especially with options.
**A:** **Parametric (variance-covariance)** assumes normal returns and uses mean/σ/z — fast but **poor for
options** and fat-tailed/skewed portfolios. **Historical simulation** reprices today's portfolio over
actual past returns and reads the percentile — no distribution assumption and handles options, but
**assumes the past repeats** and is sample-limited. **Monte Carlo** simulates many returns from assumed
distributions — most flexible for complex/optioned portfolios, but **computationally heavy and
model-dependent**. So for non-linear (option) payoffs, prefer historical or Monte Carlo over parametric.
Related: [[Backtesting_and_Simulation]]
