---
aliases: [Options Valuation, Binomial Option Model, Black-Scholes-Merton, BSM, Black Model, Option Greeks, Delta Hedging, Implied Volatility]
tags: [CFA-L2, deriv, concept, options]
date: 2026-06-03
status: evergreen
source: Official Curriculum V7 (Derivatives) Learning Module 2; Schweser Book 4, Module 29, LOS 29.a-29.n
---

# Valuation of Contingent Claims (Options)

## Binomial Option Model (29.a, 29.b, 29.d)
- Underlying moves up by factor `u` or down by `d` each period. **Risk-neutral probability of up**: `π_U = (1 + r − d) / (u − d)`, `π_D = 1 − π_U`.
- **Option value = PV of expected payoff under risk-neutral probabilities**: `c = [π_U × c_up + π_D × c_down] / (1 + r)`.
- **Worked example (Schweser):** rf = 7%, S0 = $30, u = 1.333, d = 0.75 → `π_U = (1.07 − 0.75)/(1.333 − 0.75) = 0.32/0.583 = 0.549`. Then value = PV of the 0.549/0.451 probability-weighted payoffs, discounted at 7%.
- **Two-period**: roll backward through the tree. For **American** options, check **early exercise** at each node (value = max(exercise, hold)).

## No-Arbitrage / Hedge Ratio (29.c)
- Replicate the option with a position in the underlying and risk-free borrowing/lending.
- **Hedge ratio (delta)** for one period: `h = (c_up − c_down) / (S_up − S_down)`. If the option is mispriced vs the replicating portfolio → arbitrage.

