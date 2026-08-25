---
aliases: [Dividend Discount Models, DDM, Gordon Growth Model, H-Model, PVGO, Justified PE, Sustainable Growth]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-08-25
status: evergreen
source: Schweser Book 3, Module 18, LOS 18.a-18.p
---

# Dividend Discount Models (DDM)

## DCF Input Choice (18.a)
- **Dividends**: stable, dividend-paying firms; minority perspective.
- **FCFE**: firm pays no/erratic dividends but generates FCF; control perspective. → [[Free_Cash_Flow_Valuation]]
- **Residual income**: no dividends/FCF, but quality accounting. → [[Residual_Income]]

## General DDM & Gordon Growth (18.b, 18.c, 18.d)
- Whatever the holding period, **price = PV of forecast dividends + PV of the estimated terminal value**, all at the required return.
  - **One-period DDM**: `V0 = (D1 + P1)/(1 + r)`.
  - **Two-period DDM**: `V0 = D1/(1+r) + (D2 + P2)/(1+r)^2`.
  - **Multi-period / general**: `V0 = Σ_{t=1..n} D_t/(1+r)^t + P_n/(1+r)^n`, and with `n → ∞` the terminal term vanishes: `V0 = Σ D_t/(1+r)^t`.
- **Gordon growth (constant g forever)**: `V0 = D1 / (r − g) = D0(1+g)/(r − g)`.
- **The three GGM assumptions (18.c)** — state them, don't just use the formula:
  1. **Dividends grow at a constant rate** forever.
  2. **Dividend policy is tied to earnings** (payout is stable, so dividends track earning power).
  3. **`r > g`** — the required return exceeds the long-run growth rate (otherwise the value is negative or infinite).
- **Perpetual preferred (18.d)**: a fixed-rate perpetual preferred is a level perpetuity → `V = D / r` (g = 0 in the Gordon model).

## PVGO and Leading P/E (18.g, 18.h)
- `V0 = E1/r + PVGO` → no-growth value (`E1/r`, value if 100% payout) plus present value of growth opportunities. Solve for PVGO from price: `PVGO = P0 − E1/r`.
- **Leading P/E** = `(1/r) + PVGO/E1` — splits the multiple into a no-growth component (1/r) and a growth component (PVGO/E1).
- **Justified leading P/E** = `(D1/E1)/(r − g) = payout / (r − g)`.
- **Justified trailing P/E** = `payout × (1+g) / (r − g)`.
- **Worked example (curriculum, MSEX; 2026 errata):** no-growth EPS E1 = $1.52, r = 6.8%, price = $43.20. No-growth value = 1.52/0.068 = **$22.35**; `PVGO = 43.20 - 22.35 = $20.85`, so about 48% of price is the value of growth. A high PVGO/Price (or high PVGO/E1) signals a market-priced growth firm.

## Implied Growth / Required Return (18.f, 18.i)
- Implied g (from Gordon): `g = r − D1/P0`.
- Required return: `r = D1/P0 + g` (Gordon), or from the **H-model** (below).

## Sustainable Growth (18.p)
- **Definition**: the SGR is the rate at which earnings (and dividends) can grow **indefinitely** *assuming the firm holds its **debt-to-equity ratio constant** and **issues no new equity***. Those two assumptions are what make it "sustainable" — and are the usual exam hook.
- `g = b × ROE`, where `b` = retention = `1 − payout`.
- **PRAT / DuPont expansion**: `ROE = net margin × asset turnover × financial leverage`, so `g = (P)rofit margin × (R)etention rate × (A)sset turnover × financial leverage (T)`.
- **Use beginning-of-period balance-sheet values** for ROE (and therefore for the SGR) unless the question tells you otherwise — using ending equity is a common wrong turn.

## Multistage Models and Terminal Value (18.k, 18.m, 18.n)
- Business stages: **growth → transition → maturity**. Use multistage when constant-growth is unrealistic (e.g., earnings growing far above nominal GDP growth — not sustainable in perpetuity).
- **Two-stage DDM**: PV of high-growth dividends + PV of terminal value (Gordon at stable g).
- **H-model** (growth declines linearly from gS to gL over 2H years): `V0 = [D0(1+gL) + D0 × H × (gS − gL)] / (r − gL)`, where **H = half the high-growth period**.
  - Required return (H-model): `r = (D0/P0)[(1+gL) + H(gS − gL)] + gL`.
