---
aliases: [Credit Analysis Models, Credit Valuation Adjustment, CVA, Structural Model, Reduced-Form Model, Credit Spread, Expected Exposure, LGD]
tags: [CFA-L2, fi, concept, credit]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 26, LOS 26.a-26.h
---

# Credit Analysis Models

## Building Blocks (26.a)
- **Expected exposure (EE)**: amount at risk (bond value) at a given date before recovery.
- **Recovery rate (RR)** / **Loss given default (LGD)** = `exposure × (1 − RR)`.
- **Probability of default (POD)**: likelihood of default in a period; **hazard rate** = conditional default probability.
- **Credit valuation adjustment (CVA)** = PV of **expected loss** = Σ (PV of each period's expected loss) = sum over time of `PV[ POD × LGD ]`.
- **VND (value assuming no default)** = the bond's value computed on the **benchmark binomial tree / spot curve as if default-free**. Official central identity: **fair (risky) value = VND − CVA**, and the **credit spread** = YTM(fair value) − benchmark YTM. (For an option-free bond on a flat benchmark, VND = the risk-free PV; the same tree that gives VND also generates the **expected exposures** for the CVA.)
- **Volatility note:** changing rate volatility does **not** change VND of a default-risk-free bond; vol only moves fair value when there is an **embedded option** or **credit risk** (CVA changes with the tree).
- **Sensitivity (curriculum):** a **lower POD** reduces CVA **more** than an equal-sized cut in the recovery rate (POD hits every period's expected loss; recovery only scales LGD).
- **Worked example (Schweser):** 3-yr, $100 par, **zero-coupon**, hazard rate 2%/yr, recovery 60% (LGD = 40% of exposure), benchmark flat 3%.
  - Probability of survival: Yr1 0.98, Yr2 0.9604, Yr3 0.9412; **PD**: Yr1 2%, Yr2 1.96%, Yr3 1.9208% (PD = hazard rate × prior-year PS).
  - Exposure: Yr3 $100, Yr2 100/1.03, Yr1 100/1.03²; expected loss = LGD × PD each year.
  - **CVA = Σ PV(expected loss) = $2.15**; risk-free value = 100/1.03³ = $91.51 → **risky value = 91.51 − 2.15 = $89.36**. The credit spread is the YTM gap between the two.

### Risky Floating-Rate Note — Discount Margin (26.e)
- The same VND − CVA framework values a **risky floater**. Cash flow each period = (benchmark rate at start of period + **quoted margin**) × par, set in arrears. **VND** ≈ par + PV(quoted margin); fair value = VND − CVA.
- **Discount margin (DM)** = the spread added to the benchmark rates in the tree so the Date-0 value = fair value — the floater's analogue of a fixed bond's credit spread / YTM. If the floater is priced **below par**, DM > quoted margin (and conversely). Found by trial-and-error / Solver.

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- In commodity trading, **expected exposure** is not just bond value. It includes open receivables, prepaid cargoes, replacement cost on undelivered physical contracts, positive MTM on OTC derivatives, and potential future exposure from price moves before settlement.
- Exposure is often **wrong-way**: a buyer's default probability can rise exactly when the commodity price falls and the seller is left with unwanted inventory, or when prices rise and a short supplier cannot afford to replace cargoes. POD, LGD, and exposure are therefore not independent in stress.
- Recovery depends heavily on legal title, netting enforceability, collateral quality, letters of credit, guarantees, retention-of-title clauses, and whether inventory can be located, seized, and resold. A headline recovery rate is weak without the trade-finance structure.
- Credit limits should be set by **counterparty group**, tenor, jurisdiction, product, and settlement mechanism. A low nominal receivable can still be high risk if the cargo is hard to liquidate, documentation is weak, or the counterparty controls logistics.
- CVA-style thinking is useful even when no formal CVA model is booked: expected loss rises with larger MTM exposure, longer settlement windows, weaker collateral, and stressed correlation between commodity prices and counterparty credit.
- Ratings can lag quickly deteriorating trade-credit conditions. For commodity counterparties, real-time signals such as delayed payments, reduced credit-line availability, missed margin calls, letter-of-credit confirmation difficulty, and widening bond/CDS spreads may be more timely than the agency rating.

## Credit Scores vs Ratings (26.b)
- **Credit scores**: for retail/small borrowers (e.g., FICO).
- **Credit ratings**: for corporate/sovereign issues (agency letter grades); **issuer** vs **issue** ratings; subject to stability ("through-the-cycle") and potential lag, and notching.

## Return Given Rating Transition (26.c)
- Use a **credit migration (transition) matrix** of probabilities of moving between ratings.
- **Expected % return impact** ≈ `−Σ (migration probability × Δspread × modified duration)` across possible new ratings. Downgrades widen spreads → price loss; upgrades the reverse.

## Structural vs Reduced-Form (26.d)

- **Structural (Merton / option-based)**: equity = **call option on firm assets**; default when asset value < debt face. Risky debt = risk-free debt − **put on assets**.
  - Strengths / weaknesses: economic intuition; but assets aren't traded/observable and the model assumes a simple capital structure.
- **Reduced-form**: models **default intensity (hazard rate)** statistically as a function of observable macro/firm variables; no assumption about firm structure.
  - Strengths / weaknesses: uses observable data and time-varying POD; but gives no economic "why" and relies on historical estimation (backward-looking).

## Credit Spread Dynamics (26.e, 26.f, 26.g)
- Spread compensates for **expected loss + risk/liquidity premium**. Spreads **widen** in downturns (higher POD, lower RR) and **tighten** in expansions.
- **Term structure of credit spreads**: upward-sloping for healthy issuers; can **invert** for distressed issuers (near-term default risk dominates). Drivers: credit cycle, financial conditions, issuer fundamentals, supply/demand.

## Securitized Debt (26.h)
Analyze the **collateral pool** (granularity, homogeneity), servicer quality, structure (tranching/credit enhancement), and cash-flow waterfall — not just a single obligor's balance sheet.

## Exam Traps
- **CVA = PV of expected loss**; **fair value = VND − CVA** (VND = value assuming no default).
- **Rate volatility does not change a default-free bond's VND** — it changes fair value only via an embedded option or via CVA (credit risk).
- A **decrease in POD** lowers CVA **more** than an equal decrease in the **recovery rate**.
- Risky **floater**: solve for the **discount margin (DM)** (not a credit spread); DM > quoted margin when priced below par.
- **Structural** model: equity is a **call** on assets, risky debt = risk-free − **put** on assets.
- **Reduced-form** models POD/hazard rate from observable variables (no capital-structure assumption); it is backward-looking in estimation.
- Distressed issuers can show an **inverted** credit-spread term structure.

## Q&A

### 2026-06-03 — Structural vs reduced-form credit models
**Q:** What's the core idea of each, and the key limitation?
**A:** **Structural (Merton)**: built on the firm's **capital structure** — equity is a **call option on the firm's assets** (default when assets < debt face at maturity), and risky debt = risk-free debt − **put on assets**. Limitation: firm assets aren't traded/observable and it assumes a simplistic capital structure. **Reduced-form**: models the **default intensity (hazard rate)** statistically as a function of observable macro/firm variables — no capital-structure assumption, allows time-varying POD. Limitation: no economic "why," and it's **backward-looking** (relies on historical estimation).
Related: [[Credit_Default_Swaps]]

### 2026-06-03 — Computing CVA / the credit spread
**Q:** How does CVA give the value of a risky bond and the credit spread?
**A:** `CVA = Σ PV(expected loss)`, where each period's expected loss = **POD × LGD** on that period's exposure, discounted at the benchmark rate. Then **risky value = risk-free value − CVA**, and the **credit spread** is the YTM difference between the risk-free and risky prices. (Schweser zero-coupon example: risk-free 91.51 − CVA 2.15 = risky 89.36.) POD each year = hazard rate × prior-year probability of survival; LGD = exposure × (1 − recovery).
Related: [[Credit_Default_Swaps]]
