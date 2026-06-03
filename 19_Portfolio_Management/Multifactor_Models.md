---
aliases: [Multifactor Models, Arbitrage Pricing Theory, APT, Carhart Model, Factor Models, Active Risk Decomposition]
tags: [CFA-L2, pm, concept, factor-models]
date: 2026-06-03
status: evergreen
source: Schweser Book 5, Module 37, LOS 37.a-37.g
---

# Multifactor Models

## Arbitrage Pricing Theory (37.a, 37.b, 37.c)
- **APT**: `E(R_p) = R_f + Σ (β_j × λ_j)`, where `λ_j` = factor risk premium for factor j.
- **Assumptions**: (1) returns follow a **multifactor process**, (2) investors can form **well-
  diversified** portfolios (idiosyncratic risk diversified away), (3) **no arbitrage**. (APT does **not**
  require the market portfolio or mean-variance assumptions, unlike CAPM.)
- **Arbitrage opportunity**: a combination of assets with **zero net investment, zero risk, positive
  return**. If pricing deviates from APT, build an arbitrage portfolio.

## Types of Factor Models (37.d)
| Model | Factors | Notes |
|------|------|------|
| **Macroeconomic** | Surprises in macro variables (GDP, inflation, rates) | Factor = **surprise** (actual − expected); betas = sensitivities |
| **Fundamental** | Firm attributes (size, value, momentum, P/B) | **Factor sensitivities are standardized attributes**; factor returns estimated by regression |
| **Statistical** | Factors extracted by statistics (PCA/factor analysis) | Maximize explained variance; factors lack economic interpretation |

- **Carhart four-factor**: `R_p − R_f = α + β_mkt·RMRF + β_smb·SMB + β_hml·HML + β_wml·WML` (market, size,
  value, momentum).

## Uses & Active Risk (37.e, 37.f, 37.g)
- Uses: return attribution, **risk attribution**, portfolio construction (factor tilts), passive/active
  replication, understanding style.
- **Active return** = Σ (active factor tilts × factor returns) + security selection.
- **Active risk (tracking error)** decomposes into **active factor risk + active specific risk**:
  `active risk² = active factor risk² + active specific (selection) risk²`.
- **Information ratio** = active return / active risk (→ [[Active_Portfolio_Management]]).

## Exam Traps
- APT needs **no market portfolio** and no normality — only a factor structure, diversification, no
  arbitrage (contrast with CAPM, a single-factor special case).
- **Macroeconomic** models use factor **surprises**; **fundamental** models use **standardized attributes**
  as the sensitivities (the reverse of macro).
- Arbitrage portfolio = **zero investment, zero risk, positive expected return**.
- Active risk² = active **factor** risk² + active **specific** risk².

## Q&A

### 2026-06-03 — APT vs CAPM
**Q:** What does APT assume that CAPM does not, and what is an arbitrage portfolio?
**A:** `E(R_p) = R_f + Σ β_j λ_j`. APT requires only (1) returns follow a **multifactor** process, (2)
investors can build **well-diversified** portfolios (idiosyncratic risk → 0), and (3) **no arbitrage**.
It does **not** need the market portfolio, mean-variance investors, or normally distributed returns —
CAPM is just a **single-factor special case**. If prices violate APT, you form an **arbitrage portfolio**:
**zero net investment, zero (factor) risk, positive expected return**.
Related: [[Active_Portfolio_Management]]

### 2026-06-03 — Macroeconomic vs fundamental factor models
**Q:** In each model type, what are the "factors" and what are the "sensitivities"?
**A:** **Macroeconomic** models: the **factors are surprises** (actual − expected) in macro variables
(GDP, inflation, rates); the **betas are estimated sensitivities**. **Fundamental** models: it's the
reverse — the **factor sensitivities are the (standardized) firm attributes** (size, value, momentum,
P/B) known in advance, and the **factor returns are estimated by regression**. **Statistical** models
extract factors by PCA/factor analysis to maximize explained variance, but the factors lack economic
meaning. (Carhart = market + SMB + HML + WML.)
Related: [[Active_Portfolio_Management]]
