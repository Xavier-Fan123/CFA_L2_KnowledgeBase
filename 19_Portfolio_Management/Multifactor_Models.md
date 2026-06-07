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
- **Assumptions**: (1) returns follow a **multifactor process**, (2) investors can form **well-diversified** portfolios (idiosyncratic risk diversified away), (3) **no arbitrage**. (APT does **not** require the market portfolio or mean-variance assumptions, unlike CAPM.)
- **Arbitrage opportunity**: a combination of assets with **zero net investment, zero risk, positive return**. If pricing deviates from APT, build an arbitrage portfolio.

### Worked example A — Solve a one-factor APT model (calculate λ and R_f)
Three well-diversified portfolios, single factor (official V9, Module 4, Example 1):

| Portfolio | E(R) | Factor sensitivity β |
|---|---|---|
| A | 7.5% | 0.50 |
| B | 15.0% | 2.00 |
| C | 7.0% | 0.40 |

APT line: `E(R_p) = R_f + β_p,1·λ_1`. Two equations from A and B:
- `0.075 = R_f + 0.5λ_1`
- `0.150 = R_f + 2.0λ_1` Subtract: `0.075 = 1.5λ_1 → λ_1 = 0.05`. Back-substitute: `R_f = 0.075 − 0.5(0.05) = 0.05`. So **R_f = 5%, factor premium λ_1 = 5%**, giving `E(R_p) = 0.05 + 0.05·β_p,1`. Check C: `0.05 + 0.05(0.40) = 0.07` ✔ (matches the 7.0% quoted → C is fairly priced).

### Worked example B — Determine and exploit an arbitrage (calculate the profit)
Add Portfolio D: E(R) = **8.0%**, β = 0.45 (same model as above). The required return for β = 0.45 is `0.05 + 0.05(0.45) = 0.0725 = 7.25%`. D offers 8% > 7.25% → **D is undervalued; an arbitrage exists.** Build a 50/50 replica of A and C (β = 0.5·0.50 + 0.5·0.40 = **0.45**, same factor risk as D; E(R) = 7.25%).
**Strategy:** long $10,000 of D, short $10,000 of the A/C replica (zero net investment, zero net factor risk):

| Position | Initial CF | Final CF (after 1 yr) | β |
|---|---|---|---|
| Long D | −$10,000 | +$10,800 | +0.45 |
| Short A&C replica | +$10,000 | −$10,725 | −0.45 |
| **Net** | **$0** | **+$75** | **0.00** |

Riskless **$75** profit on zero investment confirms the arbitrage. (Official V9, Module 4, Examples 2–3.)

### Worked example C — Macroeconomic factor model: portfolio return from surprises
Two factors = **surprises** in inflation (F_INFL) and GDP growth (F_GDP). Two stocks (official V9, Ex. 5):
- `R_MANM = 0.09 − 1·F_INFL + 1·F_GDP + ε_MANM`
- `R_NXT  = 0.12 + 2·F_INFL + 4·F_GDP + ε_NXT` Weights ⅓ MANM, ⅔ NXT. Portfolio equation (weighted-average the intercept and each beta): `R_P = 0.11 + 1·F_INFL + 3·F_GDP + (⅓)ε_MANM + (⅔)ε_NXT`. **Expected return = the intercept = 11%** (because E[surprise] = 0 and E[ε] = 0). If inflation surprise = 1%, GDP surprise = 0%, ε's = 0.5% each: `R_P = 0.11 + 1(0.01) + 3(0) + (⅓)(0.005) + (⅔)(0.005) = 0.125 = 12.5%`. *Trap:* the **intercept is the expected return only because each factor is a surprise** (mean 0) — not a risk-free rate.

## Types of Factor Models (37.d)

| Model | Factors | Notes |
|------|------|------|
| **Macroeconomic** | Surprises in macro variables (GDP, inflation, rates) | Factor = **surprise** (actual − expected); betas = sensitivities |
| **Fundamental** | Firm attributes (size, value, momentum, P/B) | **Factor sensitivities are standardized attributes**; factor returns estimated by regression |
| **Statistical** | Factors extracted by statistics (PCA/factor analysis) | Maximize explained variance; factors lack economic interpretation |

- **Carhart four-factor**: `R_p − R_f = α + β_mkt·RMRF + β_smb·SMB + β_hml·HML + β_wml·WML` (market, size, value, momentum).

