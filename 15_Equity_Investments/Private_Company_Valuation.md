---
aliases: [Private Company Valuation, DLOM, DLOC, Capitalized Cash Flow, Build-Up Approach, Normalized Earnings]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-08-25
status: evergreen
source: Schweser Book 3, Module 22, LOS 22.a-22.i
---

# Private Company Valuation

## Private vs Public Features (22.a, 22.b)
Private firms differ: less liquidity, fewer disclosures, owner-manager overlap, concentration of control, tax-minimization motives, shorter histories. Uses of valuation: transactions (sale/M&A), compliance (tax, financial reporting), litigation.

## Normalizing Earnings and Forecasting Private-Company FCF (22.c)
Adjust reported earnings to reflect true economics: **non-recurring/unusual items**, **discretionary expenses**, **non-market levels of owner compensation**, **personal expenses charged to the firm**, **real-estate expense based on historical cost**, and **non-market lease rates**. Related-party transactions go to arm's length. Two earnings concepts: a **strategic (synergistic) buyer** normalizes **including acquisition synergies**; a **financial buyer** does not.

**Five issues specific to forecasting private-company free cash flow (22.c)** — commonly tested and easy to omit:
1. Estimates **differ for a controlling vs a non-controlling** interest (a control buyer can change compensation, capital structure, and strategy).
2. Run **several scenarios** of future cash flow rather than one point forecast.
3. Scenarios must reflect the firm's **life-cycle stage**.
4. **Anticipate management bias** — projections usually come from the owner/manager, who is also the seller.
5. Use **FCFF (not FCFE)** when the **capital structure is expected to change**, because FCFE would need a moving required return.

## Discount Rate (22.d, 22.e)
Higher than for comparable public firms (small size, illiquidity, key-person risk).

**Five elements to factor into a private-firm discount rate (22.d)**:
1. **Size premiums** — but beware: premiums derived from **small-cap public** data may embed a **distress** premium that does not apply to a healthy private firm (a double count).
2. **Availability and cost of debt** — a private firm typically cannot borrow **as much or as cheaply**, which raises the WACC.
3. **Acquirer vs target** — use the **target's** WACC, **not the acquirer's**. (Classic trap: the acquirer's lower cost of capital does not make the target's cash flows less risky.)
4. **Projection risk** — less information and reliance on management forecasts make private-company projections riskier.
5. **Life-cycle stage** — an appropriate rate is hardest to pin down for **early-stage** firms.

Models:
- **CAPM**: often inadequate for small private firms (betas from public comps).
- **Expanded CAPM**: CAPM + **size premium** + **company-specific premium**.
- **Build-up approach**: `R_f + ERP + size + industry + company-specific` (no beta) — for private firms lacking comparables. Cost of debt typically higher; WACC reflects higher required returns.

## Three Valuation Approaches (22.g)

| Approach | Methods | Notes |
|------|------|------|
| **Income** | Free cash flow (multistage), **capitalized cash flow (CCM)**, **excess earnings (EEM)** | CCM: `V = FCF1/(r − g)`; EEM for intangible-heavy small firms |
| **Market** | Guideline public companies (GPCM), guideline transactions (GTM), prior transaction method (PTM) | Apply control premium / liquidity discounts as appropriate |
| **Asset-based** | Fair value of assets − liabilities | Floor value; weak for going concerns with intangibles |

## Income Approach: Free Cash Flow, Capitalized Cash Flow & Excess Earnings (22.g, 22.h)
- **CCM (capitalized cash flow)**: single-period flow capitalized at one rate. `V_firm = FCFF1/(WACC − g)` or `V_equity = FCFE1/(r − g)`. The denominator `(r − g)` is the **capitalization rate**. Used for small, stable firms when a full multistage forecast is impractical.
- **Excess Earnings Method (EEM)** — values **intangibles** as the residual after charging tangible assets for their required returns; firm value = FMV of tangible assets + value of intangibles. Steps:
  1. Estimate **normalized earnings**.
  2. Charge each tangible-asset class its required return: `RI = Normalized earnings − (Working capital × r_WC) − (Fixed assets × r_FA)` (working capital is lowest-risk → lowest r; intangibles highest-risk → highest r_RI).
  3. Capitalize the residual (excess earnings) as a growing perpetuity: `Value of intangibles (RV) = RI × (1 + g) / (r_RI − g)`.
  4. `Firm value = FMV of tangible assets + RV`.
  - **Worked example (Digigraf, curriculum):** WC €200,000 (r_WC 5%), fixed assets €800,000 (r_FA 11%), normalized earnings €120,000. `RI = 120,000 − 200,000×5% − 800,000×11% = 120,000 − 10,000 − 88,000 = €22,000`. Then RV = 22,000(1+g)/(r_RI − g); firm value = (200,000 + 800,000) + RV. EEM is used mainly to value **intangibles / very small businesses** when market-approach data are unavailable.

## The Three Market-Approach Methods (22.i)

