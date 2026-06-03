---
aliases: [Credit Default Swaps, CDS, Single-Name CDS, Index CDS, CDS Basis, Credit Curve Trades]
tags: [CFA-L2, fi, concept, credit, derivatives]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 27, LOS 27.a-27.e
---

# Credit Default Swaps (CDS)

## Structure (27.a)
- A CDS is insurance against credit loss: the **protection buyer pays a periodic premium** (the CDS
  coupon, standardized at 1% for IG / 5% for HY) and **receives a payout if a credit event occurs**.
- **Single-name CDS**: one reference entity/obligation; the **cheapest-to-deliver** obligation sets
  recovery. **Index CDS** (e.g., CDX, iTraxx): a basket of reference entities; lets you trade broad
  credit exposure.
- Notional, tenor, coupon, and reference obligation define the contract.

## Credit Events & Settlement (27.b)
- **Credit events**: bankruptcy, failure to pay, restructuring (restructuring not always included, esp.
  US HY). Determined by an ISDA **Determinations Committee**.
- **Settlement**: **cash** (pay loss = notional × (1 − recovery)) or **physical** (deliver bond for par).
- **Payout** ≈ `notional × (1 − recovery rate) = notional × LGD`. Recovery is set by the **cheapest-to-
  deliver** obligation (lowest post-default price).
  - **Worked example (Schweser):** $10m notional **senior** CDS on Alpha. Post-default prices: a
    *subordinated* debenture 15%, a *senior* bond 25%, another *senior* bond 30%. The buyer delivers the
    **cheapest-to-deliver among eligible (senior/pari passu) obligations** = the 25% senior bond (the 15%
    subordinated bond is not deliverable into a senior CDS) → payout = `$10m × (1 − 0.25) = $7.5m`.

## Pricing (27.c)
- **Upfront premium** ≈ `(CDS spread − CDS coupon) × effective duration` (PV of the spread-coupon
  difference).
- **CDS price (per 100)** ≈ `100 − upfront%`, where `upfront% ≈ (spread − coupon) × duration`.
  - If spread > coupon → protection buyer pays upfront; if spread < coupon → seller pays upfront.
- **Change in value** ≈ `Δspread × effective duration × notional` (gain to the protection buyer when
  spreads widen).
- Spread driven by **POD** and **LGD** (hazard rate × loss).

## Uses (27.d, 27.e)
- **Hedge / manage exposure**: buy protection to reduce credit risk; sell protection to add it.
- **Express views**: buy protection if you expect credit deterioration (spread widening); sell if you
  expect improvement.
- **Curve trades**: long/short CDS of different maturities to bet on the **shape** of the credit curve
  (e.g., curve steepener/flattener).
- **Basis trades**: exploit the **CDS-bond basis** = CDS spread − bond (cash) spread. Negative basis →
  buy the bond and buy protection for a near-riskless pickup; convergence trades across markets.

## Exam Traps
- **Payout = notional × (1 − recovery)** = notional × LGD.
- Upfront ≈ **(spread − coupon) × duration**; buyer pays when spread > coupon.
- Protection **buyer profits when spreads widen** (credit worsens).
- Index CDS for macro credit views; single-name for issuer-specific; basis trades exploit CDS vs cash bond.

## Q&A

### 2026-06-03 — CDS upfront premium and mark-to-market
**Q:** A 5-yr CDS has a spread of 5% but a standard coupon of 1%, effective duration ~4. Who pays upfront and how much? If the spread later widens 1%, who gains?
**A:** `Upfront% ≈ (spread − coupon) × duration = (5% − 1%) × 4 = 16%`. Since spread > coupon, the
**protection buyer pays ~16% of notional upfront** (the 1% running coupon under-compensates the seller).
CDS price per 100 ≈ 100 − 16 = 84. Mark-to-market: `ΔValue ≈ Δspread × duration × notional`; a **1%
widening** → the **protection buyer gains** ≈ 1% × 4 = ~4% of notional (credit worsened, protection more
valuable).
Related: [[Credit_Analysis_Models]]

### 2026-06-03 — Cheapest-to-deliver and the CDS payout
**Q:** A $10m senior CDS triggers. Post-default prices: subordinated bond 15, senior bonds 25 and 30. What's the payout?
**A:** Payout = `notional × (1 − recovery)`, and recovery is set by the **cheapest-to-deliver among
eligible (pari passu) obligations**. A **senior** CDS can only deliver senior/pari-passu debt, so the 15
subordinated bond is **not** eligible — the cheapest *senior* obligation is the 25 bond. Payout = `$10m ×
(1 − 0.25) = $7.5m`. Trap: don't grab the absolute-cheapest (15) obligation if its seniority doesn't match
the CDS.
Related: [[Credit_Analysis_Models]]
