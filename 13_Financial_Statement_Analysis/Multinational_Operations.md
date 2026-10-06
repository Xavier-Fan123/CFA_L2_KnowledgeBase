---
aliases: [Multinational Operations, Foreign Currency Translation, Current Rate Method, Temporal Method, CTA, Functional Currency]
tags: [CFA-L2, fsa, concept, fx]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V3 LM3; Schweser Book 2, Module 9, LOS 9.a-9.j
---

# Multinational Operations (Foreign Currency Translation)

## Three Currencies (9.a)
- **Local currency**: currency of the country where the subsidiary operates.
- **Functional currency**: the primary currency of the subsidiary's economic environment (management determines it).
- **Presentation (reporting) currency**: currency of the parent's financial statements.

**Method is chosen by the relationship of functional currency:**

| Situation | Method | Translate from → to |
|------|------|------|
| Functional = **local** (≠ parent's) | **Current rate method** (translation) | local → presentation |
| Functional = **parent's presentation** | **Temporal method** (remeasurement) | local → functional/presentation |
| Local = highly **inflationary** | US GAAP: temporal; IFRS: restate for inflation then current rate | — |

## Foreign Currency Transactions (9.b) — transaction exposure
- An export sale (import purchase) on account denominated in a foreign currency is recorded at the **transaction-date** rate. Any change in the functional-currency value of the receivable (payable) before settlement is a **foreign currency transaction gain or loss in net income**.
- If a **balance sheet date** falls between transaction and settlement, the receivable/payable is retranslated at the balance-sheet-date rate and the gain/loss goes to income even though it is **unrealized** (it may reverse by settlement).

| Position | Foreign currency **strengthens** | Foreign currency **weakens** |
|---|---|---|
| FC **receivable** (export) | **Gain** | Loss |
| FC **payable** (import) | Loss | **Gain** |

- Companies must disclose the **net FX gain/loss in income**, but may report transaction gains/losses in **operating or non-operating** income → operating margins may not be comparable across companies.

## Current Rate Method (Translation)
- **Assets & liabilities**: **current** (period-end) rate.
- **Common stock**: **historical** rate.
- **Income statement (revenues/expenses)**: **average** rate.
- **Dividends**: rate when declared.
- Other equity items: **historical** rates.
- Balancing item = **Cumulative Translation Adjustment (CTA)** in **equity (OCI)**. The CTA for a foreign entity is **transferred (recycled) to net income when that entity is sold or otherwise disposed of**.
- Exposure = **net assets** (shareholders' equity). Exposure disappears only if assets = liabilities (no equity) — rarely achievable.

## Temporal Method (Remeasurement)
- **Monetary** assets/liabilities (cash, receivables, payables, debt) **and non-monetary items measured at current value** (e.g., at fair value): **current** rate.
- **Non-monetary** assets/liabilities carried at historical cost (inventory at cost, PP&E, intangibles) & **equity**: **historical** rates.
- COGS and depreciation: **historical** rates (tied to non-monetary assets); most other IS items: average.
- Balancing item = **remeasurement gain/loss** in the **income statement (net income)**.
- Exposure = **net monetary assets** (usually net monetary **liability** position), adjusted for non-monetary items at current value. Easier to manage than under the current rate method: **match monetary assets with monetary liabilities** and the exposure is zero (e.g., fund the subsidiary with equity instead of local debt).

## Quick Comparison

| Dimension | Current rate | Temporal |
|---|---|---|
| When | Functional = local | Functional = parent's |
| BS rate for non-monetary | Current | Historical |
| IS gain/loss goes to | **Equity (CTA)** | **Net income** |
| Exposure | Net assets | Net monetary assets |
| Pure ratios (no rate mixing) | Preserved | Distorted |

## Rate-Direction Effects (9.c, 9.f)
- **Current rate method, depreciating local currency** → CTA is a **loss** (negative); translated assets/sales shrink. Appreciating local currency → CTA gain.
- **Temporal, depreciating local currency, net monetary liability** → remeasurement **gain** in NI.

**Foreign currency STRENGTHENS against the parent's currency (official Canadaco Example 6; reverse everything if it weakens):**

| Translated amount | Current rate method | Temporal method (net monetary **liability**) |
|---|---|---|
| Revenues, assets, liabilities | Higher | Higher |
| Net income | **Higher** | **Lower** (remeasurement loss in NI) |
| Equity | **Higher** (positive CTA) | **Lower** (loss flows through retained earnings) |

- Canadaco, temporal: a C$3,000,000 note payable while the C$ rose from 0.70 to 0.80 → a **EUR 300,000** loss (3,000,000 × 0.10) that equity financing would have avoided.

**Ratio effects (official Canadaco comparison):**
- **Current rate** method preserves ratios built **only from the balance sheet or only from the income statement** — current ratio, debt-to-assets, debt-to-equity, interest coverage, gross/operating/net margins. It **distorts mixed ratios** (turnover ratios, ROA, ROE), because balance-sheet items use the current rate and income items the average rate.
- **Temporal** method distorts almost every ratio, and the **direction cannot be generalized**.
- **Receivables turnover is identical under both methods** (sales at average and receivables at current under each).

## Hyperinflationary Economies (9.g)
- In a highly inflationary economy the subsidiary's **functional currency is irrelevant** to the choice of method.
- **US GAAP**: highly inflationary = **cumulative three-year inflation > 100%** (≈ 26% a year; apply with judgment, the trend matters too) → remeasure with the **temporal** method as if the functional currency were the reporting currency; **no inflation restatement**. This avoids the **"disappearing plant" problem** — translating historical-cost assets at ever-weaker current rates would shrink them toward zero.
- **IFRS**: first **restate** the local statements for local inflation (**IAS 29**), then translate **everything at the current rate** (IAS 21). IAS 21 gives no specific threshold; IAS 29 treats cumulative inflation approaching or exceeding 100% over three years as an indicator. The curriculum calls this the approach that best represents economic reality (Turkish land example: restate-then-translate leaves the land at about its original USD value).

## Disclosures and Using Both Methods (9.e, 9.j)
- A parent can use **both** methods at once — current rate for subsidiaries whose functional currency is local, temporal for those whose functional currency is the parent's.
- Required disclosure: the **total translation gain/loss in income** and the **CTA in equity**. There is **no** requirement to split the income amount between transaction gains/losses and temporal-method remeasurement.
- **Clean-surplus adjustment**: add the change in CTA reported in equity to net income to get a comprehensive measure of income.
- Use segment and MD&A disclosures (revenue and earnings by currency, sensitivity to rate changes) to judge how a company's countries of operation expose results to currency moves (9.j).

## Worked Example — Same Balance Sheet, Two Methods (LOS 9.e)
*(curriculum Amerco/Spanco; functional vs presentation differ; rate falls from 1.00 H to 0.80 C)*

Subsidiary BS (in US$, the local currency here): Cash 3,000; Inventory 12,000; Notes payable 10,000; Common stock 5,000 (issued at the 1.00 historical rate). Rate moves to **0.80** at period-end.

**Current rate method (all assets & liabilities @ current 0.80; equity @ historical):**

| Item | Rate | Δ in presentation value |
|---|---|---|
| Cash | 0.80 C | −600 |
| Inventory | 0.80 C | −2,400 |
| Notes payable | 0.80 C | +1,000 (liability shrinks) |
| **Net = CTA → equity (OCI)** | | **−2,000 loss** |

**Temporal method (only MONETARY items @ current; inventory & equity @ historical):**

| Item | Rate | Δ in presentation value |
|---|---|---|
| Cash | 0.80 C | −600 |
| Inventory | **1.00 H** | 0 (non-monetary, held at historical) |
| Notes payable | 0.80 C | +1,000 |
| **Net = remeasurement → net income** | | **+400 gain** |

**Read-through:** with a **net asset** exposure and a **falling** rate, the current rate method books a **−2,000 CTA loss in equity**. Switching to temporal freezes inventory at historical cost, leaving a **net monetary liability** position (notes payable 10,000 > cash 3,000) → the same rate fall produces a **+400 remeasurement gain in net income**. Same facts, opposite sign, different statement — the core LOS 9.e/9.f trap.

## Other Effects (9.g, 9.h, 9.i)
- **Hyperinflationary** economies (US GAAP): use temporal (functional = parent's). IFRS: restate local statements for inflation, then translate at the **current** rate.
- **Effective tax rate** is affected by the mix of country tax rates and currency movements.
- Sales-growth **sustainability**: distinguish organic (price/volume) growth from currency-driven and acquisition-driven growth.

### Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- A commodity group may operate in many local currencies while its real economic currency is **USD**, because purchase contracts, sale contracts, hedges, debt, and inventory marks are often USD-linked. The functional-currency decision should follow the cash-flow economics, not the legal location of the subsidiary.
- Under the temporal method, non-monetary inventory can sit at historical exchange rates while monetary debt, receivables, and payables move at current rates. For a commodity subsidiary with large stock and trade finance, this can create net-income volatility that is accounting-driven rather than a new physical trading result.
- Current-rate translation can preserve local ratios but move CTA through equity. That matters when management says operating performance is stable while reported equity, leverage, or book value changes because the local currency moved.
- Separate **transaction exposure** from **translation exposure**. A USD-priced cargo sold by a local-currency subsidiary may have limited commodity-price exposure after hedging but still create local tax, payroll, freight, and working-capital FX exposure.
- Intercompany funding and transfer pricing can change the apparent net monetary asset/liability position. For commodity groups, look for whether USD loans, local receivables, and inventory financing create natural hedges or concentrate FX gains/losses in one entity.

## Exam Traps
- Translation gain/loss location: **current rate → equity (CTA)**; **temporal → income statement**.
- "Translation" = current rate method; "remeasurement" = temporal method.
- Under temporal with a net **monetary liability** position, a **weakening** local currency produces a **gain**.
- Current rate method keeps **pure** balance-sheet and pure income-statement ratios intact, but **turnover and return ratios still change** (balance sheet at current, income statement at average). Receivables turnover is the one ratio that is the same under both methods.
- Foreign currency **receivable** + foreign currency **strengthens** → **transaction gain**; FC **payable** + FC strengthens → loss.
- **CTA is recycled** into net income when the foreign subsidiary is sold.
- US GAAP "highly inflationary" = cumulative **3-year inflation > 100%** → temporal method; IFRS → restate for inflation, then current rate.

## Q&A

### 2026-06-03 — Temporal method, net monetary liability, weakening currency → gain?
**Q:** Why does a depreciating local currency produce a remeasurement **gain** under the temporal method?
**A:** Temporal exposure = **net monetary assets**, and most firms hold a **net monetary liability** position (debt + payables > cash + receivables). When the local currency weakens, those monetary **liabilities** are worth **less** in the parent's currency → a gain. The remeasurement gain/loss flows through **net income** (unlike the current-rate CTA, which sits in equity/OCI). Mirror case: net monetary asset + weakening currency → loss.
Related: [[Currency_Exchange_Rates]]

### 2026-06-03 — Which translation method preserves financial ratios?
**Q:** Does translation distort local-currency ratios under the current rate or the temporal method?
**A:** The **current rate method preserves** pure local-currency ratios because every balance-sheet item is translated at the **same** current rate (income statement at the average rate), so ratios built from same-statement items are unchanged — but **mixed** ratios (turnover, ROA, ROE) still change because the balance sheet uses the current rate and the income statement the average rate. The **temporal method distorts** ratios because it **mixes** current rates (monetary items) with historical rates (non-monetary items, COGS, depreciation). Quick tell: current rate → functional = local; temporal → functional = parent's; gain/loss to equity (CTA) vs net income respectively.
Related: [[Intercorporate_Investments]]
