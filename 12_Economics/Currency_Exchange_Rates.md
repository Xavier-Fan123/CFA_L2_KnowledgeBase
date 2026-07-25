---
aliases: [Currency Exchange Rates, FX Forecasting, Parity Conditions, Carry Trade, Covered Interest Rate Parity, Triangular Arbitrage]
tags: [CFA-L2, econ, concept, fx]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 5, LOS 5.a-5.m
---

# Currency Exchange Rates: Determination and Forecasting

Quote convention: **P/B = price currency / base currency** (price of 1 unit of base). "Buy the base" at the **offer (ask)**; "sell the base" at the **bid**.

## Bid-Offer Spread (5.a)
- Spread quoted in **pips**. Dealer **buys base at bid, sells base at offer**.
- Spread widens with: lower currency-pair **liquidity** (volume), higher **volatility**, larger **trade size**, and as **maturity** lengthens (forward spreads ≥ spot spreads).

## The Conversion Mnemonic (Schweser)
**"Up-the-bid-and-multiply, down-the-ask-and-divide."** Given a P/B quote: converting the base→price currency means going **up** the quote → use the **bid** and **multiply**; converting price→base means going **down** the quote → use the **ask (offer)** and **divide**. (Rule: *buy the base at ask, sell the base at bid*.)

## Exam Workflow - Quotes, Arbitrage, and Forwards (5.a-5.d)
Use the same five-step order for almost every computational FX vignette:

1. **Normalize the quote.** Write it as `P/B = price currency per 1 base currency`; label the base and price currencies before touching the numbers.
2. **Choose the side of the dealer quote.** Selling the base uses the **bid** and multiplying; buying the base uses the **ask** and dividing.
3. **For triangular arbitrage, walk the cash.** Convert through the three dealer quotes in one direction, then the other if needed; never use the implied cross rate for the actual trade legs.
4. **For covered IRP, use the price-currency rate in the numerator.** `F = S * (1 + r_price * t) / (1 + r_base * t)`. If `r_base < r_price`, the base trades at a forward premium.
5. **For forward MTM, offset the old contract.** A long-base forward is offset by selling the base forward, so use the new forward **bid**; then discount the forward-rate difference at the **price-currency** rate for the remaining term.

Common exam pattern: the vignette gives extra spot or interest-rate data to tempt a shortcut. Forward valuation during the contract's life uses the **new same-maturity forward**, not spot, and the quote side must match the offsetting trade.

## Triangular Arbitrage (5.b)
Three currencies, three quotes; if the implied cross rate ≠ the quoted cross rate, arbitrage exists.
- **Cross rate**: compute from two pairs so the common currency cancels. Compare to the dealer's quote; use the **dealer quotes** (not the computed cross) when walking the triangle.
- Go around the triangle one way (clockwise), then the other; you can profit in only one direction.

**Worked example (Schweser):** dealer quotes MXN/AUD = 6.3000–6.3025; USD/MXN ask 0.0935, USD/AUD bid 0.6000. Start USD 1m, clockwise:
1. USD 1m → MXN at 0.0935 (down, divide): `1,000,000 / 0.0935 = 10,695,187 MXN`
2. MXN → AUD at 6.3025 (down, divide): `= 1,696,975 AUD`
3. AUD → USD at 0.6000 (up, multiply): `1,696,975 × 0.60 = 1,018,185 USD` → **profit ≈ USD 18,185**. (Counter-clockwise gives a USD 22,793 loss — only one direction is profitable.)

## Forward Rate (5.c) and Mark-to-Market (5.d)
- **Forward premium/discount** = `F − S` (in price-currency terms). Base currency trades at a forward **premium** when its interest rate is **lower** than the price currency's.
- Forward (covered interest parity), with day-count `τ = days/360`: `F = S × (1 + r_price·τ) / (1 + r_base·τ)`

