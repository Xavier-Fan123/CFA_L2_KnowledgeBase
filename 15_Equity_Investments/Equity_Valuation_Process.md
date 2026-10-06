---
aliases: [Equity Valuation Process, Intrinsic Value, Industry Analysis, Sum-of-the-Parts, Absolute vs Relative Valuation]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V5 LM1 (October 2026 errata applied); Schweser Book 3, Module 17, LOS 17.a-17.h
---

# Equity Valuation: Applications and Processes

## Value Concepts (17.a, 17.b, 17.c)
- **Intrinsic value**: the "true" value given complete information — unobservable. Active managers try to exploit **perceived mispricing** = **estimated** intrinsic value − market price, `V_E − P`. Requires that the market eventually corrects.
- `V_E − P = (V − P) + (V_E − V)` → **perceived mispricing = true mispricing + valuation error** (error in the estimate of intrinsic value).
- **2026 errata (5 May / 1 Sept 2026):** the practice question asking which difference active managers "attempt to exploit" now answers **estimated intrinsic value vs market price** (`V_E − P`), not true intrinsic value vs price — the manager can only trade on what they can estimate. True mispricing `V − P` is what produces the abnormal return (alpha) if the estimate is right.
- **Why active investing can work — the rational efficient markets formulation (Grossman-Stiglitz):** if prices perfectly reflected intrinsic value, nobody would pay to gather information, so prices could not reflect it; investors research only if they expect higher gross returns, and costly, hard-to-estimate values plus trading costs leave room for price to diverge from value. Active managers often also look for a **catalyst** that makes the market re-evaluate the stock.
- **Going-concern** value (operating indefinitely) vs **liquidation** value (cease operations, sell assets separately, net of liabilities; an **orderly** liquidation fetches more than an immediate one). A persistently unprofitable business can be worth more "dead than alive".
- **Which definition fits public equities? INTRINSIC value, estimated under the going-concern assumption** (official text). The other definitions serve other contexts:
- **Definitions of value (17.c)** — a distinction the exam likes:

| Concept | Definition | Who it applies to |
|---|---|---|
| **Fair market value** | The price at which a willing buyer and a willing seller, **neither under compulsion** and **both informed** of material facts, would trade | Buy-sell agreements among private-business owners; **tax** valuations |
| **Fair value** (financial reporting) | "The amount for which an asset could be exchanged, a liability settled, or an equity instrument granted could be exchanged between **knowledgeable, willing parties in an arm's length transaction**" | Accounting measurement, e.g., **impairment testing** |
| **Investment value** | Value **to a specific buyer**, including any additional value from **synergies** available only to that buyer | **Strategic buyers** in acquisitions — investment value normally exceeds fair market value by the synergy amount |

## Applications (17.d)
Stock selection, inferring (extracting) market expectations, evaluating corporate events (M&A, divestitures, spin-offs, LBOs), issuing **fairness opinions**, evaluating business strategies and models, communicating with analysts and shareholders, appraising private businesses, and share-based payment (compensation) valuation.

## The Valuation Process (five steps)
1. **Understand the business** — industry and competitive analysis plus analysis of financial reports (including earnings quality).
2. **Forecast company performance** — **top-down** (macro → industry → company) or **bottom-up** (company → industry → macro aggregation).
3. **Select the appropriate valuation model** (criteria below).
4. **Convert forecasts to a valuation** — involves judgment: **sensitivity analysis** (how value changes with growth, margin, or discount-rate assumptions) and **situational adjustments**: **control premium** (controlling stake → can redeploy assets or change capital structure), **lack-of-marketability discount** (no public market), and **illiquidity discount** for thin markets or a block that is large relative to trading volume (the **blockage factor**).
5. **Apply the valuation conclusions** — a recommendation, a fairness opinion on a transaction price, or a judgment on a strategic investment.

## Industry & Competitive Analysis (17.e)
Address: industry structure, demand/supply, life-cycle stage, profitability drivers, competitive advantage and its sustainability, and the firm's strategy.

