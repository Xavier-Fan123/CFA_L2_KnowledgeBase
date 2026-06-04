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
- **Swap rate curve** = par yields for the fixed leg of fixed-for-floating interest-rate swaps; floating
  leg now references a **market reference rate (MRR)** (transaction-based, e.g. **SOFR**; historically
  Libor). A key benchmark: many maturities, led by major banks (so comparable across countries), and the
  fixed rate is analogous to a government-bond YTM derived by bootstrapping.
- **Swap spread** = swap rate − government (Treasury) yield of equal maturity → gauges credit/liquidity.
  *By convention uses the on-the-run government bond.* Post-2008, swap spreads have narrowed to **zero or
  negative** (higher dealer capital requirements / leverage constraints) — a common trap.
- **Short-term spreads** (economy-wide credit & liquidity gauges; wider = more stress):
  - **TED spread** = MRR (Eurodollar-based) − T-bill of equal maturity.
  - **MRR−OIS spread** (formerly **Libor−OIS**) = MRR − overnight-indexed-swap (OIS) rate; the OIS floating
    leg ≈ geometric average of a daily overnight rate (e.g. fed funds / SOFR).
- **Z-spread**: constant spread added to the **default-free spot curve** to price a risky bond (best for
  pricing a corporate bond given the Treasury spot curve). **I-spread (ISPRD)**: bond YTM − the
  straight-line **interpolated swap rate** of the same maturity (a spread over the **swap** curve).

## Term-Structure Theories (23.h)
| Theory | Forward rate / curve implication |
|------|------|
| **Pure (unbiased) expectations** | Forwards = unbiased expectations of future spot; any shape |
| **Local expectations** | Risk-neutral over short horizons; all bonds earn risk-free short-term |
| **Liquidity preference** | Forwards = expected spot + **liquidity (term) premium** (rising with maturity); upward bias |
| **Segmented markets** | Rates set by supply/demand in independent maturity segments |
| **Preferred habitat** | Like segmented, but investors leave their habitat for a sufficient premium |

## Yield-Curve Factors & Risk (23.i, 23.j)
- Three empirical movements: **level** (parallel, ~explains most variance), **steepness (slope)**, and
  **curvature**.
- **Key rate (partial) durations** measure sensitivity to a change at a specific maturity; **sum ≈
  effective duration**. Used to measure/manage **shaping risk** (non-parallel shifts). Worked logic
  (curriculum Ex.): for a portfolio of zeros, KeyDur_t = 1/[(price)(Δy)]; e.g. 1y/5y/10y key rate
  durations 0.3333 / 1.6667 / 3.3333 sum to 5.333 = effective duration.
- **Maturity structure of yield volatility**: short-term yields are usually **most volatile** (driven by
  **monetary-policy** uncertainty); long-term yield volatility is driven mainly by **real-economy and
  inflation** uncertainty. Volatility affects option/price risk.

## Developing Interest Rate Views from Macro Factors (23.k)
- **Bond risk premium** = expected **excess return** of a default-free long-term bond over an equivalent
  short-term bond (a.k.a. **term / duration premium**); forward-looking, must be **estimated** (not an
  ex-post historical return). Credit/liquidity risks raise the *total* risk premium of a specific bond.
- **What drives yields** (curriculum research): inflation, GDP growth, and monetary policy explain most
  yield variance. **Monetary policy ≈ 2/3 of short/intermediate-rate variation**; **inflation ≈ 2/3 of
  long-term yield variation.**
- **Policy → curve-shape map** (memorize — common item-set trap):

| Scenario | Driver | Curve move |
|------|------|------|
| **Bear flattening** | Expansion → central bank **raises** benchmark rates to curb inflation | Short rates rise **more** than long → curve **flattens** |
| **Bull steepening** | Recession → central bank **cuts** rates to stimulate | Short rates fall **more** than long → curve **steepens** |
| **Bull flattening** | **Flight to quality** (risk-off; buy govvies) | Long rates fall **more** than short → curve **flattens** |
| (Bear steepening) | Long rates rise more than short (e.g. inflation/supply fears) | Curve **steepens** |

  - "Bull" = rates falling (prices rising); "Bear" = rates rising. Short-rate moves are **procyclical**.
- **Other supply/demand drivers**: fiscal deficits (more issuance → higher yields); **maturity structure
  of debt** (more long issuance → higher term premium — a segmented-market effect); **QE / large-scale
  asset purchases** (raise demand in targeted segments, push down the risk premium); domestic
  (pension/insurer liability-matching) and non-domestic (reserves/FX) demand.
- **Positioning on a rate view** (often via **bond futures** to limit turnover; evaluate any view vs the
  **current forward curve**, which already embeds roll-down returns):
  - Expect rates to **fall** → **extend** duration; expect rates to **rise** → **shorten** duration.
  - Expect **steepening** (long rises vs short) → **short long-term**, **buy short-term** bonds.
  - Expect **flattening** (short rises vs long) → **buy long-term**, **short short-term** bonds.
  - Curve trades can be made **duration-neutral** to isolate slope from the level move. Long-only managers
    swap between a **bullet** (single-maturity) and a **barbell** (short+long, same duration) — e.g. shift
    bullet → barbell to play an expected **bullish flattening**.

## Exam Traps
- If realized spot rates equal today's **forwards**, you earn only the **risk-free** return — active
  bets require deviating from forwards.
- **Riding the yield curve** works on an **upward-sloping, stable** curve.
- Swap spread = swap rate − Treasury (can be **negative** post-2008); TED & **MRR−OIS** (formerly
  Libor−OIS) widen with credit/liquidity stress. Z-spread = over **spot** curve; I-spread = over **swap** curve.
- Liquidity-preference theory adds a **positive term premium** → upward bias in forwards.
- **Bull/bear + steepen/flatten:** "bull" = rates **down**; bear = rates **up**. Expansion + rate hikes →
  **bear flattening**; recession + cuts → **bull steepening**; flight to quality → **bull flattening**.
- Sum of **key rate durations = effective duration** (a parallel shift moves all key rates equally).
- Steepener trade = **short long / buy short**; flattener = **buy long / short short** (often
  duration-neutral). Bullet→barbell positions for an expected **bullish flattening**.

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

### 2026-06-04 — Bear flattening vs bull steepening vs bull flattening (23.k)
**Q:** During an economic expansion the central bank raises benchmark rates. What yield-curve move is
this, and how would you position? Contrast with a recession and with a flight to quality.
**A:** Hikes in an expansion produce **bear flattening** — short rates rise **more** than long rates, so
the curve flattens ("bear" = rates rising). A **recession + rate cuts** gives **bull steepening** (short
rates fall more than long). A **flight to quality** (risk-off buying of government bonds) gives **bull
flattening** (long rates fall more than short). Memory: short-rate moves are **procyclical**; monetary
policy drives ~2/3 of short-rate variance, inflation ~2/3 of long-rate variance. Positioning: to play a
**flattener** you **buy long-term and short short-term** bonds (often **duration-neutral** to strip out
the level move); to play a **steepener**, **short long / buy short**. Long-only managers express a
bullish-flattening view by shifting from a **bullet** to a **barbell**.
Related: [[Bonds_With_Embedded_Options]]
