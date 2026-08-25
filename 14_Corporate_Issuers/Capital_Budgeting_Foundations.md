---
aliases: [Capital Budgeting, TNOCF, Terminal Year Non-Operating Cash Flow, NWC Recovery, Depreciation Tax Shield, Incremental Cash Flow, Nominal vs Real Cash Flows, Annuity Geometric Series]
tags: [CFA-L2, corp, foundation, L1-bridge]
date: 2026-08-25
status: evergreen
source: CFA Level I Corporate Issuers (Capital Investments) — NOT a 2026 L2 LOS; verified absent from all five 2026 Schweser L2 books. Retained as foundation for L2 Equity / FSA / Cost of Capital.
---

# Capital Budgeting Foundations (L1 bridge)

> ⚠️ **Scope honesty:** project capital budgeting (TNOCF, initial outlay, incremental project cash flows) is **not in the 2026 CFA L2 curriculum** — a search for "TNOCF" returns **zero hits across all five 2026 Schweser L2 books**. This is **Level I** material (Corporate Issuers — *Capital Investments*).
>
> It is kept here because each underlying logic reappears in L2 topics that **are** examinable. Each section below flags its L2 bridge.

## Project Cash Flow Skeleton

| Stage | Timing | Formula |
|---|---|---|
| **Initial outlay** (new project) | t = 0 | `Outlay = FCInv + NWCInv` |
| **Initial outlay** (replacement) | t = 0 | `Outlay = FCInv + NWCInv − Sal₀ + t(Sal₀ − B₀)` |
| **Annual after-tax operating CF** | t = 1…T | `CF = (S − C − D)(1 − t) + D = (S − C)(1 − t) + tD` |
| **Terminal non-operating CF** | t = T | `TNOCF = Sal_T + NWCInv − t(Sal_T − B_T)` |

Terminal-year total = annual operating CF **+** TNOCF.

---

## 1. Why NWC Is Recovered 100% and Untaxed

| Aspect | Fixed capital | Working capital |
|---|---|---|
| Economic nature | **Consumed** by use | **Advanced**, then revolves |
| Accounting | Depreciates toward salvage | Never depreciates |
| At termination | Recovered only at market salvage | Unwinds to cash at ~book |
| **Tax at exit** | **Taxed** on gain over book: `t(Sal − B)` | **NOT taxed** — return of principal |

`NWC = Inventory + AR − AP` is a **revolving float**. While the project runs it must be continuously replenished (inventory restocked, receivables re-extended), so it looks permanent — but it is never *destroyed*. At liquidation you stop replenishing: the last inventory sells, the last receivables collect, the float drains back to cash.

**Tax logic:** recovering NWC is not income, it is your own capital returning → no taxable event. Salvage differs because the asset's basis was written down, so the excess over book value is a **gain the tax code recaptures**.

**Caveat (assumption, not law):** 100% recovery assumes zero bad debt and zero inventory obsolescence. Real liquidations recover less. The exam always uses 100%.

**Why omitting it hurts SHORT projects most:** recovery arrives at T and is discounted by `(1+r)^(−T)`. For a 3-year project that factor barely erodes it; for a 15-year project the recovery is discounted to near-irrelevance. So the omission destroys proportionally more NPV the shorter the project → wrongly rejects high-return short projects.

> 🔗 **L2 bridge:** `WCInv` in FCFF/FCFE is the same concept — `FCFF = NI + NCC + Int(1−t) − FCInv − WCInv`. L2 refinement: WCInv **excludes cash & equivalents and short-term debt** (notes payable, current portion of LTD) because those are financing items counted elsewhere. An **increase** in WC **reduces** free cash flow. See [[Free_Cash_Flow_Valuation]].

---

## 2. Incremental Cash Flow — Every Capex Change Hits Twice

**Discipline:** a change in fixed capital investment has a **direct** effect (t=0 outlay) *and* a **secondary** effect (extra depreciation → annual tax shield). Missing the second systematically overstates cost risk.

