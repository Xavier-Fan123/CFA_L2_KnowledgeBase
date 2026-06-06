---
aliases: [GIPS, Global Investment Performance Standards, Composites, GIPS Compliance]
tags: [CFA-L2, ethics, concept, gips]
date: 2026-06-03
status: evergreen
source: Referenced in Official 2026 L2 V10, Standard III(D) Performance Presentation; GIPS Standards for Firms. (No standalone GIPS reading in the 2026 L2 curriculum — see scope note.)
---

# Global Investment Performance Standards (GIPS)

> **Scope note (verified 2026):** The 2026 Level II curriculum does **not** contain a dedicated, standalone GIPS reading. GIPS appears at L2 only as a **reference within Standard III(D) Performance Presentation** — "complying with the GIPS standards is the **best method** to meet obligations under III(D)," and members should **encourage their firms** to adopt GIPS. This note retains the core GIPS framework for review; the deeper mechanics below the "Selected Requirements" heading are **background/foundational knowledge** (from prior curricula and the GIPS Standards for Firms), not text tested verbatim in the current L2 readings.

## Link to Standard III(D) Performance Presentation
Under **III(D)**, performance communications must be **fair, accurate, and complete**. The curriculum gives two ways to comply: (1) **apply the GIPS standards** (the best method); or (2) comply **without** GIPS by — considering the audience's sophistication, presenting a **weighted composite** of similar portfolios (not a single representative account), **including terminated accounts** with their termination dates, making full disclosures (e.g., gross/net of fees, simulated/model results, prior-entity record), and maintaining supporting data/records.
**Trap:** falsely claiming GIPS compliance is itself a **III(D)** violation even if the underlying numbers are fine (official Example: a firm whose composites are **not asset-weighted** cannot claim GIPS compliance).

## Purpose & Key Principles
- GIPS are **voluntary, ethical standards** for **fair representation and full disclosure** of investment performance — so prospective clients can compare firms on a consistent basis.
- Address two abuses: **representative-account** cherry-picking and **survivorship bias**.
- Compliance is **firm-wide**, not per product/composite. A "**firm**" must be defined as a distinct business entity. Firms either comply **fully or not at all** — no partial compliance claims.

## Composites
- A **composite** = an aggregation of **all** actual fee-paying, **discretionary** portfolios managed to a similar **strategy/mandate**. Including all such portfolios prevents cherry-picking.
- Portfolios must be included **on a timely, consistent** basis; the firm must list and describe all composites (and provide any on request).

## Selected Requirements
- Use **fair value**; **time-weighted returns** (specified rules); **actual** trading costs deducted.
- Present a **minimum of 5 years** of compliant history (then build to **10 years**).
- Disclosures: definition of the firm, benchmark, fees, dispersion, leverage/derivatives use, etc.
- Cannot say "GIPS-compliant" unless the **whole firm** complies; verification (by a third party) is **recommended but not required**.

## Structure (9 Sections)
Fundamentals of compliance, input data, calculation methodology, composite construction, disclosure, presentation & reporting, real estate, private equity, wrap-fee/SMA.

## Worked Example — Asset-Weighted Composite Return
*(My own worked illustration of the standard GIPS calculation method — for review; not verbatim curriculum text.)*

A composite holds three portfolios at the **start of the period** (use beginning-of-period values to weight):

| Portfolio | Beginning value | Period return |
|-----------|-----------------|---------------|
| A | $40m | +10% |
| B | $35m | +6% |
| C | $25m | −2% |

**Step 1 — weights** (beginning value ÷ total $100m): A = 0.40, B = 0.35, C = 0.25.
**Step 2 — asset-weighted composite return** = Σ(weight × return) = 0.40(10%) + 0.35(6%) + 0.25(−2%) = 4.00% + 2.10% − 0.50% = **5.60%**.

Why **asset-weighted, not a simple average**: the simple mean would be (10+6−2)/3 = **4.67%**, which overstates the small, poorly performing account and understates the large winner. GIPS requires the composite to reflect the **actual dollars** invested, so a single representative or equal-weighted figure is **not** GIPS-compliant — this is exactly the III(D) trap where a firm claims compliance but did **not** asset-weight the composite. *(For accounts with large mid-period external cash flows, GIPS requires return calculation methods that adjust for the timing of those flows — e.g., time-weighting with revaluation at the flow date — but the asset-weighting of portfolios within the composite still uses beginning-of-period values, or beginning value plus weighted external cash flows under the more precise method.)*

## Exam Traps
- GIPS compliance is **firm-wide and all-or-nothing** — no partial/composite-only claims.
- A composite must include **all** discretionary, fee-paying portfolios of that strategy (anti-cherry-picking).
- **Third-party verification is recommended, not required**, and applies firm-wide (not to a single composite).
- Minimum initial presentation: **5 years** of compliant performance.

## Q&A

### 2026-06-03 — Why must a composite include ALL discretionary portfolios?
**Q:** What is a GIPS composite, and what abuse does the "include all" rule prevent?
**A:** A **composite** aggregates **all** actual, **fee-paying, discretionary** portfolios managed to a similar **strategy/mandate**, added on a timely and consistent basis. Requiring **all** such portfolios (not a hand-picked subset) blocks **representative-account cherry-picking** — a firm can't showcase only its best account. Combined with reporting terminated portfolios for the period they were managed, GIPS also defeats **survivorship bias**. Non-discretionary and non-fee-paying portfolios are excluded.
Related: [[Code_and_Standards]]

### 2026-06-03 — Firm-wide, all-or-nothing, and verification
**Q:** Can a firm claim GIPS compliance for just one composite, and is verification required?
**A:** No — GIPS compliance is **firm-wide and all-or-nothing**: the **whole firm** (defined as a distinct business entity) either complies or it can't claim compliance at all; there is no partial or composite-only claim. **Third-party verification is recommended but not required**, and when done it applies to the **whole firm**, not a single composite. A compliant presentation must show a **minimum of 5 years** of history, building toward 10. Returns are **time-weighted** using **fair value** and net of **actual** trading costs.
Related: [[Code_and_Standards]]

### 2026-06-04 — Worked: compute an asset-weighted composite return (and the III(D) trap)
**Q:** A composite has three portfolios with beginning values $40m/$35m/$25m and period returns +10%/+6%/−2%. What is the GIPS composite return, and why can't the firm just average the three returns?
**A:** Asset-weight by **beginning-of-period** values (weights 0.40/0.35/0.25): 0.40(10%) + 0.35(6%) + 0.25(−2%) = 4.00% + 2.10% − 0.50% = **5.60%**. A simple average would be (10+6−2)/3 = **4.67%**, which misrepresents the composite because it ignores that most of the money was in the +10% account and overweights the small −2% account. GIPS requires composites to reflect the **actual dollars invested**, so an equal-weighted or single representative-account figure is **not** GIPS-compliant. This is the classic **Standard III(D)** trap (official Example): a firm "claims compliance with the GIPS standards" but the composites are **not asset-weighted** — the violation comes from the **false compliance claim**, not from any misuse of the underlying data.
Related: [[Code_and_Standards]]
