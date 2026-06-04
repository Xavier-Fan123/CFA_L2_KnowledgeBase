---
aliases: [Publicly Traded Real Estate, REIT, REOC, Mortgage REIT, NAVPS, FFO, AFFO, Funds From Operations, Cap Rate, REIT Valuation, Price-to-FFO, Cash NOI]
tags: [CFA-L2, alt, concept, real-estate]
date: 2026-06-04
status: evergreen
source: Official Curriculum L2 Vol 8, Learning Module 3 (Investments in Real Estate through Publicly Traded Securities); Schweser Book 4
---

# Investments in Real Estate Through Publicly Traded Securities

> Companion to private/direct real estate in [[Real_Estate]] (Reading 31). This reading is REITs/REOCs:
> their structure, **NAVPS**, **FFO/AFFO**, and the **four valuation approaches**.

## Types of Publicly Traded Real Estate Securities (LOS 32.a)

| | Security | Note |
|---|---|---|
| **Equity** | **Equity REIT** | tax-advantaged trust; owns income-producing property; must distribute **>90%** of taxable income |
| | **REOC** | ordinary **taxable** corporation; used when a firm **develops & sells** property or is in a country with no REIT regime |
| **Debt** | **MBS (RMBS/CMBS)** | securitized claims on a pool of mortgage loans; far larger market than RE equity |
| | **Mortgage REIT** | invests in mortgages/mortgage securities/loans secured by real estate |

**REIT structure rules (typical):** distribute **90–100%** of taxable income; **≥75%** of assets in real
estate; **≥75%** of income from rent or mortgage interest; **U.S. "5/50 rule"** — ≥100 owners and **no 5
or fewer owners holding >50%** of shares.

## Advantages vs. Disadvantages of REITs (LOS 32.a)

**Advantages:** superior **liquidity** (trades daily), transparency, tax exemption, **predictable
earnings** (contractual rents), access to premium properties, active professional management, greater
diversification across property type/geography.

**Disadvantages (mostly flow from the high-payout rule):** **limited income growth** (little retained
earnings → may be **forced to issue equity** at bad prices), **lack of flexibility** (investment
restrictions), and **lower portfolio diversification benefit** — REITs correlate **more with equities**
than direct real estate does.

## NAVPS — Net Asset Value per Share (LOS 32.b)

NAVPS = per-share excess of assets over liabilities at **current market value** (not book/depreciated
cost) → considered the **most appropriate fundamental REIT value**, and **superior to BVPS**.

**Estimating NAVPS by capitalizing cash NOI:**
1. **Cash NOI** = potential gross income − vacancy/collection loss − operating expenses, **before**
   financing, depreciation, G&A, taxes. **Subtract non-cash (straight-line) rent** to get *cash* NOI.
2. **Forecast next-12-month NOI**: adjust current NOI for (a) **full-year effect of acquisitions** and
   (b) a **growth rate**.
3. **Value of operating real estate** = forecast cash NOI **÷ cap rate** (cap rate from comparable recent
   transactions).
4. **+ other tangible assets** (cash, receivables, land for development, prepaids) — **exclude goodwill,
   deferred financing expense, deferred tax assets** ("hard economic assets" only).
5. **− liabilities** (at market value if materially different) → **NAV**; ÷ shares → **NAVPS**.

A premium/discount of price to NAVPS reflects views on management, leverage, and governance. (NAV is a
*private-market* value, so it can diverge from public trading prices.)

## FFO and AFFO (LOS 32.c)

**FFO (Funds From Operations)** — popular measure of continuing REIT income. Official (Nareit) headline:
`FFO = (Net income + Depreciation + Amortization) − Net gains on sale of real property (+ losses)`
- **Add back D&A on real estate** (accounting depreciation usually exceeds *economic* depreciation for RE).
- **Exclude property-sale gains** (not continuing income); add back real estate **impairments/write-downs**.
- In many markets the fuller definition also **adds back deferred tax charges** (the curriculum's Baldwin
  example: FFO/share = (NI 142,187 + depreciation 90,409 − gains 2,162)/121,944 = **$1.89**; deferred tax
  n/a there but added back when present).

**AFFO (Adjusted FFO)** — a.k.a. **CAD / FAD**; closer to true economic income:
`AFFO = FFO − non-cash (straight-line) rent − maintenance capex & leasing costs`
- **AFFO is theoretically better** (it captures the capex needed to sustain the property), and a better
  read on **dividend sustainability**, **but FFO is cited more often** because AFFO is more
  estimate-dependent / **subjective**.

## Four Valuation Approaches (LOS 32.d)

| Approach | Method | Notes |
|---|---|---|
| **1. NAV** | capitalize cash NOI → NAV → NAVPS | private-market value; can differ from trading price |
| **2. P/FFO** | FFO/share × sector average P/FFO multiple | most-cited multiple; ignores leverage & capex |
| **3. P/AFFO** | AFFO/share × sector average P/AFFO multiple | reflects maintenance capex; more subjective |
| **4. DCF / DDM** | discount dividends (2- or 3-stage) / cash flows + terminal value | REITs pay out most income → DDM/DCF apt |

