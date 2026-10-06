---
aliases: [Employee Compensation, Pensions, Defined Benefit, Share-Based Compensation, Stock Options, Postemployment Benefits]
tags: [CFA-L2, fsa, concept]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V3 LM2 (October 2026 errata applied); Schweser Book 2, Module 8, LOS 8.a-8.e
---

# Employee Compensation: Post-Employment and Share-Based

## Types of Compensation (8.a) — official Exhibit 1
Five types, split by (a) **time between service and payment** and (b) **form of payment**:

| Type | Definition | Examples |
|---|---|---|
| **Short-term benefits** | Paid within 12 months | Salaries, wages, annual bonuses, medical care, social-security contributions, paid leave |
| **Long-term benefits** | Paid after 12 months | Sabbaticals, long-term disability |
| **Termination benefits** | Paid on termination | Severance, continued medical access, outplacement |
| **Share-based compensation** | In, or by reference to, the employer's shares | Restricted stock, RSUs, stock options |
| **Post-employment benefits** | Paid after retirement | Pensions, lump sums, retiree life insurance and medical care |

- **IAS 19 principle**: recognize compensation **at fair value in the period the employee provides the service** (usually when it **vests**). Timeline: **grant** (terms agreed) → **vesting** (employee becomes unconditionally entitled) → **settlement** (employer pays).
- **Short-term benefits**: expense + current liability as service is provided; cash paid at settlement is an **operating** outflow. Manufacturing labor can be **capitalized into inventory** and expensed later through cost of sales.

## Share-Based Compensation (8.b, 8.c)
- **IFRS 2 model**: measure the award's **fair value at grant date** (adjusted for awards expected not to vest), expense it **straight-line over the vesting period** with the credit to **equity** (share-based compensation reserve), and true-up for changes in estimates. Fair value is measured **once** — later share-price moves do **not** change the expense on a past grant. **No cash-flow effect** (add the expense back under the indirect method).
  - *Official Example 2*: 25,000 shares, 3-year vesting, grant-date fair value BRL 273,000 → BRL 91,000 expense a year; at settlement BRL 273,000 moves from the reserve to common stock / paid-in capital.
