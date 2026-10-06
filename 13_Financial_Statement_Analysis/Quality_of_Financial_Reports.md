---
aliases: [Quality of Financial Reports, Earnings Quality, Accruals, Mean Reversion, Cash Flow Quality, Beneish]
tags: [CFA-L2, fsa, concept]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V3 LM5 (October 2026 errata applied); Schweser Book 2, Modules 11-12, LOS 11.a-11.m, 12.a-12.e
---

# Evaluating Quality of Financial Reports

## Quality Spectrum (11.a, 11.b)
Two dimensions: **reporting quality** (GAAP, decision-useful, complete, unbiased) and **earnings/results quality** (sustainable, adequate returns). Spectrum from best to worst:
1. GAAP, decision-useful, **sustainable & adequate** returns
2. GAAP, decision-useful, but **low-quality earnings** (unsustainable/inadequate)
3. GAAP, but **biased/earnings-managed** choices
4. GAAP, but **non-compliant numbers** disguised
5. **Non-GAAP / fabricated** — fictitious

> Reporting quality and earnings quality are distinct: you can have high reporting quality reporting low (but truthful) earnings.

## Motivations & Conditions (11.b)
Earnings management thrives when **opportunity** (weak controls/board), **motivation** (meet targets, covenants, compensation), and **rationalization** coincide ("fraud triangle").

## Potential Problems (11.b) — official V3 LM5 Sections 3-5
Two basic choices create quality problems: **(1) reported amounts and timing of recognition** and **(2) classification**. Even GAAP-compliant reports can diverge from economic reality; fraudulent reports diverge from both GAAP and reality.

**Amount/timing choices — think in `Assets − Liabilities = Equity`:**

| Choice | Effect |
|---|---|
| Aggressive, premature, or fictitious revenue | Income, equity, and assets (usually A/R) **overstated** |
| Conservative (deferred) revenue | Net income, equity, assets **understated** |
| Omitted/delayed expenses | Income and equity overstated; assets overstated and/or liabilities understated (low bad-debt expense → A/R too high; low depreciation → PP&E too high; unaccrued interest/tax → payables too low) |
| Understated contingent liabilities | Equity overstated |
| Overstated financial assets / understated financial liabilities at fair value | Equity overstated via unrealized gains |
| Deferring payables, accelerating collections, deferring inventory purchases, maintenance or R&D | **CFO boosted** |

**Classification choices** usually affect one statement:
- *Balance sheet*: hide collection problems by selling receivables, moving them to a controlled entity, converting them to notes, or reclassifying them as long-term → lower DSO, better receivables turnover. Merck moved part of inventory to "other assets" → **days of inventory fell and the current ratio fell**, and the inventory-turnover time series became inconsistent.
- *Income statement*: labelling income as core/recurring or expenses as non-operating or non-recurring (including in non-GAAP metrics) inflates apparently sustainable earnings; OCI-vs-net-income classification of investments hurts comparability.
- *Cash flow statement*: classifying sales of long-term assets as operating, or **capitalizing operating outlays** (outflow lands in investing), inflates CFO.

**Accounting warning signs (official Exhibit 4)** — revenue growth above peers; rising discounts and returns; **receivables growing faster than revenue**; a large share of revenue in the final quarter of a non-seasonal business; **CFO much lower than operating income**; items moving in and out of operating revenue/expense; rising operating margin; aggressive assumptions (long depreciable lives); losses parked in non-operating income or OCI while gains sit in operating income; pay tied to reported results; biased fair-value models, or fair-value inputs inconsistent between assets and liabilities; current-type assets (A/R, inventory) shown as non-current; reserves that fluctuate or differ from peers; **high goodwill relative to total assets**; special purpose vehicles; large swings in deferred taxes; significant off-balance-sheet liabilities; rising A/P with falling A/R and inventory; capitalized expenditures in investing; sale-and-leaseback; rising bank overdrafts.

