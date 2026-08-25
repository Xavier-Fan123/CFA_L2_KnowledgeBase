---
aliases: [Exam Traps Index, Trap Index]
tags: [CFA-L2, atlas, exam-traps]
date: 2026-06-05
status: evergreen
source: Generated from note Exam Traps sections by scripts/generate_atlas.py
---

# Exam Traps Index

Cross-topic collection of `## Exam Traps` bullets. Use it for final-pass review and to identify repeated confusion patterns.


## 11 Quantitative Methods

### Big Data Projects -> [[Big_Data_Projects]]
- **Normalization → [0,1]** (outlier-sensitive); **standardization → mean 0, SD 1** (assumes normality, not outlier-sensitive). Don't swap them.
- **Recall** ↔ Type II/FN cost; **Precision** ↔ Type I/FP cost. F1 = **harmonic** mean (not arithmetic).
- **AUC = 0.5 means random**; higher (toward 1) is better.
- **Parameters are learned; hyperparameters are set by the researcher** and adjusted in tuning.
- **Stemming** is rules-based and crude; **lemmatization** is more advanced/resource-heavy.
- "Common values" are not a data-cleansing item; structured cleansing targets incomplete/invalid/inaccurate/inconsistent/non-uniform/duplicate.
- **Invalid vs. inaccurate**: invalid = outside the possible range; inaccurate = in-range but wrong. **Inconsistent vs. non-uniform**: inconsistent = values contradict each other; non-uniform = same value, different format/unit.

### Breusch-Pagan (BP) Test -> [[Breusch_Pagan_Test]]
- Dependent variable in the auxiliary regression is the **squared** residual, not the residual.
- Statistic is `n × R²`, χ² with **k** df, **one-tailed**.
- Don't confuse with **Breusch-Godfrey (BG)** = serial correlation (F-distribution), or **Durbin-Watson** = single-lag serial correlation. Side-by-side comparison: [[Statistical_Tests_Master_Table]].
- BP's auxiliary regression uses the **squared** residuals; BG's uses the **residuals themselves plus their lags**.

### Logistic Regression (Logit) -> [[Logistic_Regression]]
- Nested test is the **LR test (χ²)**, not an F-test. All L2 tests side by side: [[Statistical_Tests_Master_Table]].
- Slope = change in **log odds**, not probability.
- pseudo-R² compares only models with the **same** dependent variable.

### Machine Learning -> [[Machine_Learning]]
- **Hyperparameters are set by the researcher**; they are not learned from the data (λ in LASSO, k in KNN/k-means, NN node counts).
- **Bias error = in-sample/underfit (too simple); variance error = out-of-sample/overfit (too complex).** Linear → high bias; nonlinear → high variance.
- **# features = total independent variables** (12 fundamental + 2 technical = 14, not 70).
- **Black-box** algorithms: PCA, random forest, neural nets/DLN. **CART is the transparent/visual one.**
- Unlabeled data / "group these into k dissimilar sets" → **unsupervised (clustering)**, not CART/regression.
- **Fix overfitting** with complexity reduction + cross validation — a *smaller* sample does NOT fix it.

### Model Misspecification -> [[Model_Misspecification]]
- EOC question: "The least likely result of misspecification is ___" → answer is **"unbiased coefficients"** — because misspecification typically produces **biased** coefficients, or residuals with serial correlation / heteroskedasticity (unreliable standard errors).
- Heteroskedasticity / serial correlation are often **symptoms** of misspecification; the root cause is an omitted variable or wrong functional form. Prefer fixing the specification over only applying robust standard errors.

### Multiple Regression (Basics, Model Fit, Dummies, Influence) -> [[Multiple_Regression]]
- The nested/overall **F-test is one-tailed** even though H₀ contains "=".
- **R² always rises** with more variables; judge added variables by **adjusted R², AIC, or BIC**, not R².
- **BIC penalizes complexity more than AIC**; AIC → forecasting, BIC → goodness of fit; lower is better for both, and only comparable across models with the **same dependent variable**.
- Predict Y using **all** coefficients, including insignificant ones.
- Use **(n − 1)** dummies for n categories; the dropped category is the reference.
- Slope coefficients are **partial** — they hold other X's constant and change as regressors are added.

### Regression Assumption Violations -> [[Regression_Assumption_Violations]]
- Conditional (not unconditional) heteroskedasticity is the dangerous one.
- BP test is **one-tailed**; White corrects it. DW vs BG: DW = one lag, BG = multiple lags; both detect serial correlation.
- **DW → 0 = positive SC, DW → 4 = negative SC** (`DW ≈ 2(1−r)`). Mnemonic: "positive = pals, no gap → 0."
- **DW is invalid when a lagged dependent variable is a regressor** (i.e. in any AR model) — use the t-test on residual autocorrelations, `t = ρ̂ / (1/√T)`. See [[Time_Series_Analysis]].
- Direction confusion: *positive* SC (DW near 0) → SEs **under**estimated → t-stats too big → **Type I** error. Opposite of multicollinearity, which causes Type II.
- Multicollinearity's tell: **high R² + significant F but insignificant t-stats**.
- All three corrections (White, Newey-West) change only the **standard errors**, never the coefficients.
- Multicollinearity does **not** bias coefficients — only inflates their SEs. **Omitted-variable bias (misspecification) is the one that biases coefficients.** Don't mix them up.
- Low pairwise correlations do **not** rule out multicollinearity: three or more variables can be jointly collinear with modest pairwise correlations. Correlation alone is diagnostic only in a two-variable regression — use VIF.

