---
aliases: [Dividend Discount Models, DDM, Gordon Growth Model, H-Model, PVGO, Justified PE, Sustainable Growth]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 3, Module 18, LOS 18.a-18.p
---

# Dividend Discount Models (DDM)

## DCF Input Choice (18.a)
- **Dividends**: stable, dividend-paying firms; minority perspective.
- **FCFE**: firm pays no/erratic dividends but generates FCF; control perspective. → [[Free_Cash_Flow_Valuation]]
- **Residual income**: no dividends/FCF, but quality accounting. → [[Residual_Income]]

## General DDM & Gordon Growth (18.b, 18.c)
- `V0 = Σ Dt / (1+r)^t`.
- **Gordon growth (constant g forever)**: `V0 = D1 / (r − g) = D0(1+g)/(r − g)`. Requires `g < r`.
- **Perpetual preferred**: `V = D / r`.

## PVGO and Leading P/E (18.g, 18.h)
- `V0 = E1/r + PVGO` → no-growth value plus present value of growth opportunities.
- **Leading P/E** = `(1/r) + PVGO/E1`.
- **Justified leading P/E** = `(D1/E1)/(r − g) = payout / (r − g)`.
- **Justified trailing P/E** = `payout × (1+g) / (r − g)`.

## Implied Growth / Required Return (18.f, 18.i)
- Implied g (from Gordon): `g = r − D1/P0`.
- Required return: `r = D1/P0 + g` (Gordon), or from the **H-model** (below).

## Sustainable Growth (18.p)
- `g = b × ROE`, where `b` = retention = `1 − payout`.
- **DuPont**: `ROE = net margin × asset turnover × financial leverage`, so
  `g = b × (net margin × asset turnover × leverage)` (PRAT model).

## Multistage Models (18.k-18.o)
- Business stages: **growth → transition → maturity**. Use multistage when constant-growth is unrealistic.
- **Two-stage DDM**: PV of high-growth dividends + PV of terminal value (Gordon at stable g).
- **H-model** (growth declines linearly from gS to gL over 2H years):
  `V0 = [D0(1+gL) + D0 × H × (gS − gL)] / (r − gL)`, where **H = half the high-growth period**.
  - Required return (H-model): `r = (D0/P0)[(1+gL) + H(gS − gL)] + gL`.
- **Terminal value**: Gordon (perpetuity) or exit-multiple based.

## Strengths / Limits (18.e, 18.j)
- Gordon: simple, good for stable mature firms; **very sensitive to (r − g)**; useless for non-payers
  or g ≈ r.
- Compare model value to market price → **over/under/fairly valued**.

## Exam Traps
- Justified **leading** P/E = `payout/(r−g)`; **trailing** = `payout(1+g)/(r−g)` — don't mix.
- H-model **H = HALF** the high-growth (transition) period length.
- Gordon value explodes as `g → r`; small input changes move value a lot.
- `g = b × ROE` uses the **retention** ratio, not payout.

## Q&A

### 2026-06-03 — H-model worked example
**Q:** D0 = $2, current growth 15% declining linearly to 5% over 6 years, r = 10%. Value with the H-model.
**A:** H = half the transition period = 6/2 = **3**. `V0 = [D0(1+gL) + D0·H·(gS − gL)]/(r − gL) =
[2(1.05) + 2·3·(0.15 − 0.05)]/(0.10 − 0.05) = [2.10 + 0.60]/0.05 = 2.70/0.05 = $54`. Trap: **H is half**
the high-growth/transition period, and the long-run growth gL (not gS) goes in the denominator.
Related: [[Free_Cash_Flow_Valuation]]

### 2026-06-03 — Justified leading vs trailing P/E
**Q:** What's the difference between justified leading and trailing P/E, and when does each apply?
**A:** **Leading (forward) P/E** uses next year's earnings: `payout/(r − g)`. **Trailing P/E** uses last
year's: `payout(1+g)/(r − g)` — the extra `(1+g)` grosses the payout up to a forward basis. Use leading
when forecasts are reliable; trailing when current earnings are clean/representative. Both come from the
Gordon model and are very sensitive to `(r − g)`.
Related: [[Market_Based_Valuation]]
