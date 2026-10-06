---
aliases: [Residual Income, Economic Value Added, EVA, MVA, Residual Income Model, Clean Surplus]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V5 LM5 (October 2026 errata applied); Schweser Book 3, Module 21, LOS 21.a-21.k
---

# Residual Income (RI) Valuation

## Concept (21.a)
Residual income = earnings **in excess of the equity charge** (the cost of equity capital). A firm creates value only when it earns **above its cost of equity**.
- `RI_t = NI_t − (r × B_(t−1)) = (ROE − r) × B_(t−1)`, where B = book value of equity.
- **EVA** = `NOPAT − (WACC × invested capital)` = `EBIT(1 − t) − WACC × capital`.
  - **Worked example (Schweser):** NOPAT $2,100, WACC 14.2%, capital $18,000 → `$WACC = 0.142 × 18,000 = $2,556`; `EVA = 2,100 − 2,556 = −$456` (destroyed value that year).
- **MVA** = market value − book value of (total) capital.
- **Uses of RI models (21.b)**: equity valuation **and** measuring internal corporate performance and setting **executive compensation** (EVA-style).
- Per-share forecast: `RI_t = E_t − r × B_(t−1)` = `(ROE_t − r) × B_(t−1)` — **beginning** book value.

## Valuation Model (21.c, 21.f)
- `V0 = B0 + Σ RI_t / (1 + r)^t` — current book value plus PV of future residual income.
- **Single-stage (constant growth)**: `V0 = B0 + [(ROE − r) × B0] / (r − g)`.
- **Justified P/B** = `1 + (ROE − r)/(r − g) = (ROE − g)/(r − g)`.
  - **Worked example (Schweser):** ROE 14%, r 8%, g 4% → `P/B = (0.14 − 0.04)/(0.08 − 0.04) = 2.5`.
- Implied growth (21.g): from `P0 = B0 + (ROE − r)B0/(r − g)` → `g = r − B0(ROE − r)/(P0 − B0)`. The market's implied growth in RI rises with P/B.

## Two-Stage RI with a Terminal Price Premium (21.f)
`V0 = B0 + Σ_{t=1..T} RI_t/(1+r)^t + (P_T − B_T)/(1+r)^T` — the last term is the **premium over book value** expected at the horizon. If RI is expected to fade to zero by T, `P_T − B_T = 0`.

## Multistage RI & Continuing Residual Income (21.f, 21.h)
- **Multistage RI**: forecast RI explicitly for T periods, then add a **continuing (terminal) residual income** value at the horizon: `V0 = B0 + Σ_{t=1}^{T-1} RI_t/(1+r)^t + [ RI_T / (1 + r − ω) ] / (1+r)^{T-1}`.
- **Persistence factor ω** (0 ≤ ω ≤ 1) models the decay of terminal RI as competition erodes excess returns:
  - ω = 1 → RI persists unchanged **forever** (terminal RI is a level perpetuity at the equity charge).
  - ω = 0 → RI **drops to zero** immediately after the forecast horizon (terminal value = 0).
  - Higher ω → larger final-stage RI → higher valuation.
  - **Empirical anchor (curriculum):** Dechow et al. estimated ω ≈ **0.62** (≈ 38%/yr decay) on 1976–1995 data.
- **Drivers of persistence (Dechow/Bauman):**

| Lower ω (RI fades fast) | Higher ω (RI persists) |
|---|---|
| Extreme accounting ROE | Low dividend payout |
| Large special / non-recurring items | High historical RI persistence in the industry |
| Large accounting accruals | Strong market-leadership position |

- A separate multistage variant lets **ROE fade to r** explicitly each period; once ROE = r, RI = 0 and the terminal value is **zero**.
- **The four common continuing-RI assumptions (official)**: (1) RI continues **indefinitely at a positive level** (variant: grows with inflation, i.e., constant in real terms); (2) RI is **zero** from the terminal year onward; (3) RI **declines to zero** as ROE reverts to the cost of equity; (4) RI **declines to some mean level**.

> **Tobin's q** (closely related concept): `q = (market value of debt + equity) / replacement cost of total assets`. Like justified P/B it rises with asset productivity, but it uses **total capital** in the numerator and **replacement cost of total assets** (not equity book value) in the denominator. Theory: q → 1 as economic profits compete away. (Hard to compute — replacement costs are rarely observable.)

## Comparison to DDM / FCF (21.i)
- RI recognizes value **earlier** (much of the value is in current book value), so it relies **less on the uncertain terminal value** than DDM/FCF — useful when terminal value is hard to estimate.
- Theoretically gives the **same** value as DDM/FCF with consistent assumptions.

