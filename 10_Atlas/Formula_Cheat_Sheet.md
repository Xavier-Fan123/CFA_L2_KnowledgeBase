---
aliases: [Formula Cheat Sheet, Formula Sheet, Quicksheet, Final Review Formulas, Exam Formula Sheet]
tags: [CFA-L2, atlas, cheatsheet, formulas]
date: 2026-06-03
status: evergreen
source: Aggregated from all KB topic notes + 2026 Schweser Quicksheet
---

# CFA Level II — Cross-Topic Formula Cheat Sheet

Final-review aggregation of the highest-yield formulas across all ten topic areas. Each section links to the detail note for derivations, worked examples, and exam traps. Formulas verified against the 2026 Schweser Notes / Quicksheet during the 2026-06-03 enrichment pass.

> Convention: `r` = required return / discount rate; `t` = tax rate; `g` = growth; `σ` = volatility/std dev.

---

## 11 — Quantitative Methods → [[Regression_Assumption_Violations]] · [[Time_Series_Analysis]] · [[Logistic_Regression]]
> Every test's distribution / df / tails / decision rule: **[[Statistical_Tests_Master_Table]]**.
- **Coefficient CI**: $\hat{b}_j \pm t_c \cdot SE(\hat{b}_j)$, df $= n-k-1$, **always two-tailed**. Critical z values — 90/95/99%: two-tailed **1.645 / 1.96 / 2.58**, one-tailed **1.28 / 1.645 / 2.33**. (One-tailed at α = two-tailed at 2α, so 1.645 appears in both.)
- **Adjusted R²**: $\bar{R}^2 = 1 - \dfrac{n-1}{n-k-1}\,(1 - R^2)$.
- **AIC** $= n\ln(\text{SSE}/n) + 2(k+1)$ (forecasting); **BIC** $= n\ln(\text{SSE}/n) + \ln(n)\,(k+1)$ (goodness of fit). Lower = better; BIC penalizes added vars more.
- **F-test (overall)**: $F = \dfrac{\text{MSR}}{\text{MSE}} = \dfrac{\text{SSR}/k}{\text{SSE}/(n-k-1)}$.
- **Nested-model F**: $F = \dfrac{(\text{SSE}_R - \text{SSE}_U)/q}{\text{SSE}_U/(n-k-1)}$.
- **VIF**: $\text{VIF}_j = \dfrac{1}{1 - R^2_j}$; >5 investigate, >10 severe multicollinearity.
- **Breusch-Pagan**: $\text{BP} = n\cdot R^2$ (aux. regression of squared residuals), χ² with k df, one-tailed.
- **Logistic**: $\ln\!\left[\dfrac{p}{1-p}\right] = b_0 + b_1X_1 + \dots$; $P = \dfrac{1}{1 + e^{-y}}$. **LR test** $= -2(\ln L_{\text{restricted}} - \ln L_{\text{unrestricted}})$.
- **AR(1) mean-reverting level**: $\dfrac{b_0}{1 - b_1}$. **Unit root**: $b_1 = 1$ → not covariance stationary → first-difference.
- **RMSE** $= \sqrt{\text{mean squared forecast error}}$ — pick the model with the lowest out-of-sample RMSE.

## 12 — Economics → [[Currency_Exchange_Rates]] · [[Economic_Growth]]
- **Forward (covered IRP)**: $F = S\,\dfrac{1 + r_{\text{price}}\tau}{1 + r_{\text{base}}\tau}$, $\tau = \text{days}/360$ (P/B quote).
- **MTM of FX forward**: $V_t = \dfrac{(F_t - F_0)\times\text{size}}{1 + r_{\text{price}}(\text{days left}/360)}$ — discount at **price-currency** rate.
- **Uncovered IRP**: $E(\%\Delta S)_{A/B} \approx R_A - R_B$ (base = A). **Relative PPP**: $\%\Delta S_{A/B} \approx \text{infl}_A - \text{infl}_B$.
- **International Fisher**: $R_{\text{nom},A} - R_{\text{nom},B} \approx E(\text{infl}_A) - E(\text{infl}_B)$.
- **Cobb-Douglas**: $Y = A\,K^{\alpha}L^{1-\alpha}$. **Growth accounting**: $\%\Delta Y = \%\Delta A + \alpha\,\%\Delta K + (1-\alpha)\,\%\Delta L$.
- **Labor-productivity growth**: potential GDP growth = labor-force growth + labor-productivity growth.
- **Solow steady state**: per-capita $g^* = \dfrac{\theta}{1-\alpha}$; total $G^* = g^* + \Delta L$.