### Forward Points and the All-in Forward Rate (5.c)
In practice dealers quote a **spot rate** plus **forward points**, not the full forward outright. Forward points are scaled in **pips** (the last decimal of the quote):
- **All-in forward rate = spot rate + (forward points / scale)**, where scale = **10,000** for most pairs (4-decimal quotes), or **100** for JPY pairs quoted to 2 decimals. (Official curriculum, Reading 5.)
- Forward points are **positive** when the base trades at a forward **premium** (base rate < price rate) and **negative** at a forward **discount**. Their absolute size **grows with maturity** and with the size of the interest-rate differential.
- Build a forward quote side-consistently: **all-in bid = spot bid + points bid**, **all-in offer = spot offer + points offer**. The bid–offer factors (liquidity, volatility, term) apply to the points the same way they apply to spot.
- **Worked example (official, Reading 5):** spot EUR quote 1.1649, 1-month forward points bid = −15.9 → all-in 1-month forward bid `= 1.1649 + (−15.9/10,000) = 1.16331` (negative points → base at a forward discount). For an AUD/GBP example, spot 1.8210 + 3-month points 130 → all-in `1.8210 + 130/10,000 = 1.8340`.
- **Trap:** divide JPY-pair points by **100** (not 10,000) because the quote has only two decimals; mixing the scales is a classic error.

- **MTM value of a forward** before expiry (long base): discount the change in forward rate: `Vt = (Ft − F0) × contract size / (1 + r_price·(days remaining/360))`
  - **Worked example (Schweser):** long CAD 1m at F0 = 1.05358 AUD/CAD (90-day). After 30 days (60 left), the new 60-day forward bid = 1.06206 AUD/CAD, 60-day AUD rate = 1.16%. To unwind, sell CAD forward (up the bid): `Vt = (1.06206 − 1.05358) × 1,000,000 / (1 + 0.0116 × 60/360) = 8,480 / 1.001933 ≈ AUD 8,463.64` gain. **Discount at the price-currency (AUD) rate.**

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- Many globally traded commodities are priced in USD even when costs, taxes, freight, storage, or end-sales are in local currencies. A desk must separate the commodity hedge from the FX hedge; a flat commodity exposure can still have material currency P&L.
- For a known foreign-currency receivable or payable, the FX forward is a hedge of the cash flow, not a view that the forward is an unbiased forecast. Covered interest parity prices the forward; it does not say the future spot will equal the forward.
- Quote convention errors are operationally expensive in commodity trading because cargo invoices, letters of credit, freight, demurrage, and hedge settlements may be in different currencies. Always label the quote as `P/B` before deciding whether to use bid or offer.
- Carry trades are speculative currency positions. They should not be confused with hedging an operating FX exposure attached to a physical commodity purchase or sale.

## International Parity Conditions (5.e, 5.f)

| Condition | Statement | Holds by arbitrage? |
|------|------|------|
| **Covered IRP** | `F/S = (1+r_price)/(1+r_base)`; forward fully offsets rate differential | **Yes** (no-arb) |
| **Uncovered IRP** | Expected %ΔS (base) ≈ `r_base − r_price` (high-yield currency expected to depreciate) | No |
| **Forward rate parity** | Forward rate = unbiased predictor of future spot | No |
| **PPP** (absolute/relative/ex-ante) | absolute: `S_f/d = P_f/P_d`; relative/ex-ante: %ΔS ≈ inflation differential | Only long-run (relative) |
| **International Fisher effect** | Nominal rate differential ≈ **expected** inflation differential: `i_f − i_d = π_f^e − π_d^e` | No |
| **Real interest rate parity** | Real rates equal across markets → real yield spread `(r_f − r_d) = 0` | No (equilibrium) |

Linkages (official curriculum chain): Covered IRP always holds (arbitrage). If forward rate parity holds → UIRP holds. **UIRP + ex-ante relative PPP both holding ⇒ real interest rate parity** (real spread = 0), and it then follows that **`i_f − i_d = π_f^e − π_d^e` = the international Fisher effect** (nominal spread driven solely by expected-inflation differential). All of these (UIRP, forward parity, ex-ante PPP, Fisher) assume **risk-neutral** investors who demand no FX/inflation risk premium; only covered IRP is enforced by arbitrage.

**Worked examples (Schweser):**
- **Covered interest arbitrage**: USD MRR 8%, EUR MRR 6%, spot 1.30 USD/EUR. No-arb forward = `1.30 × (1.08/1.06) = 1.3245`. Market forward 1.35 > 1.3245 → euro forward overpriced → **sell EUR forward, buy EUR spot** to arbitrage.
- **UIRP forecast**: spot ZAR/EUR = 8.385, EUR rate 10%, ZAR rate 8%. Base (EUR) expected%ΔS ≈ `R_ZAR − R_EUR = 8% − 10% = −2%` → EUR depreciates 2% → new rate ≈ `8.385 × 0.98 = 8.217 ZAR/EUR`.
- **Ex-ante PPP**: spot USD/AUD = 1.00, expected inflation US 2% / AUD 5%. %ΔS(AUD) ≈ `inflation_USD − inflation_AUD = 2% − 5% = −3%` → AUD depreciates → ≈ 0.97 USD/AUD.

