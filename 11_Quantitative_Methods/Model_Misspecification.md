---
aliases: [Model Misspecification, Functional Form Misspecification, Omitted Variable, Variable Scaling]
tags: [CFA-L2, quant, concept, regression]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 1.3, LOS 1.g
---

# Model Misspecification

## Overview

Three principles of model specification: independent variables must have an **economic rationale**,
the model must be **parsimonious**, and the **functional form must be correct**. Misspecification
either biases / makes inconsistent the coefficients, or breaks the error-term assumptions
(heteroskedasticity / serial correlation), making inference unreliable.

## Four Functional-Form Misspecifications

### #1 Omitting a Variable
A variable that belongs in the model is left out; its effect is absorbed into the residual. If the
omitted variable is correlated with an included regressor → coefficients are **biased and
inconsistent** (omitted variable bias).

### #2 Variable Should Be Transformed
Regression assumes the dependent variable is **linearly** related to each independent variable. If
the true relationship is non-linear (e.g. portfolio returns are linear in ln(market cap), not in
market cap M), using M instead of ln(M) misspecifies the model.

### #3 Inappropriate Scaling ★
Financial-statement data usually need **standardizing**: income-statement / cash-flow items ÷ sales,
balance-sheet items ÷ total assets (i.e. **common-size**); or squaring / square-root transforms.
- Curriculum counter-example: using the **number** of tradable shares instead of the **proportion**
  (FF) → **similar companies get very different values** → inappropriate scaling.

### #4 Incorrectly Pooling Data
If the true relationship in the first 3 years differs from the second 3 years (coefficients change
over time) but you pool all 6 years into one regression → misspecified; tests and forecasts mislead.
Estimate the subperiods separately instead.

## Why Inappropriate Scaling Drives Heteroskedasticity + Multicollinearity (reasoning add-on)

> The following causal chain is derived from the heteroskedasticity / multicollinearity definitions,
> not verbatim curriculum text. The root cause in both is an unstripped **size effect**.

- **→ Heteroskedasticity**: if financial variables stay in raw dollar levels, their magnitude is tied
  to firm size. Large firms have larger absolute variation → residual variance rises with the level of
  the regressor → this is exactly **conditional heteroskedasticity**. Common-sizing removes the size
  effect and stabilizes residual variance.
- **→ Multicollinearity**: raw-dollar variables all scale up with firm size (big revenue → big assets /
  debt / profit) → they become **highly correlated** through a hidden common "size" factor.
  Common-sizing strips out that shared component and lowers the correlation.
- **Honest caveat**: pure linear constant rescaling (dollars → thousands) does NOT change correlation
  or heteroskedasticity. The CFA "inappropriate scaling" specifically means **failing to common-size
  when you should** — the root cause is the size effect contaminating both error variance and
  inter-variable correlation.

## Consequences Cheat-Sheet

| Misspecification type | Main consequence |
|------|------|
| Omitting a variable correlated with X | Biased + inconsistent coefficients |
| Omitting an uncorrelated variable, bad scaling, bad transform | Coefficients may stay unbiased, but error-term assumptions break (heteroskedasticity / serial correlation) → wrong standard errors → invalid inference |

## Exam Traps
- EOC question: "The least likely result of misspecification is ___" → answer is **"unbiased
  coefficients"** — because misspecification typically produces **biased** coefficients, or residuals
  with serial correlation / heteroskedasticity (unreliable standard errors).
- Heteroskedasticity / serial correlation are often **symptoms** of misspecification; the root cause is
  an omitted variable or wrong functional form. Prefer fixing the specification over only applying
  robust standard errors.

## Q&A

### 2026-06-01 — Why does omitting a key variable cause heteroskedasticity and serial correlation?
**Q:** Why can omitting a key variable from the model lead to heteroskedasticity and serial correlation?
**A:** The omitted variable Z does not vanish — its effect is pushed into the residual ε, so the
residual inherits Z's structure. ① **Serial correlation**: macro variables (GDP, rates) are highly
persistent; Z's "inertia" transfers to the residual, producing wave-like positive autocorrelation.
② **Heteroskedasticity**: if Z's variability differs across sample regions, the residual variance
varies too. Distinction: if the omitted variable is correlated with X, the worst consequence is
biased/inconsistent coefficients (OVB); heteroskedasticity/serial correlation is the error-assumption
layer (coefficients may stay unbiased, but standard errors fail).
Related: [[Regression_Assumption_Violations]]

### 2026-06-02 — Why does inappropriate variable scaling cause heteroskedasticity and multicollinearity?
**Q:** Why does inappropriate variable scaling lead to heteroskedasticity and multicollinearity?
**A:** The curriculum lists "inappropriate scaling" as functional-form misspecification #3 (failing to
common-size when you should). The root cause is the **size effect**: ① **heteroskedasticity** — raw
dollar variables are tied to firm size, so large firms have larger absolute variation → residual
variance rises with the regressor's level (conditional heteroskedasticity); ② **multicollinearity** —
raw dollar variables all inflate with size, so they correlate through a common "size" factor.
Common-sizing (÷ sales or total assets) fixes both. Note: pure linear constant rescaling by itself
changes neither correlation nor heteroskedasticity.
Related: [[Regression_Assumption_Violations]]
