---
aliases: [Integration of Financial Statement Analysis Techniques, FSA Integration, Financial Statement Modeling, Extended DuPont, Accruals Ratio, Earnings Quality, Market Value Decomposition, Implied PE, Segment Capital Allocation, Cash Generated from Operations]
tags: [CFA-L2, fsa, concept]
date: 2026-06-04
status: evergreen
source: Schweser Book 2, Reading 12 (Modules 12.1–12.6), LOS 12.a–12.e
---

# Integration of Financial Statement Analysis Techniques

> The capstone FSA reading: a **framework** plus six analytical lenses applied to one company (Thunderbird, with a 30% stake in associate Eagle). Ties together DuPont, accruals/earnings quality, segment analysis, and market-value decomposition.

## Framework for Analysis (LOS 12.a)

Six steps: **(1) establish the objective → (2) collect data → (3) process data → (4) analyze data → (5) develop & communicate conclusions → (6) follow up.**

- **Inputs vs. outputs trap:** communicating with management, suppliers, customers, competitors is an **input collected** in step 2. **Common-size statements are an OUTPUT of the processing step (3)** — not a collection input.
- The same framework serves equity valuation, lending/credit decisions, or assessing an accounting-standard change.

## Earnings Sources & ROE — Extended DuPont (LOS 12.b–12.c)

**5-factor extended DuPont:**

`ROE = (NI/EBT) × (EBT/EBIT) × (EBIT/Rev) × (Rev/Assets) × (Assets/Equity)`

ordered as **tax burden × interest burden × EBIT margin × asset turnover × financial leverage**.

A weak driver (e.g. falling EBIT margin) can be **masked** by higher turnover or leverage — decomposition exposes it. Higher **tax-burden / interest-burden ratios** mean the effective tax rate / interest drag **decreased**.

