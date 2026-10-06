---
aliases: [Intercorporate Investments, Equity Method, Acquisition Method, Consolidation, Goodwill, Financial Assets]
tags: [CFA-L2, fsa, concept]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V3 LM1 (October 2026 errata applied); Schweser Book 2, Module 7, LOS 7.a-7.c
---

# Intercorporate Investments

Classification is driven by **degree of influence/control**, which dictates the accounting method.

| Category | Influence | Typical ownership | Method |
|------|------|------|------|
| Investment in **financial assets** | None | < 20% | FVPL / FVOCI / amortized cost |
| Investment in **associates** | Significant | 20–50% | **Equity method** |
| **Joint venture** | Shared (joint) control | — | **Equity method** (IFRS and US GAAP) |
| **Business combination** | Control | > 50% | **Acquisition method (consolidation)** |

## Financial Assets (IFRS 9)
- **Amortized cost**: debt whose business-model objective is to **hold to collect** contractual cash flows **and** whose cash flows are **solely payments of principal and interest**.
- **FVOCI**: debt held to collect AND sell (unrealized G/L → OCI; interest/impairment → P&L). Equity may irrevocably elect FVOCI (no recycling to P&L on sale).
- **FVPL**: default for equity and trading; all changes through P&L.
- US GAAP: equity securities generally FVPL.
- IFRS 9 dropped IAS 39's held-for-trading / available-for-sale / held-to-maturity portfolio labels in favor of a **business-model approach** for debt.
- **Reclassification**: **equity — never** (the FVPL/FVOCI choice is irrevocable); **debt — only if the business model changes** (rare). No restatement of prior periods: amortized cost → FVPL remeasures to fair value with the gain/loss **in profit or loss immediately**; FVPL → amortized cost uses the fair value at the reclassification date as the new carrying amount.
- **Impairment**: IFRS 9 moved from an **incurred-loss** to an **expected-credit-loss** model — **12-month** expected losses for performing assets, **lifetime** expected losses for non-performing assets, recognized up front (earlier recognition).

## Equity Method (Associates / JVs)
- "**One-line consolidation**": investment recorded at cost, then **+ pro-rata share of investee net income** (income statement), **− dividends received** (return of capital, reduces the carrying value).
- Investment account on the balance sheet = cost + cumulative share of earnings − dividends.
- **Excess purchase price** over share of book value allocated to identifiable assets (depreciated → reduces equity income) and **goodwill**. Under the equity method, goodwill is embedded in the single investment carrying amount, not presented as a separate asset.
- **Transactions with associates**: the investor defers its **share** of unrealized profit on **upstream** (associate → investor) and **downstream** (investor → associate) sales until the goods are sold to a third party — deferral = ownership % × profit on goods still held by the buyer.
- **Fair value option**: both standards let the investor carry an equity-method investment at fair value — **US GAAP: any entity**; **IFRS: only venture capital organizations, mutual funds, unit trusts and similar entities** (including investment-linked insurance funds). Elected at initial recognition and **irrevocable**; fair-value changes, interest, and dividends go to profit or loss, and no excess purchase price is amortized (no goodwill).
- **Impairment of an equity-method investment**: goodwill sits inside the carrying amount, so the **whole investment** is tested, not the goodwill separately.
  - **IFRS**: needs objective evidence of a loss event; compare **recoverable amount** (higher of value in use and fair value less costs to sell) with carrying amount; **reversals permitted**.
  - **US GAAP**: fair value below carrying amount and the decline is other than temporary → write down to fair value; **reversals prohibited**.
- **Joint ventures**: a contractual arrangement between two or more venturers that establishes **joint control**. **Both IFRS and US GAAP require the equity method** for joint ventures.
- **Proportionate consolidation (rare exception only)**: the curriculum allows it for joint ventures "only under rare circumstances", and the 28 Apr 2026 errata states outright that proportionate consolidation is **not permitted for joint ventures** — the equity method is. Know the mechanics only as a comparison case: the venturer adds its **pro-rata share of each line** of the venture's assets, liabilities, revenues, and expenses; **no noncontrolling interest** is created; net income and equity are the **same** as under the equity method, but **assets, liabilities, revenues, and expenses are all higher** (margins and ROA look lower, leverage higher).