## 13 — Financial Statement Analysis → [[Intercorporate_Investments]] · [[Employee_Compensation]] · [[Multinational_Operations]]
- **Full goodwill** = (price ÷ %acq) − FV identifiable net assets; **Partial goodwill** = price − %acq×(FV net assets).
- **Funded status** = fair value of plan assets − PBO. **TPPC** = employer contributions − ΔFunded status.
- **Translation**: current-rate gain/loss → **CTA in equity** (exposure = net assets); temporal → **remeasurement G/L in NI** (exposure = net monetary assets).
- **Combined ratio** (P&C) = loss ratio + expense ratio; **< 100% = underwriting profit**.
- **LCR** = HQLA / 30-day net outflows; **NSFR** = available / required stable funding (≥100%).
- **Basel III capital minima** (% of risk-weighted assets): **CET1 4.5%**, **Tier 1 6%**, **total capital 8%**. P&C cycle: **low** combined ratio = **hard** market; **high** = **soft** market.

## 14 — Corporate Issuers → [[Cost_of_Capital]] · [[Dividends_and_Share_Repurchases]] · [[Corporate_Restructurings]]
- **Unlever (Hamada)**: $\beta_{\text{asset}} = \dfrac{\beta_{\text{equity}}}{1 + (1-t)(D/E)}$; **relever**: $\beta_{\text{equity}} = \beta_{\text{asset}}\,[1 + (1-t)(D/E)]$.
- **Country risk premium**: $\text{CRP} = \text{sovereign spread}\times\dfrac{\sigma_{\text{equity}}}{\sigma_{\text{bond}}}$; $r_e = R_f + \beta(\text{ERP} + \text{CRP})$.
- **Bond-yield-plus-risk-premium**: $r_e = \text{YTM}_{\text{debt}} + 3\text{–}5\%$.
- **Double-taxation effective rate**: $t_{\text{corp}} + (1 - t_{\text{corp}})\,t_{\text{div}}$.
- **Buyback EPS test**: accretive if **E/P (earnings yield) > after-tax cost of funds**.
- **Takeover premium**: $\dfrac{\text{DP} - \text{UP}}{\text{UP}}$, UP = unaffected (pre-announcement) price.

## 15 — Equity Investments → [[Dividend_Discount_Models]] · [[Free_Cash_Flow_Valuation]] · [[Residual_Income]] · [[Market_Based_Valuation]] · [[Private_Company_Valuation]]
- **Gordon**: $V_0 = \dfrac{D_1}{r - g}$. **PVGO**: $V_0 = \dfrac{E_1}{r} + \text{PVGO}$.
- **H-model**: $V_0 = \dfrac{D_0(1+g_L) + D_0\,H\,(g_S - g_L)}{r - g_L}$, **H = ½ the high-growth period**.
- **Sustainable growth**: $g = b\times\text{ROE}$ (b = retention).
- **FCFF** $= \text{NI} + \text{NCC} + \text{Int}(1-t) - \text{FCInv} - \text{WCInv} = \text{CFO} + \text{Int}(1-t) - \text{FCInv}$. **FCFE** $= \text{FCFF} - \text{Int}(1-t) + \text{net borrowing}$. (FCFF→WACC; FCFE→r.)
- **Residual income**: $\text{RI} = (\text{ROE} - r)\,B_{t-1}$; $V_0 = B_0 + \sum\text{PV(RI)}$. **EVA** $= \text{NOPAT} - \text{WACC}\times\text{capital}$.
- **Justified P/E (leading)**: $\dfrac{\text{payout}}{r - g}$; **trailing**: $\dfrac{\text{payout}(1+g)}{r - g}$. **Justified P/B**: $\dfrac{\text{ROE} - g}{r - g}$.
- **EV** = market cap + debt + preferred + minority − cash. Average P/Es with the **harmonic mean**.
- **Method of average ROE** (preferred for normalizing cyclical EPS): normalized EPS $=$ average ROE $	imes$ current BVPS.
- **Total private-co discount**: $1 - (1 - \text{DLOC})(1 - \text{DLOM})$; **DLOC** $= 1 - \dfrac{1}{1 + \text{control premium}}$.

## 16 — Fixed Income → [[Term_Structure]] · [[Arbitrage_Free_Valuation]] · [[Bonds_With_Embedded_Options]] · [[Credit_Analysis_Models]] · [[Credit_Default_Swaps]]
- **Forward rate model**: $(1 + S_T)^T = (1 + S_{T-1})^{T-1}(1 + f_{T-1,1})$.
- **Swap spread** = swap rate − Treasury; **Z-spread** over spot curve; **I-spread** over swap curve.
- **Callable** = straight − call; **Putable** = straight + put. Higher vol → lower callable, higher putable, **lower OAS**.
- **Effective duration**: $\dfrac{V_- - V_+}{2\,V_0\,\Delta y}$; **effective convexity**: $\dfrac{V_- + V_+ - 2V_0}{V_0\,\Delta y^2}$.
- **CVA** $= \sum\text{PV(expected loss)}$; expected loss = POD×LGD; **risky value = risk-free value − CVA**. **LGD** = exposure×(1 − recovery).
- **CDS upfront%** $\approx (\text{spread} - \text{coupon})\times\text{duration}$; **ΔValue** $\approx \Delta\text{spread}\times\text{duration}\times\text{notional}$; **payout** = notional×(1 − recovery).

