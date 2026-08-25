---
aliases: [Backtesting, Simulation, Monte Carlo, Historical Simulation, Survivorship Bias, Look-Ahead Bias, Data Snooping]
tags: [CFA-L2, pm, concept, backtesting]
date: 2026-08-25
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

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- Commodity futures backtests are highly sensitive to **continuous-contract construction**. The roll rule must be tradable using information known at the time: contract selection, first-notice constraints, delivery risk, liquidity migration, and whether returns include the exact roll slippage.
- Roll yield cannot be treated as a free signal. A strategy that buys backwardation and sells contango must include bid-ask spreads, brokerage, exchange fees, financing/collateral return, margin liquidity, and the market impact of rolling in crowded windows.
- Survivorship bias can appear through missing delisted contracts, discontinued delivery points, changed contract specifications, and excluding markets that became untradeable because of sanctions, capital controls, exchange limits, or liquidity collapse.
- Look-ahead bias often enters through revised inventory data, late-arriving fundamental statistics, final index weights, known future holidays/maintenance outages, or using the eventual most-liquid contract before it was actually the liquid point on the curve.
- Historical simulation is only one realized logistics regime. Stress separately for storage saturation, negative prices, export bans, force majeure, vessel delays, exchange limit moves, clearinghouse margin hikes, and sudden basis dislocations.
- Capacity matters. A backtest may work at small notional but fail once trade size exceeds screen depth, warehouse capacity, freight availability, credit lines, or counterparty appetite.

## Historical Scenario Analysis (39.e)
Evaluate the strategy under a **specific past stress** (e.g., 2008, COVID) to see tail behavior — but it is **one realized path** and may not repeat.

## Simulation Approaches (39.f, 39.g)

| Dimension | Historical simulation | Monte Carlo simulation |
|---|---|---|
| Data | Resamples **actual historical** returns | Draws from **assumed/estimated distributions** |
| Pros | Real co-movements, fat tails, no distribution assumption | Flexible, can model any distribution/correlation, unlimited paths |
| Cons | Limited to what happened (one history) | Model/assumption risk; only as good as inputs |

- Monte Carlo decisions: choose distributions, parameters, correlations, number of trials; can use **bootstrapping** (resample with replacement — especially useful when the number of simulations needed is **large relative to the historical sample**) or a **multivariate** specification. When assets/factors are **correlated**, specify a **multivariate** distribution rather than modeling each series standalone.
- Both approaches are **non-deterministic and random**, and both are used precisely because returns exhibit **skewness, excess kurtosis (fat tails), and tail dependence** — the tendency of assets to become **more correlated in the tails** (they crash together), which a normal/linear correlation model understates.
- Historical simulation shares rolling-window backtesting's core assumption: that **future randomness can be predicted from past return distributions**.

## Sensitivity Analysis (39.h)
Vary key inputs/assumptions to see how robust the conclusions are — it addresses **model risk** and, crucially, is **not restricted to the multivariate normal** that a plain Monte Carlo usually assumes (and which ignores fat tails and negative skew).

**Curriculum procedure**: fit the factor-return data to a distribution that **accounts for skewness and excess kurtosis** — the curriculum uses a **multivariate skewed Student t-distribution** — then **re-run the Monte Carlo** with it and compare against the normal-based run.

**Cost**: a multivariate skewed t needs **more parameters** (degrees of freedom and skewness on top of means, variances, correlations), so it raises **estimation error**. That trade-off — better tail realism vs more parameter risk — is the examinable point.

## Exam Traps
- **Survivorship + look-ahead + data snooping** are the three classic backtest biases.
- **Historical simulation** uses actual past data (one path); **Monte Carlo** draws from assumed distributions (flexible but model-dependent).
- Rolling-window backtests approximate real point-in-time rebalancing.
- **Tail dependence** (assets crashing together) is a main reason to move beyond normal assumptions; **bootstrapping** = resampling **with replacement**, useful when simulations needed far exceed the sample size.
- **Sensitivity analysis** re-runs the Monte Carlo under a **multivariate skewed Student t** to capture skew and fat tails — at the cost of **more parameters and more estimation error**.
- **Cross-validation** (fit on training data, assess on separate test data — including data from **other geographic markets**) is the antidote to **data snooping**.

## Q&A

### 2026-06-03 — The three classic backtesting biases
**Q:** Name and distinguish survivorship, look-ahead, and data-snooping bias.
**A:** **Survivorship bias** — the dataset drops dead/delisted firms, so only winners remain → inflated returns. **Look-ahead bias** — using information **not available at the decision date** (restated financials, reporting lags, point-in-time issues) → unrealistically good results. **Data snooping / overfitting** — testing many strategies and reporting the best; multiple testing makes a lucky result look significant → won't replicate out-of-sample. Mitigate with point-in-time data, holdout/out-of-sample tests, and adjusting for the number of trials.
Related: [[Measuring_Managing_Market_Risk]]

### 2026-06-03 — Historical vs Monte Carlo simulation
**Q:** When would you choose historical simulation over Monte Carlo, and what does each risk?
**A:** **Historical simulation** resamples **actual past returns**, so it preserves real co-movements and fat tails with **no distribution assumption** — but it's limited to the **one history** that occurred. **Monte Carlo** draws from **assumed/estimated distributions**, giving unlimited paths and the freedom to model any distribution/correlation — but it carries **model/assumption risk** (only as good as the inputs). Use sensitivity analysis (e.g., swap normal for a fat-tailed distribution) to test robustness.
Related: [[Measuring_Managing_Market_Risk]]
