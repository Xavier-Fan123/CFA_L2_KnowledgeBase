---
aliases: [Economic Growth, Growth Accounting, Production Function, Solow Model, Convergence, Capital Deepening]
tags: [CFA-L2, econ, concept, growth]
date: 2026-06-03
status: evergreen
source: Schweser Book 1, Module 6, LOS 6.a-6.l
---

# Economic Growth

## Preconditions & Investor Relevance (6.a-6.c)
- **Developed-economy drivers**: savings/investment, financial markets, rule of law, education, free trade, openness. Developing economies often lack these → constraints.
- **Stock market vs economy**: in the long run, `%ΔP = %ΔGDP + %Δ(E/GDP) + %Δ(P/E)`. Over long horizons share of profits and P/E are roughly stable, so **long-run equity appreciation ≈ sustainable GDP growth**.
- **Potential GDP** = maximum sustainable output; its **growth rate** drives long-run equity returns, real interest rates, and government debt capacity. Higher potential growth → higher real rates.

## Exam Workflow - Potential GDP and Market Implications (6.b, 6.c, 6.e)
When the vignette asks what economic growth means for assets, work in this order:

1. **Estimate potential GDP growth.** Use either growth accounting or the labor-productivity shortcut.
2. **Separate level effects from growth-rate effects.** Higher saving or capital deepening can raise the level of output; only TFP/technology sustains per-capita growth in the neoclassical model.
3. **Map growth to equities.** Long-run equity price appreciation is approximately sustainable GDP growth if `E/GDP` and `P/E` are stable; short-run equity returns can diverge through profit-share and multiple changes.
4. **Map growth to fixed income.** Higher potential growth tends to raise equilibrium real rates and debt capacity; lower potential growth tends to cap real rates and worsen fiscal sustainability.
5. **Check the model assumption.** If the case says diminishing returns, think Solow; if it says knowledge spillovers / constant returns to broad capital, think endogenous growth.

## Production Function & Growth Accounting (6.d, 6.e)
- Cobb-Douglas: `Y = A · K^α · L^(1−α)`, where `A` = total factor productivity (TFP), `α` = output elasticity of capital, constant returns to scale.
- **Growth accounting** (Solow): `%ΔY = %ΔA + α·%ΔK + (1−α)·%ΔL`.
- **Labor productivity** approach: `growth in potential GDP = growth in labor force + growth in labor productivity`.
- **Worked example (Schweser – Azikland):** labor = 60% of total factor cost → (1−α)=0.60, α=0.40; labor growth 1.5%, capital growth 3%, TFP growth 2%. `%ΔY = 2% + 0.40×3% + 0.60×1.5% = 2% + 1.2% + 0.9% = 4.1%` potential GDP growth.

## Capital Deepening vs Technological Progress (6.d)
- **Capital deepening** = more capital per worker (move **along** the per-worker production function). Subject to **diminishing marginal returns** — once capital-deep, it adds little growth.
- **Technological progress** = TFP gain (shifts the function **up**). The only source of **sustained** per-capita growth once diminishing returns set in.
- **When capital deepening stops**: firms add capital while **MPK > r** (rental rate); at the K/L where **MPK = r**, capital deepening halts and labor productivity stagnates absent technological progress. Developed economies (high K/L, low α) gain little from capital deepening; developing economies (low K/L) can still gain in the short run.

### Growth Accounting Calculation Checklist (6.d, 6.e)

| Step | Action | Exam trap |
|---|---|---|
| 1 | Identify capital share `alpha` and labor share `1 - alpha`. | If the vignette gives labor's share, capital's share is the complement. |
| 2 | Apply `%dY = %dA + alpha * %dK + (1 - alpha) * %dL`. | Do not add unweighted input growth rates. |
| 3 | If TFP is missing, solve `%dA = %dY - alpha * %dK - (1 - alpha) * %dL`. | TFP is a residual, not directly observed. |
| 4 | If using the shortcut, use `potential GDP growth = labor-force growth + labor-productivity growth`. | Labor productivity already embeds capital deepening and TFP. |
| 5 | Interpret the result for investors. | Potential GDP is a long-run anchor, not a one-period equity-return forecast. |

