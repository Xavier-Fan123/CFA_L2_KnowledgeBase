---
aliases: [Real Estate, Private Real Estate, Direct Real Estate, Overview of Types of Real Estate Investment, NOI, Cap Rate, Direct Capitalization, Equity Dividend Rate, Real Estate Cycle, Appraisal-Based Index, Transaction-Based Index, GPRI]
tags: [CFA-L2, alt, concept, real-estate]
date: 2026-06-03
status: evergreen
source: Official Curriculum 2026 L2 Vol 8, Learning Module 2 (Overview of Types of Real Estate Investment), LOS 31.a-31.e; Schweser Book 4
---

# Overview of Types of Real Estate Investment (Private / Direct)

> Official **Learning Module 2** of the Alternatives volume. This is the **private / direct, income-producing real estate** reading: investment features for valuation, economic value drivers + portfolio role, commercial property types, due diligence, the three valuation approaches, and real estate indexes. Publicly traded vehicles (REITs/REOCs) are in the companion note [[Publicly_Traded_Real_Estate]] (LM3).

## 1. Real Estate Investment Features for Valuation (31.a)

Real estate value derives from **current and potential economic uses**, expected **net cash flows**, and **capital structure**. Unique per-property features: **location, size, age, amenities**. Demand drivers: household formation, employment, income/wealth, cost/availability of owner-occupied alternatives (residential); business conditions, industry dynamics, technological/environmental/social change (commercial).

### Net Operating Income (NOI) — the core income measure
NOI is computed **before financing costs and income taxes** (analogous to EBITDA / unlevered income):

`NOI = Effective gross income − Operating expenses − Property maintenance allowance`

- **Effective gross income** = gross rent + other revenue + expense recoveries/pass-throughs − vacancy/collection loss − concessions.
- **Operating expenses** = fixed (taxes, insurance, service, repairs) + variable (utilities); may be owner-borne or passed through to tenants.
- **Property maintenance allowance** = capex needed to **maintain** current economic use (NOT upgrades that change/enhance the use). Common in North America/Europe, less so in e.g. Japan.

**Worked example — Wallonia Transit warehouse (official LM2 Example 1):** 10,000 m² single-tenant warehouse, base rent EUR52.50/m², operating-expense recovery EUR10.25/m², tenant pays property tax (EUR12,500) + insurance (EUR40,000); servicing/repairs EUR120,750; maintenance allowance EUR100,000.
- Gross rent = 52.50 × 10,000 = **EUR525,000**; expense recovery = 10.25 × 10,000 = EUR102,500.
- Effective gross income = 525,000 + 102,500 + 12,500 (tax pass-through) + 40,000 (insurance) = **EUR680,000**.
- Operating expenses = 120,750 + 12,500 + 40,000 = **EUR173,250**.
- **NOI = 680,000 − 173,250 − 100,000 = EUR406,750.**
- *Trap (recovery cap):* if servicing/repairs rise 20% (to EUR144,900), recovery is **capped** at EUR102,500, so the full EUR24,150 increase hits NOI → NOI falls to **EUR382,600**.

### Leverage and coverage measures

| Measure | Formula | Note |
|---|---|---|
| **Loan-to-value (LTV)** | Mortgage debt outstanding / Current property value | Falls as value rises or principal amortizes; lower LTV = more equity |
| **Debt service coverage (DSC)** | NOI / Debt service | Debt service = interest **+** principal; higher is safer |
| **Equity dividend rate** (cash-on-cash) | Pre-tax cash flow / Equity | First-year levered cash return, ignores taxes & capital gains |
| **Pre-tax cash flow** | NOI − Debt service | — |

