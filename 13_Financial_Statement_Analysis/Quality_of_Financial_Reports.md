---
aliases: [Quality of Financial Reports, Earnings Quality, Accruals, Mean Reversion, Cash Flow Quality, Beneish]
tags: [CFA-L2, fsa, concept]
date: 2026-08-25
status: evergreen
source: Schweser Book 2, Modules 11-12, LOS 11.a-11.m, 12.a-12.e
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

## Earnings Quality (11.e-11.h)
- **Sustainable (persistent) earnings**: recurring; high-quality earnings persist into the future. `Earnings_t+1 = α + β1·(cash flow) + β2·(accruals) + ε` — **higher persistence on the cash-flow component** than on accruals.
- **Accruals** = accrual-basis earnings − cash earnings. **High accruals → lower earnings quality** and **faster mean reversion** (accrual-heavy earnings revert toward the mean faster).
- Warning signs: revenue recognition tricks (bill-and-hold, channel stuffing), classification shifting, understated expenses, off-balance-sheet liabilities, frequent "non-recurring" charges.

## Cash Flow & Balance Sheet Quality (11.i-11.l)
- **High cash-flow quality**: CFO positive, derived from sustainable operations, correlates with earnings, not boosted by stretching payables or one-offs.
- **High balance-sheet quality**: adequate completeness, unbiased measurement, clear presentation; watch for understated liabilities and overstated/impaired assets.

## Detection Tools (11.c, 11.d)
- **Beneish M-score**: a **probit** model estimating the probability of earnings manipulation from **eight** variables. A **higher** M-score → higher probability of manipulation; the curriculum's cutoff is **M > −1.78** (e.g., M = −1.53 exceeds −1.78 → higher-than-acceptable probability, ≈6.3%).

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
- Common adjustments: capitalize vs expense, off-balance-sheet leases/debt, pension reclassifications, inventory (LIFO→FIFO), goodwill/impairments, normalizing earnings.

## Exam Traps
- **Reporting quality ≠ earnings quality** — keep the two axes separate.
- **High accruals = low earnings quality + faster mean reversion**; the cash-flow component of earnings is more persistent than the accrual component.
- Beneish: a **higher** M-score signals a **higher** probability of manipulation.
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
