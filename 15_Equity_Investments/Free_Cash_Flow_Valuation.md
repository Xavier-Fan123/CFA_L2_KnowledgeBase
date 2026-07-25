---
aliases: [Free Cash Flow Valuation, FCFF, FCFE, Free Cash Flow to Firm, Free Cash Flow to Equity]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 3, Module 19, LOS 19.a-19.m
---

# Free Cash Flow Valuation (FCFF / FCFE)

## Definitions & Perspective (19.a, 19.b)
- **FCFF**: cash available to **all** capital providers (debt + equity) after operating expenses, taxes, and reinvestment. Discount at **WACC** → firm value.
- **FCFE**: cash available to **common equity** after debt payments. Discount at **r (cost of equity)** → equity value directly.

## FCFF vs FCFE — Comparison & When to Use (19.b)
The cash-flow waterfall: operating cash (after tax, FCInv, WCInv) = **FCFF** (all capital providers, pre-financing) → subtract after-tax interest, add net borrowing → **FCFE** (common equity only, post-financing). Bridge: `FCFE = FCFF − Int(1−t) + Net borrowing`.

| Dimension | **FCFF** | **FCFE** |
|-----------|----------|----------|
| Claimants | Debt + equity (all providers) | Common equity only |
| Financing timing | **Pre-financing** (adds back after-tax interest) | **Post-financing** (interest & net borrowing already in) |
| Discount rate | **WACC** | **Cost of equity (r)** |
| Directly yields | **Firm value** | **Equity value** |
| To get equity value | Firm value − market value of debt | Already equity value |
| Sensitive to leverage? | **No** (interest added back to strip financing) | **Yes** (interest and net borrowing both move) |
| Dividends / buybacks? | No effect | No effect |

**Model choice depends on capital structure, not on control** (control = FCFE-vs-DDM, a separate axis):
- **Use FCFE** when leverage is **stable** and FCFE is positive — direct equity value, no need to estimate debt market value.
- **Use FCFF** when (1) **FCFE is negative** (high leverage / large debt repayments — hard to model), (2) **leverage is changing** (WACC is less sensitive to leverage shifts than the cost of equity, and FCFE would require forecasting net borrowing plus re-estimating r each period), or (3) **leverage is very high**.
- Note: an acquirer who will **re-lever** the firm leans toward **FCFF**, so a control stake does *not* by itself imply FCFE.

## FCFF Formulas (19.c, 19.d)
- From net income: `FCFF = NI + NCC + Int(1 − t) − FCInv − WCInv`
- From CFO: `FCFF = CFO + Int(1 − t) − FCInv`
- From EBIT: `FCFF = EBIT(1 − t) + Dep − FCInv − WCInv`
- From EBITDA: `FCFF = EBITDA(1 − t) + Dep × t − FCInv − WCInv`

> Add back **after-tax interest** because FCFF is pre-financing; under US GAAP interest paid is in CFO.

## FCFE Formulas (19.c, 19.d)
- From FCFF: `FCFE = FCFF − Int(1 − t) + Net borrowing`
- From net income: `FCFE = NI + NCC − FCInv − WCInv + Net borrowing`
- From CFO: `FCFE = CFO − FCInv + Net borrowing`

(Net borrowing = new debt issued − debt repaid.)

## Non-Cash Charges (NCC) — Add Back vs Subtract (19.c)
`NCC` in the FCFF/FCFE-from-NI formulas is the **net** of all non-cash items. Rule: a non-cash item that **reduced** NI is **added back (+)**; one that **increased** NI is **subtracted (−)**. FCFF and FCFE treat NCC **identically**.

| Non-cash item | Effect on NI | Adjustment |
|---------------|:---:|:---:|
| Depreciation / amortization / impairment | ↓ | **+** |
| **Restructuring charge (provision recorded)** | ↓ | **+** |
| **Restructuring charge REVERSAL (provision reversed → booked as income)** | ↑ | **− (subtract)** |
| Loss on sale of assets | ↓ | + |
| Gain on sale of assets | ↑ | − |
| Amortization of **bond discount** (raises interest expense) | ↓ | + |
| Amortization of **bond premium** (lowers interest expense) | ↑ | − |
| Deferred taxes (DTL increase) | — | + *only if expected to persist/recur — otherwise exclude* |

- A **restructuring charge** is a non-cash provision (estimated future cost accrued now) → add back. Its **reversal** (estimate was too high / plan scaled back) is non-cash **income** that inflates NI with no cash inflow → **subtract**. Same direction confusion as gains vs losses.
- Don't confuse the accrual with cash: actual restructuring cash paid (e.g., severance) flows through the accrued-liability change in **WCInv**; the charge/reversal accrual itself is the non-cash NCC item.

