---
aliases: [Forward Commitments, Forward Pricing, Futures Pricing, Carry Arbitrage, Interest Rate Swaps, Swap Valuation, FRA]
tags: [CFA-L2, deriv, concept, pricing]
date: 2026-06-03
status: evergreen
source: Official Curriculum V7 (Derivatives) Learning Module 1; Schweser Book 4, Module 28, LOS 28.a-28.g
---

# Pricing and Valuation of Forward Commitments

## Carry Arbitrage Model (28.a, 28.b)
Curriculum notation (official V7): the forward price is the **future value of the underlying adjusted
for carry**, where **CC** = carry costs (storage, insurance) and **CB** = carry benefits (dividends,
coupons, convenience yield).
- **No underlying cash flows**: `F0 = FV(S0) = S0 × (1 + r)^T` (annual) or `S0 × e^(rc·T)` (continuous).
  Carry arbitrage mechanics: borrow S0, buy spot, sell forward at F0 → 0 net cash flow today, riskless
  at T only if `F0 = FV(S0)`. If `F0 > FV(S0)`: sell forward + buy spot with borrowed funds (earn the
  excess); if `F0 < FV(S0)`: reverse carry — buy forward, short spot, lend proceeds.
- **With carry cash flows (Equation 4)**: `F0 = FV(S0 + CC0 − CB0) = FV(S0) + FV(CC) − FV(CB)`.
  - Carry **costs raise** F0 (the physical holder bears them, the forward holder avoids them).
  - Carry **benefits lower** F0 (the physical holder receives them, the forward holder forgoes them).
- Mnemonic: **"benefits down, costs up."** When CB > CC (e.g. high-dividend index) the forward can
  trade **below** spot (backwardation-like); when CC > CB, **above** spot (contango-like).

## Valuing a Forward During Its Life (28.a)
- Long forward value at time t: `Vt = PV[Ft − F0] = (Ft − F0) / (1 + r)^(T − t)`.
- Equivalent **direct form** (curriculum Eq. 3): `Vt = St − PV[F0]` (no-cashflow case); with carry,
  `Vt = (St − CB_t-to-T + CC_t-to-T) − PV[F0]` where the carry terms are PV'd to time t.
- At initiation **V0 = 0** (the forward price is set so no value changes hands). Short value = −Vt.
- **Worked example (V7 Eq. 3):** F0 = 105, t such that T−t = 0.25, r = 5%, observed Ft = 111.3499 (or
  equivalently spot St = 110). Long value = `(111.3499 − 105)/(1.05)^0.25 = 6.2729`, and via the direct
  form `110 − 105/(1.05)^0.25 = 6.2729`. Both routes agree.
- **Futures vs forward value**: a futures contract is **marked to market daily**, so its accumulated
  value resets to 0 after each settlement (`vt = Nf × (ft − ft−1)` then 0). A forward's value accrues
  until settlement. Prices are identical when rates are constant/uncorrelated with the underlying; they
  diverge only through the MTM/convexity effect.

## Equity Forwards & Futures (28.a)
- **Equity forward**: dividends are a carry benefit, so subtract their PV: `F0 = FV(S0 − PV(div)) =
  (S0 − PV div)(1+r)^T`. For a **continuous dividend yield δ**: `F0 = S0·e^((rc − δ)T)`.
- Profit at expiry on a long = `ST − F0`; value during life uses the general `Vt = St − PV(div) − PV[F0]`.

## Fixed-Income Forwards & Futures (28.d)
- Spot bond price (full) = quoted (clean) price + accrued interest: `S0 = B0 + AI0`. The carry benefit is
  the **PV of coupons** paid over the contract horizon: `CB0 = PVCI`; there are no carry costs (CC = 0).
- Forward/futures price: `F0 = FV(S0 − PVCI) = FV(B0 + AI0 − PVCI)`.
- For exchange-traded **bond futures**, the quoted futures price Q0 relates to F0 via the
  **conversion factor**: `F0 = Q0 × CF`, so the quoted price `Q0 = F0 / CF`. The seller delivers the
  **cheapest-to-deliver** bond (least costly after the CF adjustment).
- Long-forward profit at T: `VT = BT − F0 = (ST − AIT) − F0` (quoted-price basis).

## Interest-Rate Forwards — FRAs (28.c)
- An **FRA** (forward rate agreement) locks a single-period interest rate for an m-day deposit beginning
  h days forward. Notation **"X × Y"**: X = months to FRA expiration, Y − X = tenor of the underlying
  rate. A **1 × 4 FRA** expires in 1 month on a 3-month (90-day) MRR; a **3 × 9** expires in 3 months on
  a 6-month rate. Months are converted to days at 30 days/month.