### M&A Issues and Divergence from Economic Reality (Section 5)
- An acquisition can **boost consolidated CFO**: the target's operating cash flow enters CFO while the price goes to investing (or nowhere, if paid in shares). This can hide the acquirer's own cash-flow problems, and no "with and without the acquisition" disclosure is required.
- Incentives to misreport around deals: an acquirer paying **in stock** may inflate earnings beforehand; a target may inflate to get a better price; firms already misreporting are **more likely to acquire** (complexity hides past misstatements).
- **Purchase-price allocation bias**: understating amortizable intangibles pushes value into **goodwill**, which is **not amortized** → higher future earnings, and an uneconomic deal surfaces only when goodwill is impaired, often years later.
- **Compliant but unrealistic**: (a) VIEs — lacking voting control is **not** enough to avoid consolidation (Digilog); (b) impairments and restructuring charges booked in one period **overstate prior periods' income** and understate the current period — if such charges recur, normalize by spreading them; if truly one-off, exclude them; (c) revised estimates, sudden jumps in allowances or reserves, and large loss accruals suggest **prior** earnings were overstated, and reserves can be used to smooth earnings.
- **R&D (26 Jan 2026 errata):** under **US GAAP**, R&D is expensed. Under **IFRS**, research is expensed but **development costs are capitalized** if, and only if, the entity can show: (a) technical feasibility; (b) intention to complete and use or sell; (c) ability to use or sell; (d) how the asset will generate probable future economic benefits; (e) adequate technical, financial and other resources to complete it; (f) reliable measurement of the expenditure. The pre-errata text said "accounting standards do not permit capitalization of R&D", which is wrong for IFRS.
- **Unrecognized assets**, e.g., a large **order backlog** (aircraft makers) — use MD&A to adjust forecasts.
- **OCI items** an analyst may decide to treat as income: unrealized G/L on certain equity investments; IFRS revaluation surplus on PP&E; currency translation adjustments; pension remeasurements; cash-flow-hedge G/L.

## How to Evaluate Reporting Quality (11.c) — the 7 general steps
1. **Understand the company and its industry** (what accounting is normal for this business).
2. **Learn about management**: incentives to misreport, compensation, **insider sales**, related-party transactions.
3. **Identify significant accounting areas** where judgment or unusual rules drive results.
4. **Make comparisons**: (a) this year's statements and disclosures vs last year's; (b) accounting policies vs closest competitors (directional effect of differences); (c) ratios vs competitors.
5. **Check warning signs**: falling receivables turnover (fictitious/premature revenue or thin allowance); falling inventory turnover (obsolescence); **net income > CFO** (aggressive accruals shifting expenses to later periods).
6. **Multi-segment firms**: watch for revenue, expenses or inventory shifted into the segment the market finds attractive (strong segment, flat or worse consolidated results).
7. **Use quantitative tools** (Beneish, etc.) to assess the likelihood of misreporting.

## Earnings Quality (11.e-11.h)
- **High-quality earnings** are sustainable **and** earn at least the cost of capital (and assume high reporting quality); low-quality earnings fall short of the cost of capital and/or come from non-recurring activities.
- **Indicators of earnings quality (official list)**: (1) recurring earnings, (2) earnings persistence and related measures of accruals, (3) beating benchmarks, (4) after-the-fact confirmations — **enforcement actions and restatements** (least useful because they come too late).
- **Recurring earnings / classification shifting**: exclude discontinued operations and one-offs (asset sales, litigation or tax settlements). **Classification shifting** leaves net income unchanged but inflates "core" earnings — normal expenses relabeled as special items or pushed into discontinued operations (Borden, AmeriServe); non-operating gains netted against operating expenses (Waste Management); IP income netted against SG&A (IBM). Scrutinize income-decreasing special items when core earnings are unusually high or just beat forecasts. Non-GAAP (pro forma) measures must be reconciled to reported income; check that exclusions really are non-recurring (Groupon excluded marketing costs).
- **Persistence**: `Earnings_t+1 = α + β1·Earnings_t + ε` — higher β1 = more persistent. Split into components: `Earnings_t+1 = α + β1·(cash flow) + β2·(accruals) + ε` — **β1 > β2**, the cash-flow component is more persistent.
- **Accruals** = accrual-basis earnings − cash earnings. **High accruals → lower earnings quality** and **faster mean reversion**. **Non-discretionary** accruals come from normal transactions; **discretionary** accruals come from unusual choices and may be manipulation. Abnormal accruals = the **residual** from regressing total accruals on normal drivers (credit-sales growth, depreciable assets) — the Jones / modified Jones approach, extended in the SEC's Accounting Quality Model. A simple screen compares total accruals **scaled by average assets or average net operating income**.
- **Most dramatic signal**: **positive net income with negative operating cash flow**, year after year (Allou Health & Beauty).
- **Mean reversion**: extreme earnings (high or low) revert through competition and restructuring; don't extrapolate extremes — forecast normalized earnings; a large accrual component speeds the reversion.
- **Beating benchmarks**: consistently **exactly meeting or narrowly beating** consensus is a possible sign of earnings management (results cluster just above zero), though the evidence is debated.

