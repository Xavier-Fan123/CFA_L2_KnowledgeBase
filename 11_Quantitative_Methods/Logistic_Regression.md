---
aliases: [Logistic Regression, Logit Model, Log Odds, Likelihood Ratio Test, Qualitative Dependent Variable]
tags: [CFA-L2, quant, concept, regression]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 1.4, LOS 1.m
---

# Logistic Regression (Logit)

## Why It Exists

Used when the **dependent variable is qualitative** — usually **binary** (0/1): probability of default, dividend increase, merger, monetary tightening. Ordinary (OLS) regression is inappropriate because its fitted values can be **< 0 or > 1**, which are illogical for a probability.

## The Two Transforms: probability → odds → log odds

1. Probability → **odds**: `odds = p / (1 − p)`  (e.g. p=0.80 → odds = 4)
2. Odds → **log odds** (logistic transform): `ln[p / (1 − p)]`

The logit model uses **log odds as the dependent variable**:

`ln[p / (1 − p)] = b₀ + b₁X₁ + ... + bₖXₖ`

## Key Features

| Feature | Detail |
|------|------|
| Residual distribution | **Logistic** (like normal but **fatter tails**) |
| Estimation | **Maximum Likelihood Estimation (MLE)** — not OLS |
| Use | Probability of a discrete outcome |

## Interpreting Coefficients

- **Intercept b₀**: log odds when all X = 0.
- **Slope bⱼ** (official wording): the change in the **log odds** of the event per 1-unit change in Xⱼ, holding others constant.
- It is **NOT** a direct change in probability — the model is non-linear, so the probability change from a 1-unit move depends on the curvature at that point. Curriculum method: compute probability at the **average** X's, then bump one X by 1 unit and recompute; the difference is that variable's marginal effect.

## From Coefficients to Probability

1. Compute `ŷ` (log odds). 2. `odds = e^ŷ`. 3. `p = e^ŷ / (1 + e^ŷ) = 1 / (1 + e^(−ŷ))`.

Worked example (36 firms, dividend increase): model `ŷ = −3.445 + 0.332·Age + 12.33·(FCFE/Mcap) + 3.21·Cash`.
- All X=0: odds = e^(−3.445)=0.0319 → p = 3.09%.
- At average X: ŷ = −1.2999 → p = 21.42%.
- Raise FCFE/Mcap 0.08→0.09: ŷ = −1.1766 → p = 23.57% → +2.15% (marginal effect computed pointwise).
- "Age" is insignificant (p>0.05); the other two are significant.

## Testing

1. **Individual coefficients**: p-value / t-test, as in OLS.
2. **Nested models — Likelihood Ratio (LR) test** (the logit analogue of the joint F-test; **NOT** F):
   - `LR = −2·(LL_restricted − LL_unrestricted) = 2·(LL_unrestricted − LL_restricted)` (standard form)
   - Restricted model has **q fewer** independent variables.
   - Log-likelihood (LL) is always **negative**; **closer to 0 = better fit**.
   - LR is **χ² with q df**. H₀: the dropped coefficients are all 0. LR > critical → reject H₀.
   - Example: LL_unrestricted = −212.44, LL_restricted = −216.22, q=2 → LR = 2×3.78 = 7.56 > 5.99 → reject.
3. **Goodness of fit**: no traditional R²; software gives **pseudo-R²**, usable only to compare models with the **same dependent variable**.

## OLS vs Logit (one-page)

| Dimension | OLS | Logit |
|------|------|------|
| Dependent variable | Continuous | Binary (0/1) |
| Modeled quantity | Y | log odds `ln[p/(1−p)]` |
| Estimation | Least squares | **MLE** |
| Residual distribution | Normal | **Logistic (fat tails)** |
| Slope meaning | ΔY per unit X | Δ**log odds** per unit X (probability effect is pointwise) |
| Nested test | Joint **F-test** | **LR test** (χ², df=q) |
| Fit | R² | pseudo-R² (same-DV comparison only) |

## Exam Traps
- Nested test is the **LR test (χ²)**, not an F-test.
- Slope = change in **log odds**, not probability.
- pseudo-R² compares only models with the **same** dependent variable.

## Q&A

### 2026-06-02 — What is logistic regression and how is it tested?
**Q:** Explain logistic regression in detail and how to test it.
**A:** A logit model is used when the dependent variable is binary; OLS fails because fitted values can fall outside [0,1]. It models **log odds** `ln[p/(1−p)] = b₀+ΣbⱼXⱼ`, estimated by **MLE**, residuals **logistic (fat-tailed)**. Slope = change in log odds per unit X (probability effect must be computed pointwise at average X). Recover probability via `p = 1/(1+e^(−ŷ))`. Testing: individual p-values; nested models via the **Likelihood Ratio (LR) test** `LR = 2(LL_unrestricted − LL_restricted)`, χ² with q df (example 7.56 > 5.99 → reject); fit via pseudo-R² (same-DV only). Key trap: LR test, not F-test.
Related: [[Regression_Assumption_Violations]]
