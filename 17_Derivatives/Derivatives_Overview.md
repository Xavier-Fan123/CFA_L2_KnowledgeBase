---
aliases: [Derivatives Overview]
tags: [CFA-L2, deriv, overview]
date: 2026-06-03
status: evergreen
source: Schweser Book 4 (Modules 28-29)
---

# Derivatives — Overview

Two modules, both formula-heavy: forward commitments (linear) and options (non-linear).

## Module 28 — Forward Commitments → [[Forward_Commitments]]
Carry arbitrage pricing of forwards/futures (income lowers F, costs raise F); valuing a forward during
life = PV(Ft − F0); equity/fixed-income/interest-rate forwards; interest-rate, currency, equity swaps;
par swap rate = (1 − final DF)/Σ DF.

## Module 29 — Valuation of Contingent Claims → [[Options_Valuation]]
Binomial model (risk-neutral π_U = (1+r−d)/(u−d)); two-period & American early exercise; hedge ratio;
interest-rate options; BSM (call = S·N(d1) − Xe^(−rT)·N(d2)); Black model & swaptions; Greeks, delta
hedging, gamma risk, implied volatility.

## Cross-cutting Exam Traps
- Forward: income reduces F0, costs increase F0; value during life = PV(Ft − F0).
- Option value = PV of risk-neutral expected payoff; π_U = (1+r−d)/(u−d).
- BSM N(d1) = delta, N(d2) ≈ prob ITM; Black model values options on futures.
- Gamma highest ATM near expiry; delta hedges require dynamic rebalancing.
