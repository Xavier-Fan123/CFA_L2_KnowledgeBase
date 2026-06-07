---
aliases: [Multinational Operations, Foreign Currency Translation, Current Rate Method, Temporal Method, CTA, Functional Currency]
tags: [CFA-L2, fsa, concept, fx]
date: 2026-06-03
status: evergreen
source: Schweser Book 2, Module 9, LOS 9.a-9.j
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

## Current Rate Method (Translation)
- **Assets & liabilities**: **current** (period-end) rate.
- **Common stock**: **historical** rate.
- **Income statement (revenues/expenses)**: **average** rate.
- **Dividends**: rate when declared.
- Balancing item = **Cumulative Translation Adjustment (CTA)** in **equity (OCI)**.
- Exposure = **net assets** (shareholders' equity).

## Temporal Method (Remeasurement)
- **Monetary** assets/liabilities (cash, receivables, payables, debt): **current** rate.
- **Non-monetary** assets/liabilities (inventory, PP&E, intangibles) & **equity**: **historical** rates.
- COGS and depreciation: **historical** rates (tied to non-monetary assets); most other IS items: average.
- Balancing item = **remeasurement gain/loss** in the **income statement (net income)**.
- Exposure = **net monetary assets** (usually net monetary **liability** position).

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
- Current rate method **preserves financial ratios** computed in local currency; temporal distorts them (mixes current and historical rates).

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
- Current rate method keeps local-currency ratios intact; temporal does not.

## Q&A

### 2026-06-03 — Temporal method, net monetary liability, weakening currency → gain?
**Q:** Why does a depreciating local currency produce a remeasurement **gain** under the temporal method?
**A:** Temporal exposure = **net monetary assets**, and most firms hold a **net monetary liability** position (debt + payables > cash + receivables). When the local currency weakens, those monetary **liabilities** are worth **less** in the parent's currency → a gain. The remeasurement gain/loss flows through **net income** (unlike the current-rate CTA, which sits in equity/OCI). Mirror case: net monetary asset + weakening currency → loss.
Related: [[Currency_Exchange_Rates]]

### 2026-06-03 — Which translation method preserves financial ratios?
**Q:** Does translation distort local-currency ratios under the current rate or the temporal method?
**A:** The **current rate method preserves** pure local-currency ratios because every balance-sheet item is translated at the **same** current rate (income statement at the average rate), so ratios built from same-statement items are unchanged. The **temporal method distorts** ratios because it **mixes** current rates (monetary items) with historical rates (non-monetary items, COGS, depreciation). Quick tell: current rate → functional = local; temporal → functional = parent's; gain/loss to equity (CTA) vs net income respectively.
Related: [[Intercorporate_Investments]]