**Adjusting for equity-method associates** (20–50% stakes): remove the associate's **equity income from earnings** and the **investment from total assets** to see the parent **standalone**:
- Equity income removed → **earnings ↓ and net profit margin ↓** (if associate profitable).
- Investment asset removed → smaller denominator → **total asset turnover ↑**.
- **Do NOT adjust financial leverage** unless told how the investment was financed — assume same capital structure as the parent (key Professor's-Note trap).
- Analysts also strip **unusual items** (restructuring, litigation, goodwill impairment) from EBIT.

## Asset Base & Capital Structure (LOS 12.b)

- **Asset base**: examine **common-size** balance sheet over time. Watch rising **goodwill** (29% of assets here = many acquisitions) — no longer amortized, so a future **impairment** risk.
- **Capital structure**: the leverage ratio alone hides the *nature* of leverage:
  - **More burdensome**: financial/bond liabilities (can trigger **default** or covenant/**technical default** if unpaid).
  - **Less burdensome**: pension/employee-benefit obligations, deferred taxes, restructuring provisions (may never require cash).
- **Working capital**: current/quick ratios, **defensive interval**, and the **cash conversion cycle** (DSO + DOH − days payables). CCC falling 31.0 → 15.5 days = better WC management (faster collections, faster inventory turns, slower payments).

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- Commodity traders often report very high revenue and thin margins, so asset turnover, working-capital intensity, and financing capacity can matter more than headline sales growth.
- Inventory is both an operating asset and a trading position. Rising inventories may signal strategic storage economics, delayed sales, weak demand, or a speculative carry trade; the analyst has to reconcile inventory growth with the futures curve, hedges, and financing cost.
- Margin calls on futures and swaps can create large short-term cash needs even when the physical hedge is economically sound. CFO can therefore be volatile because collateral timing and physical settlement timing do not always match.
- Trade finance, letters of credit, borrowing-base facilities, repurchase agreements, and supplier/customer advances can be as important as reported debt. Read liquidity notes and covenant disclosures before judging leverage from the balance sheet alone.
- Fair-value gains on derivatives can improve earnings before cash is realized, while basis losses or inventory write-downs may appear later. Cash conversion and hedge documentation are central to earnings-quality analysis.

## Capital Allocation — Segment Analysis (LOS 12.b)

A **segment** = >10% of revenue **or** assets, distinct in risk/return. Use segment disclosures to judge where capital goes.

- **CapEx%-to-Assets% ratio** = (segment's % of total CapEx) / (segment's % of total assets).
  - **> 1** → firm is **growing** that segment (over-investing relative to its asset share).
  - **< 1** → firm is **shrinking** it.
- **Over-allocation red flag**: a segment with a **low/declining EBIT margin** but a **high CapEx%/Assets% ratio** (here: "specialty products") → company-wide returns may suffer.
- EBIT (accrual) is a weak cash proxy → approximate **segment cash flow ≈ EBIT + D&A**, then compute **cash operating return on average assets** = CF / average total assets.

## Earnings Quality & Cash Flow Analysis (LOS 12.d–12.e)

**Earnings quality** = persistence/sustainability; earnings closer to operating cash flow are higher quality (accruals are easier to manipulate). Measure via the **accruals ratio** — **lower = higher quality**.

**Net Operating Assets (NOA)** = operating assets − operating liabilities, where
- operating assets = total assets − cash & marketable securities;
- operating liabilities = total liabilities − total debt (ST + LT).

| Approach | Aggregate accruals | Accruals ratio |
|---|---|---|
| **Balance sheet** | `NOA_end − NOA_begin` | accruals / **average NOA** |
| **Cash flow** | `NI − CFO − CFI` | accruals / average NOA |

- **CFF is excluded** (it reflects financing decisions, not operating/investing earnings persistence).
- The two ratios can differ (acquisitions, FX, classification differences). **Wide swings** in the ratio hint at **manipulation**.
- **Cash Generated from Operations (CGO)** = CFO **+ cash interest paid + cash taxes paid** (add back, because interest & taxes reduce CFO but not operating income). Then **CGO / operating income** — if > 1, cash confirms earnings (good quality). *(IFRS: if interest is already in CFF, no add-back.)*
- Reinforcing ratios: cash return on assets, cash flow to reinvestment (vs. CapEx), cash flow to total debt, cash flow interest coverage.

## Market Value Decomposition (LOS 12.e)

Find the parent's **standalone (implied) value** by stripping out the associate:

1. **Pro rata value of associate** = associate market cap × ownership % (× FX if foreign).
2. **Implied parent value** = parent market cap − pro rata associate value.
3. **Implied standalone P/E** = implied parent value / (parent NI − equity income from associate).

Worked numbers: Thunderbird cap $137B; Eagle €60B × 30% × $1.40 = **$25.2B**; implied value = $137 − $25.2 = **$111.8B** (81.6%). Implied P/E = $111.8B / ($8B − $0.896B) = **15.7** → a **22% discount** to the S&P's 20.1 (vs. only 15% on the unadjusted 17.1 P/E) → may be **undervalued**. (Convert associate *earnings* at the **average** rate, *market value* at the **year-end** rate.)

## Exam Traps
- Removing an associate: **earnings ↓, margin ↓, asset turnover ↑**, and **leverage unchanged** (don't arbitrarily adjust equity).
- **Common-size statements = processing OUTPUT**, not a data-collection input.
- **Accruals ratio: lower = better** quality. CFF is **not** in the accruals calc; **add back interest & taxes** to get CGO.
- CapEx%/Assets% **> 1 = growing** the segment; pair a **low margin + high ratio** = over-allocation.
- Associate **earnings → average FX**, associate **market value → ending FX**.

## Q&A

### 2026-06-04 — How do you adjust ROE/DuPont for an equity-method associate?
**Q:** When analyzing a parent on a standalone basis, how do you treat income and assets from an equity-method associate, and what happens to the DuPont components?
**A:** Remove the associate's **equity income from the parent's earnings** and the **investment from total assets**. Earnings and **net profit margin fall** (assuming the associate is profitable), while **total asset turnover rises** (smaller asset base). **Leverage is left unchanged** unless the question states how the investment was financed — you assume the same capital structure as the parent, so don't arbitrarily reduce equity. EBIT margin is unaffected if equity income was never in EBIT. This isolates the parent's performance from its own asset base.
Related: [[Intercorporate_Investments]]

### 2026-06-04 — Balance-sheet vs. cash-flow accruals ratio and earnings quality
**Q:** How are the two accruals ratios computed and what do they say about earnings quality?
**A:** **Balance-sheet approach**: aggregate accruals = ΔNOA (NOA = operating assets − operating liabilities; operating assets = total assets − cash & marketable securities; operating liabilities = total liabilities − total debt), divided by **average NOA**. **Cash-flow approach**: accruals = **NI − CFO − CFI** (CFF excluded), also divided by average NOA. **Lower ratio = higher earnings quality**; wide swings suggest manipulation. Confirm quality with **CGO = CFO + cash interest + cash taxes**, then **CGO / operating income > 1** means cash flow supports reported earnings.
Related: [[Quality_of_Financial_Reports]]

### 2026-06-04 — How is implied (standalone) P/E from market value decomposition computed?
**Q:** How do you back out a parent's value and P/E excluding a listed associate?
**A:** Implied parent value = parent market cap − (associate market cap × ownership % × FX). Implied standalone P/E = implied value / (parent NI − equity income from the associate). Example: $137B − (€60B × 30% × $1.40 = $25.2B) = $111.8B implied value; ÷ ($8B − $0.896B) = **15.7×**, a deeper discount to the market multiple than the unadjusted P/E — signalling possible undervaluation. Convert associate earnings at the **average** rate and its market value at the **ending** rate.
Related: [[Market_Based_Valuation]]
