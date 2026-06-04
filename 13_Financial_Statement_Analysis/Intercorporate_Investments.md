---
aliases: [Intercorporate Investments, Equity Method, Acquisition Method, Consolidation, Goodwill, Financial Assets]
tags: [CFA-L2, fsa, concept]
date: 2026-06-03
status: evergreen
source: Schweser Book 2, Module 7, LOS 7.a-7.c
---

# Intercorporate Investments

Classification is driven by **degree of influence/control**, which dictates the accounting method.

| Category | Influence | Typical ownership | Method |
|------|------|------|------|
| Investment in **financial assets** | None | < 20% | FVPL / FVOCI / amortized cost |
| Investment in **associates** | Significant | 20–50% | **Equity method** |
| **Joint venture** | Shared control | — | **Equity method** (IFRS) |
| **Business combination** | Control | > 50% | **Acquisition method (consolidation)** |
| **SPE / VIE** | Control via risk/returns, not votes | — | **Consolidate** (sponsor / primary beneficiary) |

## Financial Assets (IFRS 9)
- **Amortized cost**: debt held to collect contractual cash flows.
- **FVOCI**: debt held to collect AND sell (unrealized G/L → OCI; interest/impairment → P&L). Equity may
  irrevocably elect FVOCI (no recycling to P&L on sale).
- **FVPL**: default for equity and trading; all changes through P&L.
- US GAAP: equity securities generally FVPL.

## Equity Method (Associates / JVs)
- "**One-line consolidation**": investment recorded at cost, then **+ pro-rata share of investee net
  income** (income statement), **− dividends received** (return of capital, reduces the carrying value).
- Investment account on the balance sheet = cost + cumulative share of earnings − dividends.
- **Excess purchase price** over share of book value allocated to identifiable assets (depreciated →
  reduces equity income) and **goodwill** (not amortized; tested for impairment).
- Watch for: upstream/downstream **unrealized profits** eliminated pro-rata; impairment if value
  declines.

## Business Combinations — Acquisition Method
- **Consolidate**: 100% of subsidiary assets, liabilities, revenues, expenses; eliminate intercompany.
- **Non-controlling interest (NCI)**: minority share of subsidiary equity and net income, reported
  within consolidated equity / below consolidated net income.
- **Goodwill** = purchase price − fair value of identifiable net assets acquired.
  - **Full goodwill** (US GAAP / IFRS option): based on fair value of the whole entity.
  - **Partial goodwill** (IFRS option): based on the **acquirer's share** only → lower goodwill, lower
    equity, lower NCI.
- Goodwill is **not amortized**; tested for impairment.
- **Worked example (Schweser – Wood/Pine):** Wood pays $450m for **75%** of Pine; FV of Pine's
  identifiable net assets = $560m.
  - **Full goodwill** = implied total FV − identifiable net assets = `($450/0.75 = $600m) − $560m = $40m`;
    NCI = `25% × $600m = $150m`.
  - **Partial goodwill** = price − acquirer's share of net assets = `$450m − 0.75×$560m = $30m`;
    NCI = `25% × $560m = $140m`.
  - The `$10m` goodwill difference is mirrored by the `$10m` NCI difference.
- **Full goodwill → higher total assets and equity → lower ROA and ROE** than partial goodwill.

### Acquisition-Method Mechanics (details the LOS expects)
- **Consideration** is measured at **fair value**, including the **acquisition-date fair value of any
  contingent consideration** (earn-outs).
- **Direct acquisition costs** (legal, valuation, advisory, consulting fees) are **expensed as incurred**
  — they are **not** capitalized into goodwill.
- **Identifiable assets/liabilities** (tangible and intangible) recorded at **fair value** at the
  acquisition date, including assets the acquiree never recognized internally (e.g., internally developed
  brand names, patents, technology).
- **Contingent liabilities**: IFRS recognizes them if **fair value is reliably measurable**; US GAAP
  recognizes only those that are **probable AND reasonably estimable**. Expected (but not obligated)
  costs — e.g., planned restructuring — are **not** liabilities at acquisition; expensed when incurred.
- **Indemnification assets** (seller contractually covers a contingency outcome) are recognized at the
  same time and on the same basis as the indemnified item.
- **Pooling-of-interests is prohibited** — all business combinations use the acquisition method under
  both IFRS and US GAAP, which substantially converges the two.

## Special Purpose & Variable Interest Entities (SPE / VIE) — part of LOS 7.a/7.b
- An **SPE/VIE** is created by a **sponsor** for a narrow purpose (often securitizing assets to move them
  off the balance sheet). The defining feature: control is **not** based on **voting interest** because
  equity holders lack sufficient at-risk capital or a controlling financial interest.