## Forecasting & Drivers (19.e, 19.f)
- Approaches: (1) grow historical FCF at a constant rate; (2) forecast each component.
- **Dividends, share repurchases, and share issuance do NOT affect FCFF or FCFE** (financing of equity, not operating). **Changes in leverage** affect FCFE (via net borrowing and interest) but not FCFF.
- Net income / EBITDA are **imperfect** proxies for cash flow (ignore reinvestment, WCInv, non-cash items).

## Valuation Models (19.j, 19.k, 19.l)
- **Single-stage**: `Firm value = FCFF1 / (WACC − g)`; `Equity = FCFE1 / (r − g)`.
- Equity value (from FCFF) = firm value − market value of debt.
- **Two/three-stage**: PV of explicit FCF + PV of terminal value (Gordon or exit multiple).
- Compare to market price → over/under/fairly valued (19.m).

## FCFF vs FCFE Valuation Paths — Same Equity Value When Consistent (19.k)
Two routes to equity value: **FCFF path** = PV(FCFF @ WACC) = firm value → **subtract market value of debt** (and preferred) → equity value. **FCFE path** = PV(FCFE @ cost of equity r) = equity value **directly**. With internally consistent assumptions they give the **same** equity value — the difference is the route, not the destination.

**Reconciliation example.** FCFF₁ = 100, WACC = 10%, g = 4% (FCFF, FCFE, and debt all grow 4%); target D/V = 30%, E/V = 70%; after-tax cost of debt = 5%.
- Back out cost of equity: `WACC = (E/V)r + (D/V)rd(1−t)` → `0.10 = 0.70r + 0.30(0.05)` → **r = 12.14%**.
- **FCFF path:** firm value `= 100/(0.10−0.04) = 1,666.67`; debt `= 30%×1,666.67 = 500`; equity `= 1,666.67 − 500 = 1,166.67`.
- **FCFE path:** after-tax interest `= 5%×500 = 25`; net borrowing (debt grows 4%) `= 4%×500 = 20`; `FCFE₁ = 100 − 25 + 20 = 95`; equity `= 95/(0.1214−0.04) = 1,166.67` ✓.
- **When they diverge in practice, trust FCFF** if leverage is changing (WACC less sensitive than r; FCFE path also needs per-period net-borrowing forecasts). Discount rate must match the flow — never FCFE @ WACC or FCFF @ r.

## Non-Operating Assets (19.l)
FCFF/FCFE value only the **operating** assets. If the firm holds significant **non-operating assets** — excess cash, excess marketable securities, land held for investment, financial (non-subsidiary) stock/bond holdings — **add their market value** to the DCF-based value: `Firm value = value of operating assets (FCFF DCF) + value of non-operating assets`. Revalue any such securities carried at book value to **current market value**. General rule: any asset excluded from the projected cash flows must be added back separately.

## Worked Example — Two-Stage FCFF
FCFF0 = $100m, grows 10% for 3 years, then 4% forever. WACC = 9%, market value of debt = $300m, 50m shares.
- Stage-1 FCFF: yr1 110, yr2 121, yr3 133.1.
- **Terminal value at end of yr3** (Gordon on yr4 FCFF): `TV3 = FCFF3(1+g)/(WACC − g) = 133.1×1.04/(0.09−0.04) = 138.42/0.05 = $2,768.5m`.
- Discount at WACC 9%: `PV = 110/1.09 + 121/1.09² + (133.1 + 2768.5)/1.09³ = 100.9 + 101.9 + 2,241.0 = $2,443.8m` = **firm value**.
- **Equity = firm value − debt = 2,443.8 − 300 = $2,143.8m** → per share `2,143.8/50 = $42.88`.
- Trap: the terminal value sits at the **end of the last explicit year** and is discounted back the **same** number of periods as the final-year flow.

