---
aliases: [Options Valuation, Binomial Option Model, Black-Scholes-Merton, BSM, Black Model, Option Greeks, Delta Hedging, Implied Volatility]
tags: [CFA-L2, deriv, concept, options]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 29, LOS 29.a-29.n
---

# Valuation of Contingent Claims (Options)

## Binomial Option Model (29.a, 29.b, 29.d)
- Underlying moves up by factor `u` or down by `d` each period. **Risk-neutral probability of up**:
  `π_U = (1 + r − d) / (u − d)`, `π_D = 1 − π_U`.
- **Option value = PV of expected payoff under risk-neutral probabilities**:
  `c = [π_U × c_up + π_D × c_down] / (1 + r)`.
- **Worked example (Schweser):** rf = 7%, S0 = $30, u = 1.333, d = 0.75 →
  `π_U = (1.07 − 0.75)/(1.333 − 0.75) = 0.32/0.583 = 0.549`. Then value = PV of the 0.549/0.451
  probability-weighted payoffs, discounted at 7%.
- **Two-period**: roll backward through the tree. For **American** options, check **early exercise** at
  each node (value = max(exercise, hold)).

## No-Arbitrage / Hedge Ratio (29.c)
- Replicate the option with a position in the underlying and risk-free borrowing/lending.
- **Hedge ratio (delta)** for one period: `h = (c_up − c_down) / (S_up − S_down)`. If the option is
  mispriced vs the replicating portfolio → arbitrage.

## Interest-Rate Options (29.e)
- Value caplets/floorlets on a binomial interest-rate tree; payoff at each node depends on the rate
  there; discount back with backward induction (no single risk-neutral 0.5 — use the tree's structure).

## Black-Scholes-Merton (29.f, 29.g, 29.h)
- **Assumptions**: underlying follows **lognormal** diffusion (continuous), constant volatility and
  risk-free rate, frictionless markets, no cash flows (base case), European exercise.
- **Call** = `S × N(d1) − X × e^(−rT) × N(d2)`; the components are a **leveraged position**:
  `N(d1)` units of stock financed by borrowing `X·e^(−rT)·N(d2)`.
- `N(d2)` ≈ risk-neutral probability the call finishes in the money; `N(d1)` = delta.
- **Put** replication: **long `N(−d2)` bonds + short `N(−d1)` stock** → `p = Xe^(−rT)N(−d2) − S·N(−d1)`.
- Carry (dividends/yield) reduces a call's value, raises a put's.

## Black Model & Swaptions (29.i, 29.j)
- **Black model**: BSM variant for **options on futures** (uses the futures price, discounts at e^(−rT)).
- Applied to **interest-rate options** and **swaptions** (option to enter a swap): a payer swaption is
  like a call on rates; a receiver swaption like a put on rates.

## Option Greeks (29.k-29.n)
| Greek | Measures sensitivity to | Notes |
|------|------|------|
| **Delta** | Underlying price | = N(d1) for a call; ranges 0→1 (call), −1→0 (put) |
| **Gamma** | Change in delta | Largest **at-the-money near expiry**; drives hedge re-balancing |
| **Vega** | Volatility | Positive for long options; largest ATM |
| **Theta** | Time decay | Usually negative for long options |
| **Rho** | Risk-free rate | Smaller effect |

- **Delta hedge**: hold `−delta` of underlying per option to be locally neutral; must **rebalance
  dynamically** as delta changes.
- **Gamma risk**: large/discontinuous moves break a delta hedge (delta itself moves) → need gamma
  management; gamma highest for ATM options near expiry.
- **Implied volatility**: the σ that sets BSM price = market price; used to quote/compare options
  (volatility surface, skew). Not a forecast — a market-consensus input.

## Exam Traps
- Risk-neutral up-probability `π_U = (1 + r − d)/(u − d)`; value = **PV of risk-neutral expected payoff**.
- BSM call = `S·N(d1) − Xe^(−rT)·N(d2)`; `N(d1)` = delta, `N(d2)` ≈ prob of finishing ITM.
- **Black model** is for options on **futures** (and swaptions).
- **Gamma is highest ATM near expiry**; delta hedges need continual rebalancing.

## Q&A

### 2026-06-03 — One-period binomial call (worked)
**Q:** S0 = $30, u = 1.333, d = 0.75, one-period rf = 7%, call strike $30. Value the call.
**A:** Risk-neutral up-prob `π_U = (1 + r − d)/(u − d) = (1.07 − 0.75)/(1.333 − 0.75) = 0.32/0.583 =
0.549`; π_D = 0.451. Payoffs: up S = 39.99 → c_up = 9.99; down S = 22.5 → c_down = 0. Value = PV of
risk-neutral expected payoff = `(0.549×9.99 + 0.451×0)/1.07 = 5.485/1.07 = $5.13`. Equivalent hedge-ratio
check: `h = (c_up − c_down)/(S_up − S_down) = 9.99/17.49 = 0.571`. For **American** options check early
exercise (value = max(exercise, hold)) at each node.
Related: [[Forward_Commitments]]

### 2026-06-03 — Reading BSM: N(d1), N(d2), and the put
**Q:** What do N(d1) and N(d2) represent, and how do you get the put value?
**A:** Call = `S·N(d1) − Xe^(−rT)·N(d2)`: it's a **leveraged stock position** — long **N(d1)** shares
(N(d1) = the call's **delta**) financed by borrowing the PV of the strike times **N(d2)**, where N(d2) ≈
the **risk-neutral probability the call finishes in-the-money**. Put (by replication / parity) =
`Xe^(−rT)·N(−d2) − S·N(−d1)`. Delta-hedging holds −delta of the underlying per option and must be
**rebalanced dynamically**; the hedge fails on large jumps because **gamma** (highest **ATM near
expiry**) makes delta itself move. The **Black model** is the futures-based variant (used for
swaptions).
Related: [[Forward_Commitments]]