## Business Combinations — Acquisition Method
- **Consolidate**: 100% of subsidiary assets, liabilities, revenues, expenses; eliminate intercompany.
- **Non-controlling interest (NCI)**: minority share of subsidiary equity and net income, reported within consolidated equity / below consolidated net income.
- **Goodwill** = purchase price − fair value of identifiable net assets acquired.
  - **Full goodwill** (US GAAP / IFRS option): based on fair value of the whole entity.
  - **Partial goodwill** (IFRS option): based on the **acquirer's share** only → lower goodwill, lower equity, lower NCI.
- Goodwill is **not amortized**; tested at least annually for impairment, with losses on the income statement.
  - **IFRS (one step)**: goodwill is allocated to **cash-generating units (CGUs)**. Impairment = carrying amount of the CGU − **recoverable amount**. The loss is applied **first to the CGU's goodwill**; once goodwill is zero, the remainder is spread **pro rata over the CGU's other non-cash assets**.
  - **US GAAP (17 Feb 2026 errata)**: goodwill is allocated to **reporting units**. An **optional qualitative assessment** comes first: if it is **more likely than not (> 50%)** that fair value exceeds carrying amount, stop. Otherwise run the **single quantitative test**: carrying amount of the reporting unit (incl. goodwill) vs its fair value; loss = the excess, **capped at the goodwill allocated** to that unit. The old two-step "implied fair value of goodwill" test is gone.
- **Worked example (Schweser – Wood/Pine):** Wood pays $450m for **75%** of Pine; FV of Pine's identifiable net assets = $560m.
  - **Full goodwill** = implied total FV − identifiable net assets = `($450/0.75 = $600m) − $560m = $40m`; NCI = `25% × $600m = $150m`.
  - **Partial goodwill** = price − acquirer's share of net assets = `$450m − 0.75×$560m = $30m`; NCI = `25% × $560m = $140m`.
  - The `$10m` goodwill difference is mirrored by the `$10m` NCI difference.
- **Full goodwill → higher total assets and equity → lower ROA and ROE** than partial goodwill.

### Acquisition-Method Mechanics (details the LOS expects)
- **Consideration** is measured at **fair value**, including the **acquisition-date fair value of any contingent consideration** (earn-outs).
- **Direct acquisition costs** (legal, valuation, advisory, consulting fees) are **expensed as incurred** — they are **not** capitalized into goodwill.
- **Identifiable assets/liabilities** (tangible and intangible) recorded at **fair value** at the acquisition date, including assets the acquiree never recognized internally (e.g., internally developed brand names, patents, technology).
- **Contingent liabilities**: recognize an assumed contingent liability at acquisition when it is a **present obligation from past events** and can be **measured reliably** (e.g., a potential warranty obligation), even if the acquiree did not previously recognize it. Expected (but not obligated) costs — e.g., planned restructuring — are **not** liabilities at acquisition; expensed when incurred.
- **Indemnification assets** (seller contractually covers a contingency outcome) are recognized at the same time and on the same basis as the indemnified item.

## Special Purpose & Variable Interest Entities (SPE / VIE) — part of LOS 7.a/7.b
- An **SPE/VIE** is created by a **sponsor** for a narrow purpose (often securitizing assets to move them off the balance sheet). The defining feature: control is **not** based on **voting interest** because equity holders lack sufficient at-risk capital or a controlling financial interest.
- **IFRS (IFRS 10 / SIC-12)**: consolidate when the **substance** of the relationship indicates **control** — the sponsor (1) can direct the entity's financial/operating policy AND (2) is exposed to **variable returns** from it.
- **US GAAP (ASC 810)**: two-component model (voting interest + variable interest). The **primary beneficiary** of a VIE **must consolidate** it regardless of voting interest. Primary beneficiary = the party with (1) **power to direct the VIE activities that most significantly affect economic performance** and (2) exposure to economics by absorbing the **majority of expected losses**, receiving the **majority of expected residual returns**, or both.
- **Securitization** (e.g., selling receivables to an SPE for cash) can be structured to keep the SPE off the sponsor's balance sheet, **understating reported leverage** — a classic analyst red flag. If consolidation is required, the SPE's assets and (non-recourse) debt come back on-balance-sheet.