**Worked example (Wallonia, official Examples 2–3):** purchase EUR3,750,000 with a EUR3,000,000 20-yr fully amortizing 4% mortgage; annual payment EUR220,745 (Yr-1 interest = 3,000,000 × 4% = EUR120,000; principal = 220,745 − 120,000 = EUR100,745).
- End-Yr-1 debt outstanding = 3,000,000 − 100,745 = EUR2,899,255 → **LTV = 2,899,255 / 3,750,000 = 0.773**. If value rises 10% to EUR4,125,000 → LTV falls to 0.703 (less leverage).
- **DSC = 406,750 / 220,745 = 1.84** (falls to 1.73 if NOI drops to EUR382,600).
- Equity = 3,750,000 − 3,000,000 = EUR750,000; pre-tax CF = 406,750 − 220,745 = EUR186,005 → **equity dividend rate = 186,005 / 750,000 = 24.8%** (falls to 21.6% at the lower NOI).

**Depreciation:** computed on the **depreciable base** = construction/acquisition cost + improvements; **land is excluded** (assumed infinite life). Periods vary by jurisdiction/property type.

## 2. Economic Value Drivers & Portfolio Role (31.b)

**Macro value drivers** (positive across the whole sector): **GDP growth, job creation, wage growth**, positive **demographics**/consumer confidence, **interest rates / credit cycle** (RE is highly debt-financed → very rate-sensitive). Higher production → demand for industrial/office/retail; income + demographics → household formation → housing demand. Because of long build times, the initial response to demand is **rising rents + falling vacancy**, then a **slow supply increase**.

### The Real Estate Cycle — four phases

- **Recovery**: business-cycle trough; little/no new construction; weak occupancy.
  - Interest rates: bottoming, begin to rise. NOI: bottoming. DSC: bottoming. LTV: peaks, begins to fall.
- **Expansion**: growth + easing credit; occupancy & rents rise; new construction starts.
  - Interest rates: rising. NOI: rising. DSC: increasing. LTV: decreasing.
- **Oversupply**: pipeline completes into softening demand → glut; occupancy & rents fall.
  - Interest rates: peak, begin to fall. NOI: peaks, begins to fall. DSC: peaks, begins to fall. LTV: bottoms, begins to rise.
- **Recession**: slowdown + tight credit; supply overhang; landlords give concessions.
  - Interest rates: low. NOI: falling. DSC: decreasing. LTV: increasing.

*Mnemonic:* across **Expansion**, the healthy direction is **NOI↑, DSC↑, LTV↓**. New supply lags, so it often arrives **after** conditions have already turned (classic boom-bust amplifier). Local factors (employers, infrastructure, zoning/tax, schools/safety) modify the macro cycle per property.

### Portfolio characteristics & lease economics
Return = **periodic income** (bond-like leases) + **capital appreciation** (equity-like, often development). Roles: current income, capital appreciation, **inflation hedge**, **diversification**, **tax benefits**. Lease structures that shape income:
- **Step-up clause** — pre-specified (non-contingent) future rent increases.
- **Indexed rent** — rent tied to an observed variable (e.g., CPI).
- **Sales-based / overage rent** — extra rent when a retailer's sales exceed a breakeven (e.g., Chandra Shops: base cut 10% but +8% overage on sales above INR1,000,000).
- **Rollover risk** — when holding period > lease term, owner may lose the tenant and forgo income.

## 3. Commercial Property Types (31.c)

- **Residential (multi-family)**: personal income, job growth, affordability of owner-occupied alternatives; **shorter leases**, tenant protections (rent/eviction limits); cash flow often modeled from **GPRI**.
- **Office**: service-industry employment; often built for anchor tenants; **remote/hybrid work** cut demand post-COVID.
- **Industrial / warehouse**: production & distribution; **e-commerce** structurally boosted warehouse demand; special-use ones hard to convert.
- **Retail**: consumer spending; regional malls vs neighborhood centers; pressured by online shopping; often **overage rent** leases.
- **Hospitality**: highly cyclical / economically sensitive; effectively **daily leases** (room rates) → most volatile cash flows.