- **Vesting conditions**: **service** (most common, typically 3-5 years); **performance** (EPS, ROIC, segment-profit targets); **market** conditions (TSR or relative share-price targets, common for executives). Leaving before vesting → the award is **forfeited**.
- **Instruments (official Exhibit 4)**: **restricted stock** (actual shares; voting and dividend rights; not tradeable; "performance shares" if performance-vested); **RSUs** (a right to receive shares; **no votes or dividends**; settle when they vest); **stock options** (non-tradeable, usually at-the-money calls); stock appreciation rights / phantom shares; employee stock purchase / ownership plans.
- **Grant-date fair value**: restricted stock and RSUs = **market price** of the share (RSUs adjusted **down** for dividends expected during vesting if they don't participate); options = an option-pricing model. Option exercise brings a **financing cash inflow** and issues shares.
- **Option fair value** (model inputs) rises with higher volatility, longer expected life, higher risk-free rate, and lower dividend yield.
- **Accounting entry**: the expense is credited to a **share-based compensation reserve** inside equity. On exercise (options) or vesting (shares) the balance is transferred out of the reserve into **common stock / additional paid-in capital** — so total equity is unaffected by the transfer itself.
- **Tax windfalls and shortfalls (8.b)** — the tax deduction is based on **intrinsic value at exercise** (options) or the **share price at settlement** (stock grants), which rarely equals the grant-date expense already booked.
  - Settlement price **above** grant-date price → **tax windfall** (deduction > cumulative expense).
  - Settlement price **below** grant-date price → **tax shortfall**.
  - **IFRS**: windfalls/shortfalls are recognized **directly in stockholders' equity**.
  - **US GAAP**: a windfall **reduces** income-tax expense and a shortfall **increases** it — i.e., it runs through the **income statement**, making the effective tax rate lumpy and share-price dependent.
- **Dilution — treasury stock method, official 2026 version**: unsettled awards are excluded from basic shares and enter **diluted** shares on a net basis:
  `Diluted shares = Basic + shares from assumed exercise/vesting − (Assumed proceeds ÷ Average share price)`, where **Assumed proceeds = cash proceeds from exercise (strike × options; zero for RSUs) + average unrecognized share-based compensation expense** (unvested awards × grant-date fair value, averaged over the last two period-ends).
  - Only awards **likely to vest** count — awards whose performance condition is not yet being met are excluded.
  - **ITM options are dilutive; ATM/OTM options are anti-dilutive** (excluded). **RSUs are dilutive** unless the average price is materially **below the grant-date price**. A **rising** share price means **more** dilution (fewer shares assumed repurchased).
  - **Net loss → basic = diluted** (diluted EPS cannot exceed basic EPS). For valuation, analysts should **add back anti-dilutive securities** from the notes — especially for loss-making firms and after large share-price declines.
- **Assumption sensitivity**: option-pricing inputs are management estimates. A **low volatility assumption lowers the option's fair value and therefore compensation expense** — a standard earnings-quality red flag (as do a low expected life, a low risk-free rate, or a high assumed dividend yield).

## Share-Based Compensation in Models and Valuation (8.c)
- **Forecast** it implicitly inside opex/margins only if it behaves like cash pay; for **early-stage** companies (SBC/revenue falls as firms mature) forecast it **discretely**, usually as a **% of revenue** (historical average, guidance, or reversion to the sector). A discrete forecast is also needed for the cash-flow statement, FCF, the cash balance, and non-GAAP metrics. Offset entry = equity; add back under the indirect method.
- **Share count**: basic shares roll forward with settlements, issuance, and buybacks; diluted shares add an assumed % of outstanding awards based on history. Option exercises bring cash; RSU vesting does not materially affect the statements.
- **Valuation**: SBC is non-cash but a **real transfer of value** that dilutes existing holders — a firm cannot raise its value by swapping cash pay for shares, and many firms buy back stock to offset dilution, which makes SBC behave like cash.
  1. **Outstanding awards** → value per share on **diluted** shares (optionally + anti-dilutive securities), or on basic + **gross** dilutive securities for a more conservative count.
  2. **Future awards** → the pragmatic fix is to **deduct SBC from free cash flow** in the DCF.
  - **Multiples**: check whether adjusted EBITDA / adjusted EPS **exclude** SBC. FCF margins and P/FCF **flatter heavy SBC users** — in the curriculum's Company A vs B example, identical net income but B's P/FCF is 37 vs A's 83 purely because B pays in shares.

## Pensions: DC vs DB (8.a, 8.d)
- **Defined contribution (DC)**: firm pays a fixed contribution; employee bears investment risk; pension expense = the contribution. No balance-sheet asset/liability beyond accrued contribution.
- **Defined benefit (DB)**: firm promises a future benefit; **firm bears investment risk**; requires estimating the obligation.
- **DC plan reporting**: same as short-term benefits — expense = the contribution, liability only for accrued unpaid contributions, contributions are an **operating** cash outflow; the employee bears investment and actuarial risk.
- **DB plans** are being **closed** (no new entrants) or **frozen** (no further benefit accrual) and replaced by DC; **OPEB** (retiree medical/life) are DB-type, often **unfunded / pay-as-you-go**, with the risks still borne by the company.

## DB Funded Status (8.d)
- **Funded status = Fair value of plan assets − PBO** (projected benefit obligation).
  - Positive → net pension **asset**; negative → net pension **liability** on the balance sheet.
- PBO grows with: service cost, interest cost, actuarial losses, past-service cost; shrinks with benefits paid.

## Periodic Pension Cost (IFRS vs US GAAP)
**Total periodic pension cost (TPPC)** = Employer contributions − (ending − beginning) funded status. This is the same under both standards; only the **allocation between P&L and OCI** differs.

| Component | IFRS | US GAAP |
|------|------|------|
| Current service cost | P&L | P&L |
| Past service cost | **P&L (immediately)** | OCI, then amortized to P&L |
| Net interest (= net pension liability × discount rate) | P&L | — |
| Interest cost / expected return on assets (separately) | — | P&L (uses **expected** return) |
| Remeasurements (actuarial G/L, asset return vs expected) | **OCI (no recycling)** | OCI, then amortized (corridor) |

- IFRS uses a single **net interest** at the discount rate; US GAAP uses an **expected return on assets** assumption (a high expected return lowers reported pension expense → an analyst red flag).

## Aggressive Assumptions (red flags, verified to Schweser)
Choices that **reduce reported pension expense and/or the PBO** (flatter earnings):
- **High discount rate** (lowers PBO and service/interest cost)
- **Low compensation growth rate**
- **Low beneficiary life expectancy**
- **Low future inflation**
- **High expected return on plan assets** — **US GAAP only**; reduces pension expense but does **not** change the PBO or the fair value of plan assets.
- Note: a **decrease in the discount rate raises the PBO** → funded status **decreases** (more underfunded).

## Worked Example — IFRS Periodic Pension Cost & Funded-Status Roll-Forward
*(curriculum Example, Module 2 "Workflow"; IFRS net-interest approach)*

Inputs: beginning **benefit obligation = 97**, beginning **plan assets = 1,010** (so beginning **net pension asset = 913**), **service cost = 9**, **discount rate = 2%**, **actual return on assets = 5%**, **benefits paid = 5**, no contributions, no amendments/assumption changes.

| Item | Calc | Amount |
|---|---|---|
| Current service cost (→ P&L, operating) | given | **9** |
| Net interest **income** (→ P&L) | beginning **funded status** × discount = `913 × 2%` | **+18.3** |
| Actual return on assets | `1,010 × 5%` | 50.5 |
| Expected (net-interest) return implied | `1,010 × 2%` | 20.2 |
| **Remeasurement** (→ OCI, no recycling) | actual − net-interest return on assets = `50.5 − 20.2` | **+30.3** |
| Ending **net pension asset** (BS) | `913 − 9 + 18.3 + 30.3` | **952.6** |

- **Benefits paid (5) are neutral** to funded status (plan assets and obligation both fall by 5) → no income or balance-sheet net effect; no contributions → **no cash-flow-statement impact**.
- **IFRS uses one net-interest number at the discount rate**; the gap between the **actual** 5% return and that net-interest rate is the **remeasurement to OCI**, NOT P&L.
- **US GAAP contrast (same facts):** service cost 9 to operating expense; a **gross interest cost** = `97 × 2% = 1.94` below operating income; a separate **expected return on assets** offset in earnings; the actual-vs-expected difference and actuarial G/L go to **OCI and are amortized** via the **corridor** (amortize only the excess of cumulative unrecognized G/L over **10% of the greater of** obligation or plan assets).

## DB Plans in Models and Valuation (8.e)
- **Modeling**: forecast **service cost, net interest, remeasurements, and employer contributions** → income statement amounts, the net pension asset/liability, and contributions on the cash-flow statement. Small, well-funded plans (net pension liability **≤ 5% of equity market cap**), especially closed or frozen ones, may not need detailed forecasts. DC expense is modeled implicitly inside opex.
- **Valuation must capture two effects**:
  1. **Funded status — asymmetric treatment**: an **underfunded** plan is treated as **debt** in enterprise value / the EV-to-equity bridge; an **overfunded** plan is **ignored**, because plan assets can only pay benefits and cannot be distributed to capital providers.
  2. **Future service cost** (not in funded status): like SBC, **leave it expensed — deduct it from FCF** (don't add it back), unless the plan is frozen.
  - **Net interest is excluded** from the DCF — it is the unwinding of the discounted obligation, already captured by deducting the net pension liability.
- **Assumptions to compare across time and peers**: aggressive (expense- and obligation-reducing) = **high discount rate, low salary growth, low life expectancy, low inflation**, a **low healthcare-cost growth rate** for OPEB, and — **US GAAP only** — a **high expected return on plan assets**.

## Exam Traps
- **Funded status = plan assets − PBO**; it is what appears (net) on the balance sheet.
- US GAAP pension **expense** uses **expected** return on assets; IFRS uses the discount rate (net interest) — a key comparability difference.
- Past service cost: **IFRS expenses immediately**; US GAAP defers through OCI.
- Remeasurements/actuarial gains-losses go to **OCI** (both standards); IFRS does **not** recycle them.
- **Treasury stock method (2026)**: assumed proceeds = exercise cash **+ average unrecognized SBC expense**; RSUs have zero exercise cash but still have unrecognized expense. Loss-making firm → diluted = basic, so **add back anti-dilutive securities** for valuation.
- **Underfunded DB plan = debt** in EV; **overfunded = ignore**. Deduct **future service cost** and **SBC** from FCF; leave **net pension interest** out of the DCF.
- SBC fair value is fixed at **grant date** — a later share-price rise does not raise the expense on existing grants.

## Q&A

### 2026-06-03 — Total periodic pension cost and IFRS vs US GAAP allocation
**Q:** How do you compute total periodic pension cost (TPPC), and what differs between IFRS and US GAAP?
**A:** `TPPC = employer contributions − (ending funded status − beginning funded status)`, equivalently service cost + interest cost − actual return on assets ± actuarial changes. The **total is the same** under both standards; only the **P&L vs OCI split** differs. IFRS: past service cost hits **P&L immediately**, and a single **net interest** = net pension liability × discount rate; remeasurements → OCI (no recycling). US GAAP: past service cost → **OCI then amortized**, and pension expense uses an **expected return on assets** plus separate interest cost; actuarial G/L → OCI with corridor amortization.
Related: [[Quality_of_Financial_Reports]]

### 2026-06-03 — Effect of lowering the discount rate on the DB plan
**Q:** A firm lowers its pension discount rate. What happens to PBO, funded status, and is it aggressive?
**A:** A **lower discount rate raises the PBO** (future benefits discounted less) → **funded status falls** (more underfunded) and service/interest cost dynamics shift. So a **high** discount rate is the *aggressive/income-flattering* choice (smaller PBO, smaller cost). Other aggressive assumptions: low compensation growth, low life expectancy, low inflation, and — **US GAAP only** — a **high expected return on plan assets**, which cuts reported pension expense but does **not** change the PBO or plan assets (a classic analyst red flag).
Related: [[Quality_of_Financial_Reports]]
