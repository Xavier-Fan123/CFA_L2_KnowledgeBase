---
aliases: [Hedge Fund Strategies, Long-Short Equity, Merger Arbitrage, Global Macro, Relative Value, Fund of Funds]
tags: [CFA-L2, alt, concept, hedge-funds]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 33, LOS 33.a-33.i
---

# Hedge Fund Strategies

## Classification (33.a)
Grouped by approach; each differs in directionality, leverage, liquidity, and tail risk.

| Category | Strategies | Characteristics |
|------|------|------|
| **Equity** | Long/short equity, **equity market neutral**, dedicated short bias | Market-neutral has low beta; L/S retains net exposure |
| **Event-driven** | **Merger (risk) arbitrage**, distressed, special situations, activist | Idiosyncratic, deal/event risk; merger arb = short, fat left tail |
| **Relative value** | **Convertible arbitrage**, fixed-income arb, volatility arb | Exploits pricing differentials; levered, sensitive to liquidity/credit stress |
| **Opportunistic** | **Global macro**, managed futures (CTAs) | Top-down, trend-following; positive in crises (crisis alpha), trades many markets |
| **Specialist** | Volatility, reinsurance/ILS | Niche risk premia, low correlation |
| **Multi-manager** | **Fund of funds**, multi-strategy | Diversification; FoF adds a second fee layer; multi-strat reallocates capital internally |

## Investment Characteristics & Role (33.b-33.g)
- **Equity market neutral**: low volatility, low correlation, modest returns, leverage to amplify;
  diversifier with steady profile.
- **Merger arbitrage**: collects the deal spread; payoff like **selling insurance** (small steady gains,
  occasional large loss if deals break) → **negatively skewed**.
- **Convertible arbitrage**: long convertible + short the stock; exposed to liquidity and credit shocks.
- **Global macro / managed futures**: directional, can provide **downside protection / crisis alpha**;
  return profile often **positively skewed** (long volatility/trend).
- **Distressed**: long undervalued distressed debt; illiquid, long horizon, equity-like risk.

## Risk Exposures via Factor Models (33.h)
- Use **multi-factor models** (e.g., conditional factor models) to reveal **hidden/nonlinear exposures**
  (option-like payoffs, hidden beta, illiquidity). Many "alpha" returns are really compensated factor
  risks. **Conditional** models capture exposures that change in up vs down markets.

## Adding to a Portfolio (33.i)
- Evaluate the **return/risk and diversification** impact; consider non-normal moments (skew, kurtosis),
  illiquidity, and how the strategy behaves in stress. A strategy with attractive standalone Sharpe may
  add little if highly correlated; crisis-alpha strategies add value despite lower standalone returns.

## Exam Traps
- **Merger arbitrage** payoff is **negatively skewed** (like selling insurance); **global macro / managed
  futures** are often **positively skewed** (crisis alpha).
- **Equity market neutral** ≈ low beta/low correlation; long/short equity keeps net market exposure.
- Conditional factor models expose **nonlinear / state-dependent** risk hidden in reported "alpha".
- Fund of funds adds **diversification but a second layer of fees**.

## Q&A

### 2026-06-03 — Skew: merger arbitrage vs global macro
**Q:** Why is merger arbitrage negatively skewed while global macro / managed futures tend to be positively skewed?
**A:** **Merger arbitrage** collects a small, fixed **deal spread** when deals close (frequent small
gains) but suffers a **large loss** when a deal breaks — economically like **selling insurance** → a fat
**left tail / negative skew**. **Global macro and managed futures (CTAs)** are directional/trend-following
and effectively **long volatility/optionality**, so they tend to win big in dislocations ("**crisis
alpha**") and bleed small in calm trends → **positive skew** and valuable downside diversification.
Related: [[Commodities]]

### 2026-06-03 — Equity market neutral vs long/short equity
**Q:** How do these two equity hedge-fund styles differ in market exposure?
**A:** **Equity market neutral** balances longs and shorts to drive **beta ≈ 0** — low volatility, low
correlation, modest returns, often **levered** to amplify the small spread; a steady diversifier.
**Long/short equity** keeps a **net** (usually net-long) market exposure, so it retains meaningful beta
and behaves more like a directional equity bet with hedging. When adding either to a portfolio, weigh
non-normal moments (skew/kurtosis), illiquidity, and stress behavior — not just standalone Sharpe.
Related: [[Commodities]]