**Gross potential rental income (GPRI)** = Market rent × Rentable space (residential cash-flow start).
**Worked example — Pinebranch (official Example 6):** 240 units × 1,200 ft² × AUD2.00/ft²/mo × 12 = **GPRI AUD6,912,000**; NOI = GPRI + other income − rental deductions (loss-to-lease, vacancy, concessions) − expenses = **AUD2,919,651**. *Key contrast:* multi-tenant Pinebranch absorbs taxes/ insurance and bleeds on **rental deductions**, whereas single-tenant Wallonia **passed those through**.

## 4. Due Diligence & Valuation Approaches (31.d)

### Due diligence — 7 elements
1. **Market review & outlook** — current prices, supply/demand; prefer **actual sale prices** over offers.
2. **Current lease review** — in-place rents vs market, vacancies, lease length, payment history (tenant credit).
3. **Future lease outlook** — renewal/re-lease costs (free rent, TI allowances, broker commissions, downtime); these are **capitalized & amortized**, not in annual operating income.
4. **Financial review** — several years of audited statements; detect **inflated NOI** (under-maintenance, overstated occupancy/rent via incentives).
5. **Documentation review** — legal/tax: clear title, no liens, zoning & environmental compliance.
6. **Property inspection & service agreements** — survey + physical/engineering/environmental inspection; assess property manager.
7. (Discrepancies → **remediation or price adjustment**.)