## Forecasting & Long-Run Fair Value (5.g, 5.h)
- Short/medium term: UIRP and PPP **seldom hold**; forward rate is a **biased** predictor.
- Long run: **relative PPP** tends to hold → real exchange rate is mean-reverting. Assess fair value via ex-ante PPP, UIRP, or forward rates.

### Forecasting Decision Rules (5.g, 5.h)

| Method | Input | Forecast logic | Best use | Main weakness |
|---|---|---|---|---|
| **Current spot** | `S0` | future spot is unchanged | neutral benchmark | ignores rates and inflation |
| **Forward rate** | `F0,T` | market forward as expected future spot | hedging / market-implied quote | biased predictor when risk premia exist |
| **UIRP** | nominal rate differential | high-yield currency expected to depreciate | rate-based forecast | fails often in the short run |
| **Relative PPP** | inflation differential | high-inflation currency expected to depreciate | long-run fair value | weak short-run predictor |
| **Real exchange rate** | nominal FX and price levels | mean reversion toward long-run real FX | valuation / misalignment | slow adjustment and regime breaks |

Use the facts to choose the model: **rates** point to UIRP/forward, **inflation** points to PPP, and **long-run over/undervaluation** points to real-exchange-rate mean reversion. If a question asks for a no-arbitrage forward, use **covered IRP**, not a forecasting parity.

## Carry Trade (5.i)
- **Borrow the low-yield (funding) currency, invest in the high-yield currency.** Profitable precisely when UIRP **fails** (high-yielder does not depreciate as predicted).
- Return ≈ interest differential ± currency move. Risk profile: small steady gains punctuated by rare large losses → **negative skew / "crash risk"** (peso problem). Returns are **not** normally distributed.

## Balance of Payments, Policy, Crises (5.j-5.m)
- **BOP flows**: persistent current-account deficits tend to pressure a currency lower (flow + portfolio mechanisms); capital-account flows can dominate short-term moves.
- **Monetary/fiscal policy (Mundell-Fleming)**: with high capital mobility, **expansionary monetary → lower rates → currency depreciation**; **expansionary fiscal → higher rates → appreciation** (rate channel). Effects can reverse under low capital mobility (trade channel).
- **Monetary models**: long-run money-supply growth → higher prices → depreciation (Dornbusch overshooting adds short-run sticky-price overshoot that mean-reverts).
- **Portfolio balance model**: the **long-run** counterpart to Mundell-Fleming for **fiscal** policy. Expansionary fiscal policy → growing stock of govt debt in investor portfolios → investors eventually demand a higher risk premium and become saturated. The short-run fiscal **appreciation** (Mundell-Fleming rate channel) is unsustainable and **reverses to long-run depreciation** unless the government reverses fiscal policy or the central bank **monetizes** the debt.

### Exchange-Rate-Determination Models (beyond parity)
| Model | Focus | Horizon | Key result |
|---|---|---|---|
| **Mundell-Fleming** | Monetary + fiscal policy via interest-rate / trade channels | Short run | Exp. monetary → depreciation; exp. fiscal → appreciation (high capital mobility) |
| **Monetary models** (incl. Dornbusch overshooting) | Money supply & inflation; PPP-based, output fixed | Mainly long run | Money growth → higher prices → depreciation; sticky prices → short-run overshooting |
| **Portfolio balance** | Sustained fiscal deficits & debt accumulation | Long run | Short-run fiscal appreciation unwinds → long-run depreciation as debt saturates / is monetized |

**Trap:** Mundell-Fleming (short run) and portfolio balance (long run) give **opposite** signs for the same expansionary fiscal policy — short-run appreciation, long-run depreciation.
- **Intervention & capital controls**: more effective for EM with smaller FX markets; aim to manage volatility/level. **Currency crisis warning signs**: deteriorating terms of trade, large foreign liabilities / declining FX reserves, rapid prior money growth, fixed/overvalued real exchange rate, banking-sector fragility, contagion.

### Policy Impact Grid (5.k, 5.l)