## Worked Example — NCC Signs → FCFE (with distractors)
Given ($m): NI 500; D&A 120; **reversal** of prior restructuring charge 40; gain on equipment sale 25; bond **discount** amortization 10; deferred-tax-liability increase 15 (expected to persist); after-tax interest 35; FCInv (net) 200; WCInv (increase) 60; net borrowing 30; dividends paid 90; share repurchases 50. **Find FCFE.**
- **NCC signs** (lowered NI → +, raised NI → −): D&A **+120**, restructuring reversal **−40**, gain on sale **−25**, bond-discount amort. **+10**, deferred-tax increase **+15** → `NCC = 80`.
- `FCFE = NI + NCC − FCInv − WCInv + Net borrowing = 500 + 80 − 200 − 60 + 30 = **350**`.
- **Distractors that do NOT enter FCFE-from-NI:** after-tax interest 35 (that's an **FCFF** add-back — interest is already deducted in NI), dividends 90, and buybacks 50 (equity distributions affect **neither** FCFF nor FCFE).
- Check via bridge: `FCFF = 500 + 80 + 35 − 200 − 60 = 355`; `FCFE = FCFF − Int(1−t) + NB = 355 − 35 + 30 = 350` ✓.

## Exam Traps
- **FCFF discounted at WACC; FCFE discounted at cost of equity.**
- Add **after-tax interest** to get FCFF (not pre-tax).
- **Leverage changes affect FCFE, not FCFF.** Dividends/buybacks affect **neither**.
- WCInv excludes cash and short-term debt; an **increase** in working capital **reduces** free cash flow.
- **Add non-operating assets** (excess cash, investment land, financial holdings at market value) to the FCFF/FCFE-derived value — the DCF only captures operating assets.

## Q&A

### 2026-06-03 — Why does leverage affect FCFE but not FCFF?
**Q:** A firm issues new debt. What happens to FCFF and FCFE?
**A:** **FCFF is unaffected** — it's the cash to **all** providers before financing, so it doesn't matter how the firm is financed (you add back after-tax interest precisely to strip out the debt effect).
**FCFE changes**: `FCFE = FCFF − Int(1−t) + net borrowing`, so new borrowing **raises** current FCFE (cash in) and future interest **reduces** it. Dividends and buybacks affect **neither** — they're distributions of equity, not operating flows. Trap: don't double-count by both changing WACC weights and adjusting the flow.
Related: [[Dividend_Discount_Models]]

### 2026-06-03 — Getting FCFF from CFO vs from EBIT
**Q:** Two analysts start from CFO and from EBIT — what are the bridges to FCFF?
**A:** From **CFO** (US GAAP, interest in CFO): `FCFF = CFO + Int(1−t) − FCInv`. From **EBIT**: `FCFF = EBIT(1−t) + Dep − FCInv − WCInv`. From **net income**: `FCFF = NI + NCC + Int(1−t) − FCInv − WCInv`. The common thread: add back **after-tax** interest (FCFF is pre-financing) and subtract reinvestment (FCInv, WCInv). WCInv excludes cash and short-term debt; rising working capital **reduces** free cash flow.
Related: [[Residual_Income]]

### 2026-07-25 — Control perspective: why FCFE over DDM (not "FCFE over FCFF")
**Q:** Why should you use FCFE instead of FCFF when a company has a controlling investor?
**A:** **Trap — the premise conflates two independent decisions.** The "ownership / control perspective" (LOS 19.a "the ownership perspective implicit in the **FCFE** approach") is an argument for **FCFE over the DDM (dividends)**, *not* for FCFE over FCFF.
- **Control vs minority axis (FCFE vs dividends):** A **minority** shareholder only receives *declared* dividends → value them with the **DDM**. A **controlling** shareholder controls dividend policy and can direct the *disposition* of all equity cash flow, so value is based on the cash the firm **could** pay out = **FCFE** — the ownership perspective implicit in FCFE. Mnemonic: *control → "what could be paid" (FCFE); no control → "what was paid" (dividends).*
- **FCFE vs FCFF is a different axis — capital structure, not control.** Both ultimately give equity value (FCFF at WACC → firm value − debt). Use **FCFE** when leverage is **stable** (direct, no need for debt market value); use **FCFF** when leverage is **changing**, very **high**, or **FCFE is negative** (WACC is less sensitive to leverage shifts than cost of equity). Note an acquirer who will *re-lever* the firm leans **toward FCFF**, so "control" does not imply FCFE over FCFF.
Related: [[Dividend_Discount_Models]], [[Residual_Income]]

### 2026-07-25 — Reversal of a restructuring charge in FCFE
**Q:** What is a reversal of a previously recorded restructuring charge, and how does it affect the FCFE calculation?
**A:** A **restructuring charge** is a non-cash **provision** — a company accrues estimated future restructuring costs (layoffs, closures) now, reducing NI with no cash out. A **reversal** occurs when that estimate proves too high (costs lower, plan scaled back): the excess provision is written back as **income**, so **NI rises with no cash inflow**. In `FCFE = NI + NCC − FCInv − WCInv + Net borrowing`, the NCC rule is *non-cash item that lowered NI → add (+); item that raised NI → subtract (−)*. So a restructuring **charge** is **added back (+)**, but its **reversal is subtracted (−)** — omitting this overstates FCFE (and FCFF, which treats NCC identically). Same sign logic as loss (+) vs gain (−) and bond discount (+) vs premium (−) amortization. Note: actual restructuring cash paid runs through **WCInv** (accrued-liability change), not NCC.
Related: [[Market_Based_Valuation]]
