---
aliases: [Free Cash Flow Valuation, FCFF, FCFE, Free Cash Flow to Firm, Free Cash Flow to Equity]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 3, Module 19, LOS 19.a-19.m
---

# Free Cash Flow Valuation (FCFF / FCFE)

## Definitions & Perspective (19.a, 19.b)
- **FCFF**: cash available to **all** capital providers (debt + equity) after operating expenses,
  taxes, and reinvestment. Discount at **WACC** → firm value.
- **FCFE**: cash available to **common equity** after debt payments. Discount at **r (cost of equity)**
  → equity value directly.

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

## Forecasting & Drivers (19.e, 19.f)
- Approaches: (1) grow historical FCF at a constant rate; (2) forecast each component.
- **Dividends, share repurchases, and share issuance do NOT affect FCFF or FCFE** (financing of equity,
  not operating). **Changes in leverage** affect FCFE (via net borrowing and interest) but not FCFF.
- Net income / EBITDA are **imperfect** proxies for cash flow (ignore reinvestment, WCInv, non-cash items).

## Valuation Models (19.j, 19.k, 19.l)
- **Single-stage**: `Firm value = FCFF1 / (WACC − g)`; `Equity = FCFE1 / (r − g)`.
- Equity value (from FCFF) = firm value − market value of debt.
- **Two/three-stage**: PV of explicit FCF + PV of terminal value (Gordon or exit multiple).
- Compare to market price → over/under/fairly valued (19.m).

## Worked Example — Two-Stage FCFF
FCFF0 = $100m, grows 10% for 3 years, then 4% forever. WACC = 9%, market value of debt = $300m, 50m shares.
- Stage-1 FCFF: yr1 110, yr2 121, yr3 133.1.
- **Terminal value at end of yr3** (Gordon on yr4 FCFF): `TV3 = FCFF3(1+g)/(WACC − g) = 133.1×1.04/(0.09−0.04)
  = 138.42/0.05 = $2,768.5m`.
- Discount at WACC 9%: `PV = 110/1.09 + 121/1.09² + (133.1 + 2768.5)/1.09³ = 100.9 + 101.9 + 2,241.0 = $2,443.8m`
  = **firm value**.
- **Equity = firm value − debt = 2,443.8 − 300 = $2,143.8m** → per share `2,143.8/50 = $42.88`.
- Trap: the terminal value sits at the **end of the last explicit year** and is discounted back the **same**
  number of periods as the final-year flow.

## Exam Traps
- **FCFF discounted at WACC; FCFE discounted at cost of equity.**
- Add **after-tax interest** to get FCFF (not pre-tax).
- **Leverage changes affect FCFE, not FCFF.** Dividends/buybacks affect **neither**.
- WCInv excludes cash and short-term debt; an **increase** in working capital **reduces** free cash flow.

## Q&A

### 2026-06-03 — Why does leverage affect FCFE but not FCFF?
**Q:** A firm issues new debt. What happens to FCFF and FCFE?
**A:** **FCFF is unaffected** — it's the cash to **all** providers before financing, so it doesn't matter
how the firm is financed (you add back after-tax interest precisely to strip out the debt effect).
**FCFE changes**: `FCFE = FCFF − Int(1−t) + net borrowing`, so new borrowing **raises** current FCFE
(cash in) and future interest **reduces** it. Dividends and buybacks affect **neither** — they're
distributions of equity, not operating flows. Trap: don't double-count by both changing WACC weights and
adjusting the flow.
Related: [[Dividend_Discount_Models]]

### 2026-06-03 — Getting FCFF from CFO vs from EBIT
**Q:** Two analysts start from CFO and from EBIT — what are the bridges to FCFF?
**A:** From **CFO** (US GAAP, interest in CFO): `FCFF = CFO + Int(1−t) − FCInv`. From **EBIT**:
`FCFF = EBIT(1−t) + Dep − FCInv − WCInv`. From **net income**: `FCFF = NI + NCC + Int(1−t) − FCInv − WCInv`.
The common thread: add back **after-tax** interest (FCFF is pre-financing) and subtract reinvestment
(FCInv, WCInv). WCInv excludes cash and short-term debt; rising working capital **reduces** free cash flow.
Related: [[Residual_Income]]