- The **FRA price `FRA0` is the implied forward rate** for the period beginning at h, derived from the
  two spot rates Lh (to expiration) and LT (to underlying maturity), set so the FRA value = 0 at
  initiation. Long (pay-fixed) FRA = synthetic **long the longer deposit, short the shorter**; it profits
  when the reference rate **rises**.
- **Settlement**: FRAs are *advanced set, advanced settled* — the rate is observed at expiration (set)
  and the cash payment is made **at expiration** (settled early), so the payoff is **discounted** by one
  period at the realized rate: payment = `[(MRR − FRA0)·tm·NA] / (1 + MRR·tm)`. (Swaps and IR options are
  *advanced set, settled in arrears* — paid at the end of the accrual period.)
- **FRA value at a later time g (Eq. 7/8)**: it equals the PV of the change in the forward rate:
  - Long (receive-floating): `Vg = NA × {[FRAg − FRA0] × tm} / [1 + D(T−g)·t(T−g)]`.
  - Short (receive-fixed): `−Vg = NA × {[FRA0 − FRAg] × tm} / [1 + D(T−g)·t(T−g)]`.
  where FRAg is the new FRA rate at g for the same underlying period and D is the current discount rate.

## Interest Rate Swaps (28.e)
- A swap = portfolio of forwards / exchange of fixed for floating. Receive-fixed = **long a fixed-rate
  bond + short a floating-rate bond**; receive-floating = the reverse.
- **Par (market) swap fixed rate** from PV factors (PVi computed off the term structure):
  `rFIX = (1 − PV_n) / (Σ_{i=1..n} PV_i) × (1/AP)`. With **annual periods (AP = 1)** this reduces to the
  familiar `s = (1 − DF_n) / (DF_1 + … + DF_n)`. **Trap:** the **final-period PV factor is used twice** —
  once with the other coupon PVs in the denominator and once on par in the numerator (`1 − PV_n`).
- Per-period fixed cash flow per unit notional: `FS = AP × rFIX`. Net periodic exchange to the
  receive-floating party = `AP × (rFLT,i − rFIX) × NA`.
- **Swap value after initiation (Eq. 11)**: `Vswap = VFIX − VFLT` (value to the **receive-fixed** party).
  Practically, value an offsetting swap at the **new** par rate rFIX,t: per unit notional the value to the
  **receive-fixed** party = `Σ PV_i × AP × (rFIX,0 − rFIX,t) × NA` (positive when rates have **fallen**,
  because the fixed bond now trades at a premium). The pay-fixed (receive-floating) value is the negative.

## Currency Swaps (28.f)
- A currency swap exchanges interest (and usually **principal at both initiation and maturity**) in **two
  currencies**. View it as being **long a bond in one currency and short a bond in the other**.
- **Pricing** a fixed-for-fixed swap solves for the fixed rate **in each currency separately**, each via
  the same par-rate formula `rFIX,k = (1 − PV_n,k)/(Σ PV_i,k)` using that currency's term structure.
- **Value (Eq.)**: `VCS = NA_a·[AP·rFIX,a·Σ PV_i,a + PV_n,a] − S_t·NA_b·[AP·rFIX,b·Σ PV_i,b + PV_n,b]`,
  i.e. the difference of the two bond values, with the foreign leg converted at the **current spot FX
  rate S_t**. Value moves with **both rate curves and the spot exchange rate**; it is 0 at initiation.

## Equity Swaps (28.g)
- Exchange an **equity return** for (1) a fixed rate, (2) a floating rate, or (3) **another equity return**
  (three types). View it as **long an equity position + short a bond** (for receive-equity/pay-fixed).
- **Pricing**: the fixed rate on a receive-equity/pay-fixed swap is **identical to the fixed rate on a
  comparable plain-vanilla interest-rate swap** — `rFIX = (1 − PV_n)/(Σ PV_i)`. The equity leg needs no
  separate "pricing" because the equity return is whatever the index does.
- **Value at time t (receive-fixed, pay-equity), per unit notional**:
  `VEQ,t = [AP·rFIX·Σ PV_i + PV_n] − (S_t / S_t-reset)`, i.e. value of the fixed-rate bond **minus** the
  current equity index relative to its level at the last reset. For receive-equity/pay-fixed the sign
  flips. Value ≈ 0 when the equity has returned the fixed rate since the last reset.

