---
aliases: [Formula Cheat Sheet, Formula Sheet, Quicksheet, Final Review Formulas, Exam Formula Sheet]
tags: [CFA-L2, atlas, cheatsheet, formulas]
date: 2026-06-03
status: evergreen
source: Aggregated from all KB topic notes + 2026 Schweser Quicksheet
---

# CFA Level II — Cross-Topic Formula Cheat Sheet

Final-review aggregation of the highest-yield formulas across all ten topic areas. Each section links to
the detail note for derivations, worked examples, and exam traps. Formulas verified against the 2026
Schweser Notes / Quicksheet during the 2026-06-03 enrichment pass.

> Convention: `r` = required return / discount rate; `t` = tax rate; `g` = growth; `σ` = volatility/std dev.

---

## 11 — Quantitative Methods → [[Regression_Assumption_Violations]] · [[Time_Series_Analysis]] · [[Logistic_Regression]]
- **Adjusted R²** = `1 − [(n−1)/(n−k−1)] × (1 − R²)`.
- **AIC** = `n·ln(SSE/n) + 2(k+1)` (forecasting); **BIC** = `n·ln(SSE/n) + ln(n)·(k+1)` (goodness of fit). Lower = better; BIC penalizes added vars more.
- **F-test (overall)** = `MSR/MSE = (SSR/k)/(SSE/(n−k−1))`.
- **Nested-model F** = `[(SSE_R − SSE_U)/q] / [SSE_U/(n−k−1)]`.
- **VIF_j** = `1/(1 − R²_j)`; >5 investigate, >10 severe multicollinearity.
- **Breusch-Pagan** = `n·R²` (aux. regression of squared residuals), χ² with k df, one-tailed.
- **Logistic**: `ln[p/(1−p)] = b0 + b1X1 + …`; `P = 1/(1 + e^(−y))`. **LR test** = `−2(lnL_restricted − lnL_unrestricted)`.
- **AR(1) mean-reverting level** = `b0/(1 − b1)`. **Unit root**: b1 = 1 → not covariance stationary → first-difference.
- **RMSE** = `√(mean squared forecast error)` — pick the model with the lowest out-of-sample RMSE.

## 12 — Economics → [[Currency_Exchange_Rates]] · [[Economic_Growth]]
- **Forward (covered IRP)**: `F = S × (1 + r_price·τ)/(1 + r_base·τ)`, τ = days/360 (P/B quote).
- **MTM of FX forward**: `Vt = (F_t − F0)×size / (1 + r_price·(days left/360))` — discount at **price-currency** rate.
- **Uncovered IRP**: `E(%ΔS)_(A/B) ≈ R_A − R_B` (base = A). **Relative PPP**: `%ΔS_(A/B) ≈ infl_A − infl_B`.
- **International Fisher**: `R_nom,A − R_nom,B ≈ E(infl_A) − E(infl_B)`.
- **Cobb-Douglas**: `Y = A·K^α·L^(1−α)`. **Growth accounting**: `%ΔY = %ΔA + α·%ΔK + (1−α)·%ΔL`.
- **Labor-productivity growth**: potential GDP growth = labor-force growth + labor-productivity growth.
- **Solow steady state**: per-capita `g* = θ/(1−α)`; total `G* = g* + ΔL`.

## 13 — Financial Statement Analysis → [[Intercorporate_Investments]] · [[Employee_Compensation]] · [[Multinational_Operations]]
- **Full goodwill** = (price ÷ %acq) − FV identifiable net assets; **Partial goodwill** = price − %acq×(FV net assets).
- **Funded status** = fair value of plan assets − PBO. **TPPC** = employer contributions − ΔFunded status.
- **Translation**: current-rate gain/loss → **CTA in equity** (exposure = net assets); temporal → **remeasurement G/L in NI** (exposure = net monetary assets).
- **Combined ratio** (P&C) = loss ratio + expense ratio; **< 100% = underwriting profit**.
- **LCR** = HQLA / 30-day net outflows; **NSFR** = available / required stable funding (≥100%).

## 14 — Corporate Issuers → [[Cost_of_Capital]] · [[Dividends_and_Share_Repurchases]] · [[Corporate_Restructurings]]
- **Unlever (Hamada)**: `β_asset = β_equity / [1 + (1−t)(D/E)]`; **relever**: `β_equity = β_asset × [1 + (1−t)(D/E)]`.
- **Country risk premium**: `CRP = sovereign yield spread × (σ_equity/σ_bond)`; `r_e = R_f + β(ERP + CRP)`.
- **Bond-yield-plus-risk-premium**: `r_e = YTM_debt + 3–5%`.
- **Double-taxation effective rate** = `t_corp + (1 − t_corp)·t_div`.
- **Buyback EPS test**: accretive if **E/P (earnings yield) > after-tax cost of funds**.
- **Takeover premium** = `(DP − UP)/UP`, UP = unaffected (pre-announcement) price.

