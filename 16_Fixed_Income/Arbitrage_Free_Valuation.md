---
aliases: [Arbitrage-Free Valuation, Binomial Interest Rate Tree, Backward Induction, Pathwise Valuation, Monte Carlo, Term Structure Models]
tags: [CFA-L2, fi, concept, valuation]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V6 LM2 (worked examples); Schweser Book 4, Module 24, LOS 24.a-24.i
---

# Arbitrage-Free Valuation Framework

## Arbitrage-Free Principle (24.a, 24.b)
- **Value = sum of the PV of each cash flow discounted at its own spot rate** ("value additivity" / law of one price). A bond's price must equal its replicating portfolio of zeros, else arbitrage.
- An arbitrage-free price rules out **two** violations, and the exam names both:
  - **Value additivity** — the value of the whole must equal the sum of the values of its parts (strip a bond into zeros: the parts must reprice to the whole).
  - **Dominance** — no asset that can never pay less than another (and sometimes pays more) may cost less. Equivalently, a risk-free asset must not offer a return above the risk-free rate. Spotting either one is a **free-lunch (arbitrage)** trade.
- Option-free, fixed-rate bonds can be valued directly off the spot curve.

## Binomial Interest Rate Tree (24.c, 24.d)
- For bonds whose **cash flows depend on the rate path** (embedded options), use a tree that lets rates vary. Assumes rates take one of **two equally likely values** each period (binomial).
- The tree is a **lognormal random walk** with two properties: (1) **higher volatility at higher rates**, (2) **non-negative rates**. Adjacent node rates differ by a factor of `e^(2σ)`.
- **Calibration**: adjust the tree's rates so it (a) is consistent with the **par/spot curve** (prices benchmark bonds to par) and (b) reflects the assumed volatility. The calibrated tree is **arbitrage-free**.

## Backward Induction (24.e, 24.f)
- Value from maturity backward: at each node, `value = [0.5 × (V_up + C) + 0.5 × (V_down + C)] / (1 + rate_node)`, using risk-neutral 0.5/0.5 probabilities, then discount to the prior node.
- For an **option-free** bond, the binomial lattice value **equals** the spot-curve value (consistency check).

## Pathwise Valuation (24.g)
- Value = **average of the values along each interest-rate path** in the tree. For an n-period tree there are `2^(n−1)` paths. Gives the same answer as backward induction for option-free bonds.

## Worked Examples (official V6 LM2 numbers)

**A. Calibrating the tree (24.d)** — par curve 1.00% (1y), 1.20% (2y), 1.25% (3y); volatility σ = 15%, so adjacent rates differ by `e^(2×0.15) = 1.3499`.
- Time 1: solve for the lower rate so the 2-year 1.20% par bond prices at 100 → **i(1,L) = 1.1943%**, **i(1,H) = 1.1943% × 1.3499 = 1.6121%**.
  - Check: node values `101.20/1.016121 = 99.5944` and `101.20/1.011943 = 100.0056`; Time 0 `= [1.20 + 0.5(99.5944 + 100.0056)]/1.01 = 100.0000` ✓.
  - The two rates average **1.4032%**, slightly **above** the 1.4028% implied forward rate — a by-product of lognormality; the tree spreads out **around** the forward curve.
- Time 2 (fit to the 3-year 1.25% par bond): **1.7863% / 1.3233% / 0.9803%**.
- With volatility near zero the tree collapses onto the implied forward rates; higher σ widens it.

**B. Backward induction (24.e)** — tree: Time 0 **2.000%**; Time 1 **4.646% / 3.442%**; Time 2 **8.167% / 6.050% / 4.482%** (calibrated to par yields of 2%, 3%, 4%). Value a 3-year, 5% annual-coupon bond:
- Time 2: `105/1.08167 = 97.0721`; `105/1.06050 = 99.0099`; `105/1.04482 = 100.4958`.
- Time 1: upper `[5 + 0.5(97.0721 + 99.0099)]/1.04646 = 98.4663`; lower `[5 + 0.5(99.0099 + 100.4958)]/1.03442 = 101.2672`.
- Time 0: `[5 + 0.5(98.4663 + 101.2672)]/1.02 = **102.8105**` — the same price as discounting at the spot rates, which confirms the tree is arbitrage-free (24.f).

**C. Pathwise valuation (24.g)** — 3-year zero (face 100) on tree A; 2^(3−1) = **4 paths**:

