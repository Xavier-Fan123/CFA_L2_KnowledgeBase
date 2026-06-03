---
aliases: [Cost of Capital, Required Return on Equity, Equity Risk Premium, Country Risk Premium, Beta Estimation, Hamada]
tags: [CFA-L2, corp, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 2, Module 15, LOS 15.a-15.f
---

# Cost of Capital: Advanced Topics

## Top-Down vs Bottom-Up Factors (15.a)
- **Top-down (macro)**: interest rates / monetary policy, inflation, GDP/cycle, exchange rates,
  sovereign risk — raise or lower the whole cost-of-capital level.
- **Bottom-up (firm)**: revenue/earnings cyclicality, operating & financial leverage, size, asset
  liquidity, governance — drive a firm's spread over the macro baseline.

## Cost of Debt (15.b)
- **YTM / market-based**: yield on the firm's traded debt (preferred when available).
- **Debt-rating (synthetic)**: match rating → matrix yield; useful when no traded debt.
- **For private firms**: build a synthetic rating from interest-coverage and leverage ratios.

## Equity Risk Premium (15.c)
- **Historical**: average realized equity return − risk-free. Choices: arithmetic vs geometric mean,
  short vs long-bond risk-free, sample period. Subject to **survivorship bias** and may not reflect
  the future.
- **Forward-looking**:
  - **DDM/Grinold-Kroner**: `ERP ≈ dividend yield + expected growth − risk-free`, where expected return
    `= D/P + expected inflation + real earnings growth + Δ(P/E) − Δshares`.
  - Survey-based.

## Required Return on Equity (15.d, 15.e)
- **CAPM**: `r_e = R_f + β × ERP`.
- **Expanded CAPM** (private/illiquid): CAPM + **size premium** + **company-specific (idiosyncratic)
  premium**.
- **Build-up approach**: `R_f + ERP + size premium + specific premium` (no beta; for private firms).
- **Bond-yield-plus-risk-premium**: `r_e = YTM on firm's debt + equity risk premium (3–5% typical)`.

## Country Risk (emerging markets) (15.c)
- **Country spread / country risk premium (CRP)** added for emerging markets:
  `CRP = sovereign yield spread × (σ_equity / σ_bond)` (equity vol relative to bond vol).
  Then `r_e = R_f + β × (ERP + CRP)` (or β applied to mature-market ERP, CRP added).

## Beta Estimation (15.a, 15.e)
- Regression beta is noisy for the subject firm; use **comparable (pure-play) companies**:
  1. Take comparable's **equity (levered) beta**; **unlever** (Hamada):
     `β_asset = β_equity / [1 + (1 − t)(D/E)]`.
  2. **Relever** to the subject firm's capital structure:
     `β_equity = β_asset × [1 + (1 − t)(D/E_subject)]`.
- Use the **project's** (not the firm's) risk for project cost of capital.

## Capital Structure & Peers (15.f)
- Evaluate a firm's WACC and structure **relative to peers**: leverage, debt maturity, cost of debt,
  coverage; identify whether the structure is optimal/sustainable.

## Exam Traps
- **Unlever then relever** beta when the comparable's leverage differs from the subject's (Hamada).
- Build-up and expanded CAPM are for **private/illiquid** firms (add size + specific premiums).
- Country risk premium scales the sovereign spread by **equity-to-bond volatility ratio**.
- Use **project** risk, not company-average risk, for a project's discount rate.

## Q&A

### 2026-06-03 — Unlever and relever beta (pure-play / Hamada)
**Q:** A comparable has equity beta 1.4, D/E 0.5, tax 25%. The subject firm has D/E 1.0, tax 25%. What's the subject's equity beta?
**A:** Two steps. **Unlever** the comparable to its asset (unlevered) beta:
`β_asset = 1.4 / [1 + (1−0.25)(0.5)] = 1.4 / 1.375 = 1.018`. **Relever** to the subject's structure:
`β_equity = 1.018 × [1 + (1−0.25)(1.0)] = 1.018 × 1.75 = 1.78`. Then plug into CAPM `r_e = R_f + β·ERP`.
Trap: you strip out the comparable's financial risk, then add back the **subject's**; use the **project's**
risk for a project discount rate, not the company average.
Related: [[Dividends_and_Share_Repurchases]]

### 2026-06-03 — Country risk premium for an emerging market
**Q:** How do you build the country risk premium, and where does it go in CAPM?
**A:** `CRP = sovereign yield spread × (σ_equity / σ_bond)` — the sovereign bond spread (EM yield − developed
yield, same currency) scaled by the **relative volatility of the equity market to the bond market**. Then
`r_e = R_f + β × (mature-market ERP + CRP)`. Intuition: the bond spread captures default risk; multiplying
by equity/bond vol scales it up to equity-market risk.
Related: [[Equity_Valuation_Process]]