## Effect on Statements & Ratios (7.c)
- Equity method vs consolidation: **net income is identical**, but consolidation grosses up revenue, assets, and liabilities → **lower margins, higher leverage-looking ratios** under consolidation; equity method understates the asset/liability base.
- Higher ownership method generally raises reported revenue/assets but the **same bottom-line income**.

## Exam Traps
- Equity-method dividends **reduce** the investment account (not income).
- **Joint venture → equity method** under **both** IFRS and US GAAP. Proportionate consolidation is not the JV default — the 2026 errata corrects a practice solution to say it is **not permitted** for JVs.
- **US GAAP goodwill impairment is no longer two-step.** Optional qualitative screen (more likely than not, > 50%), then one quantitative test: reporting-unit carrying amount (incl. goodwill) vs fair value, loss = excess **capped at allocated goodwill**. The old "implied fair value of goodwill" step was removed by the 17 Feb 2026 errata.
- Net income is the **same** under equity method and full consolidation; ratios differ because of the grossed-up base.
- **Partial goodwill** (IFRS) < full goodwill → lower total assets and lower NCI.
- FVOCI **debt** recycles to P&L on sale; FVOCI **equity** election does **not** recycle.
- IFRS 9: **equity** classifications can never be reclassified; **debt** only on a change of business model, with no restatement of prior periods.
- **Impairment reversals**: IFRS **permits** reversing an equity-method impairment (in line with IAS 36); US GAAP **prohibits** it.
- **Fair value option for associates**: any entity under US GAAP; only venture-capital-type entities (VC, mutual funds, unit trusts) under IFRS.
- **SPE/VIE**: control is by **power + variable economics, not votes** — IFRS consolidates on **substance/control**; US GAAP consolidates if you are the **primary beneficiary**. Off-balance-sheet securitization **understates leverage** until consolidation pulls the assets/debt back on.
- **Acquisition costs are expensed** (not added to goodwill); **contingent consideration** is included in the purchase price at **fair value**.

## Q&A

### 2026-06-03 — Full vs partial goodwill: which ratios change, and how?
**Q:** An acquirer buys 75% of a target. How do full vs partial goodwill differ, and what's the ratio impact?
**A:** **Full goodwill** = (price ÷ % acquired) − FV of identifiable net assets; **partial goodwill** = price − (% acquired × FV of identifiable net assets). Full ≥ partial, and the goodwill difference exactly equals the NCI difference (full NCI uses % × full entity FV; partial NCI uses % × net-asset FV). Because full goodwill grosses up **both** total assets and equity, it produces **lower ROA and ROE** than partial goodwill. Net income is identical under both. (Wood/Pine: full GW $40m / NCI $150m vs partial GW $30m / NCI $140m.)
Related: [[Quality_of_Financial_Reports]]

### 2026-06-03 — Equity method vs consolidation: same income, different ratios?
**Q:** If net income is identical, why do equity method and full consolidation give different ratios?
**A:** The equity method is a **one-line consolidation**: only the pro-rata share of net income hits the income statement and the net investment sits as one asset line — revenue, total assets, and total liabilities are **understated** relative to the economic reality. Full consolidation **grosses up** 100% of the sub's revenue, assets, and liabilities (with NCI for the minority). So consolidation shows **lower margins and higher apparent leverage**, while net income, total equity attributable to the parent, and ROE are the **same**. Trap: equity-method dividends **reduce the carrying value of the investment**, they are not income.
Related: [[Multinational_Operations]]

### 2026-06-04 — When must a sponsor consolidate an SPE/VIE, and why does it matter?
**Q:** A company sets up a special purpose entity to securitize receivables. When is it consolidated, and what is the analytical concern?
**A:** Control of an SPE/VIE is **not** based on voting interest. **IFRS (IFRS 10/SIC-12)** requires consolidation when the **substance** shows control — the sponsor directs the entity's policies and is exposed to its **variable returns**. **US GAAP (ASC 810)** requires the **primary beneficiary** — the party with power to direct the VIE activities that most affect economic performance and exposure to expected losses and/or residual returns — to consolidate the VIE regardless of votes. The concern: firms historically used SPEs to move debt **off-balance-sheet** (securitization), **understating leverage**; consolidation pulls the SPE's assets and (often non-recourse) debt back on, raising reported leverage. Trap: **direct acquisition costs are expensed**, and **contingent consideration** is part of the purchase price at fair value.
Related: [[Quality_of_Financial_Reports]]
