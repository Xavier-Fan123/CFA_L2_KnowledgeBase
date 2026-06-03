---
aliases: [Currency Exchange Rates, FX Forecasting, Parity Conditions, Carry Trade, Covered Interest Rate Parity, Triangular Arbitrage]
tags: [CFA-L2, econ, concept, fx]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 5, LOS 5.a-5.m
---

# Currency Exchange Rates: Determination and Forecasting

Quote convention: **P/B = price currency / base currency** (price of 1 unit of base). "Buy the base"
at the **offer (ask)**; "sell the base" at the **bid**.

## Bid-Offer Spread (5.a)
- Spread quoted in **pips**. Dealer **buys base at bid, sells base at offer**.
- Spread widens with: lower currency-pair **liquidity** (volume), higher **volatility**, larger **trade
  size**, and as **maturity** lengthens (forward spreads ≥ spot spreads).

## The Conversion Mnemonic (Schweser)
**"Up-the-bid-and-multiply, down-the-ask-and-divide."** Given a P/B quote: converting the base→price
currency means going **up** the quote → use the **bid** and **multiply**; converting price→base means
going **down** the quote → use the **ask (offer)** and **divide**. (Rule: *buy the base at ask, sell the
base at bid*.)

## Triangular Arbitrage (5.b)
Three currencies, three quotes; if the implied cross rate ≠ the quoted cross rate, arbitrage exists.
- **Cross rate**: compute from two pairs so the common currency cancels. Compare to the dealer's quote;
  use the **dealer quotes** (not the computed cross) when walking the triangle.
- Go around the triangle one way (clockwise), then the other; you can profit in only one direction.

**Worked example (Schweser):** dealer quotes MXN/AUD = 6.3000–6.3025; USD/MXN ask 0.0935, USD/AUD bid
0.6000. Start USD 1m, clockwise:
1. USD 1m → MXN at 0.0935 (down, divide): `1,000,000 / 0.0935 = 10,695,187 MXN`
2. MXN → AUD at 6.3025 (down, divide): `= 1,696,975 AUD`
3. AUD → USD at 0.6000 (up, multiply): `1,696,975 × 0.60 = 1,018,185 USD` → **profit ≈ USD 18,185**.
(Counter-clockwise gives a USD 22,793 loss — only one direction is profitable.)

## Forward Rate (5.c) and Mark-to-Market (5.d)
- **Forward premium/discount** = `F − S` (in price-currency terms). Base currency trades at a forward
  **premium** when its interest rate is **lower** than the price currency's.
- Forward (covered interest parity), with day-count `τ = days/360`:
  `F = S × (1 + r_price·τ) / (1 + r_base·τ)`
- **MTM value of a forward** before expiry (long base): discount the change in forward rate:
  `Vt = (Ft − F0) × contract size / (1 + r_price·(days remaining/360))`
  - **Worked example (Schweser):** long CAD 1m at F0 = 1.05358 AUD/CAD (90-day). After 30 days (60 left),
    the new 60-day forward bid = 1.06206 AUD/CAD, 60-day AUD rate = 1.16%. To unwind, sell CAD forward (up
    the bid): `Vt = (1.06206 − 1.05358) × 1,000,000 / (1 + 0.0116 × 60/360) = 8,480 / 1.001933 ≈ AUD 8,463.64`
    gain. **Discount at the price-currency (AUD) rate.**

## International Parity Conditions (5.e, 5.f)

| Condition | Statement | Holds by arbitrage? |
|------|------|------|
| **Covered IRP** | `F/S = (1+r_price)/(1+r_base)`; forward fully offsets rate differential | **Yes** (no-arb) |
| **Uncovered IRP** | Expected %ΔS (base) ≈ `r_base − r_price` (high-yield currency expected to depreciate) | No |
| **Forward rate parity** | Forward rate = unbiased predictor of future spot | No |
| **PPP** (absolute/relative/ex-ante) | %ΔS ≈ inflation differential | Only long-run (relative) |
| **International Fisher effect** | Nominal rate differential ≈ expected inflation differential (equal real rates) | No |

Linkages: Covered IRP always holds. If forward rate parity holds → UIRP holds. International Fisher
links rate diffs to inflation diffs; ex-ante PPP links inflation diffs to %ΔS. **If ex-ante relative
PPP and international Fisher both hold → UIRP holds.** UIRP assumes investors are **risk-neutral**
(they demand no premium for FX risk).

**Worked examples (Schweser):**
- **Covered interest arbitrage**: USD MRR 8%, EUR MRR 6%, spot 1.30 USD/EUR. No-arb forward =
  `1.30 × (1.08/1.06) = 1.3245`. Market forward 1.35 > 1.3245 → euro forward overpriced → **sell EUR
  forward, buy EUR spot** to arbitrage.