| Policy shock | High capital mobility | Low capital mobility / trade channel |
|---|---|---|
| **Expansionary monetary** | lower rates -> capital outflow -> depreciation | depreciation still likely through money supply and lower rates |
| **Restrictive monetary** | higher rates -> capital inflow -> appreciation | appreciation, unless recessionary effects dominate |
| **Expansionary fiscal** | higher rates -> capital inflow -> appreciation | higher income/imports -> current-account pressure -> depreciation |
| **Restrictive fiscal** | lower rates -> capital outflow -> depreciation | lower imports -> current-account support -> appreciation |
| **Monetary + fiscal expansion** | ambiguous, because the policies push rates in opposite directions | usually ambiguous; read the stated channel |

If the vignette explicitly says **high capital mobility**, use the interest-rate channel first. If it emphasizes low capital mobility, import growth, or trade balance pressure, use the trade channel.

### Crisis Diagnostic Checklist (5.m)
A currency-crisis vignette usually combines several of these:

- **Overvalued real exchange rate** or a fixed peg that has become hard to defend.
- **Falling FX reserves** against large short-term foreign-currency liabilities.
- **Rapid domestic credit / money growth**, often tied to banking-sector weakness.
- **Worsening current account** or deteriorating terms of trade.
- **Large fiscal deficits** financed by money creation or external borrowing.
- **Contagion** from a similar country or currency regime.
- **Policy inconsistency**, such as defending a peg while running loose money or fiscal policy.

The strongest answer is usually not "one bad ratio." It is the combination of an overvalued currency, fragile external funding, and limited reserves.

## Exam Traps
- Mind the quote convention — a forward **premium on the base** means `F > S` in P/B terms.
- Carry trade ≠ free money: it works while UIRP fails, but carries crash risk (negative skew).
- Covered IRP is the only parity condition enforced by arbitrage; the rest are equilibrium tendencies.
- Expansionary monetary policy → currency **depreciates** (rate channel, high capital mobility).

- In a forward MTM problem, discount at the **price-currency** rate and use the new forward quote that offsets the old position.
- Do not use a no-arbitrage covered-IRP forward as proof that the forward is an unbiased forecast; no-arbitrage and forecasting are separate ideas.
- Currency crises are usually multi-signal cases: overvaluation plus weak reserves plus short-term FX debt is stronger evidence than any single symptom.

## Q&A

### 2026-06-03 — Marking a forward to market: which rate and which side?
**Q:** When you value an FX forward before expiry, which interest rate do you discount at, and do you use the bid or the offer of the new forward?
**A:** Two rules. (1) **Discount at the price-currency rate** for the remaining days (the value is expressed in the price currency). (2) To value an existing long-base forward you must **offset it** by entering a new forward to **sell the base** for the remaining maturity → use the side of the new quote that applies to selling the base (**up the bid**). `Vt = (F_new − F0) × size / (1 + r_price·(days left/360))`. A positive number is a gain to the long-base position. Trap: do not discount at the base-currency rate, and do not use the spot rate to mark a forward.
Related: [[Economics_Overview]]

### 2026-06-07 - FX vignette workflow: quote side, arbitrage, and forward MTM
**Q:** What is the safest order for solving FX quote, triangular-arbitrage, and forward-value questions?
**A:** First label the quote as `P/B`; second choose the quote side (sell base = bid and multiply, buy base = ask and divide); third walk the actual dealer quotes around the triangle if arbitrage is possible; fourth use covered IRP for a no-arbitrage forward; fifth, for MTM, offset the old contract with the new remaining-maturity forward and discount the rate difference at the **price-currency** rate. Most errors come from using the implied cross rate for a trade leg, using spot instead of the new forward, or discounting at the base-currency rate.
Related: [[Economics_Overview]]

### 2026-06-07 - Choosing the correct FX forecast model
**Q:** How do you decide whether to use spot, forward, UIRP, PPP, or real-exchange-rate mean reversion to forecast a future spot rate?
**A:** Use the model implied by the input data and wording. **Forward** is a market-implied hedge/quote and is not guaranteed unbiased; **UIRP** uses nominal rate differentials; **relative PPP** uses expected inflation differentials; **real-exchange-rate mean reversion** is the long-run fair-value tool; current spot is a neutral benchmark. If the question asks for no-arbitrage, that is **covered IRP**, not a forecasting claim.
Related: [[Economics_Overview]]

### 2026-06-07 - Currency crisis warning signs
**Q:** What combination of facts is most persuasive for a currency-crisis risk question?
**A:** Look for a cluster: overvalued/fixed exchange rate, falling reserves, large short-term foreign-currency debt, rapid domestic credit or money growth, a current-account deficit or terms-of-trade shock, fragile banks, and contagion. A single symptom is weak evidence; overvaluation plus reserve weakness plus external funding pressure is the classic crisis setup.
Related: [[Economic_Growth]]

