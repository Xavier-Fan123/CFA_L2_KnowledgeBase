---
aliases: [Forward Commitments, Forward Pricing, Futures Pricing, Carry Arbitrage, Interest Rate Swaps, Swap Valuation, FRA]
tags: [CFA-L2, deriv, concept, pricing]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 28, LOS 28.a-28.g
---

# Pricing and Valuation of Forward Commitments

## Carry Arbitrage Model (28.a, 28.b)
- **No underlying cash flows**: `F0 = S0 × (1 + r)^T` (forward price = future value of spot at the
  risk-free rate). Carry arbitrage: borrow, buy spot, sell forward → must be no-arb.
- **With carry cash flows**: `F0 = [S0 − PV(income) + PV(costs)] × (1 + r)^T`,
  equivalently `F0 = S0(1 + r)^T − FV(income) + FV(costs)`.
  - Income (dividends, coupons, convenience yield) **lowers** the forward; storage/costs **raise** it.

## Valuing a Forward During Its Life (28.a)
- Long forward value: `Vt = PV[ Ft − F0 ] = (Ft − F0) / (1 + r)^(T − t)`.
- At initiation V0 = 0 (forward price set so no value changes hands).

## Equity, Fixed-Income, Interest-Rate Forwards (28.a, 28.c, 28.d)
- **Equity forward**: subtract PV of expected dividends: `F0 = (S0 − PV div)(1+r)^T`.
- **Fixed-income forward/futures**: account for **accrued interest** and, for bond futures, the
  **conversion factor** and cheapest-to-deliver: `F0 = [(S0 − PV coupons)(1+r)^T] / CF`.
- **FRA / interest-rate forward**: locks a forward rate; value derived from the implied forward rate vs
  contract rate, discounted. Futures differ from forwards because of **daily mark-to-market** (convexity:
  futures price slightly differs when rates correlate with the underlying).

## Interest Rate Swaps (28.e)
- A swap = portfolio of forwards / exchange of fixed for floating.
- **Par (market) swap fixed rate**: `s = (1 − final discount factor) / (Σ discount factors)`
  = `(1 − DF_n) / (DF_1 + DF_2 + ... + DF_n)`.
- **Swap value** (to fixed-rate payer, after initiation) = PV(floating leg) − PV(fixed leg); reprice the
  fixed leg at the new par swap rate and discount the difference.

## Currency & Equity Swaps (28.f, 28.g)
- **Currency swap**: exchange principal and interest in two currencies; each leg priced like a bond in
  its own currency; value depends on both rate curves and the spot FX rate.
- **Equity swap**: exchange equity return for fixed/floating; value updated as the equity index and
  rates move; fixed rate set like an interest-rate swap at initiation.

## Exam Traps
- Income (dividends/coupons) **reduces** the forward price; storage costs **increase** it.
- Forward value during life = **PV of (Ft − F0)**; zero at initiation.
- Par swap rate = `(1 − final DF) / (sum of DFs)`.
- Futures ≠ forwards because of **daily MTM** (convexity / correlation effect).

## Q&A

### 2026-06-03 — Par swap rate from discount factors (worked)
**Q:** 1-, 2-, 3-year discount factors are 0.970, 0.940, 0.905. What's the par fixed swap rate?
**A:** `s = (1 − DF_n)/ΣDF = (1 − 0.905)/(0.970 + 0.940 + 0.905) = 0.095/2.815 = 3.375%`. Intuition: the
fixed rate makes PV(fixed leg) = PV(floating leg) = par at initiation, so the swap has **zero value** at
inception. After initiation, value to the **fixed-rate payer** = PV(floating) − PV(fixed), found by
repricing the fixed leg at the new par rate and discounting the difference.
Related: [[Options_Valuation]]

### 2026-06-03 — How do income and costs move the forward price?
**Q:** Why does dividend income lower a forward price while storage cost raises it?
**A:** `F0 = [S0 − PV(income) + PV(costs)](1+r)^T`. Holding the **forward** instead of the asset means you
**forgo** any income the asset pays (dividends, coupons, convenience yield) → the forward is cheaper by
that PV. Conversely you **avoid** carrying costs (storage, insurance) the physical holder bears → the
forward is dearer by that PV. Value during life = `PV(Ft − F0)`; zero at initiation. Futures differ from
forwards only via **daily mark-to-market** (a convexity effect when rates correlate with the underlying).
Related: [[Options_Valuation]]