**Multiples — pros:** P/FFO and P/AFFO globally accepted, comparable across alternatives, FFO data widely
available. **Cons:** ignore **non-income real assets** (development land, vacant buildings); FFO ignores
recurring maintenance capex; one-time gains/charges distort FFO/AFFO. **Adjust for leverage** in relative
value (FFO/AFFO are **levered** income → P/FFO is lower for higher-leverage REITs; EV/EBITDA is
leverage-neutral and EBITDA/EV ≈ the cap rate).

**Three drivers of P/FFO, P/AFFO, EV/EBITDA differences:** (1) expected **FFO/AFFO growth** (business
model, supply-constrained geography, management); (2) **risk of the underlying real estate** (apartments
> hotels in stability → higher multiple); (3) **capital structure / access to capital** (more leverage →
lower multiple, possible equity overhang).

### Worked Examples (official LM3)
**NAVPS (Exhibit 2):** LTM real estate NOI $270,432 − non-cash rent $7,667 + acquisition adj. $4,534 =
pro forma cash NOI $267,299; + next-12-mo growth (1.5%) $4,009 → estimated forward cash NOI $271,308.
Capitalize at **7.00%** → value of operating RE = 271,308 / 0.07 = **$3,875,829**; + cash, land,
receivables, prepaids → gross asset value $4,045,072; − total debt $1,010,988 − other liabilities
$119,886 → **NAV $2,914,198**; ÷ 55,689 shares = **NAVPS $52.33**.
- **P/FFO:** FFO = AFFO + non-cash rent + recurring capex; e.g., $4,000,000 + $215,000 + $700,000 =
  $4,915,000; ÷ 800,000 shares = **FFO/share $6.14**; at price $80 → **P/FFO = 13.0×**. *(Trap: do NOT
  add depreciation to AFFO to get FFO, and do NOT subtract the rent/capex items — both are wrong-direction
  distractors giving 14.3× / 20.7×.)*
- **Relative value (apply sector multiple):** FFO/share $4.28 × sector P/FFO 13.5× = **$57.78/share**;
  or AFFO/share $4.05 × sector P/AFFO 18.3× = **$74.12/share**.
- **Two-step DDM:** dividends $4.00, $4.18, then terminal value = $4.54/(0.08 − 0.04) = $113.57 at end of
  Yr 3; discount at 8% → **value $100.91/share**.

## Public vs. Private Real Estate (LOS 32.e)

**Private/direct advantages:** direct exposure, returns driven by the actual property, **tax benefits**
(accelerated depreciation, capital-gain timing), inflation hedge, **illiquidity premium**, control,
**lower correlation** with other assets. **Private drawbacks:** illiquidity, high fees, high minimums, low
transparency, fewer protections, appraisal lag, leverage risk.

**Public advantages:** high **liquidity**, professional management, tax efficiency (REITs),
diversification, low minimums, low entry/exit cost, regulatory protection, transparency, limited
liability. **Public drawbacks:** **higher volatility**, **higher correlation with stocks**, dividends
taxed as ordinary income, agency conflict, equity markets **penalize high leverage**, price ≠ NAV.

## Exam Traps
- **AFFO subtracts** non-cash rent and maintenance capex/leasing costs from FFO (it does NOT add them).
  FFO **adds back depreciation** and **excludes property-sale gains**.
- Use **cash NOI** (strip straight-line/non-cash rent) and **forecast** NOI (acquisitions + growth)
  before applying the **cap rate**; exclude goodwill / deferred items from NAV assets.
- **CREF (commingled real estate fund) is a PRIVATE vehicle**, not a publicly traded security.
- REITs offer relatively **low growth from reinvested operating cash flow** (because of the high payout
  requirement) — and **higher equity correlation** → weaker portfolio diversification than direct RE.
- **NAVPS uses market values** and is superior to BVPS; it is not "exactly" intrinsic value.

## Q&A

### 2026-06-04 — How do FFO and AFFO differ, and which is better?
**Q:** Define FFO and AFFO and explain which is the better measure of REIT economic income.
**A:** **FFO = net income + depreciation + deferred tax − gains on property sales (+ losses)** — it adds
back depreciation (accounting > economic depreciation for real estate) and strips non-recurring sale
gains. **AFFO = FFO − non-cash (straight-line) rent − recurring maintenance capex & leasing costs** (also
called CAD/FAD). **AFFO is theoretically superior** because it nets out the capital spending required to
sustain the properties, making it a better gauge of **dividend sustainability** — but **FFO is cited more
often** in practice because AFFO depends more on subjective estimates.
Related: [[Real_Estate]]

### 2026-06-04 — How do you estimate NAVPS from cash NOI?
**Q:** Walk through estimating a REIT's NAVPS by capitalizing cash net operating income.
**A:** (1) Start with **cash NOI** = gross income − vacancy/collection − operating expenses, removing
**non-cash straight-line rent**. (2) **Forecast** next year's cash NOI: add the full-year impact of
acquisitions and apply a growth rate. (3) Capitalize: **value of operating real estate = forecast cash
NOI ÷ cap rate** (cap rate from comparable transactions). (4) **Add other hard assets** (cash,
receivables, development land) but exclude goodwill, deferred financing costs, and deferred tax assets.
(5) **Subtract liabilities** (at market value) → NAV; divide by shares → **NAVPS**. NAVPS uses market
values and beats BVPS, which relies on depreciated historical cost.
Related: [[Real_Estate]]
