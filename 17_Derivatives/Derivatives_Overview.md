---
aliases: [Derivatives Overview]
tags: [CFA-L2, deriv, overview]
date: 2026-06-03
status: evergreen
source: Schweser Book 4 (Modules 28-29)
---

# Derivatives — Overview

Two modules, both formula-heavy: forward commitments (linear) and options (non-linear).

Maps to **Official Curriculum Volume 7 (Derivatives)**: Learning Module 1 (Forward Commitments, 7 LOS) and Learning Module 2 (Contingent Claims, 14 LOS).

## Module 28 / LM1 — Forward Commitments → [[Forward_Commitments]]
Carry arbitrage `F0 = FV(S0 + CC − CB)` (benefits lower F, costs raise F); valuing a forward during life `Vt = PV(Ft − F0) = St − PV[F0]`; equity / fixed-income (accrued interest, conversion factor) forwards; **FRAs** (X×Y, advanced-set/advanced-settled, value `= NA·(FRAg − FRA0)·tm / [1 + D·t]`); interest-rate, currency, and equity **swaps**; par swap rate `= (1 − PV_n)/(Σ PV_i)·(1/AP)`; swap value `= VFIX − VFLT`.

## Module 29 / LM2 — Valuation of Contingent Claims → [[Options_Valuation]]
Binomial model (risk-neutral `π = (1+r−d)/(u−d)`, value `= PV[π·c+ + (1−π)·c−]`); two-period & American early exercise; hedge ratio `h = (c+ − c−)/(S+ − S−)`; interest-rate options on a binomial tree; **BSM** `call = S·N(d1) − Xe^(−rT)·N(d2)` with `d1 = [ln(S/X)+(r+σ²/2)T]/(σ√T)`, `d2 = d1 − σ√T`; carry-adjusted BSM; **Black model** (futures/IR options/swaptions); the **five Greeks**, delta hedging `NH = −Port.Δ/Δ_H`, gamma risk, implied volatility.

## Cross-cutting Exam Traps
- Forward: carry **benefits/income reduce** F0, **costs increase** it; value during life = PV(Ft − F0).
- Swap value = VFIX − VFLT; **positive to the fixed receiver when rates fall**; equity-swap fixed rate = comparable IRS fixed rate; currency swap = two bonds converted at the **current spot FX**.
- Option value = PV of **risk-neutral** expected payoff; `π = (1+r−d)/(u−d)`; American → check early exercise.
- BSM: `N(d1)` = delta, `N(d2)` ≈ RN prob ITM; carry term `e^(−γT)` on the stock; **Black** values options on **futures** (and IR options/swaptions; payer swaption ≈ call on rates).
- **Gamma highest ATM near expiry** and equal for call & put; delta hedges require **dynamic rebalancing**; rho is **+ for calls, − for puts**; implied vol is **forward-looking**.