**Generalized (straight-line to zero salvage):**

`ΔNPV = −ΔFCInv × [1 − (t/N) × PVA(r,N)]`

**Worked example** — ΔCapex = 250,000; N = 5; SL; tax = 40%; r = 10%:

| Effect | Timing | Amount |
|---|---|---|
| Direct outlay | t = 0 | −250,000 |
| Extra depreciation | t = 1…5 | 250,000/5 = 50,000/yr |
| Tax shield | t = 1…5 | 50,000 × 0.40 = **+20,000/yr** |

`ΔNPV = −250,000 + 20,000 × PVA(10%,5) = −250,000 + 20,000(3.7908) = −174,184`
Check via formula: `1 − (0.40/5)(3.7908) = 0.6967` → `−250,000 × 0.6967 = −174,175` ✓

**Economic reading:** the after-tax cost of a capital asset is only **~70 cents on the dollar** — the tax code subsidizes capex.

**The schedule matters, not just the total.** Accelerated depreciation (DDB/MACRS) and straight-line give **identical total nominal shields** but different **present values**, because acceleration front-loads them → **accelerated depreciation raises NPV** with no change to project economics. Classic exam setup: two identical projects, different depreciation methods.

Why `CF = (S − C)(1 − t) + tD` is written that way: depreciation is non-cash and enters **only** through the `tD` shield term.

> 🔗 **L2 bridge:** identical mechanism drives the after-tax cost of debt `r_d(1 − t)` in [[Cost_of_Capital]].

---

## 3. The Annuity Formula IS a Geometric Series

`PVA = PMT/(1+r) + PMT/(1+r)² + … + PMT/(1+r)^N`

Geometric with **first term** `a = PMT/(1+r)` and **common ratio** `q = 1/(1+r)`. Apply `S_N = a(1−qᴺ)/(1−q)`; denominator `1 − 1/(1+r) = r/(1+r)`:

`PVA = PMT × [1 − (1+r)^(−N)] / r`

| Geometric series | Finance | Meaning |
|---|---|---|
| first term `a` | `PMT/(1+r)` | first payment, discounted one period |
| common ratio `q` | `1/(1+r)` | **the discount factor** |
| `n` terms | `N` | periods |
| `q → 0` as `n → ∞` | **perpetuity** `= PMT/r` | — |

> 🔗 **L2 bridge — highest-value item here.** Change the ratio to `(1+g)/(1+r)` and sum to infinity:
> `PV = [D₁/(1+r)] / [1 − (1+g)/(1+r)] = [D₁/(1+r)] / [(r−g)/(1+r)] = **D₁/(r−g)**`
> **That is the Gordon Growth Model** — and therefore the terminal value in every multistage DDM, FCFF/FCFE model, and residual income continuing value. **Every L2 Equity valuation model is one geometric series with a different first term and ratio.** See [[Dividend_Discount_Models]], [[Free_Cash_Flow_Valuation]], [[Residual_Income]].

Exam practice: use the BA II Plus (`N`, `I/Y`, `PMT`, `CPT PV`); keep the derivation as the safety net for deformed shapes.

---

## 4. Nominal vs. Real — Direction Discipline

> **Core rule: inflation erodes the real value of any contractually fixed nominal amount. Whether that helps or hurts depends on whether you RECEIVE it or PAY it.**

| Fixed nominal item | Why locked | Real value | Effect on firm |
|---|---|---|---|
| **Depreciation tax shield** | tax law fixes it at **historical cost** | erodes | **HURTS** — you *receive* it; higher real taxes, lower real CF |
| **Interest on fixed-rate debt** | coupon fixed by contract | erodes | **HELPS** — you *pay* it; real burden shrinks |

**The erosion runs the same way for both; the impact on the firm is opposite.** This is the standard confusion point. Unexpected inflation transfers wealth from lender to borrower, while simultaneously taxing the firm harder through the frozen depreciation base.

