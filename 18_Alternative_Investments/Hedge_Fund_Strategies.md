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
- **Equity market neutral**: low volatility, low correlation, modest returns, leverage to amplify; diversifier with steady profile.
- **Merger arbitrage**: collects the deal spread; payoff like **selling insurance** (small steady gains, occasional large loss if deals break) → **negatively skewed**. Economically = **long a riskless bond (the spread) + short a binary put** that pays out if the deal fails.
- **Convertible arbitrage**: long convertible + short the stock (delta-hedge), long gamma/vega; exposed to **liquidity and credit** shocks; suffers when volatility collapses or credit gaps.
- **Fixed-income arbitrage**: exploit mispricings between related rate instruments; highly **levered**, vulnerable to liquidity/funding stress (carry-trade-like blow-up risk).
- **Global macro / managed futures (CTAs)**: directional/trend-following, can provide **downside protection / crisis alpha**; return profile often **positively skewed** (long volatility/trend).
- **Distressed**: long undervalued distressed debt; illiquid, long horizon, equity-like risk.
- **Specialist** (volatility, reinsurance/ILS): niche premia, low correlation; reinsurance pays a steady premium but takes large catastrophe tail losses (insurance-like, negatively skewed).

**Worked example — merger-arb payoff (official LM4 Example 4):** Acquirer A at $45 offers 1 A for 2 T; T pre-announce $15, post-announce jumps to $19, A falls to $42. Manager buys 20,000 T (cost $380,000) and shorts 10,000 A (proceeds $420,000) → net **deal spread = +$40,000** if it closes. If the deal **breaks**, prices revert: cover A at $45 (−$450,000) and T falls to $15 ($300,000) → total loss **−$110,000** [= (420,000 − 450,000) + (−380,000 + 300,000)]. Hence "long $40k riskless bond + short a binary put paying $110k on failure" → the classic **negative-skew / fat-left-tail** signature.

## Risk Exposures via Factor Models (33.h)
- Use **multi-factor models** to reveal **hidden/nonlinear exposures** (option-like payoffs, hidden beta, illiquidity). Many "alpha" returns are really compensated factor risks.
- **Conditional linear factor model** (official form) adds a **crisis dummy** so betas can differ in stress vs normal times: `R(i,t) = αᵢ + Σₖ βᵢₖ·F(k,t) + Σₖ Dₜ·β*ᵢₖ·F(k,t) + εᵢₜ` where `Dₜ = 1` during financial-crisis periods (e.g., Jun 2007–Feb 2009), else 0; `β*ᵢₖ` is the **incremental** crisis exposure. The six base risk factors (Hasanhodzic & Lo): **equity (S&P 500), interest-rate (bond), currency (USD), commodity (GSCI), credit (Baa−Aaa spread), and volatility (ΔVIX)**.
- Return not explained by factors splits into **(1) alpha** (manager skill), **(2) omitted factors**, and **(3) random error**. Build the model via **stepwise regression** to avoid multicollinearity.

## Adding to a Portfolio (33.i)
- Evaluate the **return/risk and diversification** impact; consider non-normal moments (skew, kurtosis), illiquidity, and how the strategy behaves in stress. A strategy with attractive standalone Sharpe may add little if highly correlated; crisis-alpha strategies add value despite lower standalone returns.

## Exam Traps
- **Merger arbitrage** payoff is **negatively skewed** = **long riskless bond (spread) + short binary put** (pays out if deal breaks); **global macro / managed futures** are often **positively skewed** (crisis alpha, long volatility/trend).
- **Equity market neutral** ≈ low beta/low correlation; long/short equity keeps net (usually net-long) market exposure.
- The **conditional** factor model uses a **crisis dummy** to expose **state-dependent** tail betas hidden in reported "alpha"; residual return = alpha + omitted factors + random error.
- **Fund of funds** adds **diversification but a second layer of fees**; **multi-strategy** reallocates capital internally (one fee layer) but concentrates operational/manager risk.

## Q&A

### 2026-06-03 — Skew: merger arbitrage vs global macro
**Q:** Why is merger arbitrage negatively skewed while global macro / managed futures tend to be positively skewed?
**A:** **Merger arbitrage** collects a small, fixed **deal spread** when deals close (frequent small gains) but suffers a **large loss** when a deal breaks — economically like **selling insurance** → a fat **left tail / negative skew**. **Global macro and managed futures (CTAs)** are directional/trend-following and effectively **long volatility/optionality**, so they tend to win big in dislocations ("**crisis alpha**") and bleed small in calm trends → **positive skew** and valuable downside diversification.
Related: [[Commodities]]

### 2026-06-03 — Equity market neutral vs long/short equity
**Q:** How do these two equity hedge-fund styles differ in market exposure?
**A:** **Equity market neutral** balances longs and shorts to drive **beta ≈ 0** — low volatility, low correlation, modest returns, often **levered** to amplify the small spread; a steady diversifier. **Long/short equity** keeps a **net** (usually net-long) market exposure, so it retains meaningful beta and behaves more like a directional equity bet with hedging. When adding either to a portfolio, weigh non-normal moments (skew/kurtosis), illiquidity, and stress behavior — not just standalone Sharpe.
Related: [[Commodities]]

### 2026-06-04 — Conditional factor model: why the crisis dummy?
**Q:** What does a conditional linear factor model add over a plain multi-factor regression of hedge fund returns, and what goes in the residual?
**A:** It adds a **crisis dummy** $D_t$ (1 in stress periods, e.g., Jun 2007–Feb 2009) interacted with each factor, so the model estimates **two betas per factor** — a normal-times $\beta_{i,k}$ and an **incremental crisis** $\beta^{*}_{i,k}$: $R_{i,t}=\alpha_i+\sum_k\beta_{i,k}F_{k,t}+\sum_k D_t\beta^{*}_{i,k}F_{k,t}+\varepsilon$. This exposes **state-dependent / nonlinear tail risk** that a single-beta model hides (many strategies pick up large hidden betas only in crises). The six base factors are equity (S&P 500), rates (bond), currency (USD), commodity (GSCI), credit (Baa−Aaa), and volatility (ΔVIX). The unexplained part = **alpha (skill) + omitted factors + random error**; stepwise regression limits multicollinearity.
Related: [[Commodities]]
