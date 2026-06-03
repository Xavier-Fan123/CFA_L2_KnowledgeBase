---
aliases: [Term Structure, Yield Curve Dynamics, Spot and Forward Rates, Swap Spread, Riding the Yield Curve, Term Structure Theories]
tags: [CFA-L2, fi, concept, rates]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 23, LOS 23.a-23.k
---

# Term Structure and Interest Rate Dynamics

## Spot, Forward, Par (23.a, 23.b)
- **Spot rate** `S_T`: YTM on a zero maturing at T. Bonds priced off spot rates are arbitrage-free.
- **Forward rate model**: `(1 + S_T)^T = (1 + S_(T−1))^(T−1) × (1 + f_(T−1,1))`.
  - The forward rate `f` is the **breakeven** reinvestment rate that equates rolling strategies.
- **Bootstrapping**: derive spot rates sequentially from the **par curve** (par bond prices = 100).
- **Forward pricing**: `forward price of a bond = current price / discount factor` to the settlement date.

## Active Management & Riding the Curve (23.c, 23.d)
- If spot rates evolve **as today's forward rates predict**, all bonds earn the one-period risk-free
  return (no excess return). Active managers bet rates will **differ** from the forwards.
- **Riding / rolling down the yield curve**: when the curve is **upward sloping and expected to stay
  stable**, buy longer maturities and earn price appreciation as the bond "rolls down" to lower yields —
  outperforms buy-and-hold at the short end.

## Swap Curve & Spreads (23.e, 23.f, 23.g)
- **Swap rate curve** = par yields for the fixed leg of interest-rate swaps; a key benchmark
  (continuous maturities, reflects bank credit).
- **Swap spread** = swap rate − government (Treasury) yield of equal maturity → gauges credit/liquidity.
- **Short-term spreads**: **TED spread** (interbank rate − T-bill) and **Libor-OIS** spread gauge
  economy-wide **credit & liquidity** risk; wider = more stress.
- **Z-spread**: constant spread over the spot curve; **I-spread**: over the swap curve.

## Term-Structure Theories (23.h)
| Theory | Forward rate / curve implication |
|------|------|
| **Pure (unbiased) expectations** | Forwards = unbiased expectations of future spot; any shape |
| **Local expectations** | Risk-neutral over short horizons; all bonds earn risk-free short-term |
| **Liquidity preference** | Forwards = expected spot + **liquidity (term) premium** (rising with maturity); upward bias |
| **Segmented markets** | Rates set by supply/demand in independent maturity segments |
| **Preferred habitat** | Like segmented, but investors leave their habitat for a sufficient premium |

## Yield-Curve Factors & Risk (23.i, 23.j, 23.k)
- Three empirical movements: **level** (parallel, ~explains most variance), **steepness (slope)**, and
  **curvature**.
- **Key rate (partial) durations** measure sensitivity to a change at a specific maturity; sum ≈
  effective duration. Used to manage non-parallel shifts.
- **Maturity structure of yield volatility**: short-term yields are usually **most volatile** (policy
  driven); volatility affects option/price risk.

## Exam Traps
- If realized spot rates equal today's **forwards**, you earn only the **risk-free** return — active
  bets require deviating from forwards.
- **Riding the yield curve** works on an **upward-sloping, stable** curve.
- Swap spread = swap rate − Treasury; TED & Libor-OIS widen with credit/liquidity stress.
- Liquidity-preference theory adds a **positive term premium** → upward bias in forwards.

## Q&A

### 2026-06-03 — When does "riding the yield curve" beat buy-and-hold?
**Q:** What must be true for rolling down the yield curve to add return, and why?
**A:** The curve must be **upward-sloping and expected to stay stable** over the horizon. You buy a bond
longer than your horizon; as time passes the bond "rolls down" to lower-yield points on the (unchanged)
curve, gaining price as its yield falls → you capture more than the short-rate carry. If rates instead
rise to match today's **forward rates**, every bond earns only the one-period risk-free return and the
strategy's edge disappears. Risk: an actual upward shift/steepening can turn the roll-down into a loss.
Related: [[Arbitrage_Free_Valuation]]

### 2026-06-03 — Liquidity preference vs pure expectations
**Q:** How does the liquidity preference theory change the read on forward rates?
**A:** **Pure (unbiased) expectations**: forward rate = market's unbiased expectation of the future spot,
so an upward curve means rates are expected to rise. **Liquidity preference** adds a **positive term
(liquidity) premium** that rises with maturity, so `forward = expected future spot + term premium` →
forwards are an **upward-biased** estimate of expected spots, and the curve can slope up even if rates
are expected to be flat. Local expectations: risk-neutral only over short horizons (all bonds earn the
risk-free rate short-term).
Related: [[Arbitrage_Free_Valuation]]