### Time Series Analysis -> [[Time_Series_Analysis]]
- **Durbin-Watson is invalid for AR models** (lagged dependent variable as regressor). Detect serial correlation of AR residuals with the **t-test on residual autocorrelations**, SE = **`1/√T`**, `t = ρ̂·√T`. Any significant residual autocorrelation ⇒ add lags / re-specify.
- **Two-period AR(1) forecast feeds the one-period FORECAST, not the actual value**: `x̂ₜ₊₂ = b₀ + b₁x̂ₜ₊₁` (a classic trap is to reuse `xₜ`). Multiperiod forecasts are more uncertain.
- DF test cannot test `b₁ = 1` directly; it tests the transformed `g = b₁ − 1 = 0` with a **modified** t.
- **"Cannot reject H₀" = has unit root = non-stationary** (do not reverse this).
- Random walk (with or without drift) is non-stationary; the fix is **first differencing**, not adding variables or changing proxies.
- Only a covariance-stationary series is guaranteed a **finite mean-reverting level**.
- **ARCH ≠ unit root**: ARCH concerns the error *variance*; a unit root concerns the series *level*.
- Test ARCH by regressing **squared residuals on lagged squared residuals**; significant `a₁` → ARCH → SEs wrong → use **GLS**. If ARCH exists you **can** forecast next-period variance.
- **Linear vs. log-linear**: constant *amount* of change → linear; constant *rate* (exponential) → log-linear. Serially correlated trend residuals (DW ≠ 2) → abandon the trend model for AR.
- A **seasonal lag** added to AR(1) keeps it an **AR(1) with a seasonal term, not AR(2)**. Detect seasonality via a significant residual autocorrelation at lag 4 (quarterly) / 12 (monthly).
- Two time series: regression is valid **only** if (a) neither has a unit root, or (b) both have unit roots **and are cointegrated** (DF-EG test). One-has-one-doesn't → invalid.
- Out-of-sample **RMSE** (lower = better) chooses between competing forecasting models.


## 12 Economics

### Currency Exchange Rates: Determination and Forecasting -> [[Currency_Exchange_Rates]]
- Mind the quote convention — a forward **premium on the base** means `F > S` in P/B terms.
- Carry trade ≠ free money: it works while UIRP fails, but carries crash risk (negative skew).
- Covered IRP is the only parity condition enforced by arbitrage; the rest are equilibrium tendencies.
- Expansionary monetary policy → currency **depreciates** (rate channel, high capital mobility).
- In a forward MTM problem, discount at the **price-currency** rate and use the new forward quote that offsets the old position.
- Do not use a no-arbitrage covered-IRP forward as proof that the forward is an unbiased forecast; no-arbitrage and forecasting are separate ideas.
- Currency crises are usually multi-signal cases: overvaluation plus weak reserves plus short-term FX debt is stronger evidence than any single symptom.

### Economic Growth -> [[Economic_Growth]]
- **Capital deepening cannot sustain growth** (diminishing returns); only **TFP / technological progress** sustains per-capita growth in the neoclassical model.
- Neoclassical: higher savings raises the **level** of output and **temporarily** its growth, but **not the long-run growth rate**. Endogenous theory: savings **can** raise the long-run rate.
- Convergence is **conditional/club**, not absolute, empirically.
- If the question gives output growth and input growth, TFP is the **residual** after subtracting weighted capital and labor contributions.
- In equity-market growth questions, sustainable GDP growth is only a long-run anchor; short-run returns also depend on `E/GDP` and `P/E` changes.
- Removing trade barriers can raise aggregate growth while hurting import-competing workers/firms; do not call every participant a winner.


## 13 Financial Statement Analysis

### Analysis of Financial Institutions -> [[Analysis_of_Financial_Institutions]]
- **CAMELS** order: Capital, Asset quality, Management, Earnings, Liquidity, Sensitivity.
- **Combined ratio < 100%** = underwriting profit; > 100% = underwriting loss (insurer relies on investment income).
- **Basel III minima: CET1 4.5%, Tier 1 6%, Total capital 8%** of risk-weighted assets; LCR and NSFR both ≥ **100%**.
- **Hard vs soft P&C market**: a **low** combined ratio marks a **hard** (profitable, high-rate) market; a **high** combined ratio marks a **soft** market. L&H carries **more interest-rate risk** than P&C because of its longer contracts and larger float.
- A growing share of **Level 3** (unobservable-input) assets is a bank earnings-quality red flag.
- LCR addresses **short-term (30-day)** liquidity; NSFR addresses **structural/long-term** funding.

### Employee Compensation: Post-Employment and Share-Based -> [[Employee_Compensation]]
- **Funded status = plan assets − PBO**; it is what appears (net) on the balance sheet.
- US GAAP pension **expense** uses **expected** return on assets; IFRS uses the discount rate (net interest) — a key comparability difference.
- Past service cost: **IFRS expenses immediately**; US GAAP defers through OCI.
- Remeasurements/actuarial gains-losses go to **OCI** (both standards); IFRS does **not** recycle them.

