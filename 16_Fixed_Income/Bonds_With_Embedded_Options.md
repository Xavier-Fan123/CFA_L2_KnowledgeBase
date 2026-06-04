---
aliases: [Bonds with Embedded Options, Callable Bond, Putable Bond, OAS, Option-Adjusted Spread, Effective Duration, Convertible Bond]
tags: [CFA-L2, fi, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 25, LOS 25.a-25.q
---

# Valuation and Analysis of Bonds with Embedded Options

## Option Decomposition (25.b)
- **Callable**: `V_callable = V_straight − V_call option` (issuer holds the call → hurts the holder).
- **Putable**: `V_putable = V_straight + V_put option` (holder holds the put → benefits the holder).

## Valuation in the Tree (25.c, 25.f, 25.m)
- Use the calibrated binomial tree (→ [[Arbitrage_Free_Valuation]]) with backward induction, applying
  the option rule at each node:
  - **Callable**: value = `min(computed value, call price)` (issuer calls when it's cheap to refinance).
  - **Putable**: value = `max(computed value, put price)` (holder puts when the bond is worth less).
- **Capped floater**: `value = straight floater − value of the embedded cap` (cap benefits issuer);
  **floored floater**: `value = straight floater + value of the floor` (floor benefits holder).

## Effect of Volatility & Curve (25.d, 25.e, 25.h)
- Higher interest-rate **volatility → higher option value** → **lower** callable price, **higher**
  putable price.
- Curve shape: a callable's call option is more valuable when rates **fall** / the curve is low and flat;
  a putable's put is more valuable when rates **rise**.

## Option-Adjusted Spread (OAS) (25.g, 25.h)
- **OAS** = the constant spread added to all tree rates that makes the model price = market price, after
  **removing the option** → comparable across bonds with different optionality.
- **Higher assumed volatility → lower OAS** (more value attributed to the option, less to spread).
- A bond is **cheap** if its OAS > the OAS of comparable bonds.
- **Worked example (Schweser):** 3-yr 6% callable, market price $99.95; value on the benchmark
  (20% vol) tree = $101.77. Adding a constant **OAS of 100 bps** to every tree rate forces the model
  value down to $99.95. The OAS is added **after** applying the call/put node rule (option removed).

## Duration & Convexity (25.i-25.l)
- **Effective duration** captures sensitivity to parallel curve shifts allowing cash flows to change:
  `ED = (V− − V+) / (2 × V0 × Δy)`.
- **Callable ≤ straight** and **putable ≤ straight** effective duration; the embedded option **shortens**
  expected life as rates approach the exercise region.
- **Effective convexity**: callable bonds can have **negative** convexity (price compression near the
  call); putable bonds have **positive** convexity.
- **One-sided durations** (up vs down) better capture the **asymmetric** sensitivity when the option is
  **near the money**: for a **callable**, one-sided **up**-duration > **down**-duration (price capped on
  the way down as it nears the call price → less sensitive to rate falls). For a **putable**,
  **down**-duration > **up**-duration (put floors the price on the way up). **Key-rate durations** isolate
  sensitivity to specific maturity shifts (shaping risk).

## Convertible Bonds (25.n-25.q)
**Defining features**: bondholder's right to convert debt into a fixed number of shares during the
conversion period at a preset **conversion price**; **conversion ratio** = par / conversion price.
Ratio/price are adjusted for stock splits, bonus issues, and above-**threshold** dividends. If also
**callable**, the issuer can force conversion (**forced conversion**) by calling once the share price is
well above the conversion price, capping the bondholder's redemption value below the conversion value.

**Value components & measures** (all per the curriculum):
- **Conversion (parity) value** = underlying share price × conversion ratio.
- **Minimum (floor) value** = **max(conversion value, straight-bond value)** — else arbitrage (buy the
  cheap convertible; convert & sell shares, or capture the higher yield).
- **Market conversion price** = convertible price / conversion ratio (the effective break-even price paid
  per share by buying the bond and converting).
- **Market conversion premium per share** = market conversion price − share price.
- **Market conversion premium ratio** = (market conversion premium per share) / share price. The premium
  behaves like a **call-option price**: it caps downside at the (fluctuating) straight value — but unlike a
  true option the floor is **not fixed** (it moves with rates and credit spreads).
- **Premium over straight value** = (convertible price / straight value) − 1. Higher premium → **less
  attractive** convertible; it is a **flawed** downside measure because the straight value is not fixed.
- **Components of convertible value** ≈ straight bond value + **call option on the stock**; for a
  **callable convertible**, subtract the issuer's call option on the bond (≈ straight + stock call −
  issuer call). A **putable convertible** adds the put.

**Risk-return spectrum (25.q)** — depends on where the share price sits vs the conversion price:

| Region | Share price vs conversion price | Behaves like | Key drivers |
|------|------|------|------|
| **Busted convertible** | Share **well below** | **Bond** (out-of-money call) | rates, credit spread; floor → PV of recovery as S→0 |
| **Hybrid / mixed** | Share **near** conversion price | Both bond & stock | option time value largest here |
| **Equity-like** | Share **well above** | **Stock** (in-the-money call; tracks parity) | share price; rates matter little |

- **Worked example (Schweser – BSC):** 7% convertible, price $985, conversion ratio 25, straight value
  $950, stock $35.
  - Conversion value = `25 × $35 = $875`; **minimum value = max($875, $950) = $950**.
  - Market conversion price = `$985 / 25 = $39.40`; **market conversion premium/share = $39.40 − $35 = $4.40**;
    **premium ratio = $4.40 / $35 = 12.6%**; **premium over straight value = $985/$950 − 1 = 3.7%**.

## Exam Traps
- Higher vol → **lower** callable, **higher** putable, and **lower OAS**.
- Apply **min(value, call price)** for calls, **max(value, put price)** for puts at each node.
- Callable convexity can be **negative**; OAS removes the option to allow apples-to-apples comparison.
- Convertible minimum value = **max(conversion value, straight value)**.
- **Busted convertible** = share price **well below** conversion price → trades like a **bond** (driven by
  rates/credit, not the share). Deep ITM → trades like the **stock**; near the conversion price → hybrid.
- Callable: one-sided **up**-duration > down-duration; putable: **down** > up. Higher vol still →
  callable down / putable up / **OAS down**.

## Q&A

### 2026-06-03 — How does higher rate volatility move callable, putable, and OAS?
**Q:** Interest-rate volatility rises. What happens to a callable price, a putable price, and OAS?
**A:** Higher vol raises the value of **both** embedded options. Callable = straight − call option, so a
more valuable call → **lower callable price**. Putable = straight + put option, so → **higher putable
price**. For a given market price, attributing more value to the option leaves **less** for the spread →
**lower OAS** with higher assumed vol. Compare bonds on OAS (option removed): higher OAS = cheaper.
Related: [[Arbitrage_Free_Valuation]]

### 2026-06-03 — Why can a callable bond have negative convexity?
**Q:** Explain the duration/convexity behavior of a callable bond as rates fall.
**A:** As rates fall, a normal bond's price rises at an increasing rate (positive convexity). But the
issuer's **call caps the upside** near the call price — the price compresses as it approaches the strike,
so the price-yield curve bends the "wrong" way → **negative convexity** in that region. Effective
duration `ED = (V− − V+)/(2·V0·Δy)` is **shorter** than the straight bond's because the expected life
shortens as the call moves in-the-money. Putables stay **positively convex** (the put supports the price
floor as rates rise).
Related: [[Term_Structure]]

### 2026-06-04 — Convertible value measures and the risk-return spectrum (25.n-25.q)
**Q:** A 7% convertible trades at $985 (conversion ratio 25, straight value $950, stock $35). Give
conversion value, minimum value, market conversion price/premium, premium ratio, and premium over
straight value. When does the bond act like stock vs like a bond?
**A:** Conversion (parity) value = `25 × $35 = $875`. **Minimum value = max($875, $950) = $950** (the
straight value is the floor here). Market conversion price = `$985/25 = $39.40`; market conversion premium
per share = `$39.40 − $35 = $4.40`; **premium ratio = $4.40/$35 = 12.6%**; **premium over straight value =
$985/$950 − 1 = 3.7%**. Behavior: when the share is **well above** the conversion price the convertible is
**equity-like** (tracks parity, rates barely matter); **well below** it is a **busted convertible** acting
**bond-like** (driven by rates/credit, floor → PV of recovery as S→0); **near** the conversion price it is
a **hybrid** with the largest option time value. The market conversion premium resembles a call premium
but the floor (straight value) is **not fixed** — it moves with rates/spreads, so "premium over straight
value" is a flawed downside gauge.
Related: [[Credit_Analysis_Models]]
