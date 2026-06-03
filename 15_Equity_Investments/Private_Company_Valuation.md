---
aliases: [Private Company Valuation, DLOM, DLOC, Capitalized Cash Flow, Build-Up Approach, Normalized Earnings]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 3, Module 22, LOS 22.a-22.g
---

# Private Company Valuation

## Private vs Public Features (22.a, 22.b)
Private firms differ: less liquidity, fewer disclosures, owner-manager overlap, concentration of
control, tax-minimization motives, shorter histories. Uses of valuation: transactions (sale/M&A),
compliance (tax, financial reporting), litigation.

## Normalizing Earnings (22.c)
Adjust reported earnings to reflect true economics: **owner compensation** to market levels,
**related-party** transactions to arm's length, **personal/non-business expenses** removed, **one-time**
items, real-estate/rent adjustments. Two earnings concepts: with strategic (synergistic) buyer vs
financial buyer.

## Discount Rate (22.d, 22.e)
Higher than for comparable public firms (small size, illiquidity, key-person risk). Models:
- **CAPM**: often inadequate for small private firms (betas from public comps).
- **Expanded CAPM**: CAPM + **size premium** + **company-specific premium**.
- **Build-up approach**: `R_f + ERP + size + industry + company-specific` (no beta) — for private firms
  lacking comparables. Cost of debt typically higher; WACC reflects higher required returns.

## Three Valuation Approaches (22.g)
| Approach | Methods | Notes |
|------|------|------|
| **Income** | Free cash flow (multistage), **capitalized cash flow (CCM)**, excess earnings | CCM: `V = FCF1/(r − g)`; excess earnings for intangible-heavy small firms |
| **Market** | Guideline public companies (GPCM), guideline transactions (GTM), prior transactions | Apply control premium / liquidity discounts as appropriate |
| **Asset-based** | Fair value of assets − liabilities | Floor value; weak for going concerns with intangibles |

## Discounts & Premiums (22.f)
- **DLOC** (discount for lack of control): applied when valuing a **non-controlling** interest; related
  to the control premium: `DLOC = 1 − [1 / (1 + control premium)]`.
- **DLOM** (discount for lack of marketability): for illiquid (private) interests.
- **Total discount** = `1 − (1 − DLOC)(1 − DLOM)` (applied multiplicatively, not additively).

## Exam Traps
- **Total discount is multiplicative**: `1 − (1 − DLOC)(1 − DLOM)`, not the simple sum.
- A **minority** interest gets **DLOC**; a **controlling** interest typically does not.
- **Build-up / expanded CAPM** add size and company-specific premiums for private/small firms.
- CCM uses a **single** capitalization rate (r − g) on normalized cash flow.

## Q&A

### 2026-06-03 — Combining DLOC and DLOM (worked)
**Q:** A 10% stake warrants a 15% DLOC and a 20% DLOM. What's the total discount, and why not 35%?
**A:** Discounts are **multiplicative**, not additive: `total = 1 − (1 − DLOC)(1 − DLOM) = 1 −
(0.85)(0.80) = 1 − 0.68 = 32%`. They stack on a shrinking base, so the combined discount (32%) is less
than the simple sum (35%). DLOC applies because a **minority** stake lacks control; DLOM because a private
interest is illiquid. A controlling, marketable interest would get neither.
Related: [[Market_Based_Valuation]]

### 2026-06-03 — Which discount rate model for a small private firm?
**Q:** Why is CAPM often inadequate for private companies, and what's used instead?
**A:** CAPM relies on a market beta and assumes a diversified investor; small private firms have no traded
beta, key-person and liquidity risk, and often undiversified owners. Use the **expanded CAPM** (CAPM +
size premium + company-specific premium) or the **build-up approach** (`R_f + ERP + size + industry +
company-specific`, no beta). Both raise the required return above a comparable public firm's. The
**capitalized cash flow method** then applies a single rate: `V = FCF1/(r − g)`.
Related: [[Cost_of_Capital]]
