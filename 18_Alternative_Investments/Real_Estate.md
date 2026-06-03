---
aliases: [Real Estate, Private Real Estate, REITs, Cap Rate, NOI, NAVPS, FFO, AFFO]
tags: [CFA-L2, alt, concept, real-estate]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Modules 31-32, LOS 31.a-31.e, 32.a-32.d
---

# Real Estate Investments (Private + Publicly Traded)

## Private Real Estate Features (31.a, 31.b, 31.c)
- Characteristics: **heterogeneity**, illiquidity, high unit cost, high transaction costs, **appraisal-
  based** (lagged/smoothed) values, active management. Roles: income, diversification, inflation hedge.
- Property types: **office, retail, industrial/warehouse, multifamily (residential), hospitality** —
  differ in lease structure, cyclicality, and tenant risk.

## Valuation Approaches (31.d)
| Approach | Method |
|------|------|
| **Income** | **Direct capitalization**: `Value = NOI_year1 / cap rate`; or **DCF** of NOI + reversion |
| **Cost** | Replacement cost of improvements + land − depreciation (floor; for unusual properties) |
| **Sales comparison** | Adjust recent comparable sale prices for differences |

- **NOI** = rental income − vacancy/collection loss − operating expenses (before financing & taxes).
- **Cap rate** = `discount rate − growth rate` = `NOI / value`. Use **stabilized/normalized NOI** if
  current NOI is temporarily distorted (e.g., renovation).
- **Gross income multiplier** = price / gross income (crude).
- **Worked example (Schweser – max loan / returns):** property appraised $1,200,000, NOI $135,000,
  10% interest-only loan, max LTV 80%, min DSCR 1.5.
  - LTV constraint: `1,200,000 × 80% = $960,000`. DSCR constraint: max debt service = `135,000/1.5 =
    $90,000` → loan = `90,000/0.10 = $900,000`. **Max loan = lower = $900,000** (LTV then 75%).
  - With $300,000 equity: first-year cash flow = `135,000 − 90,000 = 45,000` → **equity dividend rate =
    45,000/300,000 = 15%**. With $300k land, 30-yr SL depreciation, 20% tax: depreciation $30,000, tax =
    `0.20 × (135,000 − 90,000 − 30,000) = 3,000` → **after-tax return = (45,000 − 3,000)/300,000 = 14%**.

## Indexes (31.e)
- **Appraisal-based** indexes (e.g., NCREIF): smoothed, **understate volatility** and lag the market.
- **Transaction-based** indexes: use actual sales, higher (truer) volatility but noisier.
- **REIT indexes**: real-time but carry equity-market characteristics.

## Publicly Traded Real Estate / REITs (32.a-32.d)
- Types: **REITs** (own income property; must distribute most income → little corporate tax),
  **REOCs**, mortgage REITs.
- **Valuation methods**:
  1. **Net asset value per share (NAVPS)**: capitalize first-year cash NOI at a market cap rate →
     property value, add other tangible assets, subtract liabilities, ÷ shares. The most fundamental
     REIT measure (**superior to BVPS**, which uses depreciated historical cost); market price can trade
     at a **premium/discount to NAV** reflecting management, leverage, and governance views.
  2. **Relative value**: **price-to-FFO** and **price-to-AFFO** multiples.
  3. **DCF / dividend discount** of expected distributions.
- **FFO (funds from operations)** = net income + **depreciation** + deferred taxes − **gains on property
  sales** (+ losses). Adds back non-cash depreciation that GAAP overstates for real estate.
- **AFFO (adjusted FFO)** = FFO − **recurring maintenance capex** − straight-line rent adjustments.
  AFFO is a better economic (cash) measure than FFO.

## Exam Traps
- **Direct cap: value = year-1 NOI / cap rate**; cap rate = discount rate − growth.
- **FFO adds back depreciation and removes gains on sales**; AFFO further subtracts maintenance capex.
- Appraisal-based indexes **understate volatility** and lag; transaction-based are more volatile.
- NOI is **before** financing costs and taxes.

## Q&A

### 2026-06-03 — Sizing a real-estate loan: LTV vs DSCR
**Q:** Property value $1.2m, NOI $135k, 10% interest-only, max LTV 80%, min DSCR 1.5. What's the max loan?
**A:** Compute both constraints and take the **lower**. **LTV:** 1.2m × 80% = $960k. **DSCR:** max debt
service = NOI/DSCR = 135,000/1.5 = $90,000; at 10% interest-only that's a loan of 90,000/0.10 = **$900k**.
Binding = the smaller, so **max loan = $900k** (implied LTV 75%). With $300k equity, first-year equity
dividend rate = (135,000 − 90,000)/300,000 = **15%**.
Related: [[Private_Company_Valuation]]

### 2026-06-03 — FFO vs AFFO, and why NAVPS beats BVPS for a REIT
**Q:** Why do REIT analysts use FFO/AFFO and NAVPS instead of net income and book value?
**A:** GAAP depreciates real estate even though property often appreciates, so net income and depreciated
**book value** understate economic value. **FFO = NI + depreciation + deferred tax − gains on property
sales** strips out that non-cash/one-off noise; **AFFO = FFO − recurring maintenance capex − straight-line
rent adjustments** is the better **cash** measure. **NAVPS** marks the property to market (capitalize
year-1 NOI at a market cap rate, add other assets, subtract liabilities, ÷ shares), so it reflects current
value far better than depreciated-cost BVPS; the stock can trade at a premium/discount to NAV.
Related: [[Market_Based_Valuation]]
