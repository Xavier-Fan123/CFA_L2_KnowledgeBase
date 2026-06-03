---
aliases: [Quality of Financial Reports, Earnings Quality, Accruals, Mean Reversion, Cash Flow Quality, Beneish]
tags: [CFA-L2, fsa, concept]
date: 2026-06-03
status: evergreen
source: Schweser Book 2, Modules 11-12, LOS 11.a-11.m, 12.a-12.e
---

# Evaluating Quality of Financial Reports

## Quality Spectrum (11.a, 11.b)
Two dimensions: **reporting quality** (GAAP, decision-useful, complete, unbiased) and **earnings/results
quality** (sustainable, adequate returns). Spectrum from best to worst:
1. GAAP, decision-useful, **sustainable & adequate** returns
2. GAAP, decision-useful, but **low-quality earnings** (unsustainable/inadequate)
3. GAAP, but **biased/earnings-managed** choices
4. GAAP, but **non-compliant numbers** disguised
5. **Non-GAAP / fabricated** — fictitious

> Reporting quality and earnings quality are distinct: you can have high reporting quality reporting
> low (but truthful) earnings.

## Motivations & Conditions (11.b)
Earnings management thrives when **opportunity** (weak controls/board), **motivation** (meet targets,
covenants, compensation), and **rationalization** coincide ("fraud triangle").

## Earnings Quality (11.e-11.h)
- **Sustainable (persistent) earnings**: recurring; high-quality earnings persist into the future.
  `Earnings_t+1 = α + β1·(cash flow) + β2·(accruals) + ε` — **higher persistence on the cash-flow
  component** than on accruals.
- **Accruals** = accrual-basis earnings − cash earnings. **High accruals → lower earnings quality** and
  **faster mean reversion** (accrual-heavy earnings revert toward the mean faster).
- Warning signs: revenue recognition tricks (bill-and-hold, channel stuffing), classification shifting,
  understated expenses, off-balance-sheet liabilities, frequent "non-recurring" charges.

## Cash Flow & Balance Sheet Quality (11.i-11.l)
- **High cash-flow quality**: CFO positive, derived from sustainable operations, correlates with
  earnings, not boosted by stretching payables or one-offs.
- **High balance-sheet quality**: adequate completeness, unbiased measurement, clear presentation;
  watch for understated liabilities and overstated/impaired assets.

## Detection Tools (11.c, 11.d)
- **Beneish M-score**: probability of manipulation (higher → more likely manipulator); inputs include
  DSR, gross-margin index, asset-quality index, sales-growth index, total-accruals-to-assets.
- Bankruptcy/Altman Z-score for distress; trend & cross-sectional ratio analysis.

## Integration / Adjustments (Module 12)
- Apply a **framework**: define purpose → collect data → make **adjustments** for comparability
  (accounting standards, methods, assumptions) → analyze.
- Common adjustments: capitalize vs expense, off-balance-sheet leases/debt, pension reclassifications,
  inventory (LIFO→FIFO), goodwill/impairments, normalizing earnings.

## Exam Traps
- **Reporting quality ≠ earnings quality** — keep the two axes separate.
- **High accruals = low earnings quality + faster mean reversion**; the cash-flow component of earnings
  is more persistent than the accrual component.
- Beneish: a **higher** M-score signals a **higher** probability of manipulation.

## Q&A

### 2026-06-03 — Why do high accruals signal low earnings quality?
**Q:** What's the link between accruals, earnings persistence, and mean reversion?
**A:** Accruals = accrual-basis earnings − cash earnings. In `Earnings_t+1 = α + β1·CashFlow + β2·Accruals`,
the **cash-flow component is more persistent** (higher β) than the accrual component. So earnings dominated
by **high accruals are less sustainable and mean-revert faster** — they fade toward the average sooner.
Practically, a firm whose earnings are propped up by accruals (vs cash) has **lower earnings quality**, even
if every number is GAAP-compliant.
Related: [[Employee_Compensation]]

### 2026-06-03 — Reporting quality vs earnings quality
**Q:** Can a company have high reporting quality but low earnings quality?
**A:** Yes — they are **independent axes**. **Reporting quality** = are the statements GAAP-compliant,
decision-useful, complete, and unbiased? **Earnings (results) quality** = are the economic results
**sustainable and adequate** (high return on capital)? A firm can faithfully and transparently report
genuinely **poor, unsustainable** earnings → high reporting quality, low earnings quality. The danger
zone is high reporting *appearance* hiding biased or fabricated numbers. Beneish **M-score**: a **higher**
score → **higher** probability of manipulation.
Related: [[Analysis_of_Financial_Institutions]]