### Case lessons (revenue and expense recognition)
- **Sunbeam** (channel stuffing, bill-and-hold): receivables grew far faster than revenue (+38.5% vs +18.7% in 1997), receivables/revenue and **DSO** rose (DSO 77.6 → 92.4 days).
- **MicroStrategy** (multiple-element contracts): service revenue was mis-allocated to **earlier-recognized software (product) revenue**.
- **WorldCom** (capitalized "line costs"): gross PP&E jumped from ~30% to 37%, 45% and 47% of total assets. Expense-capitalization checks: non-current assets growing while margins hold; **asset turnover falling with steady or rising revenue**; depreciation relative to the asset base; capex relative to gross PP&E rising.
- **Related parties**: **tunneling** = moving wealth out of the public company to insiders' entities; **propping** = insiders injecting resources to keep the company alive and preserve future gains.

## Bankruptcy Prediction (11.h, 11.i, 11.k)
- **Altman Z-score (discriminant analysis)**: `Z = 1.2(NWC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(MV equity/BV liabilities) + 1.0(Sales/TA)` — liquidity, accumulated profitability and age, profitability, leverage (solvency), activity. **Higher Z is better**: **Z < 1.81 → high probability of bankruptcy; Z > 3.00 → low; 1.81-3.00 → grey zone**.
- Limitations and developments: Altman is **single-period and static** → **hazard models** (Shumway) use every year of data; accounting models look backward and assume a going concern → **market-based models** (Merton: equity as a call on the firm's assets, using equity value, debt, equity returns and volatility), CDS and bond prices; the best models **combine** accounting and market data (e.g., Bharath-Shumway).

## Cash Flow Quality (11.i, 11.l)
- High-quality CFO for an established company: **positive; from sustainable sources; enough to cover capex, dividends and debt repayment; low volatility vs peers** — plus faithful reporting. Life cycle matters: a start-up normally has negative CFO and CFI funded by financing.
- "Low-quality" cash flow means either genuinely poor performance (results quality) **or** misrepresentation (reporting quality).
- Manipulation channels: **timing** — selling receivables, delaying payables (DSO falls, days payable rise); **classification** — shifting investing/financing inflows into operating. A large or widening gap between earnings and CFO flags earnings manipulation, but **Satyam's** fabricated cash "kept pace" with profits and slipped past NI-vs-CFO screens — read the statement qualitatively too (e.g., surging unbilled revenue).

## Balance Sheet Quality (11.j, 11.k)
- Reporting quality = **completeness, unbiased measurement, clear presentation**; results quality = optimal leverage, adequate liquidity, economically successful asset allocation.
- **Completeness**: off-balance-sheet obligations understate leverage — e.g., **take-or-pay purchase contracts** → **constructive capitalization** (add the PV of future purchase payments to both assets and liabilities); **unconsolidated JVs / equity-method investees** hide liabilities and **overstate net profit margin** (share of profit included, share of sales not); many unconsolidated affiliates with ownership **near 50%** is a warning sign.
- **Unbiased measurement** matters most where valuation is subjective: understated impairments (inventory, PP&E, goodwill); **goodwill large relative to market value**, or market value of equity below book value → impairment probably overdue (Sealed Air); deferred-tax-asset valuation allowance; investments valued with **unobservable (Level 3) inputs**; pension discount rate.

## Detection Tools (11.c, 11.d)
- **Beneish M-score**: a **probit** model estimating the probability of earnings manipulation from **eight** variables. A **higher** (less negative) M-score → higher probability of manipulation. Curriculum cutoff: **M > −1.78**, i.e., a manipulation probability above **3.8%** (M = −1.49 ≈ 6.8%). Where to set the cutoff trades off **Type I** errors (missing a manipulator) against **Type II** errors (flagging a non-manipulator). Schweser example: M = −1.53 exceeds −1.78 → ≈6.3%, flag.

| Variable | Definition | Manipulation signal |
|---|---|---|
| **DSRI** days sales receivable index | days' sales in receivables, year t ÷ year t−1 | **> 1** → revenue may be inflated / recognition accelerated |
| **GMI** gross margin index | gross margin **year t−1 ÷ year t** | **> 1** → margin **deteriorated**; pressure to manipulate |
| **AQI** asset quality index | (non-current assets other than PP&E ÷ total assets), t ÷ t−1 | **> 1** → possible **excessive capitalization** of expenses |
| **SGI** sales growth index | sales, t ÷ t−1 | **> 1** → growth firms face pressure to keep meeting expectations |
| **DEPI** depreciation index | depreciation rate **t−1 ÷ t** (rate = dep. expense ÷ (dep. + PP&E)) | **> 1** → depreciating **more slowly** (longer lives / higher salvage) |
| **SGAI** SG&A index | SG&A as % of sales, t ÷ t−1 | rising SG&A may predispose to manipulation (fitted coefficient is **negative**) |
| **Accruals** | (income before extraordinary items − CFO) ÷ total assets | higher accruals → lower earnings quality |
| **LEVI** leverage index | total debt ÷ total assets, t ÷ t−1 | rising leverage (fitted coefficient is **negative**) |

  - Don't memorize the coefficients — interpret the **direction** of each index. Note the two counterintuitive ones: **SGAI and LEVI carry negative fitted coefficients**, opposite to what Beneish expected.
  - **Limitations**: it relies on accounting data that may not reflect economic reality, and once managers know the model they **game its inputs** — the model's predictive power has **declined over time**.
- Bankruptcy/Altman Z-score for distress; trend & cross-sectional ratio analysis.

## Sources of Information about Risk (11.m)
The financial statements themselves signal risk (high leverage/low coverage = financial risk; volatile operating cash flows or falling margins = operating risk; bankruptcy/Beneish models = distress/reporting risk). But the **best risk information often comes from sources beyond the primary statements**:

- **Notes to the financial statements** — required disclosures about **contingent obligations** (amounts, timing, uncertainties), **pension/post-employment** assumptions, and **financial-instrument risks**; year-over-year changes in management estimates carry risk signals.
- **Management commentary / MD&A** — management's own assessment of the key risks; content often **differs** from (does not just repeat) the note disclosures and reveals the management perspective.
- **Other required disclosures** tied to specific events — capital raising, **non-timely filings**, management changes, M&A.
- **Financial press / online media** — useful if used judiciously.

**Limited usefulness of the auditor's opinion (key exam point):**
- A clean opinion states the statements are fairly presented in conformity with GAAP and (where required) that internal controls are effective. A **going-concern** opinion or a reported **internal-control weakness** is a clear warning sign.
- **BUT the audit opinion is rarely a timely source of risk information** — it covers **historical** statements and lags events (Kodak's clean-with-going-concern opinion was dated *after* it had already filed for bankruptcy; Groupon's control weakness never appeared in an opinion because of newly-public exemptions, then was remedied before the first required opinion).
- **Auditor-related red flags**: a **discretionary change of auditor** (especially **multiple** changes → "auditor shopping," as at a Madoff feeder fund with 3 auditors in 3 years); an auditor whose **size/ capability is inadequate** for the company's complexity (Madoff's $50bn operation audited by a 3-person firm); or any **independence** concern (auditor too close to management, or the client is a large share of the auditor's revenue).

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- For commodity merchants, high reported revenue can be economically thin because many flows are pass-through. Test whether the firm reports as **principal vs. agent**, whether buy/sell legs are grossed up, and whether volume growth actually creates margin, cash conversion, and risk-adjusted return.
- Inventory accounting is central. Compare inventory measurement with the risk policy: lower of cost and net realizable value (NRV), fair-value inventory, exchange hedges, and basis exposure can move earnings in different periods even when the economic hedge is sensible.
- Derivative gains deserve a cash-quality check. Positive fair-value marks on swaps, forwards, and options may reverse, require collateral, or depend on Level 2/Level 3 curves; they are not the same as cash collected from customers.
- Repeated "one-off" adjustments around storage losses, demurrage, sanctions, credit losses, restructuring, contract disputes, or inventory write-downs are not automatically non-recurring for a trading business. They may be part of the operating risk profile.
- Off-balance-sheet commitments matter: take-or-pay contracts, long-term purchase/sale commitments, guarantees, letters of credit, tolling agreements, and lease/storage obligations can create liquidity risk before they appear as debt.
- Strong reporting quality requires reconciliation among MD&A risk language, derivative footnotes, inventory policy, segment margins, collateral/margin disclosures, and operating cash flow. A clean audit opinion is not enough for a commodity trader.

## Integration / Adjustments (Module 12)
- Apply a **framework**: define purpose → collect data → make **adjustments** for comparability (accounting standards, methods, assumptions) → analyze.
- Common adjustments: capitalize vs expense, off-balance-sheet obligations (take-or-pay purchase commitments, unconsolidated affiliates), pension reclassifications, inventory (LIFO→FIFO), goodwill/impairments, normalizing earnings. (Leases are now on the balance sheet under IFRS 16 / ASC 842 — the 2 Jun 2026 errata deleted a curriculum sentence calling operating leases off-balance-sheet liabilities.)

## Exam Traps
- **Reporting quality ≠ earnings quality** — keep the two axes separate.
- **High accruals = low earnings quality + faster mean reversion**; the cash-flow component of earnings is more persistent than the accrual component.
- Beneish: a **higher** M-score signals a **higher** probability of manipulation (cutoff −1.78 ≈ 3.8%). **Altman Z is the reverse**: a **higher** Z is **safer** (< 1.81 distress, > 3.00 safe).
- **Positive net income with negative CFO** is the most dramatic accrual red flag; **receivables growing faster than revenue** (rising DSO) points to premature or fictitious revenue.
- **Classification shifting** does not change net income — it moves expenses into "special/non-recurring" items or discontinued operations to inflate **core** earnings.
- Booking a big impairment or restructuring charge in one period **overstates prior periods'** earnings (conservative now, aggressive before).
- **R&D**: US GAAP expenses it all; IFRS capitalizes **development** costs once the six criteria are met (26 Jan 2026 errata).
- Capitalizing operating costs (WorldCom) **raises CFO** (outflow moves to investing) and shows up as rising PP&E/total assets and falling asset turnover.
- The **auditor's opinion is NOT a timely risk source** (it lags — covers historical statements). But a **change of auditor**, an **undersized auditor**, or **going-concern/control-weakness** language are genuine red flags. Best risk info: **notes + MD&A + event-driven disclosures**, not the audit report.

## Q&A

### 2026-06-03 — Why do high accruals signal low earnings quality?
**Q:** What's the link between accruals, earnings persistence, and mean reversion?
**A:** Accruals = accrual-basis earnings − cash earnings. In `Earnings_t+1 = α + β1·CashFlow + β2·Accruals`, the **cash-flow component is more persistent** (higher β) than the accrual component. So earnings dominated by **high accruals are less sustainable and mean-revert faster** — they fade toward the average sooner. Practically, a firm whose earnings are propped up by accruals (vs cash) has **lower earnings quality**, even if every number is GAAP-compliant.
Related: [[Employee_Compensation]]

### 2026-06-03 — Reporting quality vs earnings quality
**Q:** Can a company have high reporting quality but low earnings quality?
**A:** Yes — they are **independent axes**. **Reporting quality** = are the statements GAAP-compliant, decision-useful, complete, and unbiased? **Earnings (results) quality** = are the economic results **sustainable and adequate** (high return on capital)? A firm can faithfully and transparently report genuinely **poor, unsustainable** earnings → high reporting quality, low earnings quality. The danger zone is high reporting *appearance* hiding biased or fabricated numbers. Beneish **M-score**: a **higher** score → **higher** probability of manipulation.
Related: [[Analysis_of_Financial_Institutions]]

### 2026-06-04 — Is the auditor's opinion a good source of information about risk?
**Q:** What are the main sources of information about a company's risk, and how useful is the auditor's opinion?
**A:** Beyond ratios from the statements (leverage, coverage, cash-flow volatility, Beneish/Altman), the richest risk information is in the **notes** (contingent obligations, pensions, financial-instrument risks), the **MD&A/management commentary** (management's own risk view, which often differs from the notes), and **event-driven disclosures** (capital raises, non-timely filings, management changes, M&A). The **auditor's opinion is generally NOT a timely risk source** because it covers **historical** statements and lags events — e.g., **Kodak's** clean (going-concern) opinion was dated *after* its bankruptcy filing, and **Groupon's** control weakness never showed up in an opinion. What *is* a red flag: a **discretionary auditor change** (or multiple changes → "auditor shopping"), an **undersized/ inadequate auditor** relative to the firm's complexity, a **going-concern** opinion, a reported **internal-control weakness**, or any **independence** concern.
Related: [[Integration_of_FSA_Techniques]]