**Consistency rule (#1 practical error):**
- **Nominal cash flows → nominal discount rate**
- **Real cash flows → real discount rate**
- Never mix. Fisher: `(1 + nominal) = (1 + real)(1 + inflation)`; approx. `nominal ≈ real + inflation`.

**Two directional errors — don't assume a prior:**

| Error | Result |
|---|---|
| Forecast CFs in **real** terms, discount at the **nominal** rate | **UNDER**valuation — most common |
| Inflate revenues/costs but forget **depreciation doesn't inflate** | **OVER**valuation of the shield |

**Refinements:** only **unexpected** inflation redistributes wealth (expected inflation is already priced into nominal rates and contracts). **Differential inflation** — inputs inflating faster than outputs compresses real margins independent of any tax effect.

> 🔗 **L2 bridge:** the identical logic drives the **temporal method** in FSA. Non-monetary assets (inventory, PP&E) sit at **historical cost** while monetary items move at current rates; a **net monetary liability** position produces a **remeasurement gain** when the local currency depreciates — i.e. *holding fixed nominal liabilities during inflation is a gain.* See [[Multinational_Operations]] (LOS 9.e/9.f trap) and [[Currency_Exchange_Rates]].

---

## Exam Traps

- **NWC recovery is NOT taxed** (return of principal); **salvage IS taxed**, but only on the gain over book value `t(Sal − B)`.
- Omitting NWC recovery understates terminal CF — and the distortion is **largest for short projects** (less discounting).
- A capex change hits **twice**: t=0 outlay **and** the annual depreciation tax shield. Net after-tax cost ≈ `ΔFCInv × [1 − (t/N)·PVA]`.
- **Accelerated depreciation raises NPV** vs. straight-line despite an identical total nominal shield — front-loading raises its PV.
- Depreciation enters cash flow **only** through `tD` — it is non-cash.
- **Inflation hurts the depreciation shield but helps the fixed-rate borrower.** Same erosion, opposite impact.
- **Never discount real cash flows at a nominal rate** (or vice versa) — the classic error undervalues the project.
- `PMT/(r−g)` is the same geometric series as `PVA`, with ratio `(1+g)/(1+r)` — this is Gordon Growth.

## Q&A

### 2026-08-02 — TNOCF, NWC recovery, tax shields, annuities, and inflation direction
**Q:** Four gaps: (1) what is NWC recovery in TNOCF; (2) net NPV impact of a capex increase; (3) how the annuity formula maps to a geometric series; (4) which direction inflation moves the tax shield vs. interest expense.
**A:** (1) `TNOCF = Sal_T + NWCInv − t(Sal_T − B_T)`. Fixed capital is **consumed**; working capital is **advanced** and revolves, so it unwinds to cash at termination and is **untaxed** (return of principal), unlike salvage. Omitting it hurts **short** projects most (less discounting). (2) Every capex change hits **twice**: `ΔNPV = −ΔFCInv[1 − (t/N)·PVA(r,N)]`. For 250,000 / 5yr / 40% / 10%: `−250,000 + 20,000(3.7908) = −174,184` — after-tax cost is only ~70% of sticker. Accelerated depreciation raises NPV via front-loaded shields despite identical totals. (3) PVA is geometric with `a = PMT/(1+r)`, `q = 1/(1+r)`; swap the ratio to `(1+g)/(1+r)` and sum to infinity → `D₁/(r−g)` = **Gordon Growth**, the skeleton of every L2 equity model. (4) Inflation erodes any **fixed nominal** amount, but direction of impact depends on receive vs. pay: the **depreciation shield (received) erodes → HURTS**; **fixed-rate interest (paid) erodes → HELPS**. Never mix nominal CFs with real rates.
Related: [[Free_Cash_Flow_Valuation]], [[Cost_of_Capital]], [[Multinational_Operations]], [[Dividend_Discount_Models]]
