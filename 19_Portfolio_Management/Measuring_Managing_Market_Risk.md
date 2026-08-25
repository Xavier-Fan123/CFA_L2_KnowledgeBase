---
aliases: [Measuring and Managing Market Risk, Value at Risk, VaR, Expected Shortfall, Sensitivity Risk, Scenario Risk, Risk Budgeting]
tags: [CFA-L2, pm, concept, risk]
date: 2026-08-25
status: evergreen
source: Schweser Book 5, Module 38, LOS 38.a-38.l
---

# Measuring and Managing Market Risk

## Value at Risk (38.a)
- **VaR** = the **minimum loss** expected over a given period at a given confidence level (e.g., "5% 1-day VaR = $1m" → at least $1m loss is expected 5% of the time / on ~1 in 20 days).
- Three elements: a **loss amount**, a **time period**, and a **probability**.
- **Worked example (Schweser):** "There is a 5% probability of a loss of **$25,000 or more** in any given month" = a **monthly 5% VaR of $25,000**. Equivalently: "5% of the time, the **minimum** monthly loss is $25,000." The $25,000 is a **minimum** (not maximum) loss at that confidence.

## Estimation Methods (38.b, 38.c)

- **Parametric (variance-covariance)**: assume normal returns; VaR from mean, σ, and z-score.
  - Pros / cons: simple, fast; **poor for options/non-normal** (fat tails, skew).
- **Historical simulation**: reprice the current portfolio over actual past returns; read the percentile.
  - Pros / cons: no distribution assumption, handles options; but **assumes the past repeats** and is limited by sample.
- **Monte Carlo simulation**: simulate many returns from assumed distributions.
  - Pros / cons: flexible, handles complex portfolios; **computationally heavy**, model-dependent.

**VaR z-thresholds (normal):** 5% VaR = **1.65σ** below the mean; 1% VaR = **2.33σ** below; 16% VaR = **1σ** below (one-standard-deviation move). All three start by **risk decomposition** — mapping holdings to risk factors. Parametric & Monte Carlo only need parameter *estimates* (no formal data history required); historical simulation *requires* the actual return history.

### Worked example — Parametric (variance-covariance) VaR (38.c)
Official V9, Module 5. Portfolio = **$150,000,000**, 80% SPY (equity) + 20% SPLB (corp bond).
**Annual inputs (judgment-adjusted):** E(R_SPY)=10.5%, σ_SPY=20%; E(R_SPLB)=6%, σ_SPLB=8.5%; ρ = −0.06.

1. **Portfolio expected return:** `E(R_P) = 0.8(0.105) + 0.2(0.06) = 0.0960` (9.6%).
2. **Portfolio volatility:** `σ_P = √[(0.8)²(0.20)² + (0.2)²(0.085)² + 2(0.8)(0.2)(−0.06)(0.20)(0.085)] = 0.15988` (≈16.0%).
3. **Convert to daily** (250 trading days; divide return by 250, σ by √250): `E(R_P)_daily = 0.096/250 = 0.000384`; `σ_daily = 0.15988/√250 = 0.010112`.
4. **5% daily VaR** = `[E(R_P)_daily − 1.65·σ_daily]·(−1)·$150m`:
   - Step 1: `0.010112 × 1.65 = 0.016685`
   - Step 2: `0.000384 − 0.016685 = −0.016301`
   - Step 3: flip sign → `0.016301`
   - Step 4: `0.016301 × $150,000,000 = $2,445,150`.

   **→ Daily 5% VaR ≈ $2,445,150** ("on 5% of days, loss is at least $2.44m").
- **1% daily VaR:** use 2.33σ → `(0.000384 − 2.33·0.010112)·(−1)·$150m = $3,476,550`.
- **Annual 5% VaR:** annualize first (E=0.096, σ=0.15988): `(0.096 − 1.65·0.15988)·(−1)·$150m ≈ $25.17m`. **TRAP:** you **cannot** annualize a daily VaR by ×250 or ×√250 — you must re-annualize the mean and σ *then* compute VaR. (Multiplying daily VaR by √250 only works if the expected return is assumed zero.)

### Worked example — Historical simulation VaR (same portfolio)
Reprice the 80/20 portfolio over each day's *actual* SPY/SPLB returns (e.g., Day 1 = 0.8(0.80%) + 0.2(−0.53%)), sort the resulting daily portfolio returns, and read the percentile. Official results (Excel `=percentile`): 1% VaR = **$2,643,196**; 5% VaR = **$1,622,272**; 16% VaR = **$880,221**. These differ from parametric mainly because historical simulation uses the data's own (lower-volatility) distribution and makes **no normality assumption** — the actual SPY sample had abnormally low volatility vs the 20% long-run input used above.

## Advantages & Limitations (38.d)
- **+**: single, comparable number; widely used; aggregates across positions.
- **−**: says nothing about the **size of losses beyond VaR**; sensitive to assumptions/look-back; can understate tail risk; not subadditive in general (historical/parametric).

## Extensions (38.e)
- **Conditional VaR (CVaR) / expected shortfall**: average loss **given** that loss exceeds VaR (tail).
- **Incremental VaR**: change in VaR from adding/removing a position. **Marginal VaR**: sensitivity to a small change. **Relative (ex-ante tracking) VaR**: VaR of active return vs benchmark.