## 15 — Equity Investments → [[Dividend_Discount_Models]] · [[Free_Cash_Flow_Valuation]] · [[Residual_Income]] · [[Market_Based_Valuation]] · [[Private_Company_Valuation]]
- **Gordon**: `V0 = D1/(r − g)`. **PVGO**: `V0 = E1/r + PVGO`.
- **H-model**: `V0 = [D0(1+gL) + D0·H·(gS − gL)]/(r − gL)`, **H = ½ the high-growth period**.
- **Sustainable growth**: `g = b × ROE` (b = retention).
- **FCFF** = `NI + NCC + Int(1−t) − FCInv − WCInv` = `CFO + Int(1−t) − FCInv`. **FCFE** = `FCFF − Int(1−t) + net borrowing`. (FCFF→WACC; FCFE→r.)
- **Residual income**: `RI = (ROE − r)·B_(t−1)`; `V0 = B0 + ΣPV(RI)`. **EVA** = `NOPAT − WACC×capital`.
- **Justified P/E (leading)** = `payout/(r − g)`; **trailing** = `payout(1+g)/(r − g)`. **Justified P/B** = `(ROE − g)/(r − g)`.
- **EV** = market cap + debt + preferred + minority − cash. Average P/Es with the **harmonic mean**.
- **Total private-co discount** = `1 − (1 − DLOC)(1 − DLOM)`; **DLOC** = `1 − 1/(1 + control premium)`.

## 16 — Fixed Income → [[Term_Structure]] · [[Arbitrage_Free_Valuation]] · [[Bonds_With_Embedded_Options]] · [[Credit_Analysis_Models]] · [[Credit_Default_Swaps]]
- **Forward rate model**: `(1 + S_T)^T = (1 + S_(T−1))^(T−1)·(1 + f_(T−1,1))`.
- **Swap spread** = swap rate − Treasury; **Z-spread** over spot curve; **I-spread** over swap curve.
- **Callable** = straight − call; **Putable** = straight + put. Higher vol → lower callable, higher putable, **lower OAS**.
- **Effective duration** = `(V− − V+)/(2·V0·Δy)`; **effective convexity** = `(V− + V+ − 2V0)/(V0·Δy²)`.
- **CVA** = ΣPV(expected loss); expected loss = POD×LGD; **risky value = risk-free value − CVA**. **LGD** = exposure×(1 − recovery).
- **CDS upfront%** ≈ `(spread − coupon)×duration`; **ΔValue** ≈ `Δspread×duration×notional`; **payout** = notional×(1 − recovery).

## 17 — Derivatives → [[Forward_Commitments]] · [[Options_Valuation]]
- **Forward price**: `F0 = [S0 − PV(income) + PV(costs)]·(1+r)^T`. **Value during life** = `PV(F_t − F0)`.
- **Par swap rate**: `s = (1 − DF_n)/ΣDF`.
- **Binomial risk-neutral up-prob**: `π_U = (1 + r − d)/(u − d)`; option = `[π_U·c_up + π_D·c_down]/(1+r)`.
- **Hedge ratio (delta)** = `(c_up − c_down)/(S_up − S_down)`.
- **BSM call** = `S·N(d1) − Xe^(−rT)·N(d2)`; **put** = `Xe^(−rT)·N(−d2) − S·N(−d1)`. N(d1) = delta; N(d2) ≈ prob ITM.
- **Greeks**: gamma highest **ATM near expiry**; Black model values options on **futures** (and swaptions).

## 18 — Alternative Investments → [[Commodities]] · [[Real_Estate]] · [[Hedge_Fund_Strategies]]
- **Commodity total return** = spot return + **roll return** + collateral return. Backwardation → +roll; contango → −roll.
- **Direct cap (RE)**: `Value = NOI_year1 / cap rate`; **cap rate** = r − g = NOI/value.
- **FFO** = NI + depreciation + deferred tax − gains on sales. **AFFO** = FFO − maintenance capex − straight-line rent.
- **Loan sizing**: min of LTV constraint (value×max LTV) and DSCR constraint (NOI/DSCR → debt service → loan).
- Skew: merger arb = **negative** (sell-insurance); global macro/managed futures = **positive** (crisis alpha).

## 19 — Portfolio Management → [[Active_Portfolio_Management]] · [[Multifactor_Models]] · [[Measuring_Managing_Market_Risk]]
- **APT**: `E(R_p) = R_f + Σ β_j λ_j`.
- **Information ratio** = active return / active risk (tracking error). **Sharpe** uses total risk.
- **Fundamental law**: `IR = IC·√BR·TC`; `E(R_A) = IC·√BR·TC·σ_A`; optimal `σ_A* = (IR/SR_B)·σ_B`; `SR_P² = SR_B² + IR²`.
- **Active risk²** = active factor risk² + active specific risk².
- **VaR** = minimum loss at a confidence level over a period (use **CVaR/expected shortfall** for tail size).
- **Taylor rule**: `policy rate = neutral + inflation + 0.5(inflation gap) + 0.5(output gap)`.
- **Breakeven inflation** = nominal yield − real (TIPS) yield.
- **Total cost of ETF ownership** = expense ratio + spreads + premium/discount + tracking error.

## 20 — Ethics & GIPS → [[Code_and_Standards]] · [[GIPS]]
- No core formulas. Decision rules: follow the **stricter** of law vs Code & Standards; **mosaic theory** allowed; **priority of transactions** = clients > employer > self.
- **GIPS**: firm-wide, all-or-nothing; composite = **all** discretionary fee-paying portfolios of a strategy; min **5 years** of compliant history (build to 10); verification recommended, not required.

---

## How to use this sheet
- This is a **recall** tool, not a substitute for the detail notes — every line links to a note with the
  derivation, a worked example, and the exam traps. Drill the formula here, then click through if it doesn't
  click. For computational topics, the worked examples in the linked notes show the plug-and-chug.