## 17 — Derivatives → [[Forward_Commitments]] · [[Options_Valuation]]
- **Forward price**: $F_0 = [S_0 - \text{PV(income)} + \text{PV(costs)}](1+r)^T$. **Value during life**: $\text{PV}(F_t - F_0)$.
- **Par swap rate**: $s = \dfrac{1 - \text{DF}_n}{\sum \text{DF}}$.
- **Binomial risk-neutral up-prob**: $\pi_U = \dfrac{1 + r - d}{u - d}$; option $= \dfrac{\pi_U\,c_{\text{up}} + \pi_D\,c_{\text{down}}}{1+r}$.
- **Hedge ratio (delta)**: $\dfrac{c_{\text{up}} - c_{\text{down}}}{S_{\text{up}} - S_{\text{down}}}$.
- **BSM call** $= S\,N(d_1) - Xe^{-rT}N(d_2)$; **put** $= Xe^{-rT}N(-d_2) - S\,N(-d_1)$. N(d1) = delta; N(d2) ≈ prob ITM.
- **Greeks**: gamma highest **ATM near expiry**; Black model values options on **futures** (and swaptions).

## 18 — Alternative Investments → [[Commodities]] · [[Real_Estate]] · [[Hedge_Fund_Strategies]]
- **Commodity total return** = spot return + **roll return** + collateral return. Backwardation → +roll; contango → −roll.
- **Direct cap (RE)**: $\text{Value} = \dfrac{\text{NOI}_{\text{year 1}}}{\text{cap rate}}$; **cap rate** $= r - g = \text{NOI}/\text{value}$.
- **FFO** = NI + depreciation + deferred tax − gains on sales. **AFFO** = FFO − maintenance capex − straight-line rent.
- **Loan sizing**: min of LTV constraint (value×max LTV) and DSCR constraint (NOI/DSCR → debt service → loan).
- Skew: merger arb = **negative** (sell-insurance); global macro/managed futures = **positive** (crisis alpha).

## 19 — Portfolio Management → [[Active_Portfolio_Management]] · [[Multifactor_Models]] · [[Measuring_Managing_Market_Risk]]
- **APT**: $E(R_p) = R_f + \sum \beta_j \lambda_j$.
- **Information ratio** = active return / active risk (tracking error). **Sharpe** uses total risk.
- **Market timer's IC** $= 2(\%	ext{ correct}) - 1$ (50% correct $\Rightarrow$ IC $=0$).
- **Fundamental law**: $\text{IR} = \text{IC}\sqrt{\text{BR}}\;\text{TC}$; $E(R_A) = \text{IC}\sqrt{\text{BR}}\;\text{TC}\,\sigma_A$; optimal $\sigma_A^* = \dfrac{\text{IR}}{\text{SR}_B}\,\sigma_B$; $\text{SR}_P^2 = \text{SR}_B^2 + \text{IR}^2$.
- **Active risk²** = active factor risk² + active specific risk².
- **ETF premium/discount** $= \dfrac{	ext{ETF price} - 	ext{NAV}}{	ext{NAV}}$; **tracking error** = annualized SD of the **daily tracking differences**.
- **VaR** = minimum loss at a confidence level over a period (use **CVaR/expected shortfall** for tail size).
- **Taylor rule**: `policy rate = neutral + inflation + 0.5(inflation gap) + 0.5(output gap)`.
- **Breakeven inflation** = nominal yield − real (TIPS) yield.
- **Total cost of ETF ownership** = expense ratio + spreads + premium/discount + tracking error.

## 20 — Ethics & GIPS → [[Code_and_Standards]] · [[GIPS]]
- No core formulas. Decision rules: follow the **stricter** of law vs Code & Standards; **mosaic theory** allowed; **priority of transactions** = clients > employer > self.
- **GIPS**: firm-wide, all-or-nothing; composite = **all** discretionary fee-paying portfolios of a strategy; min **5 years** of compliant history (build to 10); verification recommended, not required.

---

## How to use this sheet
- This is a **recall** tool, not a substitute for the detail notes — every line links to a note with the derivation, a worked example, and the exam traps. Drill the formula here, then click through if it doesn't click. For computational topics, the worked examples in the linked notes show the plug-and-chug.