## Interest-Rate Options (29.e)
- Value caplets/floorlets on a binomial interest-rate tree; payoff at each node depends on the rate there; discount back with backward induction (no single risk-neutral 0.5 — use the tree's structure).

## Black-Scholes-Merton (29.f, 29.g, 29.h)
- **Assumptions** (six): (1) underlying follows **geometric Brownian motion → lognormal** prices (continuous paths); (2) **constant volatility σ**; (3) **constant risk-free rate**; (4) frictionless markets / continuous trading, short selling with full use of proceeds; (5) no cash flows on the underlying (base case — relaxed below); (6) **European** exercise.
- **Call** = `S·N(d1) − e^(−rT)·X·N(d2)`  …(Eq. 10)
- **Put** = `e^(−rT)·X·N(−d2) − S·N(−d1)`  …(Eq. 11), using `N(−x) = 1 − N(x)`.
- **The d-terms** (memorize): `d1 = [ln(S/X) + (r + σ²/2)·T] / (σ·√T)`  and  `d2 = d1 − σ·√T`.
- **Interpretation as a replicating (leveraged) portfolio** `nS·S + nB·B`, with `B = e^(−rT)·X`:

| Position | shares of stock nS | bonds nB |
|---|---|---|
| **Call** | `N(d1) > 0` (buy) | `−N(d2) < 0` (borrow) |
| **Put** | `−N(−d1) < 0` (short) | `N(−d2) > 0` (lend) |

- A **call = leveraged long stock** (buy stock on margin); a **put = short stock + long bonds**.
- `N(d1)` = the option's **delta**; `N(d2)` = **risk-neutral probability the call finishes ITM** (`Prob(ST > X)`), and `N(−d2)` = RN prob the put finishes ITM. BSM = `PV[E(payoff)]` under the **risk-neutral** measure, discounted at the **risk-free** rate.

## BSM with Carry Benefits — Equities & Currencies (29.h)
Model a continuous carry yield **γ** (dividends for stocks, **foreign rate rf for FX**, coupon yield for bonds; carry costs enter as negative γ):
- **Call** = `S·e^(−γT)·N(d1) − e^(−rT)·X·N(d2)`  …(Eq. 12)
- **Put** = `e^(−rT)·X·N(−d2) − S·e^(−γT)·N(−d1)`  …(Eq. 13)
- `d1 = [ln(S/X) + (r − γ + σ²/2)·T] / (σ·√T)`, `d2 = d1 − σ·√T`.
- **Carry-adjusted put–call parity (Eq. 14)**: `p + S·e^(−γT) = c + e^(−rT)·X`.
- **Higher carry benefit → lower call, higher put** (it lowers the forward/expected underlying).
- **Currency options**: underlying = spot FX **S (domestic per foreign)**; γ = **foreign risk-free rate rf**; r = **domestic** risk-free rate; both S and X quoted in the same (domestic) currency unit. Trap: the carry rate is the *foreign* rate, the discount rate is the *domestic* rate.

## Black Model — Options on Futures (29.i)
For underlyings that are **costless to carry** (futures/forwards), use the futures price F0(T):
- **Call** = `e^(−rT)·[F0(T)·N(d1) − X·N(d2)]`  …(Eq. 15)
- **Put** = `e^(−rT)·[X·N(−d2) − F0(T)·N(−d1)]`  …(Eq. 16)
- `d1 = [ln(F0(T)/X) + (σ²/2)·T] / (σ·√T)`, `d2 = d1 − σ·√T` (no carry/rate term in d1 — it is embedded in F0). **Futures put–call parity**: `c = e^(−rT)·[F0(T) − X] + p`.

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- Exchange-traded commodity options are commonly options on futures, so the Black model intuition is usually the right starting point: the futures price already embeds financing, storage, and convenience-yield economics.
- Commodity option hedging is usually done with the futures contract for the same delivery month or the closest liquid proxy. That leaves **basis risk** when the option references a different grade, location, pricing window, or physical index.
- Delta hedges are fragile around inventory shocks, weather events, refinery outages, sanctions, export bans, and delivery-period squeezes. These are jump risks; they violate the continuous-trading intuition behind BSM/Black and make gamma and liquidity management central.
- Implied volatility can differ sharply by contract month because each delivery month has its own inventory and seasonality. A flat volatility assumption is especially weak for energy and agriculture curves.
- Storage, swing, and take-or-pay contracts often contain embedded optionality. Black-style models may help with intuition, but operational constraints and path dependence often require simulation or specialized physical-asset valuation.

## Interest-Rate Options & Swaptions (29.i, 29.j)
Black-model variants. **Interest-rate option** (standard market model) — underlying is a **forward rate** FRA(0,t_{j−1},tm), discounted to settlement `t_{j−1}+tm` (settled in arrears), scaled by accrual period AP:
- **Call** = `AP·e^(−r(t_{j−1}+tm))·[FRA·N(d1) − RX·N(d2)]`  …(Eq. 18)
- **Put** = `AP·e^(−r(t_{j−1}+tm))·[RX·N(−d2) − FRA·N(−d1)]`  …(Eq. 19) with `d1 = [ln(FRA/RX) + (σ²/2)·t_{j−1}]/(σ·√t_{j−1})`, `d2 = d1 − σ·√t_{j−1}`.
- An **interest-rate call** pays when the rate **exceeds** RX (borrower's hedge); a **put** pays when the rate is **below** RX (lender's hedge). Long cap + short floor (same RX) = pay-fixed/receive-floating swap.

**Swaptions** — option on a swap; underlying = **forward swap rate RFIX**, discounted by the **annuity factor** `PVA = Σ PV_{0,tj}` (no separate discount factor — the annuity embeds it):
- **Payer swaption** (right to **pay fixed**): `PAYSWN = AP·PVA·[RFIX·N(d1) − RX·N(d2)]`  …(Eq. 20)
- **Receiver swaption** (right to **receive fixed**): `RECSWN = AP·PVA·[RX·N(−d2) − RFIX·N(−d1)]`  …(Eq. 21) with `d1 = [ln(RFIX/RX) + (σ²/2)·T]/(σ·√T)`, `d2 = d1 − σ·√T`; rates in **decimals** (0.02, not 2%).
- **Payer swaption ≈ call on rates** (gains as fixed rates rise); **receiver swaption ≈ put on rates**. Equivalences: long payer + short receiver (same RX) = pay-fixed forward swap. **Long a callable bond ≈ long a straight bond + short a receiver swaption** (the embedded call resembles a receiver swaption).

## Option Greeks (29.k-29.n)
The Greeks are **static (comparative-statics) risk measures** — sensitivity of value to one input, holding others constant.

| Greek | Sensitivity to | Formula / sign | Key facts |
|------|------|------|------|
| **Delta** | Underlying price | call `= e^(−γT)·N(d1) ≥ 0`; put `= −e^(−γT)·N(−d1) ≤ 0` | call delta 0→1, put −1→0; ≈ N(d1) when γ=0 |
| **Gamma** | Δ in delta (2nd order) | `≥ 0`; **gamma of call = gamma of put** | largest **ATM near expiry**; 0 for stock; non-linearity risk |
| **Theta** | Calendar time passing | usually `< 0` (long options decay) | decay **accelerates** as expiry nears; stock theta = 0 |
| **Vega** | Volatility σ | `> 0` for long options | largest **ATM**; based on *unobservable* future vol; hedge vol with options |
| **Rho** | Risk-free rate r | **call rho > 0, put rho < 0** | smallest practical effect |

- **Delta hedge** — make the **portfolio delta-neutral**. Optimal hedge units of the hedging instrument: `NH = −(Portfolio delta) / (Delta_H)`. If NH < 0 → short the hedge; NH > 0 → long it. Stock has delta = +1 per share. *Example:* short calls on 1,000 shares with call delta 0.50 → portfolio delta −500 → buy `−(−500)/1 = 500` shares. Must **rebalance dynamically** as delta drifts (continuous trading is the BSM ideal).
- **Delta approximation** of an option's price change: `Δc ≈ Delta_c·(ΔS)`; biased **low** for both up and down moves (the true curve lies above the tangent). **Delta-plus-gamma approximation** is more accurate: `Δc ≈ Delta_c·ΔS + ½·Gamma_c·(ΔS)²`.
- **Gamma risk**: large/discontinuous jumps break a delta hedge because **delta itself moves**; gamma is the residual risk after delta-neutralizing. Manage gamma **first** (only options change gamma; stock cannot), **then** neutralize delta with stock (stock has zero gamma). Gamma highest **ATM near expiry**.
- **Implied volatility**: the σ that makes BSM price = market price — a **forward-looking, market-consensus view of future volatility** (vs *historical* volatility, which is backward-looking). Not directly observable. **Volatility smile/skew** = implied vol plotted vs strike (2-D); **volatility surface** = implied vol vs strike **and** expiration (3-D). If BSM held exactly the surface would be **flat**; in practice it is not, evidencing departures from the lognormal/constant-vol assumptions.

## Exam Traps
- Risk-neutral up-probability `π = (1 + r − d)/(u − d)` (curriculum: `[FV(1) − d]/(u − d)`); value = **PV of risk-neutral expected payoff** `c = PV[π·c+ + (1−π)·c−]`. For **American** options, check early exercise (max(exercise, hold)) at each node.
- BSM call = `S·N(d1) − Xe^(−rT)·N(d2)`; **`d1 = [ln(S/X) + (r + σ²/2)T]/(σ√T)`, `d2 = d1 − σ√T`**. `N(d1)` = delta, `N(d2)` ≈ risk-neutral prob of finishing ITM. Use `N(−x) = 1 − N(x)`.
- **Carry-adjusted BSM** multiplies the stock term by `e^(−γT)` and d1 uses `(r − γ + σ²/2)`; higher carry → **lower call, higher put**. Currency options: γ = **foreign** rate, discount at **domestic** rate.
- **Black model** is for options on **futures/forwards** (d1 has no rate/carry term — it's in F0); also used for **interest-rate options** and **swaptions**. **Payer swaption ≈ call on rates**, receiver ≈ put.
- Swaption discounting uses the **annuity factor PVA**, not a single discount factor; rates in decimals.
- **Delta**: call `e^(−γT)N(d1)` (0→1), put `−e^(−γT)N(−d1)` (−1→0). **Hedge units `NH = −Port.delta/Δ_H`**.
- **Gamma of a call = gamma of a put**; gamma **highest ATM near expiry**; gamma is the risk left after delta-neutralizing; delta-plus-gamma approximation beats delta alone.
- **Rho**: call **positive**, put **negative**. **Theta** usually negative (decay accelerates near expiry).
- **Implied volatility** is forward-looking (vs historical = backward-looking); a non-flat **vol surface** signals BSM-assumption breakdown.

## Q&A

### 2026-06-03 — One-period binomial call (worked)
**Q:** S0 = $30, u = 1.333, d = 0.75, one-period rf = 7%, call strike $30. Value the call.
**A:** Risk-neutral up-prob `π_U = (1 + r − d)/(u − d) = (1.07 − 0.75)/(1.333 − 0.75) = 0.32/0.583 = 0.549`; π_D = 0.451. Payoffs: up S = 39.99 → c_up = 9.99; down S = 22.5 → c_down = 0. Value = PV of risk-neutral expected payoff = `(0.549×9.99 + 0.451×0)/1.07 = 5.485/1.07 = $5.13`. Equivalent hedge-ratio check: `h = (c_up − c_down)/(S_up − S_down) = 9.99/17.49 = 0.571`. For **American** options check early exercise (value = max(exercise, hold)) at each node.
Related: [[Forward_Commitments]]

### 2026-06-03 — Reading BSM: N(d1), N(d2), and the put
**Q:** What do N(d1) and N(d2) represent, and how do you get the put value?
**A:** Call = `S·N(d1) − Xe^(−rT)·N(d2)`: it's a **leveraged stock position** — long **N(d1)** shares (N(d1) = the call's **delta**) financed by borrowing the PV of the strike times **N(d2)**, where N(d2) ≈ the **risk-neutral probability the call finishes in-the-money**. Put (by replication / parity) = `Xe^(−rT)·N(−d2) − S·N(−d1)`. Delta-hedging holds −delta of the underlying per option and must be **rebalanced dynamically**; the hedge fails on large jumps because **gamma** (highest **ATM near expiry**) makes delta itself move. The **Black model** is the futures-based variant (used for swaptions).
Related: [[Forward_Commitments]]

### 2026-06-04 — BSM d1/d2 and the carry-adjusted form
**Q:** Write the BSM d1 and d2, and how do they change for a dividend-paying stock or a currency option?
**A:** Base case: `d1 = [ln(S/X) + (r + σ²/2)·T]/(σ·√T)`, `d2 = d1 − σ·√T`; call = `S·N(d1) − e^(−rT)X·N(d2)`, put = `e^(−rT)X·N(−d2) − S·N(−d1)`. **With a continuous carry yield γ** (dividend yield, or the foreign rate for FX): multiply the stock term by `e^(−γT)` and use `d1 = [ln(S/X) + (r − γ + σ²/2)·T]/(σ·√T)`. Carry-adjusted parity: `p + S·e^(−γT) = c + e^(−rT)X`. Higher γ **lowers the call, raises the put**. For a **currency option** the underlying is the spot FX (domestic/foreign), **γ = the foreign risk-free rate**, and the discount rate r = the **domestic** rate.
Related: [[Forward_Commitments]]

### 2026-06-04 — Black model, IR options, and swaptions
**Q:** How do the Black model, interest-rate option, and swaption pricing formulas relate?
**A:** All are Black-model variants where the underlying's carry is embedded in a forward price/rate.
**Options on futures**: `c = e^(−rT)[F0(T)·N(d1) − X·N(d2)]`, `p = e^(−rT)[X·N(−d2) − F0(T)·N(−d1)]`, with `d1 = [ln(F0/X) + (σ²/2)T]/(σ√T)` (no rate term — it's in F0). **Interest-rate option** swaps F0(T) for a **forward rate FRA**, multiplies by accrual period AP, and discounts to settlement `t_{j−1}+tm`: `c = AP·e^(−r(t_{j−1}+tm))[FRA·N(d1) − RX·N(d2)]`. **Swaption** uses the **forward swap rate RFIX** and an **annuity factor PVA** instead of a single discount factor: payer `= AP·PVA·[RFIX·N(d1) − RX·N(d2)]`, receiver `= AP·PVA·[RX·N(−d2) − RFIX·N(−d1)]`. A **payer swaption ≈ call on rates**, receiver ≈ put on rates; a callable bond ≈ straight bond − a receiver swaption.
Related: [[Forward_Commitments]]

### 2026-06-04 — Delta-hedge sizing and gamma management
**Q:** We are short 1,000 calls with delta 0.50. How many shares to delta-hedge, and what about gamma?
**A:** Hedge units `NH = −(Portfolio delta)/Delta_H`. The short-call portfolio delta is `−1,000 × 0.50 = −500`; hedging with stock (delta = +1) gives `NH = −(−500)/1 = +500` → **buy 500 shares**. The hedge is only **locally** valid and must be **rebalanced dynamically** as delta drifts. The residual is **gamma risk** — large jumps move delta itself (delta approximation is biased low; `Δc ≈ Δ·ΔS + ½·Γ·ΔS²` is better). Because **stock has zero gamma**, you set gamma first using *other options*, then neutralize delta with stock. Gamma (equal for the call and its matching put) is **highest ATM near expiry**.
Related: [[Forward_Commitments]]