## Strengths, Weaknesses, Accounting (21.j, 21.k)
- **Strengths (official)**: terminal value is a **small** share of total value; uses **readily available accounting data**; works **without dividends or near-term positive FCF**; works when **cash flows are unpredictable**; focuses on economic profitability.
- **Weaknesses**: accounting data can be **manipulated** by management; inputs may need **significant adjustments**; requires the **clean surplus relation** (`B_t = B_(t−1) + E_t − D_t`) to hold or be adjusted for; relies on book value and ROE not being distorted.
- **Most appropriate when**: no dividends or an unpredictable dividend pattern; **negative FCF for many years** but positive FCF expected eventually; **great uncertainty about the terminal value**. Least appropriate when clean surplus is badly violated or book value and ROE are unpredictable.
- **Fundamental drivers** of RI: **book value of equity** and **ROE**. RI valuation is most closely related to **P/B**: PV of expected RI > 0 ⇔ justified P/B > 1.
- **Accounting adjustments (21.k)**:
  - **Clean surplus violations** — items booked directly to equity (OCI: FX translation, some pension remeasurements, FVOCI gains/losses) → adjust net income to comprehensive income so RI and book value reconcile.
  - **Book value adjustments** — off-balance-sheet items, differences from **fair value** (e.g., LIFO inventory, pension positions), and the **amortization of certain intangible assets**.
  - **Earnings adjustments** — strip **non-recurring items** misclassified as recurring; watch aggressive accounting and differences in international standards.

## Exam Traps
- `RI = (ROE − r) × beginning book value`; the charge uses **beginning-of-period** equity.
- **Justified P/B = (ROE − g)/(r − g)** — same as the relative-value result.
- RI puts most value in **current book value**, reducing terminal-value dependence (vs DDM/FCF).
- **Clean surplus** must hold; OCI items (FX, FVOCI, pension remeasurements) violate it.
- **Persistence factor** sits in the terminal term as `RI_T/(1 + r − ω)`, NOT `/(r − g)`. ω = 1 → perpetuity of RI; ω = 0 → terminal value zero. Don't confuse ω-decay with the ROE-fades-to-r variant (terminal = 0).
- **Tobin's q** uses **replacement cost of total assets** and **total capital** — not equity book value.
- Two-stage RI terminal term can be written as the **premium over book at T**: `(P_T − B_T)/(1+r)^T`.
- **Four continuing-RI assumptions**: persists (positive level / constant real), zero, declines to zero (ROE → r), declines to a mean level.

## Q&A

### 2026-06-03 — Why does RI rely less on terminal value than DDM/FCF?
**Q:** With consistent assumptions RI gives the same value as DDM — so why prefer it?
**A:** Because RI **front-loads** value: `V0 = B0 + Σ PV(RI)`, and current book value B0 is a known, large chunk of value. DDM/FCF push most value into a distant, uncertain **terminal value**, so RI is less sensitive to terminal-value error — valuable when the firm pays no dividends, has negative FCF, or the terminal value is hard to pin down, **provided accounting quality is high**.
Related: [[Free_Cash_Flow_Valuation]]

### 2026-06-03 — Clean surplus violations
**Q:** What is the clean-surplus requirement and what breaks it?
**A:** Clean surplus: `ending BV = beginning BV + NI − dividends`, i.e. **all income flows through the income statement**. It breaks when items bypass NI and go **directly to equity / OCI**: foreign-currency translation (CTA), some pension remeasurements, and FVOCI gains/losses. These dirty-surplus items must be adjusted for, or the RI model misstates value. (EVA recap: `NOPAT − WACC×capital`; MVA = market − book capital.)
Related: [[Multinational_Operations]]

### 2026-06-04 — Continuing RI and the persistence factor ω
**Q:** How does the persistence factor enter a multistage RI valuation, and what does ω = 0.62 mean?
**A:** Forecast RI explicitly through year T−1, then capitalize terminal RI with the persistence factor: `V0 = B0 + Σ PV(RI_t) + PV[ RI_T/(1 + r − ω) ]`. **ω = 1** → RI continues unchanged forever; **ω = 0** → RI vanishes after the horizon (terminal value 0); higher ω → higher value. The curriculum's empirical estimate **ω ≈ 0.62** implies RI decays ~38%/year (mean reversion of ROE toward r). Low payout and high industry persistence raise ω; extreme ROE, large special items, and big accruals lower it. Trap: the denominator is `(1 + r − ω)`, **not** `(r − g)`.
Related: [[Free_Cash_Flow_Valuation]]
