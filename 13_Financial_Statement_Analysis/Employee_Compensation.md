---
aliases: [Employee Compensation, Pensions, Defined Benefit, Share-Based Compensation, Stock Options, Postemployment Benefits]
tags: [CFA-L2, fsa, concept]
date: 2026-06-03
status: evergreen
source: Schweser Book 2, Module 8, LOS 8.a-8.e
---

# Employee Compensation: Post-Employment and Share-Based

## Share-Based Compensation (8.b, 8.c)
- Aligns employee/owner interests; **non-cash** but a real expense. Examples: stock options, RSUs,
  stock appreciation rights, phantom stock.
- **Stock options**: measured at **fair value at grant date** (option-pricing model), expensed over the
  **vesting (service) period**. Fair value rises with: higher volatility, longer life, higher risk-free
  rate, lower dividend yield.
- Forecasting: model compensation expense (grants × fair value / vesting) and dilution from new shares.

## Pensions: DC vs DB (8.a, 8.d)
- **Defined contribution (DC)**: firm pays a fixed contribution; employee bears investment risk;
  pension expense = the contribution. No balance-sheet asset/liability beyond accrued contribution.
- **Defined benefit (DB)**: firm promises a future benefit; **firm bears investment risk**; requires
  estimating the obligation.

## DB Funded Status (8.d)
- **Funded status = Fair value of plan assets − PBO** (projected benefit obligation).
  - Positive → net pension **asset**; negative → net pension **liability** on the balance sheet.
- PBO grows with: service cost, interest cost, actuarial losses, past-service cost; shrinks with
  benefits paid.

## Periodic Pension Cost (IFRS vs US GAAP)
**Total periodic pension cost (TPPC)** = Employer contributions − (ending − beginning) funded status.
This is the same under both standards; only the **allocation between P&L and OCI** differs.

| Component | IFRS | US GAAP |
|------|------|------|
| Current service cost | P&L | P&L |
| Past service cost | **P&L (immediately)** | OCI, then amortized to P&L |
| Net interest (= net pension liability × discount rate) | P&L | — |
| Interest cost / expected return on assets (separately) | — | P&L (uses **expected** return) |
| Remeasurements (actuarial G/L, asset return vs expected) | **OCI (no recycling)** | OCI, then amortized (corridor) |

- IFRS uses a single **net interest** at the discount rate; US GAAP uses an **expected return on assets**
  assumption (a high expected return lowers reported pension expense → an analyst red flag).

## Aggressive Assumptions (red flags, verified to Schweser)
Choices that **reduce reported pension expense and/or the PBO** (flatter earnings):
- **High discount rate** (lowers PBO and service/interest cost)
- **Low compensation growth rate**
- **Low beneficiary life expectancy**
- **Low future inflation**
- **High expected return on plan assets** — **US GAAP only**; reduces pension expense but does **not**
  change the PBO or the fair value of plan assets.
- Note: a **decrease in the discount rate raises the PBO** → funded status **decreases** (more underfunded).

## Analyst Adjustments (8.e)
- Reclassify the **total** periodic pension cost: many analysts move all of it (or its operating part)
  appropriately, and reclassify the interest/return components to the **financing/investing** sections
  of the cash flow statement.
- Compare the **discount rate, expected return, and compensation growth** assumptions across firms —
  aggressive assumptions flatter earnings and shrink the obligation.

## Exam Traps
- **Funded status = plan assets − PBO**; it is what appears (net) on the balance sheet.
- US GAAP pension **expense** uses **expected** return on assets; IFRS uses the discount rate (net
  interest) — a key comparability difference.
- Past service cost: **IFRS expenses immediately**; US GAAP defers through OCI.
- Remeasurements/actuarial gains-losses go to **OCI** (both standards); IFRS does **not** recycle them.

## Q&A

### 2026-06-03 — Total periodic pension cost and IFRS vs US GAAP allocation
**Q:** How do you compute total periodic pension cost (TPPC), and what differs between IFRS and US GAAP?
**A:** `TPPC = employer contributions − (ending funded status − beginning funded status)`, equivalently
service cost + interest cost − actual return on assets ± actuarial changes. The **total is the same**
under both standards; only the **P&L vs OCI split** differs. IFRS: past service cost hits **P&L
immediately**, and a single **net interest** = net pension liability × discount rate; remeasurements →
OCI (no recycling). US GAAP: past service cost → **OCI then amortized**, and pension expense uses an
**expected return on assets** plus separate interest cost; actuarial G/L → OCI with corridor amortization.
Related: [[Quality_of_Financial_Reports]]

### 2026-06-03 — Effect of lowering the discount rate on the DB plan
**Q:** A firm lowers its pension discount rate. What happens to PBO, funded status, and is it aggressive?
**A:** A **lower discount rate raises the PBO** (future benefits discounted less) → **funded status
falls** (more underfunded) and service/interest cost dynamics shift. So a **high** discount rate is the
*aggressive/income-flattering* choice (smaller PBO, smaller cost). Other aggressive assumptions: low
compensation growth, low life expectancy, low inflation, and — **US GAAP only** — a **high expected
return on plan assets**, which cuts reported pension expense but does **not** change the PBO or plan
assets (a classic analyst red flag).
Related: [[Quality_of_Financial_Reports]]
