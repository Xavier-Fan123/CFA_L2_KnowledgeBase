---
aliases: [Residual Income, Economic Value Added, EVA, MVA, Residual Income Model, Clean Surplus]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 3, Module 21, LOS 21.a-21.k
---

# Residual Income (RI) Valuation

## Concept (21.a)
Residual income = earnings **in excess of the equity charge** (the cost of equity capital). A firm
creates value only when it earns **above its cost of equity**.
- `RI_t = NI_t − (r × B_(t−1)) = (ROE − r) × B_(t−1)`, where B = book value of equity.
- **EVA** = `NOPAT − (WACC × invested capital)` = `EBIT(1 − t) − WACC × capital`.
  - **Worked example (Schweser):** NOPAT $2,100, WACC 14.2%, capital $18,000 →
    `$WACC = 0.142 × 18,000 = $2,556`; `EVA = 2,100 − 2,556 = −$456` (destroyed value that year).
- **MVA** = market value − book value of (total) capital.

## Valuation Model (21.c, 21.f)
- `V0 = B0 + Σ RI_t / (1 + r)^t` — current book value plus PV of future residual income.
- **Single-stage (constant growth)**:
  `V0 = B0 + [(ROE − r) × B0] / (r − g)`.
- **Justified P/B** = `1 + (ROE − r)/(r − g) = (ROE − g)/(r − g)`.
  - **Worked example (Schweser):** ROE 14%, r 8%, g 4% → `P/B = (0.14 − 0.04)/(0.08 − 0.04) = 2.5`.
- Implied growth: solve the single-stage equation given market P/B (21.g).

## Continuing Residual Income (21.h)
RI is assumed to fade as competition erodes excess returns. A **persistence factor ω** (0 ≤ ω ≤ 1)
models the decay: ω = 1 → RI persists forever; ω = 0 → RI disappears after the forecast horizon.

## Comparison to DDM / FCF (21.i)
- RI recognizes value **earlier** (much of the value is in current book value), so it relies **less on
  the uncertain terminal value** than DDM/FCF — useful when terminal value is hard to estimate.
- Theoretically gives the **same** value as DDM/FCF with consistent assumptions.

## Strengths, Weaknesses, Accounting (21.j, 21.k)
- **Use when**: firm pays no dividends, FCF is negative, terminal value is uncertain, but accounting is
  high quality.
- **Weaknesses**: relies on accounting data that can be manipulated; requires **clean surplus** to hold
  (all income flows through the income statement). Violations: items booked directly to equity (OCI:
  FX translation, some pension and FVOCI items) break clean surplus and require adjustment.

## Exam Traps
- `RI = (ROE − r) × beginning book value`; the charge uses **beginning-of-period** equity.
- **Justified P/B = (ROE − g)/(r − g)** — same as the relative-value result.
- RI puts most value in **current book value**, reducing terminal-value dependence (vs DDM/FCF).
- **Clean surplus** must hold; OCI items (FX, FVOCI, pension remeasurements) violate it.

## Q&A

### 2026-06-03 — Why does RI rely less on terminal value than DDM/FCF?
**Q:** With consistent assumptions RI gives the same value as DDM — so why prefer it?
**A:** Because RI **front-loads** value: `V0 = B0 + Σ PV(RI)`, and current book value B0 is a known,
large chunk of value. DDM/FCF push most value into a distant, uncertain **terminal value**, so RI is
less sensitive to terminal-value error — valuable when the firm pays no dividends, has negative FCF, or
the terminal value is hard to pin down, **provided accounting quality is high**.
Related: [[Free_Cash_Flow_Valuation]]

### 2026-06-03 — Clean surplus violations
**Q:** What is the clean-surplus requirement and what breaks it?
**A:** Clean surplus: `ending BV = beginning BV + NI − dividends`, i.e. **all income flows through the
income statement**. It breaks when items bypass NI and go **directly to equity / OCI**: foreign-currency
translation (CTA), some pension remeasurements, and FVOCI gains/losses. These dirty-surplus items must be
adjusted for, or the RI model misstates value. (EVA recap: `NOPAT − WACC×capital`; MVA = market − book
capital.)
Related: [[Multinational_Operations]]