## Sensitivity & Scenario Measures (38.f-38.i)
- **Sensitivity**: equity **beta**; fixed-income **duration & convexity**; option **Greeks (delta, gamma, vega)**. Measure exposure to a single risk factor, but **not probability** of loss.
- **Scenario risk**: **historical** scenarios (replay a past crisis) and **hypothetical/stress** tests (extreme but plausible). Capture non-normal, multi-factor stress that VaR may miss.
- **Stress test** = sensitivity or scenario analysis run with **extreme** input changes, usually to test the effect on **equity or solvency**.
- **Reverse stress test (38.h)** runs the logic **backwards**: instead of asking what scenario X would cost, it starts from **business failure** and identifies the **scenarios that would produce it**. Use it to surface vulnerabilities nobody thought to put on the scenario list.
- Limits of both: scenario and sensitivity measures give **no probability** (and sensitivity measures give no size of the factor move); a **historical scenario need not repeat**, and a **hypothetical scenario can be misspecified**.

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- A commodity trading book should be mapped to more than one price factor: outright futures, calendar spreads, location/grade basis, FX, freight, volatility, interest rates, and counterparty exposure. A single flat-price VaR can miss the risk that actually drives P&L.
- Parametric VaR is weak for commodity books with options, spread positions, illiquid tenors, or physical optionality. Return distributions can be skewed, fat-tailed, and jumpy because inventories, weather, outages, policy actions, and delivery constraints are discontinuous.
- Stress tests should include curve dislocations, basis blowouts, exchange limit moves, sudden margin calls, loss of credit lines, and liquidity evaporation in deferred contracts. These scenarios often matter more than the percentile loss from a calm historical window.
- Risk limits should distinguish **economic hedge effectiveness** from **cash liquidity**. A hedge can reduce final price exposure while creating interim collateral needs that exceed available working capital.

## Constraints & Users (38.j, 38.k, 38.l)
- **Constraints**: **risk budgeting** (allocate a total risk limit across units), **position limits**, **scenario limits**, **stop-loss limits**.
- Different users emphasize different measures: **banks** (regulatory VaR, liquidity, leverage), **asset managers** (active risk / relative VaR), **pensions** (surplus-at-risk, liability-relative), **insurers** (economic capital, scenario/stress).

## Exam Traps
- VaR is a **minimum** loss at a confidence level, not the maximum; it ignores **how bad** the tail is — use **CVaR/expected shortfall** for that.
- **Parametric VaR is poor for option-heavy portfolios** (non-normal); historical/Monte Carlo handle them.
- Sensitivity measures give **exposure**, not loss probability; scenario analysis covers tail/multi-factor stress.
- **Reverse stress test = start from failure and work back to the scenarios that cause it** — the opposite direction from an ordinary stress test.
- z-thresholds: **5% → 1.65σ, 1% → 2.33σ, 16% → 1σ**. Higher confidence (1% vs 5%) → larger z → larger VaR.
- **Never annualize a daily VaR** by ×250 or ×√250. Re-annualize mean (×250) and σ (×√250) *first*, then compute VaR. The √250 shortcut is valid only under a zero-expected-return assumption.
- Parametric needs only mean + σ (+ correlations); it does **not** require a data history (historical sim does).

## Q&A

### 2026-06-03 — What exactly does "5% VaR = $25,000/month" mean?
**Q:** State the correct interpretation and what VaR fails to tell you.
**A:** It means there is a **5% probability of losing $25,000 or more** in a month — i.e., 5% of the time the loss is **at least** $25,000. VaR is a **minimum** loss at that confidence, **not** a maximum, and it says **nothing about how large** the loss is once you're in the tail. For the average loss beyond VaR, use **conditional VaR / expected shortfall**. Other extensions: incremental VaR (Δ from adding a position), marginal VaR (sensitivity), relative/ex-ante tracking VaR (active return vs benchmark).
Related: [[Backtesting_and_Simulation]]

### 2026-06-03 — Which VaR method for an options-heavy book?
**Q:** Compare parametric, historical, and Monte Carlo VaR, especially with options.
**A:** **Parametric (variance-covariance)** assumes normal returns and uses mean/σ/z — fast but **poor for options** and fat-tailed/skewed portfolios. **Historical simulation** reprices today's portfolio over actual past returns and reads the percentile — no distribution assumption and handles options, but **assumes the past repeats** and is sample-limited. **Monte Carlo** simulates many returns from assumed distributions — most flexible for complex/optioned portfolios, but **computationally heavy and model-dependent**. So for non-linear (option) payoffs, prefer historical or Monte Carlo over parametric.
Related: [[Backtesting_and_Simulation]]

### 2026-06-04 — Compute parametric VaR for a two-asset portfolio (worked)
**Q:** $150m portfolio, 80% equity (E=10.5%, σ=20%) / 20% bond (E=6%, σ=8.5%), ρ=−0.06. Find the daily 5% VaR.
**A:** (1) `E(R_P)=0.8(0.105)+0.2(0.06)=9.6%`. (2) `σ_P=√[0.8²·0.2²+0.2²·0.085²+2·0.8·0.2·(−0.06)·0.2·0.085] =15.99%`. (3) Daily: E=0.096/250=0.0384%, σ=0.1599/√250=1.0112%. (4) 5% VaR = `(0.000384 − 1.65·0.010112)· (−1)·$150m = $2,445,150` — on 5% of days the loss is **at least** $2.44m. For 1% VaR swap 1.65→**2.33** (→$3.48m). To get the **annual** VaR, re-annualize E and σ first (`0.096 − 1.65·0.15988`)·$150m ≈ **$25.2m** — do **not** scale the daily VaR by √250.
Related: [[Backtesting_and_Simulation]]