- **Three-stage DDM** — two common variants:
  1. **Three-step (growth / transition / maturity)**: a constant high growth, then constant transition growth, then a constant mature growth → discount each stage's dividends, add a Gordon terminal value at the start of the mature phase.
  2. **Growth + H-model tail**: a constant high-growth stage 1, then an **H-model** decline to the mature rate. Discount stage-1 dividends + PV of the H-model value.
- **Terminal value**: Gordon (perpetuity) or **exit / price multiple** based (e.g., terminal P/E × terminal EPS) → see [[Market_Based_Valuation]].
- **Share repurchases**: a DDM still works if the analyst nets the buyback effect into the **per-share** dividend growth rate (total distributions ÷ a shrinking share count).

## Multistage Strengths & Limitations (18.l)
**Strengths**
- **Flexible** — any growth pattern can be modeled.
- Can be run **in reverse**: solve for the required return or the growth rate **implied by the market price**.
- Forces the analyst to make every growth/return assumption **explicit and reviewable**, and to test their impact.
- **Easy to build and compute** in a spreadsheet.

**Limitations**
- Output is only as good as the **assumptions and projections** fed in.
- The model must be **fully understood** for its assumptions' effects to be traced.
- Values are **very sensitive** to the growth and required-return inputs.
- **Formula and data-entry errors** are easy to make and hard to spot.

## Spreadsheet Modeling (18.o)
In practice analysts use a **spreadsheet** rather than a stylized closed-form model, because a spreadsheet handles **any number of stages** with a separate growth rate for each, and is more flexible and computationally accurate. The steps:
1. **Establish the base level** of dividends (or cash flows).
2. **Forecast the change** in dividends for each year of the foreseeable future.
3. Estimate the **normalized long-run growth rate** at the end of the supernormal period, so a **terminal value** can be computed.
4. **Discount and sum** all projected dividends plus the terminal value back to today.

## Strengths / Limits of the Gordon Model (18.e, 18.j)
**GGM strengths**
- Very applicable to **stable, mature dividend-paying** firms.
- Applies easily to **broad equity indexes**.
- **Simple to communicate and explain.**
- Useful for backing out **price-implied growth rates**, **required returns**, and the **value of growth opportunities (PVGO)**.
- Can be **embedded in more complex valuations** (e.g., as the terminal-value step of a multistage model).

**GGM limitations**
- Values are **extremely sensitive** to `r` and `g`, both hard to estimate precisely.
- **Cannot be applied to non-dividend-paying** stocks.
- Breaks down for firms with **unpredictable or non-constant** growth patterns.

- Compare model value to market price → **over/under/fairly valued** (model value below market → overvalued).

## Exam Traps
- Justified **leading** P/E = `payout/(r−g)`; **trailing** = `payout(1+g)/(r−g)` — don't mix.
- H-model **H = HALF** the high-growth (transition) period length.
- Gordon value explodes as `g → r`; small input changes move value a lot.
- `g = b × ROE` uses the **retention** ratio, not payout — and the SGR assumes a **constant D/E ratio and no new equity issuance**, on **beginning-of-period** balance-sheet values.
- Terminal value in any DDM comes from **either the Gordon model or a market multiple** (e.g., terminal P/E × terminal EPS) — 18.m expects both.
- Know the **18.l list**: multistage models are flexible, invertible (solve for r or g), explicit, and spreadsheet-friendly; but assumption-driven, sensitivity-prone, and error-prone.

## Q&A

### 2026-06-03 — H-model worked example
**Q:** D0 = $2, current growth 15% declining linearly to 5% over 6 years, r = 10%. Value with the H-model.
**A:** H = half the transition period = 6/2 = **3**. `V0 = [D0(1+gL) + D0·H·(gS − gL)]/(r − gL) = [2(1.05) + 2·3·(0.15 − 0.05)]/(0.10 − 0.05) = [2.10 + 0.60]/0.05 = 2.70/0.05 = $54`. Trap: **H is half** the high-growth/transition period, and the long-run growth gL (not gS) goes in the denominator.
Related: [[Free_Cash_Flow_Valuation]]

### 2026-06-03 — Justified leading vs trailing P/E
**Q:** What's the difference between justified leading and trailing P/E, and when does each apply?
**A:** **Leading (forward) P/E** uses next year's earnings: `payout/(r − g)`. **Trailing P/E** uses last year's: `payout(1+g)/(r − g)` — the extra `(1+g)` grosses the payout up to a forward basis. Use leading when forecasts are reliable; trailing when current earnings are clean/representative. Both come from the Gordon model and are very sensitive to `(r − g)`.
Related: [[Market_Based_Valuation]]