## Exam Traps
- `F0 = FV(S0 + CC0 − CB0)`: carry **benefits (income) reduce** F0; carry **costs increase** it.
- Forward value during life = **PV of (Ft − F0)** = `St − PV[F0]`; **zero at initiation**.
- **FRA0 = the implied forward rate**; FRA is *advanced set, advanced settled* (payoff discounted one
  period); swaps/IR options are *settled in arrears*. FRA value at g = PV of `(FRAg − FRA0)`.
- Par swap rate = `(1 − PV_n)/(Σ PV_i) × (1/AP)`; the **final PV factor appears twice** (denominator
  with coupons, numerator on par). With AP = 1 it is `(1 − DF_n)/ΣDF`.
- **Swap value = VFIX − VFLT** to the receive-fixed party; equals `Σ PV × (rFIX,0 − rFIX,t) × NA` —
  **positive to the fixed receiver when rates fall**.
- **Equity-swap fixed rate = the comparable interest-rate-swap fixed rate** (do not re-derive separately).
- **Currency swap**: two bonds in two currencies; price each leg with its own curve; convert the foreign
  leg at the **current spot FX rate**.
- Futures ≠ forwards because of **daily MTM** (convexity / correlation effect); futures value resets to 0.

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

### 2026-06-04 — FRA notation and valuation at time g (worked)
**Q:** What does a "3 × 9 FRA" mean, and how do you value a long 6 × 9 FRA after it moves?
**A:** "3 × 9" = expires in **3 months** on a **6-month** (9 − 3) reference rate; the **FRA price is the
implied forward rate** for that period, set so initial value = 0. Value at time g = **PV of the change in
the FRA rate**: `Vg = NA × {[FRAg − FRA0]·tm} / [1 + D(T−g)·t(T−g)]` (long/receive-floating). Example:
long 6 × 9 FRA, NA = C$10,000,000, FRA0 = 0.877%, tm = 90/360. After 90 days the new 3-month FRA rate
FRAg = (say) 1.10% and the discount rate D(T−g) over the remaining 90 days is 1.35%; then
`Vg = 10,000,000 × [(0.0110 − 0.00877)(0.25)] / [1 + 0.0135(0.25)] ≈ 10,000,000 × 0.0005575 / 1.003375 ≈
C$5,556`. FRAs are **advanced set, advanced settled** (payoff discounted one period); swaps settle in
arrears.
Related: [[Options_Valuation]]

### 2026-06-04 — Valuing an interest-rate swap after rates move
**Q:** A 5-year receive-fixed swap was struck at rFIX,0 = 3.0%. Rates fall and the new par swap rate is
rFIX,t = 2.4%. Is the swap worth positive or negative to us, and how is it computed?
**A:** **Positive** to the receive-fixed party when rates fall. `Vswap = VFIX − VFLT`; equivalently value
an offsetting swap at the new par rate: per unit notional `V = Σ PV_i × AP × (rFIX,0 − rFIX,t) × NA`. With
annual resets, AP = 1; if Σ PV_i (the annuity factor on the remaining 5 cash flows) = 4.65 and NA =
$10,000,000, then `V = 4.65 × (0.030 − 0.024) × 10,000,000 = +$279,000`. Intuition: we keep receiving the
above-market 3.0% fixed coupon, so our fixed bond trades at a premium. The pay-fixed counterparty has the
mirror-image **−$279,000**.
Related: [[Options_Valuation]]

### 2026-06-04 — Currency vs equity swap pricing shortcuts
**Q:** How do you price a fixed-for-fixed currency swap and a receive-equity/pay-fixed equity swap?
**A:** **Currency swap** = long one currency's bond, short the other's; solve for the **fixed rate in each
currency separately** using that currency's PV factors (`rFIX,k = (1 − PV_n,k)/Σ PV_i,k`), and value as the
difference of the two bonds with the foreign leg converted at the **current spot FX rate**:
`VCS = NA_a[AP·rFIX,a·ΣPV_a + PV_n,a] − S_t·NA_b[AP·rFIX,b·ΣPV_b + PV_n,b]`. **Equity swap** fixed rate =
**the same as a comparable plain-vanilla interest-rate swap** (`(1 − PV_n)/ΣPV_i`); no separate equity-leg
pricing is needed. Equity-swap value at t (receive-fixed, pay-equity) = fixed-bond value −
(current index / index at last reset).
Related: [[Options_Valuation]]