### 2026-06-03 — Why does the carry trade have negative skew?
**Q:** The carry trade looks like steady profit — where's the catch?
**A:** It profits **only while uncovered interest rate parity fails** (the high-yield currency does not depreciate by the rate differential as UIRP predicts). Returns are small and positive most of the time (you pocket the interest differential), but in risk-off episodes the funding (low-yield) currency spikes and the high-yield currency crashes, producing rare large losses → **negative skew / "crash risk" (peso problem)**, fat left tail. So returns are **not** normally distributed and Sharpe ratios overstate attractiveness.
Related: [[Economics_Overview]]

### 2026-06-04 — Forward points: how do you build the all-in forward rate?
**Q:** A dealer quotes spot plus forward points. How do I turn the points into a forward rate, and how do I pick the bid vs offer side?
**A:** **All-in forward = spot + (forward points / scale)**, where scale = **10,000** for normal 4-decimal pairs and **100** for JPY 2-decimal pairs. Stay side-consistent: all-in bid = spot bid + points bid, all-in offer = spot offer + points offer. Positive points = base at a forward **premium** (base interest rate < price-currency rate); negative points = forward **discount**. Example: spot 1.1649, 1-month points bid −15.9 → all-in bid `1.1649 + (−15.9/10,000) = 1.16331`. Trap: using /10,000 on a JPY pair (should be /100), and flipping the sign of negative points. Points grow with maturity and with the rate differential.
Related: [[Economics_Overview]]

### 2026-06-04 — Real interest rate parity vs the international Fisher effect
**Q:** How does "real interest rate parity" fit with the other parity conditions, and is it the same as the international Fisher effect?
**A:** They are linked but distinct. **Real interest rate parity** states that **real** interest rates converge across markets, so the real yield spread `(r_f − r_d) = 0`. It is the **joint outcome** of two conditions both holding: **uncovered IRP** (`%ΔS_f/d = i_f − i_d`) and **ex-ante relative PPP** (`%ΔS_f/d = π_f^e − π_d^e`). Setting the two equal gives `i_f − i_d = π_f^e − π_d^e`, i.e. the nominal yield spread is driven solely by the expected-inflation differential — and the curriculum reserves the name **international Fisher effect** for exactly that nominal-rate/expected-inflation relationship (some authors instead call UIRP the international Fisher effect; the official text does not). Both assume risk-neutral investors who demand no FX or inflation risk premium. (Official curriculum, Reading 5, "The Fisher Effect, Real Interest Rate Parity, and International Parity Conditions.")
Related: [[Economics_Overview]]

### 2026-06-15 — What is the portfolio balance model?
**Q:** What is the portfolio balance model?
**A:** It is the **long-run counterpart to Mundell-Fleming** for **fiscal** policy. Expansionary fiscal policy is financed by issuing domestic-currency debt; investors keep accumulating that debt until they become **saturated** and demand a higher risk premium. So the **short-run appreciation** from Mundell-Fleming's interest-rate channel is unsustainable and **reverses into long-run depreciation** — unless the government reverses its fiscal stance or the central bank **monetizes** the debt. Key trap: Mundell-Fleming (short run) and the portfolio balance model (long run) can give **opposite** FX signs for the *same* expansionary fiscal policy. It is one of three exchange-rate-determination models beyond parity, alongside Mundell-Fleming (interest-rate/trade channels, short run) and the monetary models (money supply/inflation, with Dornbusch overshooting).
Related: [[Economics_Overview]]

### 2026-06-03 — Mundell-Fleming: policy effects on the exchange rate
**Q:** Under high capital mobility, what do expansionary monetary and fiscal policy do to the currency?
**A:** With **high** capital mobility the **interest-rate channel** dominates. Expansionary **monetary** policy → lower domestic rates → capital outflow → currency **depreciates**. Expansionary **fiscal** policy → higher rates (crowding out / more borrowing) → capital inflow → currency **appreciates**. Restrictive policies reverse these. Under **low** capital mobility the **trade (income) channel** can dominate and reverse the fiscal result (expansion worsens the trade balance → depreciation). The two expansionary policies together leave the FX effect **ambiguous** (they push rates in opposite directions).
Related: [[Economics_Overview]]