**Worked example - solve for TFP residual:** output growth is 3.8%, capital grows 4.0%, labor grows 1.0%, and labor's income share is 65%. Then `alpha = 35%`, so `TFP growth = 3.8% - 0.35(4.0%) - 0.65(1.0%) = 1.75%`.

## Natural Resources & Demographics (6.f, 6.g, 6.h)
- Resource **ownership** is not required for growth (can import); the "resource curse" can even hinder growth (Dutch disease, weak institutions).
- Growth sources: **physical capital, human capital, technological development**. Demographics, immigration, and labor-force participation drive the labor-input component.

## Growth Theories (6.i)

- **Classical (Malthus)**: population growth eats up gains; subsistence.
  - Long-run per-capita growth: **zero** (no sustained growth).
- **Neoclassical (Solow)**: diminishing returns to capital; economy reaches **steady state**; only TFP growth sustains it.
  - Long-run per-capita growth: `g* = θ / (1−α)`; total `G* = g* + ΔL`; capital deepening cannot sustain growth.
- **Endogenous**: R&D / knowledge has **positive externalities** → no diminishing returns to (broad) capital; saving/investment **can** affect long-run growth.
  - Long-run per-capita growth: determined within the model; self-sustaining.

**Solow steady-state formulas** (θ = growth rate of technology/TFP, α = capital's share):
- Sustainable growth of **output per capita** `g* = θ / (1 − α)`.
- Sustainable growth of **total output** `G* = g* + ΔL` (add labor-force growth).
- **Professor's note trap:** capital (K) does **not** appear — capital deepening still occurs in steady state but does **not** raise the growth rate. In steady state MPK = Y/K is constant and output per worker grows at θ/(1−α).
- On the steady-state path the **marginal product of capital = the real interest rate** of the economy and is constant (= αY/K for Cobb-Douglas), even though k = K/L keeps rising at θ/(1−α). (Official curriculum.)

**Endogenous growth model formulas** (official curriculum, Reading 6, Eq. 12):
- Production function is a **straight line** (constant returns to broad/knowledge capital, no diminishing returns at the economy level): `ye = c · ke`, where `c` is the constant economy-wide MPK and the output-to-capital ratio is fixed at `c`. (Contrast: neoclassical function curves and flattens.)
- Growth rate of output per capita: **`Δye/ye = Δke/ke = s·c − δ − n`** (s = saving rate, c = output/capital ratio, δ = depreciation rate, n = labor-force growth). This is **both** the short-run and long-run rate, so a **higher saving rate `s` permanently raises growth** — the key result that distinguishes endogenous from neoclassical theory.
- **Worked example (official, Example 12):** s rises 20% → 23.5%, c = 0.7040, δ = 10%, n = 1%. New per-capita growth `= 0.235 × 0.7040 − 0.10 − 0.01 = 0.0554 = 5.54%` (vs prior 3.08%). The 2.46% faster growth compounds: after 10 years per-capita income is `exp(0.0246 × 10) = exp(0.246) ≈ 1.279` → **~28% higher, and permanently so** (no diminishing returns), versus only a temporary lift in the Solow model.
- Implication: with constant/increasing returns to knowledge capital, **incomes need NOT converge** — developed economies can keep growing as fast as or faster than developing ones.

### Growth Theory Identification Table (6.i)

| Vignette clue | Model | What changes long-run per-capita growth? | Saving-rate effect | Convergence implication |
|---|---|---|---|---|
| population pressure, subsistence wages | **Classical / Malthusian** | none in the long run | eaten up by population growth | no sustained per-capita growth |
| diminishing MPK, curved production function, steady state | **Neoclassical / Solow** | TFP / technology only | higher level and temporary growth boost | conditional convergence |
| R&D spillovers, knowledge capital, constant returns to broad capital | **Endogenous** | saving, R&D, human capital, technology policy | permanent growth-rate effect | convergence not guaranteed |

Exam shortcut: if the question says **saving permanently raises growth**, it is endogenous. If it says **saving raises output but not the steady-state growth rate**, it is neoclassical.

## Convergence Hypotheses (6.j)
- **Absolute convergence**: all countries converge to the same per-capita income level. (Not supported.)
- **Conditional convergence**: countries converge **only if** they share the same savings rate, population growth, and production function — convergence to **their own** steady state.
- **Club convergence**: only members of a "club" (similar institutions) converge; poor countries outside the club may diverge.

## Government & Trade (6.k, 6.l)
- Rationale for **subsidizing R&D/knowledge**: positive externalities → private investment is below the social optimum.
- **Removing trade barriers**: raises investment and growth, reallocates toward comparative advantage; convergence is faster for open economies.
- **Free trade by model** (LOS 6.l pairing is neoclassical vs endogenous): **Neoclassical** — capital flows to capital-scarce countries (higher MPK) → faster capital deepening → **temporary** growth boost, **permanently higher level**, faster convergence. **Endogenous** — bigger markets, competition, scale economies, and international knowledge spillovers → **permanently higher growth rate**.

### Policy and Trade Effects Checklist (6.k, 6.l)

| Policy / change | Immediate channel | Long-run growth effect | Distribution issue |
|---|---|---|---|
| **R&D / knowledge incentives** | raises private investment in innovation | higher TFP and knowledge spillovers | benefits may be broad but uneven by industry |
| **Human-capital investment** | raises labor productivity | higher potential GDP through productivity | delayed payoff; depends on institutions |
| **Removing trade barriers** | more competition and specialization | higher productivity, investment, and growth | import-competing sectors lose jobs/wages |
| **Opening capital markets** | more financing for productive capital | can speed capital deepening and convergence | raises exposure to external shocks |

For trade-barrier questions, separate **aggregate growth** from **sector effects**. The economy can gain through specialization and productivity while some workers and firms lose during reallocation.

## Exam Traps
- **Capital deepening cannot sustain growth** (diminishing returns); only **TFP / technological progress** sustains per-capita growth in the neoclassical model.
- Neoclassical: higher savings raises the **level** of output and **temporarily** its growth, but **not the long-run growth rate**. Endogenous theory: savings **can** raise the long-run rate.
- Convergence is **conditional/club**, not absolute, empirically.

- If the question gives output growth and input growth, TFP is the **residual** after subtracting weighted capital and labor contributions.
- In equity-market growth questions, sustainable GDP growth is only a long-run anchor; short-run returns also depend on `E/GDP` and `P/E` changes.
- Removing trade barriers can raise aggregate growth while hurting import-competing workers/firms; do not call every participant a winner.

## Q&A

### 2026-07-11 — Free trade under the growth models
**Q:** What do the growth models predict about opening an economy to free trade?
**A:** The tested pairing (LOS 6.l) is neoclassical vs endogenous. **Neoclassical**: capital flows to capital-scarce economies with higher MPK → faster capital deepening → **temporary** growth-rate boost, **permanently higher output level**, and **faster (conditional) convergence** — the long-run rate returns to g* = θ/(1−α). **Endogenous**: larger markets, competition, economies of scale, and knowledge/technology spillovers raise innovation → **permanently higher growth rate**; also lets developing countries import technology. Shortcut: "temporary boost / level / convergence" → neoclassical; "permanent rate increase via spillovers" → endogenous. Always separate aggregate gains from **import-competing sector losses**. (Classical/Malthus is not tested on trade; any gain would be diluted by population growth — beyond-curriculum note.)
Related: [[Economics_Overview]]

### 2026-06-03 — Solow steady-state growth rate: per-capita vs total
**Q:** In the neoclassical (Solow) model, what is the sustainable growth rate, and does saving/capital change it?
**A:** Per-capita sustainable growth `g* = θ/(1−α)` (TFP growth ÷ labor's share); total-output growth `G* = g* + ΔL`. Capital (K) does **not** enter the formula — a higher savings rate raises the **level** of the per-worker output path and **temporarily** its growth, but once steady state is reached, capital deepening cannot raise the long-run growth rate (diminishing MPK). Only **TFP growth (θ)** raises g*. (Endogenous-growth theory is the exception: there saving/investment *can* lift the permanent rate.)
Related: [[Economics_Overview]]

### 2026-06-07 - Solving for TFP as the growth-accounting residual
**Q:** Output grows 3.8%, capital grows 4.0%, labor grows 1.0%, and labor's income share is 65%. What is TFP growth?
**A:** Use capital's share as the complement: `alpha = 35%`. Growth accounting gives `%dY = %dA + alpha * %dK + (1 - alpha) * %dL`, so `%dA = 3.8% - 0.35(4.0%) - 0.65(1.0%) = 1.75%`. Trap: do not weight labor by 35%; the vignette gave labor's share, so capital's share is the complement.
Related: [[Economics_Overview]]

### 2026-06-07 - Identifying the growth model from vignette clues
**Q:** How do you distinguish classical, neoclassical, and endogenous growth theory in a question stem?
**A:** Classical/Malthusian stems emphasize population pressure and subsistence, so no sustained per-capita growth. Neoclassical/Solow stems emphasize diminishing marginal product of capital, a steady state, and saving raising the **level** but not the long-run growth rate. Endogenous stems emphasize R&D, knowledge spillovers, human capital, constant returns to broad capital, and saving/investment raising the **permanent growth rate**.
Related: [[Economics_Overview]]

### 2026-06-07 - Trade-barrier removal: aggregate gains vs sector losses
**Q:** What does removing trade barriers do to growth, investment, employment, wages, and profits?
**A:** Aggregate growth tends to improve through specialization, competition, productivity, and investment. But the gains are not uniform: export-competitive and expanding sectors gain investment, profits, jobs, and wages, while import-competing sectors can lose employment and pricing power during reallocation. On the exam, separate the economy-wide growth effect from the distributional sector effect.
Related: [[Currency_Exchange_Rates]]

### 2026-06-03 — Capital deepening vs technological progress
**Q:** Why can't capital deepening sustain per-capita growth, but technology can?
**A:** Capital deepening = raising K/L, a **move along** the per-worker production function → subject to **diminishing marginal returns**; firms add capital only while MPK > rental rate r, and stop when MPK = r, after which extra capital adds ~nothing. Technological progress raises **TFP (A)**, which **shifts the whole function up**, so it keeps adding output without bound → it is the only source of **sustained** per-capita growth in the neoclassical model. Developed economies (high K/L) gain little from deepening; developing economies (low K/L) can still gain in the short run.

### 2026-06-04 — Endogenous growth model: formula and why saving matters permanently
**Q:** What is the endogenous-growth-model growth equation, and why does a higher saving rate raise growth permanently there but only temporarily in the Solow model?
**A:** The endogenous model uses a **linear** production function `ye = c·ke` (constant economy-wide MPK = c, no diminishing returns to broad/knowledge capital from R&D externalities). Per-capita growth is **`Δye/ye = s·c − δ − n`** (saving rate × output-capital ratio − depreciation − labor growth), which is both the short- and long-run rate. Because there are **no diminishing returns**, a higher `s` shifts this rate up **permanently**. In the **neoclassical/Solow** model, diminishing MPK means a higher `s` only lifts growth during the transition to a new steady state, after which growth reverts to `θ/(1−α)` (saving changes the **level**, not the long-run **rate**). Official Example 12: s 20%→23.5%, c=0.704, δ=10%, n=1% gives `0.235×0.704 − 0.10 − 0.01 = 5.54%`, ~2.46% above the old 3.08%, compounding to ~28% higher income after 10y.
Related: [[Economics_Overview]]

### 2026-06-04 — Two methods to forecast potential GDP growth
**Q:** What are the two growth-accounting ways to estimate the growth rate of potential GDP?
**A:** (1) **Growth-accounting equation** (from the Cobb-Douglas function): `%ΔY = %ΔTFP + α·%ΔK + (1−α)·%ΔL`, where α and (1−α) are capital's and labor's income shares. (2)
**Labor-productivity approach:** `growth in potential GDP = long-term growth of the labor force + long-term growth of labor productivity`. Method (2) is often preferred in practice because labor-productivity trends are more stable/observable than a separately estimated TFP residual. Trap: TFP is never measured directly — it is the **residual** left after subtracting the weighted input growth from output growth.
Related: [[Economics_Overview]]

### 2026-06-03 — Three convergence hypotheses
**Q:** Distinguish absolute, conditional, and club convergence.
**A:** **Absolute** — all countries converge to the same per-capita income regardless of conditions (neoclassical model does **not** imply this; empirically unsupported). **Conditional** — convergence occurs **only for countries sharing the same savings rate, population growth, and production function**; each converges to **its own** steady state, with poorer members growing faster en route (this is what Solow actually predicts). **Club** — only members of a "club" with similar institutions converge; poor countries **outside** the club can fall further behind (diverge).
Related: [[Economics_Overview]]