### Integration of Financial Statement Analysis Techniques -> [[Integration_of_FSA_Techniques]]
- Removing an associate: **earnings ↓, margin ↓, asset turnover ↑**, and **leverage unchanged** (don't arbitrarily adjust equity).
- **Common-size statements = processing OUTPUT**, not a data-collection input.
- **Accruals ratio: lower = better** quality. CFF is **not** in the accruals calc; **add back interest & taxes** to get CGO.
- CapEx%/Assets% **> 1 = growing** the segment; pair a **low margin + high ratio** = over-allocation.
- Associate **earnings → average FX**, associate **market value → ending FX**.

### Intercorporate Investments -> [[Intercorporate_Investments]]
- Equity-method dividends **reduce** the investment account (not income).
- Net income is the **same** under equity method and full consolidation; ratios differ because of the grossed-up base.
- **Partial goodwill** (IFRS) < full goodwill → lower total assets and lower NCI.
- FVOCI **debt** recycles to P&L on sale; FVOCI **equity** election does **not** recycle.
- **SPE/VIE**: control is by **power + variable economics, not votes** — IFRS consolidates on **substance/control**; US GAAP consolidates if you are the **primary beneficiary**. Off-balance-sheet securitization **understates leverage** until consolidation pulls the assets/debt back on.
- **Acquisition costs are expensed** (not added to goodwill); **contingent consideration** is included in the purchase price at **fair value**.

### Multinational Operations (Foreign Currency Translation) -> [[Multinational_Operations]]
- Translation gain/loss location: **current rate → equity (CTA)**; **temporal → income statement**.
- "Translation" = current rate method; "remeasurement" = temporal method.
- Under temporal with a net **monetary liability** position, a **weakening** local currency produces a **gain**.
- Current rate method keeps local-currency ratios intact; temporal does not.

### Evaluating Quality of Financial Reports -> [[Quality_of_Financial_Reports]]
- **Reporting quality ≠ earnings quality** — keep the two axes separate.
- **High accruals = low earnings quality + faster mean reversion**; the cash-flow component of earnings is more persistent than the accrual component.
- Beneish: a **higher** M-score signals a **higher** probability of manipulation.
- The **auditor's opinion is NOT a timely risk source** (it lags — covers historical statements). But a **change of auditor**, an **undersized auditor**, or **going-concern/control-weakness** language are genuine red flags. Best risk info: **notes + MD&A + event-driven disclosures**, not the audit report.


## 14 Corporate Issuers

### Capital Budgeting Foundations (L1 bridge) -> [[Capital_Budgeting_Foundations]]
- **NWC recovery is NOT taxed** (return of principal); **salvage IS taxed**, but only on the gain over book value `t(Sal − B)`.
- Omitting NWC recovery understates terminal CF — and the distortion is **largest for short projects** (less discounting).
- A capex change hits **twice**: t=0 outlay **and** the annual depreciation tax shield. Net after-tax cost ≈ `ΔFCInv × [1 − (t/N)·PVA]`.
- **Accelerated depreciation raises NPV** vs. straight-line despite an identical total nominal shield — front-loading raises its PV.
- Depreciation enters cash flow **only** through `tD` — it is non-cash.
- **Inflation hurts the depreciation shield but helps the fixed-rate borrower.** Same erosion, opposite impact.
- **Never discount real cash flows at a nominal rate** (or vice versa) — the classic error undervalues the project.
- `PMT/(r−g)` is the same geometric series as `PVA`, with ratio `(1+g)/(1+r)` — this is Gordon Growth.

### Corporate Restructurings -> [[Corporate_Restructurings]]
- **Materiality** rule of thumb: transaction is "large" if value > **10% of acquirer's pre-deal EV** (size + fit). Announcement-day price reaction is a **poor** predictor of long-run value.
- **Comparable-company** multiples have **no** control premium → **add** one (best for spin-offs); **comparable-transaction** multiples **embed** the premium.
- **Takeover premium** = (DP − SP)/SP, using the **pre-announcement (unaffected)** price as denominator (exclude rumor run-up; use ~1 week prior or VWAP). Historical median ≈ 30%.
- **EPS** stock-financed accretion/dilution hinges on **relative P/E** (acquirer P/E > target → accretive); cash/debt-financed → compare **target E/P vs after-tax cost of debt**. Accretion ≠ value creation.
- **Pro forma WACC** changes both **weights and costs** of capital; defend an **investment-grade** rating to avoid a several-hundred-bp WACC jump.
- **Spin-off** = pro-rata new shares via stock dividend, **no cash** to parent; **carve-out** = sell a stake via IPO for **cash**; **split-off** = holders swap parent shares for subsidiary shares.

### Cost of Capital: Advanced Topics -> [[Cost_of_Capital]]
- **Finance lease cost of debt = the rate implicit in the lease (RIIL)** — the IRR equating asset fair value (+ lessor's direct costs) to PV of lease payments + residual value. Use the **IBR** only when the RIIL is not determinable.
- **2026 errata - private-company premiums**: add SP/IP/SCRP/CRP only when the risk is not already captured by beta, ERP, or country assumptions. Peer beta can make a separate IP double-count industry risk.
- **Unlever then relever** beta when the comparable's leverage differs from the subject's (Hamada).
- **Expanded CAPM** = R_f + β·ERP + **SP + SCRP** (uses peer beta); **Build-up** = R_f + ERP + **SP + IP + SCRP** (NO beta — implicit β=1). Don't double-count beta in build-up. Illiquidity → marketability **discount on value**, not a premium in r_e.
- **Grinold-Kroner**: a rise in expected **inflation does NOT change ERP** (i added, R_f subtracted, cancel). Earnings growth term = i + g − ΔS; %ΔP/E is the repricing term.
- **DDM ERP** assumes a **constant P/E**; if P/E will change, add a repricing adjustment.
- Country risk premium (Damodaran) scales the sovereign spread by **equity-to-bond volatility ratio**.
- **Fama-French**: SMB = size, HML = value, RMW = profitability, CMA = investment. The market beta differs from the single-factor CAPM beta once extra factors are added.
- Use **project** risk, not company-average risk, for a project's discount rate.
- Cost of debt for an EM issuer: add a **country risk premium** from a country **risk rating (CRR)**, and match the **currency** of the cash flows.

### Analysis of Dividends and Share Repurchases -> [[Dividends_and_Share_Repurchases]]
- Buyback EPS test: compare **E/P (earnings yield)** to the **after-tax cost** of the funds — above → accretive, below → dilutive.
- BVPS rises only if shares are repurchased **below** book value per share.
- Dividend **cuts** carry the strongest negative signal; cash dividends raise D/E and cut liquidity.
- **13.e list of six** — investment opportunities, earnings volatility, financial flexibility, taxes, **flotation costs**, contractual/legal restrictions. Flotation costs push payout **down**, not up.
- **Dutch auction**: bids filled **lowest-first**, but everyone accepted is paid the **single highest accepted price** — not their own bid.
- **Agency runs two ways**: higher payout fixes the shareholder-manager conflict but **worsens** the shareholder-bondholder conflict; the latter is controlled by **indenture covenants**.
- Global trend: **fewer** dividend payers, **more** repurchases (US since the 1980s; UK/Europe since the 1990s).

### ESG and Corporate Governance -> [[ESG_and_Corporate_Governance]]
- Dispersed ownership → **principal-agent**; concentrated ownership → **principal-principal** (minority expropriation) conflict.
- Dual-class structures separate **control rights from cash-flow rights** — a governance red flag.
- ESG analysis should center on **financially material** factors, not all ESG issues.
- ESG **integration ≠ screening**: integration folds ESG into the valuation/forecast; screening just includes/excludes names. Equity use → opportunities + downside; FI use → **credit spread**.
- **Horizontal** ownership = mutual cross-holdings; **vertical/pyramid** = controlling stakes through tiers of holding companies. **CEO duality** (CEO = chair) raises governance risk.
- **Interlocking directorates are NOT prohibited** — there is no rule to "violate." What fails is the **independence test** (significant remuneration / ownership / employment relationship) or the **comply-or-explain disclosure** obligation.
- Counterintuitive point the exam likes: family control / interlocking directorates can **reduce** the principal-agent conflict while creating a **principal-principal** one. Don't assume every governance concentration is purely negative.
- **Board independence standard: a MAJORITY should be independent** — and the **audit, compensation, and nomination** committees specifically must be "sufficiently independent."
- **Long tenure (>10 years) cuts both ways**: deep firm knowledge vs. resistance to change and becoming "too friendly with management, affecting independence."


## 15 Equity Investments

### Dividend Discount Models (DDM) -> [[Dividend_Discount_Models]]
- Justified **leading** P/E = `payout/(r−g)`; **trailing** = `payout(1+g)/(r−g)` — don't mix.
- H-model **H = HALF** the high-growth (transition) period length.
- Gordon value explodes as `g → r`; small input changes move value a lot.
- `g = b × ROE` uses the **retention** ratio, not payout — and the SGR assumes a **constant D/E ratio and no new equity issuance**, on **beginning-of-period** balance-sheet values.
- Terminal value in any DDM comes from **either the Gordon model or a market multiple** (e.g., terminal P/E × terminal EPS) — 18.m expects both.
- Know the **18.l list**: multistage models are flexible, invertible (solve for r or g), explicit, and spreadsheet-friendly; but assumption-driven, sensitivity-prone, and error-prone.

### Equity Valuation: Applications and Processes -> [[Equity_Valuation_Process]]
- Analyst edge = **perceived** mispricing, which includes estimation error in intrinsic value.
- **Sum-of-the-parts** can reveal a **conglomerate discount**.
- Choose the model that fits the firm: non-payer with negative FCF but clean accounting → residual income.
- **Fair market value** = hypothetical willing buyer/seller; **investment value** = value to a **specific** buyer **including synergies** (the strategic-buyer measure). Don't use the two interchangeably.
- Porter's five: new entrants, substitutes, **buyer** power, **supplier** power, rivalry — buyers and suppliers are two separate forces.

### Free Cash Flow Valuation (FCFF / FCFE) -> [[Free_Cash_Flow_Valuation]]
- **FCFF discounted at WACC; FCFE discounted at cost of equity.**
- Add **after-tax interest** to get FCFF (not pre-tax).
- **Leverage changes affect FCFE, not FCFF.** Dividends/buybacks affect **neither**.
- WCInv excludes cash and short-term debt; an **increase** in working capital **reduces** free cash flow.
- **Add non-operating assets** (excess cash, investment land, financial holdings at market value) to the FCFF/FCFE-derived value — the DCF only captures operating assets.

### Market-Based (Relative) Valuation -> [[Market_Based_Valuation]]
- **EV subtracts cash** and adds debt/preferred/minority — a common error.
- **EV/EBITDA's two drawbacks**: EBITDA **overstates CFO when working capital grows**, and **FCFF ties to theory better** than EBITDA. Advantages ≠ the whole answer.
- Normalizing cyclical EPS: the **method of average ROE is preferred** over the method of historical average EPS.
- **P/B is the multiple for firms holding liquid assets** (banks/insurers) and for firms **expected to be wound up**; its weakness is **intangibles**, size effects, accounting conventions, and inflation.
- **EV/EBITDA** is preferred when capital structures differ (P/E is distorted by leverage).
- Use the **harmonic mean** to average P/Es across firms, not the arithmetic mean; the arithmetic mean is biased **upward** by outliers.
- Justified P/B = `(ROE − g)/(r − g)`; P/B > 1 when ROE > r.
- **P/CF**: always pin down the cash-flow definition (CF vs CFO vs FCFE vs EBITDA). The simple **CF** (EPS + noncash charges) **ignores WCInv and non-cash revenue**. EBITDA pairs with **EV**, not price.
- **Justified dividend yield = (r − g)/(1 + g)** — it is the **inverse** orientation of P/E-type multiples, so *higher* yield = *cheaper*. Trailing yield uses the **dividend rate** (annualized latest dividend).

### Private Company Valuation -> [[Private_Company_Valuation]]
- **Total discount is multiplicative**: `1 − (1 − DLOC)(1 − DLOM)`, not the simple sum.
- A **minority** interest gets **DLOC**; a **controlling** interest typically does not.
- **Build-up / expanded CAPM** add size and company-specific premiums for private/small firms.
- **Use the TARGET's WACC, not the acquirer's**, when discounting the target's cash flows; and check that a size premium taken from small-cap public data isn't double-counting **distress**.
- Use **FCFF** rather than FCFE whenever the **capital structure is expected to change**.
- **DLOM** has three curriculum estimation routes: **restricted vs public shares**, **pre-IPO vs post-IPO**, and **put prices**.
- Market approach has **three** methods — GPCM, GTM, and **PTM** (the subject company's own prior stock sales). GTM multiples already embed a control premium; **GPCM multiples do not**.
- CCM uses a **single** capitalization rate (r − g) on normalized cash flow.
- **EEM** charges tangible assets (WC, fixed) their required returns first; the leftover (**excess earnings**) is the intangibles' RI, capitalized at `RI(1+g)/(r_RI − g)`. Firm value adds back **FMV of tangible assets**. Don't forget the tangible-asset value — EEM alone prices only the intangibles.

### Residual Income (RI) Valuation -> [[Residual_Income]]
- `RI = (ROE − r) × beginning book value`; the charge uses **beginning-of-period** equity.
- **Justified P/B = (ROE − g)/(r − g)** — same as the relative-value result.
- RI puts most value in **current book value**, reducing terminal-value dependence (vs DDM/FCF).
- **Clean surplus** must hold; OCI items (FX, FVOCI, pension remeasurements) violate it.
- **Persistence factor** sits in the terminal term as `RI_T/(1 + r − ω)`, NOT `/(r − g)`. ω = 1 → perpetuity of RI; ω = 0 → terminal value zero. Don't confuse ω-decay with the ROE-fades-to-r variant (terminal = 0).
- **Tobin's q** uses **replacement cost of total assets** and **total capital** — not equity book value.


## 16 Fixed Income

### Arbitrage-Free Valuation Framework -> [[Arbitrage_Free_Valuation]]
- Binomial tree = **lognormal** (non-negative rates, higher vol at higher rates); spacing factor `e^(2σ)`.
- Backward induction uses **risk-neutral 0.5/0.5** probabilities, discounting node-by-node.
- **Monte Carlo** is for **path-dependent** instruments (MBS); a binomial tree is **not** path-dependent.
- CIR volatility depends on √r; Vasicek volatility is constant (can go negative).
- **Four models, two families**: *equilibrium* = **CIR** (√r volatility, non-negative rates) and **Vasicek** (constant volatility, rates can go negative); *arbitrage-free* = **Ho-Lee** (normal, rates can go negative) and **KWF** (lognormal in ln r, so rates stay positive). "Time-dependent drift θ_t fitted to market prices" = arbitrage-free family.
- Arbitrage requires violating **value additivity OR dominance** — know both names.

### Valuation and Analysis of Bonds with Embedded Options -> [[Bonds_With_Embedded_Options]]
- Higher vol → **lower** callable, **higher** putable, and **lower OAS**.
- Apply **min(value, call price)** for calls, **max(value, put price)** for puts at each node.
- Callable convexity can be **negative**; OAS removes the option to allow apples-to-apples comparison.
- Convertible minimum value = **max(conversion value, straight value)**.
- **Busted convertible** = share price **well below** conversion price → trades like a **bond** (driven by rates/credit, not the share). Deep ITM → trades like the **stock**; near the conversion price → hybrid.
- Callable: one-sided **up**-duration > down-duration; putable: **down** > up. Higher vol still → callable down / putable up / **OAS down**.

### Credit Analysis Models -> [[Credit_Analysis_Models]]
- **CVA = PV of expected loss**; **fair value = VND − CVA** (VND = value assuming no default).
- **Rate volatility does not change a default-free bond's VND** — it changes fair value only via an embedded option or via CVA (credit risk).
- A **decrease in POD** lowers CVA **more** than an equal decrease in the **recovery rate**.
- Risky **floater**: solve for the **discount margin (DM)** (not a credit spread); DM > quoted margin when priced below par.
- **Structural** model: equity is a **call** on assets, risky debt = risk-free − **put** on assets.
- **Reduced-form** models POD/hazard rate from observable variables (no capital-structure assumption); it is backward-looking in estimation.
- Distressed issuers can show an **inverted** credit-spread term structure.

### Credit Default Swaps (CDS) -> [[Credit_Default_Swaps]]
- **Curve-steepening trade** = buy **long**-maturity protection, sell **short**-maturity (the near-term view is the better one); a **flattening** trade is the reverse. A **naked** CDS means no underlying exposure at all.
- **Synthetic CDO cheaper than cash CDO → buy synthetic, sell cash.** The synthetic gets its exposure by **selling protection**, not by owning bonds.
- **Payout = notional × (1 − recovery)** = notional × LGD.
- One-period **fair spread ≈ (1 − RR) × POD**; don't confuse the **CDS coupon** (standardized 1% IG / 5% HY) with the **CDS spread** (the risk-justified rate).
- Upfront ≈ **(spread − coupon) × duration**; buyer pays when spread > coupon (price < 100). A **negative** upfront means the **seller** pays and **price > 100** (e.g. −2% → price 102).
- Protection **buyer profits when spreads widen** (credit worsens).
- Index CDS for macro credit views; single-name for issuer-specific; basis trades exploit CDS vs cash bond.

### Term Structure and Interest Rate Dynamics -> [[Term_Structure]]
- If realized spot rates equal today's **forwards**, you earn only the **risk-free** return — active bets require deviating from forwards.
- **Riding the yield curve** works on an **upward-sloping, stable** curve.
- Swap spread = swap rate − Treasury (can be **negative** post-2008); TED & **MRR−OIS** (formerly Libor−OIS) widen with credit/liquidity stress. Z-spread = over **spot** curve; I-spread = over **swap** curve.
- Liquidity-preference theory adds a **positive term premium** → upward bias in forwards.
- **Bull/bear + steepen/flatten:** "bull" = rates **down**; bear = rates **up**. Expansion + rate hikes → **bear flattening**; recession + cuts → **bull steepening**; flight to quality → **bull flattening**.
- Sum of **key rate durations = effective duration** (a parallel shift moves all key rates equally).
- Steepener trade = **short long / buy short**; flattener = **buy long / short short** (often duration-neutral). Bullet→barbell positions for an expected **bullish flattening**.


## 17 Derivatives

### Pricing and Valuation of Forward Commitments -> [[Forward_Commitments]]
- `F0 = FV(S0 + CC0 − CB0)`: carry **benefits (income) reduce** F0; carry **costs increase** it.
- Forward value during life = **PV of (Ft − F0)** = `St − PV[F0]`; **zero at initiation**.
- **FRA0 = the implied forward rate**; FRA is *advanced set, advanced settled* (payoff discounted one period); swaps/IR options are *settled in arrears*. FRA value at g = PV of `(FRAg − FRA0)`.
- Par swap rate = `(1 − PV_n)/(Σ PV_i) × (1/AP)`; the **final PV factor appears twice** (denominator with coupons, numerator on par). With AP = 1 it is `(1 − DF_n)/ΣDF`.
- **Swap value = VFIX − VFLT** to the receive-fixed party; equals `Σ PV × (rFIX,0 − rFIX,t) × NA` — **positive to the fixed receiver when rates fall**.
- **Equity-swap fixed rate = the comparable interest-rate-swap fixed rate** (do not re-derive separately).
- **Currency swap**: two bonds in two currencies; price each leg with its own curve; convert the foreign leg at the **current spot FX rate**.
- Futures ≠ forwards because of **daily MTM** (convexity / correlation effect); futures value resets to 0.

### Valuation of Contingent Claims (Options) -> [[Options_Valuation]]
- Risk-neutral up-probability `π = (1 + r − d)/(u − d)` (curriculum: `[FV(1) − d]/(u − d)`); value = **PV of risk-neutral expected payoff** `c = PV[π·c+ + (1−π)·c−]`. For **American** options, check early exercise (max(exercise, hold)) at each node.
- BSM call = `S·N(d1) − Xe^(−rT)·N(d2)`; **`d1 = [ln(S/X) + (r + σ²/2)T]/(σ√T)`, `d2 = d1 − σ√T`**. `N(d1)` = delta, `N(d2)` ≈ risk-neutral prob of finishing ITM. Use `N(−x) = 1 − N(x)`.
- **Carry-adjusted BSM** multiplies the stock term by `e^(−γT)` and d1 uses `(r − γ + σ²/2)`; higher carry → **lower call, higher put**. Currency options: γ = **foreign** rate, discount at **domestic** rate.
- **Black model** is for options on **futures/forwards** (d1 has no rate/carry term — it's in F0); also used for **interest-rate options** and **swaptions**. **Payer swaption ≈ call on rates**, receiver ≈ put.
- Swaption discounting uses the **annuity factor PVA**, not a single discount factor; rates in decimals.
- **Delta**: call `e^(−γT)N(d1)` (0→1), put `−e^(−γT)N(−d1)` (−1→0). **Hedge units `NH = −Port.delta/Δ_H`**.
- **Gamma of a call = gamma of a put**; gamma **highest ATM near expiry**; gamma is the risk left after delta-neutralizing; delta-plus-gamma approximation beats delta alone.
- **Rho**: call **positive**, put **negative**. **Theta** usually negative (decay accelerates near expiry).
- **Implied volatility** is forward-looking (vs historical = backward-looking); a non-flat **vol surface** signals BSM-assumption breakdown.


## 18 Alternative Investments

### Commodities and Commodity Derivatives -> [[Commodities]]
- **Backwardation → positive roll return; contango → negative roll return.** In backwardation you buy **more** (cheaper) deferred contracts to keep dollar exposure; in contango you buy **fewer**.
- Commodities have **no cash flows** → no DCF; convenience yield is central.
- Keynes's **normal backwardation**: speculators earn a risk premium for bearing producers' price risk.
- Total return = spot + **roll** + collateral; roll return = (near − far)/near × % rolled (an **accounting** figure — cannot be isolated into a tradable portfolio).
- Index returns hinge on **weighting + roll + rebalancing**: floating/production weights → small rebalancing trades; **frequent rebalancing helps mean-reverting, hurts trending** markets.

### Hedge Fund Strategies -> [[Hedge_Fund_Strategies]]
- **Merger arbitrage** payoff is **negatively skewed** = **long riskless bond (spread) + short binary put** (pays out if deal breaks); **global macro / managed futures** are often **positively skewed** (crisis alpha, long volatility/trend).
- **Equity market neutral** ≈ low beta/low correlation; long/short equity keeps net (usually net-long) market exposure.
- The **conditional** factor model uses a **crisis dummy** to expose **state-dependent** tail betas hidden in reported "alpha"; residual return = alpha + omitted factors + random error.
- **Fund of funds** adds **diversification but a second layer of fees plus NETTING RISK** (incentive fees paid to winning sub-managers while losers drag the net return); **multi-strategy** nets internally (one fee layer, no netting risk) and reallocates faster, but concentrates operational risk.
- **Specialist = volatility trading + life settlements** in the 2026 reading. Volatility traders trade the **term structure of volatility** (OTC option spreads, VIX futures, volatility/variance swaps); life-settlement managers want **low surrender value, low premiums, short life expectancy**.
- **Dedicated short = 60%–120% short**; **short-biased = 30%–60% net short**. Convertible arb runs roughly **300% long / 200% short**.
- 20% hedge funds added to 60/40: **σ down, Sharpe up, Sortino up, max drawdown down**.

### Investments in Real Estate Through Publicly Traded Securities -> [[Publicly_Traded_Real_Estate]]
- **AFFO subtracts** non-cash rent and maintenance capex/leasing costs from FFO (it does NOT add them). FFO **adds back depreciation** and **excludes property-sale gains**.
- Use **cash NOI** (strip straight-line/non-cash rent) and **forecast** NOI (acquisitions + growth) before applying the **cap rate**; exclude goodwill / deferred items from NAV assets.
- **CREF (commingled real estate fund) is a PRIVATE vehicle**, not a publicly traded security.
- REITs offer relatively **low growth from reinvested operating cash flow** (because of the high payout requirement) — and **higher equity correlation** → weaker portfolio diversification than direct RE.
- **NAVPS uses market values** and is superior to BVPS; it is not "exactly" intrinsic value.

### Overview of Types of Real Estate Investment (Private / Direct) -> [[Real_Estate]]
- **Direct cap: value = year-1 NOI / cap rate**, and **cap rate = r − g**. Higher r ↓ value; higher g ↓ cap rate ↑ value. **Terminal value uses NOI_n(1+g)/(r−g)** (next-period NOI), not current NOI.
- **Cap rate ≠ discount rate.** `r` = required return (risk-free + risk premium); cap rate = `r − g` and is **lower than r** whenever g > 0. Equal only if g = 0. Invert to read market growth: `g = r − cap rate`.
- **Cap rate and value always move in opposite directions** — "cap rate compression" = falling cap rates = rising prices.
- **Stabilized NOI has a second step**: capitalize the normalized NOI, **then subtract** the value lost to the temporary decline. Skipping step ② overstates value.
- A cap rate can be **backed out of a comparable sale** (`NOI_comp / price_comp`) and applied to the subject — a common quiz format.
- **NOI is before financing and taxes**; **expense recoveries are capped** at the contractual amount — cost overruns above the cap hit NOI fully.
- Over the cycle's **Expansion**, the favorable triad is **NOI↑, DSC↑, LTV↓**. New **supply lags**, so oversupply often appears right as demand softens.
- **DSC uses NOI / total debt service** (interest **+ principal**); **equity dividend rate** = (NOI − debt service) / equity, ignores taxes and capital gains.
- **Cost approach** = floor/replacement value; **land is not depreciated**. In **oversupply**, replacement cost > market price.
- **Appraisal-based indexes understate volatility and lower correlation** (smoothing) → they **overstate** the optimal RE allocation. **Transaction-based** (repeat-sales / hedonic) are truer but noisier.


## 19 Portfolio Management

### Analysis of Active Portfolio Management -> [[Active_Portfolio_Management]]
- **IR = active return / active risk** (tracking error); **Sharpe uses total risk**.
- IR is invariant to aggressiveness (unconstrained); `SR_P² = SR_B² + IR²`.
- Fundamental law: `IR = IC × √BR × TC`; breadth must be **independent** decisions.
- Market timing = low breadth; broad security selection = high breadth.
- **Market timer's IC = 2(% correct) − 1.** 50% right means **zero** skill, not 0.5.
- **Sector rotation** is evaluated by the same fundamental law, with each sector bet counted as one (highly correlated) decision.

### Backtesting and Simulation -> [[Backtesting_and_Simulation]]
- **Survivorship + look-ahead + data snooping** are the three classic backtest biases.
- **Historical simulation** uses actual past data (one path); **Monte Carlo** draws from assumed distributions (flexible but model-dependent).
- Rolling-window backtests approximate real point-in-time rebalancing.
- **Tail dependence** (assets crashing together) is a main reason to move beyond normal assumptions; **bootstrapping** = resampling **with replacement**, useful when simulations needed far exceed the sample size.
- **Sensitivity analysis** re-runs the Monte Carlo under a **multivariate skewed Student t** to capture skew and fat tails — at the cost of **more parameters and more estimation error**.
- **Cross-validation** (fit on training data, assess on separate test data — including data from **other geographic markets**) is the antidote to **data snooping**.

### Economics and Investment Markets -> [[Economics_and_Investment_Markets]]
- A factor affects markets only via **rates, cash flows, or the risk premium**; only **surprises** move prices.
- **Credit spreads widen in recessions, tighten in expansions**; yield curve flattens/inverts late cycle.
- **Breakeven inflation = nominal − real yield**.
- Equity risk premium exists because stocks are a **poor consumption hedge** (pay off badly in bad times) — formally, the **negative covariance between the payoff and the inter-temporal rate of substitution** is the risk premium.
- **Higher expected GDP growth → lower inter-temporal rate of substitution → less saving → HIGHER real rates.** The chain runs through diminishing marginal utility; getting the direction backwards is the classic error.
- A **single-period risk-free bond has zero covariance → zero risk premium**; the premium appears only once the terminal value is uncertain.

### Exchange-Traded Funds (ETFs) -> [[Exchange_Traded_Funds]]
- The **AP in-kind creation/redemption arbitrage** keeps price ≈ NAV and drives tax efficiency.
- **ETNs carry issuer counterparty (credit) risk** (unsecured debt), unlike physically-backed ETFs.
- Premiums/discounts often reflect **stale NAV** (closed underlying markets), not mispricing.
- Total cost of ownership ≠ just the expense ratio — include spreads, premium/discount, tracking error. **Short-term traders optimize spreads; long-term holders optimize the management fee.**
- **Tracking DIFFERENCE is a level; tracking ERROR is the annualized SD of daily tracking differences.** A steady fee drag gives a big difference with a small error.
- The three named ETF risks are **counterparty, fund closure, and expectation-related** risk — the third one covers daily-reset leveraged/inverse products.
- Portfolio uses come in **three** curriculum buckets: **efficient portfolio management**, **asset class exposure management**, **active investing**.

### Measuring and Managing Market Risk -> [[Measuring_Managing_Market_Risk]]
- VaR is a **minimum** loss at a confidence level, not the maximum; it ignores **how bad** the tail is — use **CVaR/expected shortfall** for that.
- **Parametric VaR is poor for option-heavy portfolios** (non-normal); historical/Monte Carlo handle them.
- Sensitivity measures give **exposure**, not loss probability; scenario analysis covers tail/multi-factor stress.
- **Reverse stress test = start from failure and work back to the scenarios that cause it** — the opposite direction from an ordinary stress test.
- z-thresholds: **5% → 1.65σ, 1% → 2.33σ, 16% → 1σ**. Higher confidence (1% vs 5%) → larger z → larger VaR.
- **Never annualize a daily VaR** by ×250 or ×√250. Re-annualize mean (×250) and σ (×√250) *first*, then compute VaR. The √250 shortcut is valid only under a zero-expected-return assumption.
- Parametric needs only mean + σ (+ correlations); it does **not** require a data history (historical sim does).

### Multifactor Models -> [[Multifactor_Models]]
- **Factor portfolio** = sensitivity **1 to one factor, 0 to all others** (a pure factor bet). **Tracking portfolio** = a chosen set of sensitivities that **replicates a benchmark**. Do not swap them.
- APT needs **no market portfolio** and no normality — only a factor structure, diversification, no arbitrage (contrast with CAPM, a single-factor special case).
- **Macroeconomic** models use factor **surprises**; **fundamental** models use **standardized attributes** as the sensitivities (the reverse of macro).
- Arbitrage portfolio = **zero investment, zero risk, positive expected return**.
- Active risk² = active **factor** risk² + active **specific** risk².


## 20 Ethics

### Application of the Code and Standards: Level II -> [[Application_of_the_Code_and_Standards]]
- This reading adds **no new rules** — losing points here means failing to **apply** known Standards, not lack of theory.
- Identify **all** Standards implicated; partial identification loses credit.
- Don't confuse the two case types: the **last two** cases also need **corrective actions + a firm policy**, not just a yes/no.
- Use the **2024** subsection names: **I(E) Competence** exists; **VI(A)** is **"Avoid or Disclose Conflicts."**
- "No violation" is sometimes the correct answer (e.g., conduct that merely *looks* like a conflict but is fully disclosed and managed) — read for whether the member **disclosed/avoided** appropriately before concluding a breach.

### Code of Ethics and Standards of Professional Conduct -> [[Code_and_Standards]]
- Choose the response demanding the **highest ethical standard**; partial compliance is still a violation.
- Follow the **stricter** of applicable law or the Code & Standards.
- **Mosaic theory** is allowed (not an MNPI violation); acting on material nonpublic info is not.
- Confidentiality (III-E) does **not** shield a client's **illegal** activity.
- **Standard I has FIVE subsections now** — don't forget **I(E) Competence** (added 2024).
- **VI(A)** is **"Avoid or Disclose"** (avoid first); "Disclosure of Conflicts" is the **old** title.
- **V(B)** now also requires disclosing the **nature of services AND the costs** to the client.
- A single fact pattern usually implicates **several** Standards — name **all** that apply, not just one.
- "CFA" is an **adjective** (CFA charterholder); using it as a noun violates **VII(B)**.

### Global Investment Performance Standards (GIPS) -> [[GIPS]]
- GIPS compliance is **firm-wide and all-or-nothing** — no partial/composite-only claims.
- A composite must include **all** discretionary, fee-paying portfolios of that strategy (anti-cherry-picking).
- **Third-party verification is recommended, not required**, and applies firm-wide (not to a single composite).
- Minimum initial presentation: **5 years** of compliant performance.
