---
aliases: [Active Portfolio Management, Information Ratio, Fundamental Law, Information Coefficient, Breadth, Transfer Coefficient, Active Risk]
tags: [CFA-L2, pm, concept, active-management]
date: 2026-06-03
status: evergreen
source: Schweser Book 5, Module 35, LOS 35.a-35.f
---

# Analysis of Active Portfolio Management

## Value Added (35.a)
- **Active return** = `R_P − R_B` (portfolio − benchmark). Value added comes from over/under-weighting relative to the benchmark.
- Can be decomposed into **factor (style) tilts** + **security selection**.

## Sharpe vs Information Ratio (35.b)
- **Sharpe ratio** = `(R_P − R_f) / σ_P` — uses **total** risk; unaffected by adding cash/leverage.
- **Information ratio (IR)** = `(R_P − R_B) / σ(R_P − R_B)` = **active return / active risk (tracking error)**.
  - **Ex ante** (expected) vs **ex post** (realized).
  - IR is **unaffected by the aggressiveness** of active weights (scaling active positions scales both numerator and denominator) — assuming no benchmark/cash constraints.

## The Fundamental Law (35.c)
- `E(R_A) = IC × √BR × σ_A × TC`, and `IR = IC × √BR × TC`.
  - **IC** (information coefficient): correlation between forecast and realized active returns (skill).
  - **BR** (breadth): number of **independent** active decisions per year. *Example: active positions in 10 securities each month → BR = 10 × 12 = 120.*
  - **TC** (transfer coefficient): correlation between actual and optimal active weights; **1 = no constraints**. `TC²` = fraction of realized active-return variance explained by skill; `(1 − TC²)` = constraint-induced noise.
  - **σ_A**: active risk (aggressiveness).
- **Optimal active risk** (unconstrained): `σ_A* = (IR / SR_B) × σ_B`; max Sharpe of the active portfolio satisfies `SR_P² = SR_B² + IR²`.

## Applications & Strategy Comparison (35.d, 35.e)
- IR aids **manager selection** and choosing the **level of active risk**.
- **Market timing**: few, large, correlated bets → **low breadth**; **security selection**: many small independent bets → **high breadth**. The fundamental law shows breadth's leverage on IR (via √BR).

## Strengths & Limitations (35.f)
- Provides a framework linking skill, breadth, and implementation to performance.
- Limitations: **BR assumes independent decisions** (correlated bets overstate breadth); **IC is hard to estimate** and unstable; ex-ante inputs are noisy.

## Exam Traps
- **IR = active return / active risk** (tracking error); **Sharpe uses total risk**.
- IR is invariant to aggressiveness (unconstrained); `SR_P² = SR_B² + IR²`.
- Fundamental law: `IR = IC × √BR × TC`; breadth must be **independent** decisions.
- Market timing = low breadth; broad security selection = high breadth.

## Q&A

### 2026-06-03 — Fundamental law worked (and breadth done right)
**Q:** A manager has IC 0.05, makes active bets in 50 securities each quarter, TC 0.8, with active risk 4%. Expected active return and IR?
**A:** Breadth = **independent** decisions per year = 50 × 4 = **200**. `IR = IC×√BR×TC = 0.05×√200×0.8 = 0.05×14.14×0.8 = 0.566`. `E(R_A) = IR×σ_A = 0.566×4% = 2.26%` (equivalently IC×√BR×TC×σ_A). Trap: BR counts **independent** bets — if those 50 positions are highly correlated, true breadth is far below 200 and IR is overstated. TC = 1 only with no constraints.
Related: [[Multifactor_Models]]

### 2026-06-03 — Information ratio vs Sharpe ratio
**Q:** Why is IR (not Sharpe) the right gauge of active skill, and how do they relate?
**A:** **Sharpe = (R_P − R_f)/σ_P** uses **total** risk and is invariant to adding cash/leverage — it measures total-portfolio efficiency. **IR = active return / active risk (tracking error)** isolates value added **versus the benchmark** and (unconstrained) is invariant to how aggressive the active weights are. The optimal amount of active risk gives `SR_P² = SR_B² + IR²`, so a higher IR is what lets an active manager beat the benchmark's Sharpe. Choose managers on IR; size active risk via `σ_A* = (IR/SR_B)·σ_B`.
Related: [[Multifactor_Models]]
