---
aliases: [Economic Growth, Growth Accounting, Production Function, Solow Model, Convergence, Capital Deepening]
tags: [CFA-L2, econ, concept, growth]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 6, LOS 6.a-6.l
---

# Economic Growth

## Preconditions & Investor Relevance (6.a-6.c)
- **Developed-economy drivers**: savings/investment, financial markets, rule of law, education,
  free trade, openness. Developing economies often lack these → constraints.
- **Stock market vs economy**: in the long run, `%ΔP = %ΔGDP + %Δ(E/GDP) + %Δ(P/E)`. Over long
  horizons share of profits and P/E are roughly stable, so **long-run equity appreciation ≈
  sustainable GDP growth**.
- **Potential GDP** = maximum sustainable output; its **growth rate** drives long-run equity returns,
  real interest rates, and government debt capacity. Higher potential growth → higher real rates.

## Production Function & Growth Accounting (6.d, 6.e)
- Cobb-Douglas: `Y = A · K^α · L^(1−α)`, where `A` = total factor productivity (TFP), `α` = output
  elasticity of capital, constant returns to scale.
- **Growth accounting** (Solow): `%ΔY = %ΔA + α·%ΔK + (1−α)·%ΔL`.
- **Labor productivity** approach: `growth in potential GDP = growth in labor force + growth in labor productivity`.
- **Worked example (Schweser – Azikland):** labor = 60% of total factor cost → (1−α)=0.60, α=0.40; labor
  growth 1.5%, capital growth 3%, TFP growth 2%.
  `%ΔY = 2% + 0.40×3% + 0.60×1.5% = 2% + 1.2% + 0.9% = 4.1%` potential GDP growth.

## Capital Deepening vs Technological Progress (6.d)
- **Capital deepening** = more capital per worker (move **along** the per-worker production function).
  Subject to **diminishing marginal returns** — once capital-deep, it adds little growth.
- **Technological progress** = TFP gain (shifts the function **up**). The only source of **sustained**
  per-capita growth once diminishing returns set in.
- **When capital deepening stops**: firms add capital while **MPK > r** (rental rate); at the K/L where
  **MPK = r**, capital deepening halts and labor productivity stagnates absent technological progress.
  Developed economies (high K/L, low α) gain little from capital deepening; developing economies (low
  K/L) can still gain in the short run.

## Natural Resources & Demographics (6.f, 6.g, 6.h)
- Resource **ownership** is not required for growth (can import); the "resource curse" can even hinder
  growth (Dutch disease, weak institutions).
- Growth sources: **physical capital, human capital, technological development**. Demographics,
  immigration, and labor-force participation drive the labor-input component.

## Growth Theories (6.i)

| Theory | Key idea | Long-run per-capita growth |
|------|------|------|
| **Classical (Malthus)** | Population growth eats up gains; subsistence | **Zero** (no sustained growth) |
| **Neoclassical (Solow)** | Diminishing returns to capital; economy reaches **steady state**; only TFP growth sustains it | per-capita `g* = θ / (1−α)`; total `G* = g* + ΔL`; capital deepening cannot sustain growth |
| **Endogenous** | R&D / knowledge has **positive externalities** → no diminishing returns to (broad) capital; saving/investment **can** affect long-run growth | Determined within the model; self-sustaining |

**Solow steady-state formulas** (θ = growth rate of technology/TFP, α = capital's share):
- Sustainable growth of **output per capita** `g* = θ / (1 − α)`.
- Sustainable growth of **total output** `G* = g* + ΔL` (add labor-force growth).
- **Professor's note trap:** capital (K) does **not** appear — capital deepening still occurs in steady
  state but does **not** raise the growth rate. In steady state MPK = Y/K is constant and output per
  worker grows at θ/(1−α).

## Convergence Hypotheses (6.j)
- **Absolute convergence**: all countries converge to the same per-capita income level. (Not supported.)
- **Conditional convergence**: countries converge **only if** they share the same savings rate,
  population growth, and production function — convergence to **their own** steady state.
- **Club convergence**: only members of a "club" (similar institutions) converge; poor countries
  outside the club may diverge.

## Government & Trade (6.k, 6.l)
- Rationale for **subsidizing R&D/knowledge**: positive externalities → private investment is below the
  social optimum.
- **Removing trade barriers**: raises investment and growth, reallocates toward comparative advantage;
  convergence is faster for open economies.

## Exam Traps
- **Capital deepening cannot sustain growth** (diminishing returns); only **TFP / technological
  progress** sustains per-capita growth in the neoclassical model.
- Neoclassical: higher savings raises the **level** of output and **temporarily** its growth, but **not
  the long-run growth rate**. Endogenous theory: savings **can** raise the long-run rate.
- Convergence is **conditional/club**, not absolute, empirically.

## Q&A

### 2026-06-03 — Solow steady-state growth rate: per-capita vs total
**Q:** In the neoclassical (Solow) model, what is the sustainable growth rate, and does saving/capital change it?
**A:** Per-capita sustainable growth `g* = θ/(1−α)` (TFP growth ÷ labor's share); total-output growth
`G* = g* + ΔL`. Capital (K) does **not** enter the formula — a higher savings rate raises the **level**
of the per-worker output path and **temporarily** its growth, but once steady state is reached, capital
deepening cannot raise the long-run growth rate (diminishing MPK). Only **TFP growth (θ)** raises g*.
(Endogenous-growth theory is the exception: there saving/investment *can* lift the permanent rate.)
Related: [[Economics_Overview]]

### 2026-06-03 — Capital deepening vs technological progress
**Q:** Why can't capital deepening sustain per-capita growth, but technology can?
**A:** Capital deepening = raising K/L, a **move along** the per-worker production function → subject to
**diminishing marginal returns**; firms add capital only while MPK > rental rate r, and stop when MPK = r,
after which extra capital adds ~nothing. Technological progress raises **TFP (A)**, which **shifts the
whole function up**, so it keeps adding output without bound → it is the only source of **sustained**
per-capita growth in the neoclassical model. Developed economies (high K/L) gain little from deepening;
developing economies (low K/L) can still gain in the short run.

### 2026-06-03 — Three convergence hypotheses
**Q:** Distinguish absolute, conditional, and club convergence.
**A:** **Absolute** — all countries converge to the same per-capita income regardless of conditions
(neoclassical model does **not** imply this; empirically unsupported). **Conditional** — convergence
occurs **only for countries sharing the same savings rate, population growth, and production function**;
each converges to **its own** steady state, with poorer members growing faster en route (this is what
Solow actually predicts). **Club** — only members of a "club" with similar institutions converge; poor
countries **outside** the club can fall further behind (diverge).
Related: [[Economics_Overview]]