### Valuation approaches
**(A) Income approach** — the DCF analogue; primary for income property.
- **Direct capitalization** (single-year NOI as a perpetuity): `Property value = NOI / Cap rate`  (where `Cap rate = r − g`) *Worked (Wallonia Example 8):* NOI EUR406,750, r = 12.5%, g = 2% → value = 406,750 / (0.125 − 0.02) = **EUR3,873,810** (falls ~6% to EUR3,643,810 if NOI = EUR382,600). Use **stabilized/normalized NOI** in the numerator if current NOI is distorted.
- **Cap rate interpretation:** Cap rate = NOI / value (akin to a bond's current yield or the inverse of EV/EBITDA). Curriculum also calls it the property's **current yield**, i.e. the **income return** component of an index return (the remainder being capital return). Its **reciprocal is a valuation multiple** — an 8% cap rate = paying **12.5× NOI**. **Going-in cap rate** = based on first-year income at purchase; **terminal cap rate** = based on income after the assumed future sale. g < 0 ⇒ property nearing end of useful life.
- **Two ways to obtain a cap rate — both testable:**
  1. **Market-derived from comparables:** `cap rate = NOI_comp / sale price_comp`, then apply to the subject. *Curriculum quiz:* comp sold for $2,500,000 with NOI $200,000 → cap rate **8%**; subject NOI $130,000 → value = 130,000/0.08 = **$1,625,000**.
  2. **From fundamentals:** `cap rate = r − g` (Gordon Growth rearranged, with NOI replacing dividends).
- **⚠️ Cap rate ≠ discount rate** (curriculum states this explicitly): the discount rate `r` is the **required return** = risk-free + risk premium; the cap rate is an **income yield** = `r − g`, applied to a **single year's** NOI. With `g > 0` the **cap rate is strictly lower than the discount rate**; they coincide only when `g = 0`. Useful inversion: **`g = r − cap rate`** backs out the growth the market is pricing.
- **Stabilized NOI — TWO steps, not one.** If first-year NOI is temporarily distorted (e.g. vacancy during renovation): ① recompute NOI **as if the disruption were over** and capitalize that **stabilized/normalized NOI**; ② **subtract the value lost from the temporary NOI decline**. Capitalizing stabilized NOI alone **overstates** value.
- **DCF method** (multi-year projections + terminal value): `Value = Σ[NOIₜ / (1+r)^t] + Terminal value / (1+r)^n`,  where `Terminal value = NOIₙ(1+g) / (r − g)`

**(B) Cost approach** — replacement cost of land + improvements − depreciation; sets a value **floor** (an investor "should not pay more than the cost to build a comparable"). *Worked (Wallonia Example 10):* cost estimate EUR4,350,000; depreciable base = 4,350,000 − 750,000 (land) = EUR3,600,000; SL over 30 yrs = EUR120,000/yr; 4 years old → less EUR480,000 → **EUR3,870,000**. During **oversupply**, replacement cost typically **exceeds** market price.

**(C) Sales comparison (market) approach** — adjust recent comparable sale prices for differences (size, age, location, condition, **timing of sale**). Most common unit = **price per square foot/meter**. Recent sales weighted more; valid only with enough comparable transactions.

> **Gross income multiplier (GIM)** = Sale price / Gross income — a crude relative-value shortcut (curriculum / general-knowledge addition for completeness; not a primary LM2 method).

## 5. Real Estate Indexes (31.e)

- **Appraisal-based** (e.g., NCREIF, GREFI via NCREIF/INREV/ANREV): periodic professional **appraisals** of portfolio properties.
  - Bias / property: **appraisal lag** → **smoothed**, **understates volatility**, **lowers correlation** with other assets, **overstates Sharpe** → **overstates** the appropriate RE allocation.
- **Transaction-based**: actual sales via econometrics: **repeat-sales** (same property sold ≥ twice) or **hedonic** (regress price on characteristics — size/age/quality/location).
  - Bias / property: truer (higher) volatility but **noisier**; repeat-sales needs frequent trades.
- **REIT / listed**: prices of listed REITs/REOCs.
  - Bias / property: real-time & investable but carries **equity-market** characteristics (high stock correlation).

**Appraisal-based holding-period return** (single-period IRR proxy): `HPR = [NOI − Capital expenditures + (End market value − Begin market value)] / Begin market value` *Worked (Wallonia Example 12):* NOI EUR406,750, capex EUR100,000; begin MV = 3,750,000 × 1.056 = EUR3,960,000; end MV = 3,960,000 × 1.032 = EUR4,086,720 → HPR = (406,750 − 100,000 + 126,720) / 3,960,000 = **10.95%**.

**Adjusting for appraisal lag:** (1) **"unsmooth"** the index via a reverse-AR model $R_t^* = aR_t + (1-a)R_{t-1}^*$ → higher volatility & correlation (more realistic); or (2) use a **transaction-based** index when comparing RE to public assets.

## Exam Traps
- **Direct cap: value = year-1 NOI / cap rate**, and **cap rate = r − g**. Higher r ↓ value; higher g ↓ cap rate ↑ value. **Terminal value uses NOI_n(1+g)/(r−g)** (next-period NOI), not current NOI.
- **Cap rate ≠ discount rate.** `r` = required return (risk-free + risk premium); cap rate = `r − g` and is **lower than r** whenever g > 0. Equal only if g = 0. Invert to read market growth: `g = r − cap rate`.
- **Cap rate and value always move in opposite directions** — "cap rate compression" = falling cap rates = rising prices.
- **Stabilized NOI has a second step**: capitalize the normalized NOI, **then subtract** the value lost to the temporary decline. Skipping step ② overstates value.
- A cap rate can be **backed out of a comparable sale** (`NOI_comp / price_comp`) and applied to the subject — a common quiz format.
- **NOI is before financing and taxes**; **expense recoveries are capped** at the contractual amount — cost overruns above the cap hit NOI fully.
- Over the cycle's **Expansion**, the favorable triad is **NOI↑, DSC↑, LTV↓**. New **supply lags**, so oversupply often appears right as demand softens.
- **DSC uses NOI / total debt service** (interest **+ principal**); **equity dividend rate** = (NOI − debt service) / equity, ignores taxes and capital gains.
- **Cost approach** = floor/replacement value; **land is not depreciated**. In **oversupply**, replacement cost > market price.
- **Appraisal-based indexes understate volatility and lower correlation** (smoothing) → they **overstate** the optimal RE allocation. **Transaction-based** (repeat-sales / hedonic) are truer but noisier.

## Q&A

### 2026-06-03 — Compute NOI, DSC, LTV and equity dividend rate from a pro forma
**Q:** Given effective gross income, operating expenses, a maintenance allowance and an amortizing loan, how do I get NOI, DSC, LTV and the equity dividend rate?
**A:** **NOI = Effective gross income − Operating expenses − Property maintenance allowance** (before financing & taxes). Then **LTV = mortgage outstanding / property value**; **DSC = NOI / debt service** (debt service includes **interest + principal**); **equity dividend rate = (NOI − debt service) / equity**. Using the official Wallonia case: NOI EUR406,750, debt service EUR220,745 → DSC = **1.84**; equity EUR750,000 → equity dividend rate = (406,750 − 220,745)/750,000 = **24.8%**. Watch the **expense-recovery cap**: a 20% rise in repairs above the cap cuts NOI to EUR382,600, dropping DSC to 1.73 and the equity dividend rate to 21.6%.
Related: [[Publicly_Traded_Real_Estate]]

### 2026-08-02 — What is a cap rate?
**Q:** What is the cap rate in real estate valuation?
**A:** `Cap rate = NOI / value`, i.e. the property's **income yield** on first-year NOI (before financing and taxes) — so `Value = NOI / cap rate`. Its **reciprocal is a valuation multiple** (8% cap rate = 12.5× NOI), making it the real estate analogue of an **earnings yield**. Obtain it two ways: **(1) from comparables**, `NOI_comp / price_comp` — comp at $2.5m with NOI $200k → 8%, so a subject with NOI $130k is worth $1,625,000; **(2) from fundamentals**, `cap rate = r − g` (Gordon Growth with NOI for dividends). **Key trap: cap rate ≠ discount rate** — `r` is the required return (risk-free + risk premium), the cap rate is `r − g` and is **lower than r** whenever g > 0. Invert for market-implied growth: `g = r − cap rate`; `cap rate > r` ⇒ `g < 0` ⇒ property near end of useful life. Cap rate and value move **inversely**. **Going-in** cap rate → first-year NOI (direct capitalization); **terminal** cap rate → the DCF terminal value `NOIₙ(1+g)/(r−g)` (**next**-period NOI). If first-year NOI is distorted, capitalize **stabilized NOI** and then **subtract** the value lost to the temporary decline.
Related: [[Publicly_Traded_Real_Estate]], [[Dividend_Discount_Models]]

### 2026-06-03 — Value a property by direct capitalization vs DCF, and the terminal-value trap
**Q:** When do I use direct cap vs DCF, and what's the terminal-value formula?
**A:** **Direct capitalization** (value = NOI / cap rate, with **cap rate = r − g**) fits a property with **stable, perpetual-growth NOI** — e.g., Wallonia: 406,750 / (0.125 − 0.02) = **EUR3,873,810**. Use a **stabilized NOI** if current NOI is distorted. **DCF** fits when you have visibility into changing NOI: discount projected NOI plus a **terminal value = NOI_n(1+g)/(r − g)** — note it uses **next-period** (post-horizon) NOI. The **going-in cap rate** applies at purchase; the **terminal cap rate** applies to post-sale income and is often higher (older asset, more risk).
Related: [[Dividend_Discount_Models]], [[Free_Cash_Flow_Valuation]]

### 2026-06-03 — Why do appraisal-based indexes understate real estate risk?
**Q:** How do appraisal-based and transaction-based RE indexes differ, and why does it matter for asset allocation?
**A:** **Appraisal-based** indexes (NCREIF/GREFI) value properties by periodic professional appraisals. Appraisals **lag** the market (rising markets: transactions move first; falling markets the same) and not every property is reappraised each quarter, so the index is **smoothed** → it **understates volatility**, **lowers correlation** with stocks/bonds, and **overstates Sharpe**, which **overstates** the optimal RE allocation. **Transaction-based** indexes use actual sales via **repeat-sales** (same property sold twice) or **hedonic** regressions (control for size/age/quality/location) — truer volatility but noisier. Fixes: **unsmooth** the appraisal index ($R_t^*=aR_t+(1-a)R_{t-1}^*$) or use a transaction-based index for cross-asset comparisons.
Related: [[Publicly_Traded_Real_Estate]]