**The five elements of industry structure (Porter)** — know all five by name:
1. **Threat of new entrants** into the industry.
2. **Threat of substitutes.**
3. **Bargaining power of buyers.**
4. **Bargaining power of suppliers.**
5. **Rivalry among existing competitors.**

**Quality-of-earnings checks that belong in the valuation process (17.e)** — categories to scan before trusting the inputs:
- **Accelerating or premature recognition of income.**
- **Reclassifying gains and non-operating income** into operating results.
- **Expense recognition and losses** (understating or deferring them).
- **Amortization, depreciation, and discount rates** (assumptions that flatter earnings).
- **Off-balance-sheet issues.**

These often surface **only in the footnotes and disclosures**, not on the face of the statements → [[Quality_of_Financial_Reports]].

## Model Types (17.f, 17.g, 17.h)
- **Absolute valuation**: estimates intrinsic value directly — DDM, FCF, residual income, asset-based.
- **Relative valuation**: value relative to peers via **multiples** (method of comparables).
- **Sum-of-the-parts**: value each business segment separately and add (the **breakup value**); a **conglomerate discount** may apply — the market discounts companies in multiple **unrelated** businesses. Official explanations: (1) **inefficient internal capital markets** (capital allocated across divisions doesn't maximize shareholder value); (2) **endogenous factors** (poorly performing companies tend to expand by acquiring unrelated businesses); (3) **research measurement errors** (the discount may not really exist). A breakup value above going-concern value can prompt a **divestiture or spin-off**.
- **Model selection criteria (official)**: the model should be (1) **consistent with the characteristics of the company** (dividends? positive FCF? asset-heavy? quality accounting?), (2) **appropriate given the availability and quality of data**, and (3) **consistent with the purpose of the valuation** and the analyst's perspective (e.g., a controlling vs minority view).
- **Effective research report**: timely; clear, incisive language; objective and well researched, with key assumptions identified; separates **facts from opinions**; analysis, forecasts, valuation, and recommendation **internally consistent**; enough information for the reader to critique the valuation; states **risk factors**; discloses **conflicts of interest**.

## Exam Traps
- Analyst edge = **perceived** mispricing `V_E − P` (estimated value vs price), which includes estimation error in intrinsic value. "Which difference do active managers attempt to exploit?" → **estimated intrinsic value vs market price**.
- **Sum-of-the-parts** can reveal a **conglomerate discount**.
- Choose the model that fits the firm: non-payer with negative FCF but clean accounting → residual income.
- **Fair market value** = hypothetical willing buyer/seller; **investment value** = value to a **specific** buyer **including synergies** (the strategic-buyer measure). Don't use the two interchangeably.
- For **public-equity** valuation the relevant definition is **intrinsic value** (going concern) — not fair market value or accounting fair value.
- Conglomerate discount explanations: **internal capital market inefficiency, endogenous factors, measurement error**.
- Porter's five: new entrants, substitutes, **buyer** power, **supplier** power, rivalry — buyers and suppliers are two separate forces.

## Q&A

### 2026-06-03 — Perceived vs true mispricing
**Q:** Why is the analyst's edge "perceived" mispricing, and what risks does that hide?
**A:** `Perceived mispricing = true mispricing + error in your estimate of intrinsic value`. You only ever observe market price and **your** intrinsic-value estimate, so apparent mispricing blends a real opportunity with your own estimation error. Two extra conditions must hold to profit: (1) the market must **eventually converge** to intrinsic value, and (2) you need the right **catalyst/horizon**. A confident but wrong intrinsic estimate produces false "mispricing."
Related: [[Market_Based_Valuation]]

### 2026-06-03 — Choosing a valuation model
**Q:** How do you pick among DDM, FCF, residual income, and multiples?
**A:** Match the model to the firm: **DDM** for stable dividend payers (minority view); **FCFE/FCFF** for firms with positive, forecastable free cash flow or a control perspective; **residual income** for non-payers with negative FCF but **high-quality accounting** and uncertain terminal value; **multiples** for quick relative views and when peers are comparable; **asset-based / sum-of-the-parts** for holding companies or to surface a conglomerate discount. Also weigh purpose and data availability.
Related: [[Dividend_Discount_Models]]