- **UIRP forecast**: spot ZAR/EUR = 8.385, EUR rate 10%, ZAR rate 8%. Base (EUR) expected
  %ΔS ≈ `R_ZAR − R_EUR = 8% − 10% = −2%` → EUR depreciates 2% → new rate ≈ `8.385 × 0.98 = 8.217 ZAR/EUR`.
- **Ex-ante PPP**: spot USD/AUD = 1.00, expected inflation US 2% / AUD 5%. %ΔS(AUD) ≈
  `inflation_USD − inflation_AUD = 2% − 5% = −3%` → AUD depreciates → ≈ 0.97 USD/AUD.

## Forecasting & Long-Run Fair Value (5.g, 5.h)
- Short/medium term: UIRP and PPP **seldom hold**; forward rate is a **biased** predictor.
- Long run: **relative PPP** tends to hold → real exchange rate is mean-reverting. Assess fair value
  via ex-ante PPP, UIRP, or forward rates.

## Carry Trade (5.i)
- **Borrow the low-yield (funding) currency, invest in the high-yield currency.** Profitable precisely
  when UIRP **fails** (high-yielder does not depreciate as predicted).
- Return ≈ interest differential ± currency move. Risk profile: small steady gains punctuated by rare
  large losses → **negative skew / "crash risk"** (peso problem). Returns are **not** normally distributed.

## Balance of Payments, Policy, Crises (5.j-5.m)
- **BOP flows**: persistent current-account deficits tend to pressure a currency lower (flow + portfolio
  mechanisms); capital-account flows can dominate short-term moves.
- **Monetary/fiscal policy (Mundell-Fleming)**: with high capital mobility, **expansionary monetary →
  lower rates → currency depreciation**; **expansionary fiscal → higher rates → appreciation** (rate
  channel). Effects can reverse under low capital mobility (trade channel).
- **Portfolio balance / monetary models**: long-run money-supply growth → depreciation.
- **Intervention & capital controls**: more effective for EM with smaller FX markets; aim to manage
  volatility/level. **Currency crisis warning signs**: deteriorating terms of trade, large foreign
  liabilities / declining FX reserves, rapid prior money growth, fixed/overvalued real exchange rate,
  banking-sector fragility, contagion.

## Exam Traps
- Mind the quote convention — a forward **premium on the base** means `F > S` in P/B terms.
- Carry trade ≠ free money: it works while UIRP fails, but carries crash risk (negative skew).
- Covered IRP is the only parity condition enforced by arbitrage; the rest are equilibrium tendencies.
- Expansionary monetary policy → currency **depreciates** (rate channel, high capital mobility).

## Q&A

### 2026-06-03 — Marking a forward to market: which rate and which side?
**Q:** When you value an FX forward before expiry, which interest rate do you discount at, and do you use
the bid or the offer of the new forward?
**A:** Two rules. (1) **Discount at the price-currency rate** for the remaining days (the value is
expressed in the price currency). (2) To value an existing long-base forward you must **offset it** by
entering a new forward to **sell the base** for the remaining maturity → use the side of the new quote
that applies to selling the base (**up the bid**). `Vt = (F_new − F0) × size / (1 + r_price·(days left/360))`.
A positive number is a gain to the long-base position. Trap: do not discount at the base-currency rate,
and do not use the spot rate to mark a forward.
Related: [[Economics_Overview]]

### 2026-06-03 — Why does the carry trade have negative skew?
**Q:** The carry trade looks like steady profit — where's the catch?
**A:** It profits **only while uncovered interest rate parity fails** (the high-yield currency does not
depreciate by the rate differential as UIRP predicts). Returns are small and positive most of the time
(you pocket the interest differential), but in risk-off episodes the funding (low-yield) currency
spikes and the high-yield currency crashes, producing rare large losses → **negative skew / "crash
risk" (peso problem)**, fat left tail. So returns are **not** normally distributed and Sharpe ratios
overstate attractiveness.
Related: [[Economics_Overview]]

### 2026-06-03 — Mundell-Fleming: policy effects on the exchange rate
**Q:** Under high capital mobility, what do expansionary monetary and fiscal policy do to the currency?
**A:** With **high** capital mobility the **interest-rate channel** dominates. Expansionary **monetary**
policy → lower domestic rates → capital outflow → currency **depreciates**. Expansionary **fiscal**
policy → higher rates (crowding out / more borrowing) → capital inflow → currency **appreciates**.
Restrictive policies reverse these. Under **low** capital mobility the **trade (income) channel** can
dominate and reverse the fiscal result (expansion worsens the trade balance → depreciation). The two
expansionary policies together leave the FX effect **ambiguous** (they push rates in opposite directions).
Related: [[Economics_Overview]]