## Uses & Active Risk (37.e, 37.f, 37.g)
- Uses: return attribution, **risk attribution**, portfolio construction (factor tilts), passive/active replication, understanding style.
- **Benefit of multiple risk dimensions (37.f):** the CAPM splits wealth only between the risk-free asset and one broad market index. Recognizing **multiple sources of systematic risk** lets an investor improve on that mean-variance result by **tilting away from the market portfolio** — taking **above-average exposure to factors they have a comparative advantage in bearing** (and below-average exposure to those they don't). Different investors have different appetites/abilities to bear inflation, growth, credit, liquidity, etc., so the same factor that is a risk to one investor can be an opportunity for another.
- **Active return** = Σ (active factor tilts × factor returns) + security selection.
- **Active risk (tracking error)** decomposes into **active factor risk + active specific risk**: `active risk² = active factor risk² + active specific (selection) risk²`.
- **Information ratio** = active return / active risk (→ [[Active_Portfolio_Management]]).

### Commodity Hedge Fund Extension (Beyond Curriculum)
This section is a professional hedge-fund application, not CFA curriculum text.

- Commodity hedge-fund factor models should include more than broad commodity beta. Common factors include **carry/term structure**, momentum/trend, inventory tightness, seasonality, USD, real rates, inflation surprises, growth/industrial demand, volatility, liquidity, freight, and credit/funding stress.
- Factor definitions must match the traded instrument. A crude outright future, a refinery crack spread, a WTI-Brent spread, and a call option can have very different exposures even if all are "oil" trades.
- Active return attribution should separate **factor premia** from true idiosyncratic alpha. A long-backwardation book may be earning carry; a trend book may be earning momentum; a short-option book may be selling volatility, not generating pure forecasting skill.
- Statistical factors from PCA can be useful for risk compression, but they need economic labeling before capital is allocated. An unlabeled component may actually be USD, China demand, refinery margin, freight, or liquidity.
- Conditional betas matter. A book can have low normal-times commodity beta and large crisis beta when exchanges raise margin, liquidity vanishes, correlations rise, or delivery constraints dominate.
- Apparent arbitrage portfolios are rarely zero-risk in commodities. Residual basis, funding, storage, delivery optionality, settlement timing, and position limits often explain why a spread remains open.

## Exam Traps
- APT needs **no market portfolio** and no normality — only a factor structure, diversification, no arbitrage (contrast with CAPM, a single-factor special case).
- **Macroeconomic** models use factor **surprises**; **fundamental** models use **standardized attributes** as the sensitivities (the reverse of macro).
- Arbitrage portfolio = **zero investment, zero risk, positive expected return**.
- Active risk² = active **factor** risk² + active **specific** risk².

## Q&A

### 2026-06-03 — APT vs CAPM
**Q:** What does APT assume that CAPM does not, and what is an arbitrage portfolio?
**A:** `E(R_p) = R_f + Σ β_j λ_j`. APT requires only (1) returns follow a **multifactor** process, (2) investors can build **well-diversified** portfolios (idiosyncratic risk → 0), and (3) **no arbitrage**. It does **not** need the market portfolio, mean-variance investors, or normally distributed returns — CAPM is just a **single-factor special case**. If prices violate APT, you form an **arbitrage portfolio**: **zero net investment, zero (factor) risk, positive expected return**.
Related: [[Active_Portfolio_Management]]

### 2026-06-03 — Macroeconomic vs fundamental factor models
**Q:** In each model type, what are the "factors" and what are the "sensitivities"?
**A:** **Macroeconomic** models: the **factors are surprises** (actual − expected) in macro variables (GDP, inflation, rates); the **betas are estimated sensitivities**. **Fundamental** models: it's the reverse — the **factor sensitivities are the (standardized) firm attributes** (size, value, momentum, P/B) known in advance, and the **factor returns are estimated by regression**. **Statistical** models extract factors by PCA/factor analysis to maximize explained variance, but the factors lack economic meaning. (Carhart = market + SMB + HML + WML.)
Related: [[Active_Portfolio_Management]]

### 2026-06-04 — Determine whether an arbitrage opportunity exists (worked)
**Q:** A one-factor APT model is `E(R) = 0.05 + 0.05·β`. Portfolio D has E(R) = 8% and β = 0.45. Is there an arbitrage, and how big is the profit on a $10,000 trade?
**A:** Required return for β = 0.45 is `0.05 + 0.05(0.45) = 7.25%`. D offers **8% > 7.25%**, so D is **undervalued → arbitrage exists**. Replicate D's β with a 50/50 mix of portfolios A (β 0.50) and C (β 0.40), β = 0.45, E(R) = 7.25%. **Long $10,000 D, short $10,000 of the A/C replica**: zero net investment, zero net factor risk (0.45 − 0.45 = 0). Final cash flows: +$10,800 (D) − $10,725 (replica) = **+$75 riskless profit**. Rule: long the cheap (high-return) leg, short the expensive (low-return) leg with matching factor sensitivity.
Related: [[Active_Portfolio_Management]]

### 2026-06-04 — Macro factor model: expected vs realized portfolio return
**Q:** With `R_P = 0.11 + 1·F_INFL + 3·F_GDP + ε`, what is the expected return, and the realized return if inflation surprise = 1%, GDP surprise = 0%, ε = 0?
**A:** **Expected return = the intercept = 11%**, because in a macro model the factors are *surprises* (actual − expected) with mean 0, and E[ε] = 0 — so every term except the intercept vanishes in expectation. The intercept is **not** the risk-free rate; it is the expected return. Realized return adds the surprise impacts: `0.11 + 1(0.01) + 3(0) = 0.12 = 12%`. A positive sensitivity means the stock rises when that factor surprises to the upside; the inflation factor premium is typically negative.
Related: [[Economics_and_Investment_Markets]]
