---
aliases: [Backtesting, Simulation, Monte Carlo, Historical Simulation, Survivorship Bias, Look-Ahead Bias, Data Snooping]
tags: [CFA-L2, pm, concept, backtesting]
date: 2026-06-03
status: evergreen
source: Schweser Book 5, Module 39, LOS 39.a-39.h
---

# Backtesting and Simulation

## Objectives & Steps (39.a, 39.b)
- **Backtesting** assesses how a strategy **would have performed** historically — to gauge risk/return before committing capital.
- Steps: (1) **specify** strategy/hypothesis and investment universe; (2) form portfolios (often **long-short factor** quantile portfolios, e.g., top minus bottom decile); (3) **rebalance on a rolling window** and track returns; (4) compute performance/risk metrics.
- Uses a **rolling-window** procedure to mimic real, point-in-time rebalancing.

## Metrics & Visuals (39.c)
Report risk-adjusted returns (Sharpe, IR), drawdowns, turnover, hit rate; visuals: cumulative return curves, rolling performance, return distributions, factor-exposure plots.

## Problems in Backtesting (39.d)
- **Survivorship bias**: excluding dead/delisted firms inflates results.
- **Look-ahead bias**: using data not actually available at the decision time (e.g., restated financials, reporting lags).
- **Data snooping / overfitting**: testing many strategies and reporting the best → spurious; multiple-testing inflates apparent significance.
- **Transaction-cost / liquidity** neglect; **regime dependence** (one historical path).

## Historical Scenario Analysis (39.e)
Evaluate the strategy under a **specific past stress** (e.g., 2008, COVID) to see tail behavior — but it is **one realized path** and may not repeat.

## Simulation Approaches (39.f, 39.g)

| Dimension | Historical simulation | Monte Carlo simulation |
|---|---|---|
| Data | Resamples **actual historical** returns | Draws from **assumed/estimated distributions** |
| Pros | Real co-movements, fat tails, no distribution assumption | Flexible, can model any distribution/correlation, unlimited paths |
| Cons | Limited to what happened (one history) | Model/assumption risk; only as good as inputs |

- Monte Carlo decisions: choose distributions, parameters, correlations, number of trials; can use **bootstrapping** (resample with replacement) or a **multivariate** specification.

## Sensitivity Analysis (39.h)
Vary key inputs/assumptions (e.g., use a fat-tailed distribution instead of normal) to see how robust the conclusions are — addresses model risk.

## Exam Traps
- **Survivorship + look-ahead + data snooping** are the three classic backtest biases.
- **Historical simulation** uses actual past data (one path); **Monte Carlo** draws from assumed distributions (flexible but model-dependent).
- Rolling-window backtests approximate real point-in-time rebalancing.

## Q&A

### 2026-06-03 — The three classic backtesting biases
**Q:** Name and distinguish survivorship, look-ahead, and data-snooping bias.
**A:** **Survivorship bias** — the dataset drops dead/delisted firms, so only winners remain → inflated returns. **Look-ahead bias** — using information **not available at the decision date** (restated financials, reporting lags, point-in-time issues) → unrealistically good results. **Data snooping / overfitting** — testing many strategies and reporting the best; multiple testing makes a lucky result look significant → won't replicate out-of-sample. Mitigate with point-in-time data, holdout/out-of-sample tests, and adjusting for the number of trials.
Related: [[Measuring_Managing_Market_Risk]]

### 2026-06-03 — Historical vs Monte Carlo simulation
**Q:** When would you choose historical simulation over Monte Carlo, and what does each risk?
**A:** **Historical simulation** resamples **actual past returns**, so it preserves real co-movements and fat tails with **no distribution assumption** — but it's limited to the **one history** that occurred. **Monte Carlo** draws from **assumed/estimated distributions**, giving unlimited paths and the freedom to model any distribution/correlation — but it carries **model/assumption risk** (only as good as the inputs). Use sensitivity analysis (e.g., swap normal for a fat-tailed distribution) to test robustness.
Related: [[Measuring_Managing_Market_Risk]]