| Method | Data source | What to watch |
|---|---|---|
| **Guideline public company method (GPCM)** | Price multiples of **traded public** comparables, adjusted for risk differences | **Advantage**: plenty of data. **Drawback**: public firms may not be comparable. To add a **control premium** for a controlling interest, consider the **transaction type, industry conditions, type of consideration (cash vs stock), and reasonableness** |
| **Guideline transactions method (GTM)** | Multiples from **completed sales of whole companies** (public and private) — the premium is already embedded | Consider **transaction type, contingent consideration, type of consideration, data availability, and the date of the data** (stale multiples reflect a different market) |
| **Prior transaction method (PTM)** | **Historical sales of the subject company's own stock** | Best when the data are **recent, arm's-length, and of the same motivation**; weakest when the prior deal was a related-party or differently motivated trade |

## Discounts & Premiums (22.f)
The adjustment depends on **what the benchmark value represents versus what you are valuing**:

| Benchmark value is... | You are valuing... | Adjustment |
|---|---|---|
| Sale of an **entire company** (control) | a **minority** interest | apply a **DLOC** |
| **Public shares / minority** interests | a **controlling** interest | add a **control premium** |
| **Highly marketable** securities (public shares) | an illiquid private interest | apply a **DLOM** |

- **DLOC** (discount for lack of control): `DLOC = 1 − [1 / (1 + control premium)]`; can also be estimated by valuing on **reported** rather than **normalized** earnings (the minority holder cannot capture the normalization).
- **DLOM** (discount for lack of marketability) — **three estimation methods**: (1) **restricted-share prices vs the same issuer's publicly traded shares**; (2) **pre-IPO vs post-IPO** transaction prices; (3) the **price of a put option** on the interest (the cost of buying liquidity). All three are hard to implement in practice.
- **Total discount** = `1 − (1 − DLOC)(1 − DLOM)` (applied multiplicatively, not additively).

## Exam Traps
- **Total discount is multiplicative**: `1 − (1 − DLOC)(1 − DLOM)`, not the simple sum.
- A **minority** interest gets **DLOC**; a **controlling** interest typically does not.
- **Build-up / expanded CAPM** add size and company-specific premiums for private/small firms.
- **Use the TARGET's WACC, not the acquirer's**, when discounting the target's cash flows; and check that a size premium taken from small-cap public data isn't double-counting **distress**.
- Use **FCFF** rather than FCFE whenever the **capital structure is expected to change**.
- **DLOM** has three curriculum estimation routes: **restricted vs public shares**, **pre-IPO vs post-IPO**, and **put prices**.
- Market approach has **three** methods — GPCM, GTM, and **PTM** (the subject company's own prior stock sales). GTM multiples already embed a control premium; **GPCM multiples do not**.
- CCM uses a **single** capitalization rate (r − g) on normalized cash flow.
- **EEM** charges tangible assets (WC, fixed) their required returns first; the leftover (**excess earnings**) is the intangibles' RI, capitalized at `RI(1+g)/(r_RI − g)`. Firm value adds back **FMV of tangible assets**. Don't forget the tangible-asset value — EEM alone prices only the intangibles.

## Q&A

### 2026-06-03 — Combining DLOC and DLOM (worked)
**Q:** A 10% stake warrants a 15% DLOC and a 20% DLOM. What's the total discount, and why not 35%?
**A:** Discounts are **multiplicative**, not additive: `total = 1 − (1 − DLOC)(1 − DLOM) = 1 − (0.85)(0.80) = 1 − 0.68 = 32%`. They stack on a shrinking base, so the combined discount (32%) is less than the simple sum (35%). DLOC applies because a **minority** stake lacks control; DLOM because a private interest is illiquid. A controlling, marketable interest would get neither.
Related: [[Market_Based_Valuation]]

### 2026-06-03 — Which discount rate model for a small private firm?
**Q:** Why is CAPM often inadequate for private companies, and what's used instead?
**A:** CAPM relies on a market beta and assumes a diversified investor; small private firms have no traded beta, key-person and liquidity risk, and often undiversified owners. Use the **expanded CAPM** (CAPM + size premium + company-specific premium) or the **build-up approach** (`R_f + ERP + size + industry + company-specific`, no beta). Both raise the required return above a comparable public firm's. The **capitalized cash flow method** then applies a single rate: `V = FCF1/(r − g)`.
Related: [[Cost_of_Capital]]

### 2026-06-04 — Excess Earnings Method worked example
**Q:** A small firm has working capital $200k (required return 5%), fixed assets $800k (11%), and normalized earnings $120k. How does the EEM value it?
**A:** EEM isolates the **intangibles'** value. Charge the tangible assets first: `RI = 120,000 − (200,000×5%) − (800,000×11%) = 120,000 − 10,000 − 88,000 = $22,000` of excess earnings. Capitalize it as a growing perpetuity at the (high) intangibles rate: `RV = 22,000(1+g)/(r_RI − g)`. Then `firm value = FMV of tangible assets ($1,000,000) + RV`. EEM is used for intangible-heavy or very small firms when guideline market data are unavailable. Trap: remember to **add back the tangible-asset FMV** — the residual income only values the intangibles.
Related: [[Residual_Income]]