- **IFRS (IFRS 10 / SIC-12)**: consolidate when the **substance** of the relationship indicates
  **control** — the sponsor (1) can direct the entity's financial/operating policy AND (2) is exposed to
  **variable returns** from it.
- **US GAAP (ASC 810)**: two-component model (voting interest + variable interest). The **primary
  beneficiary** of a VIE **must consolidate** it regardless of voting interest. Primary beneficiary =
  the party that absorbs the **majority of expected losses**, receives the **majority of expected
  residual returns**, or both.
- **Securitization** (e.g., selling receivables to an SPE for cash) can be structured to keep the SPE
  off the sponsor's balance sheet, **understating reported leverage** — a classic analyst red flag.
  If consolidation is required, the SPE's assets and (non-recourse) debt come back on-balance-sheet.

## Effect on Statements & Ratios (7.c)
- Equity method vs consolidation: **net income is identical**, but consolidation grosses up revenue,
  assets, and liabilities → **lower margins, higher leverage-looking ratios** under consolidation;
  equity method understates the asset/liability base.
- Higher ownership method generally raises reported revenue/assets but the **same bottom-line income**.

## Exam Traps
- Equity-method dividends **reduce** the investment account (not income).
- Net income is the **same** under equity method and full consolidation; ratios differ because of the
  grossed-up base.
- **Partial goodwill** (IFRS) < full goodwill → lower total assets and lower NCI.
- FVOCI **debt** recycles to P&L on sale; FVOCI **equity** election does **not** recycle.
- **SPE/VIE**: control is by **risk/returns, not votes** — IFRS consolidates on **substance/control**;
  US GAAP consolidates if you are the **primary beneficiary**. Off-balance-sheet securitization
  **understates leverage** until consolidation pulls the assets/debt back on.
- **Acquisition costs are expensed** (not added to goodwill); **contingent consideration** is included
  in the purchase price at **fair value**.

## Q&A

### 2026-06-03 — Full vs partial goodwill: which ratios change, and how?
**Q:** An acquirer buys 75% of a target. How do full vs partial goodwill differ, and what's the ratio impact?
**A:** **Full goodwill** = (price ÷ % acquired) − FV of identifiable net assets; **partial goodwill** =
price − (% acquired × FV of identifiable net assets). Full ≥ partial, and the goodwill difference exactly
equals the NCI difference (full NCI uses % × full entity FV; partial NCI uses % × net-asset FV). Because
full goodwill grosses up **both** total assets and equity, it produces **lower ROA and ROE** than partial
goodwill. Net income is identical under both. (Wood/Pine: full GW $40m / NCI $150m vs partial GW $30m /
NCI $140m.)
Related: [[Quality_of_Financial_Reports]]

### 2026-06-03 — Equity method vs consolidation: same income, different ratios?
**Q:** If net income is identical, why do equity method and full consolidation give different ratios?
**A:** The equity method is a **one-line consolidation**: only the pro-rata share of net income hits the
income statement and the net investment sits as one asset line — revenue, total assets, and total
liabilities are **understated** relative to the economic reality. Full consolidation **grosses up** 100%
of the sub's revenue, assets, and liabilities (with NCI for the minority). So consolidation shows **lower
margins and higher apparent leverage**, while net income, total equity attributable to the parent, and ROE
are the **same**. Trap: equity-method dividends **reduce the carrying value of the investment**, they are
not income.
Related: [[Multinational_Operations]]

### 2026-06-04 — When must a sponsor consolidate an SPE/VIE, and why does it matter?
**Q:** A company sets up a special purpose entity to securitize receivables. When is it consolidated, and
what is the analytical concern?
**A:** Control of an SPE/VIE is **not** based on voting interest. **IFRS (IFRS 10/SIC-12)** requires
consolidation when the **substance** shows control — the sponsor directs the entity's policies and is
exposed to its **variable returns**. **US GAAP (ASC 810)** requires the **primary beneficiary** — the
party absorbing the majority of expected losses and/or residual returns — to consolidate the VIE
regardless of votes. The concern: firms historically used SPEs to move debt **off-balance-sheet**
(securitization), **understating leverage**; consolidation pulls the SPE's assets and (often non-recourse)
debt back on, raising reported leverage. Trap: **direct acquisition costs are expensed**, and **contingent
consideration** is part of the purchase price at fair value.
Related: [[Quality_of_Financial_Reports]]