| Path | Year 1 | Year 2 | Year 3 | PV |
|---|---|---|---|---|
| 1 (HH) | 1.0000% | 1.6121% | 1.7863% | 95.7291 |
| 2 (HL) | 1.0000% | 1.6121% | 1.3233% | 96.1665 |
| 3 (LH) | 1.0000% | 1.1943% | 1.3233% | 96.5636 |
| 4 (LL) | 1.0000% | 1.1943% | 0.9803% | 96.8916 |
| **Average** | | | | **96.3377** |

e.g., path 1: `100/(1.01 × 1.016121 × 1.017863) = 95.7291`. The average equals the backward-induction value of the same zero (96.3377). Pascal's triangle counts the paths to each node (1-2-1 at Time 2).

## Monte Carlo Simulation (24.h)
- Generates many random rate paths; used for **path-dependent** securities (e.g., **MBS** where prepayments depend on the rate history). Add a constant (drift adjustment / OAS) so simulated values match market prices. More paths → more precision (not necessarily more accuracy).

## Term-Structure Models (24.i)
- **Equilibrium models** (CIR, Vasicek): describe rate dynamics from economic assumptions; may not fit the current curve exactly.
  - **CIR**: mean-reverting, volatility scales with √r (rates stay non-negative).
  - **Vasicek**: mean-reverting, **constant** volatility (allows negative rates).
- **Arbitrage-free models** (Ho-Lee, KWF): start from **observed market prices** on the assumption that traded securities are correctly priced, and calibrate to **fit the current term structure exactly**.
  - **Ho-Lee**: `dr_t = θ_t·dt + σ·dz_t`. The **time-dependent drift θ_t** is solved from market prices so the model reproduces today's curve. Short rates are **normally** distributed with **constant volatility** → **rates can go negative**.
  - **Kalotay-Williams-Fabozzi (KWF)**: `d ln(r_t) = θ_t·dt + σ·dz_t` — the **lognormal** version of Ho-Lee. Same calibration logic, but modeling **ln(r)** keeps rates **non-negative** and makes volatility proportional to the rate level.

## Exam Traps
- Binomial tree = **lognormal** (non-negative rates, higher vol at higher rates); spacing factor `e^(2σ)`.
- Backward induction uses **risk-neutral 0.5/0.5** probabilities, discounting node-by-node.
- **Monte Carlo** is for **path-dependent** instruments (MBS); a binomial tree is **not** path-dependent.
- CIR volatility depends on √r; Vasicek volatility is constant (can go negative).
- **Four models, two families**: *equilibrium* = **CIR** (√r volatility, non-negative rates) and **Vasicek** (constant volatility, rates can go negative); *arbitrage-free* = **Ho-Lee** (normal, rates can go negative) and **KWF** (lognormal in ln r, so rates stay positive). "Time-dependent drift θ_t fitted to market prices" = arbitrage-free family.
- Arbitrage requires violating **value additivity OR dominance** — know both names.

## Q&A

### 2026-06-03 — Equilibrium vs arbitrage-free term-structure models
**Q:** Contrast CIR, Vasicek, and Ho-Lee.
**A:** **CIR** and **Vasicek** are **equilibrium** models — they derive rate dynamics from economic assumptions and do **not** necessarily fit today's curve. Both are mean-reverting; **CIR** volatility scales with **√r** (so rates stay non-negative), **Vasicek** has **constant** volatility (can produce negative rates). **Ho-Lee** is an **arbitrage-free** model: it's calibrated via a risk-neutral drift to **fit the current market term structure exactly** (constant volatility). Exam tell: "fits the current curve" = arbitrage-free (Ho-Lee); "from economic assumptions" = equilibrium (CIR/Vasicek).
Related: [[Bonds_With_Embedded_Options]]

### 2026-06-03 — Monte Carlo vs binomial tree: which and when?
**Q:** Why must MBS be valued with Monte Carlo rather than a binomial tree?
**A:** MBS cash flows are **path-dependent** — prepayments depend on the **history** of rates, not just the current node — and a recombining binomial tree is **not** path-dependent (it only knows the current rate). Monte Carlo generates many full rate **paths**, so it can model prepayment behavior along each path; a constant drift adjustment (OAS) is added so simulated values match market prices. More paths → more **precision** (not necessarily more accuracy). For option-free bonds, tree backward-induction, pathwise valuation, and spot-curve valuation all agree.
Related: [[Credit_Analysis_Models]]
