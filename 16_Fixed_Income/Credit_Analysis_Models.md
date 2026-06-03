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
- **Probability of default (POD)**: likelihood of default in a period; **hazard rate** = conditional
  default probability.
- **Credit valuation adjustment (CVA)** = PV of **expected loss** = Σ (PV of each period's expected
  loss) = sum over time of `PV[ POD × LGD ]`.
- **Credit spread ≈ CVA** spread; `value of risky bond = value of risk-free bond − CVA`.
- **Worked example (Schweser):** 3-yr, $100 par, **zero-coupon**, hazard rate 2%/yr, recovery 60%
  (LGD = 40% of exposure), benchmark flat 3%.
  - Probability of survival: Yr1 0.98, Yr2 0.9604, Yr3 0.9412; **PD**: Yr1 2%, Yr2 1.96%, Yr3 1.9208%
    (PD = hazard rate × prior-year PS).
  - Exposure: Yr3 $100, Yr2 100/1.03, Yr1 100/1.03²; expected loss = LGD × PD each year.
  - **CVA = Σ PV(expected loss) = $2.15**; risk-free value = 100/1.03³ = $91.51 → **risky value =
    91.51 − 2.15 = $89.36**. The credit spread is the YTM gap between the two.

## Credit Scores vs Ratings (26.b)
- **Credit scores**: for retail/small borrowers (e.g., FICO).
- **Credit ratings**: for corporate/sovereign issues (agency letter grades); **issuer** vs **issue**
  ratings; subject to stability ("through-the-cycle") and potential lag, and notching.

## Return Given Rating Transition (26.c)
- Use a **credit migration (transition) matrix** of probabilities of moving between ratings.
- **Expected % return impact** ≈ `−Σ (migration probability × Δspread × modified duration)` across
  possible new ratings. Downgrades widen spreads → price loss; upgrades the reverse.

## Structural vs Reduced-Form (26.d)
| Model | Idea | Strengths / Weaknesses |
|------|------|------|
| **Structural** (Merton / option-based) | Equity = **call option on firm assets**; default when asset value < debt face. Risky debt = risk-free debt − **put on assets** | Economic intuition; but assets aren't traded/observable, assumes simple capital structure |
| **Reduced-form** | Models **default intensity (hazard rate)** statistically as a function of observable macro/firm variables; no assumption about firm structure | Uses observable data, time-varying POD; but no economic "why," relies on historical estimation (backward-looking) |

## Credit Spread Dynamics (26.e, 26.f, 26.g)
- Spread compensates for **expected loss + risk/liquidity premium**. Spreads **widen** in downturns
  (higher POD, lower RR) and **tighten** in expansions.
- **Term structure of credit spreads**: upward-sloping for healthy issuers; can **invert** for
  distressed issuers (near-term default risk dominates). Drivers: credit cycle, financial conditions,
  issuer fundamentals, supply/demand.

## Securitized Debt (26.h)
Analyze the **collateral pool** (granularity, homogeneity), servicer quality, structure
(tranching/credit enhancement), and cash-flow waterfall — not just a single obligor's balance sheet.

## Exam Traps
- **CVA = PV of expected loss**; risky bond value = risk-free value − CVA.
- **Structural** model: equity is a **call** on assets, risky debt = risk-free − **put** on assets.
- **Reduced-form** models POD/hazard rate from observable variables (no capital-structure assumption);
  it is backward-looking in estimation.
- Distressed issuers can show an **inverted** credit-spread term structure.

## Q&A

### 2026-06-03 — Structural vs reduced-form credit models
**Q:** What's the core idea of each, and the key limitation?
**A:** **Structural (Merton)**: built on the firm's **capital structure** — equity is a **call option on
the firm's assets** (default when assets < debt face at maturity), and risky debt = risk-free debt −
**put on assets**. Limitation: firm assets aren't traded/observable and it assumes a simplistic capital
structure. **Reduced-form**: models the **default intensity (hazard rate)** statistically as a function
of observable macro/firm variables — no capital-structure assumption, allows time-varying POD.
Limitation: no economic "why," and it's **backward-looking** (relies on historical estimation).
Related: [[Credit_Default_Swaps]]

### 2026-06-03 — Computing CVA / the credit spread
**Q:** How does CVA give the value of a risky bond and the credit spread?
**A:** `CVA = Σ PV(expected loss)`, where each period's expected loss = **POD × LGD** on that period's
exposure, discounted at the benchmark rate. Then **risky value = risk-free value − CVA**, and the
**credit spread** is the YTM difference between the risk-free and risky prices. (Schweser zero-coupon
example: risk-free 91.51 − CVA 2.15 = risky 89.36.) POD each year = hazard rate × prior-year probability
of survival; LGD = exposure × (1 − recovery).
Related: [[Credit_Default_Swaps]]
