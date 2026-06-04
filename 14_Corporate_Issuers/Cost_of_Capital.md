---
aliases: [Cost of Capital, Required Return on Equity, Equity Risk Premium, Country Risk Premium, Beta Estimation, Hamada, Grinold-Kroner, Fama-French, Build-Up Approach, Expanded CAPM, BYPRP]
tags: [CFA-L2, corp, concept, valuation]
date: 2026-06-03
status: evergreen
source: Official Curriculum 2026 L2 V4, Reading "Cost of Capital: Advanced Topics" (Schweser Book 2, Module 15); LOS a-f
---

# Cost of Capital: Advanced Topics

## Cost of Capital Factors — Top-Down vs Bottom-Up (15.a) — official Exhibit 1
`WACC = w_d·r_d·(1−t) + w_p·r_p + w_e·r_e`; `r_d = R_f + credit spread`; `r_e = R_f + β × ERP`.
Drivers split into:
- **Top-down (systematic — in R_f and ERP)**: capital availability; market conditions
  (interest rates, inflation, business cycle, FX volatility); legal/regulatory & **country risk**
  (common-law systems → deeper markets, lower cost); tax jurisdiction.
- **Bottom-up (firm-specific — in credit spread and β)**: revenue/earnings/cash-flow volatility;
  asset nature & liquidity (collateral); financial strength, profitability, leverage; security features
  (a put or convertible feature lowers cost of debt at issuance).
- Preferred equity sits between debt and common: lower ERP than common → lower cost than common equity.

## Cost of Debt (15.b)
Method depends on: type of debt (traded / non-traded / bank / lease), liquidity, credit rating, currency.
- **Traded (straight) debt → YTM**: use YTM on the longest-maturity straight bond (or a more liquid
  shorter bond if it trades more reliably). Reflects the current cost of issuing similar new debt.
- **Non-traded debt, rating exists → matrix pricing**: YTM of other issuers with the same rating/maturity.
- **Non-traded, no rating → synthetic rating**: deduce a rating from **interest-coverage (IC)** and
  **leverage (D/E)** ratios (e.g., AAA: IC > 10, D/E < 35%; BBB: 3 < IC < 5, 42–44%), then take the
  matrix YTM or add that rating's credit spread to R_f.
- **Bank debt**: use the rate on recent/comparable bank borrowings (the IBR).
- **Leases**: the implicit lease rate is a cost of debt; a low implicit rate can beat the firm's unsecured
  IBR (but a lease still adds leverage).
- **International (15.c)**: cost of debt should match the **currency of the cash flows**. For a less-mature
  market, add a **country risk premium** derived from a **country risk rating (CRR)**: CRP = (local median
  yield for the rating) − (benchmark-country yield). E.g., rating-2 country at 4.5% vs benchmark 4.0% → CRP 0.5%.

## Equity Risk Premium (15.c)
**Historical (ex-post)** — four key choices:
1. which equity index, 2. sample period, 3. mean measure (**arithmetic > geometric**), 4. risk-free proxy
(short bill vs long bond). Subject to **survivorship bias**; recency-laden; may not reflect the future.

**Forward-looking (ex-ante)** — three methods:
- **Survey-based**: poll experts (sensitive to recent returns; EM > DM).
- **DDM / Gordon growth**: `ERP = E(D₁/V₀) + E(g) − R_f` — i.e., expected dividend yield + expected
  earnings growth − risk-free. Assumes a **constant P/E** (earnings, dividends, price grow at the same g);
  add a P/E-expansion adjustment if that won't hold. Multi-stage version: solve the IRR that sets
  index price = PV(Stage1) + PV(Stage2) + PV(Stage3), then subtract R_f.
- **Macroeconomic — Grinold-Kroner (2001)**:
  `ERP = [DY + %ΔP/E + i + g − ΔS] − E(R_f)`, where
  expected **earnings growth per share = i + g − ΔS** (expected inflation + real EPS growth − % change in
  shares outstanding), and **%ΔP/E** = expected repricing (P/E expansion/contraction, proxy 0 if fairly
  valued). Common proxies: DY = index dividend yield; i = nominal − real (TIPS) yield; g = real GDP growth.
  - **Worked example (official):** R_f 2.5%, i 1.6%, g 3.0%, %ΔP/E 0, DY 2.2%, ΔS −0.7% →
    `ERP = {2.2 + 0 + [1.6 + 3.0 − (−0.7)]} − 2.5 = 5.0%`.
  - **Trap:** a rise in **expected inflation does NOT change ERP** — i is added but R_f rises by the same
    amount, so they cancel. Falling **expected income (DY)** lowers ERP. Not appropriate where the equity
    market is a small share of the economy (many EMs).

## Required Return on Equity (15.d, 15.e)
Public-company methods: DDM, bond-yield-plus, and risk-based (CAPM / Fama-French).
- **DDM (Gordon)**: `r_e = D₁/P₀ + g`. Needs publicly traded shares paying a stable, predictable dividend.
  Multi-stage: solve `P₀ = Σ Dₜ/(1+r_e)ᵗ + Pₙ/(1+r_e)ⁿ` for r_e (an IRR; include the terminal price Pₙ).
- **Bond-yield-plus-risk-premium (BYPRP)**: `r_e = r_d + RP`, r_d = YTM on the firm's long-term debt,
  RP ≈ historical equity-over-corporate-bond premium (3–5% typical). Needs traded debt; RP is somewhat
  arbitrary. (Ex: r_d 4.3% + RP 6.1% = 10.4%.)
- **CAPM**: `r_e = R_f + β × ERP`. β from the **market model** regression of excess stock returns on
  excess market returns; choose index, estimation window, and R_f proxy (short bill vs long bond — a
  short rate on a steep curve understates r_e).
- **Fama-French 3-factor**: `r_e = R_f + β₁·ERP + β₂·SMB + β₃·HML` (SMB = **size** premium small−large;
  HML = **value** premium high−low book-to-market).
- **Fama-French 5-factor**: adds `+ β₄·RMW + β₅·CMA` (RMW = **profitability** robust−weak;
  CMA = **investment** conservative−aggressive). The market β usually differs from the CAPM β.

### Private companies (15.e) — add premiums, beta from peers
Risk factor models can't be applied directly (no prices); private firms are smaller, less liquid, owner-managed.
Add a **size premium (SP)**, **industry premium (IP)**, and **specific-company risk premium (SCRP)**.
Illiquidity is usually handled as a **discount for lack of marketability (on value)**, NOT as a premium in r_e.
- **Expanded CAPM**: `r_e = R_f + β_peer × ERP + SP + SCRP` (β unlevered from public peers then relevered).
- **Build-up**: `r_e = R_f + ERP + SP + IP + SCRP` (no beta; ERP not beta-adjusted ⇒ implicit β = 1.0 =
  average-risk large-cap; then add size/industry/specific premiums). Use when comparable publics are unavailable.

## Country Risk & International Models (emerging markets) (15.c, 15.e)
- **Country spread model**: `ERP = ERP_developed + (λ × CRP)`, where λ = the company's exposure to the
  local country. So `r_e = R_f + β × (mature-market ERP) + λ·CRP`.
- **CRP — sovereign yield spread method**: CRP ≈ (EM sovereign bond yield, in the developed currency) −
  (developed-market govt yield). Caveat: a **bond** spread may not capture **equity** risk.
- **CRP — Damodaran refinement**: `CRP = sovereign yield spread × (σ_equity / σ_bond)` — scale the bond
  spread by relative equity-vs-bond volatility. Requires local equity AND bond return histories.
- **Global CAPM (GCAPM)**: single global-index factor; tends to give a low/negative β for EM stocks
  (low EM–DM correlation). Reasonable only if operations are limited to developed countries.
- **International CAPM (ICAPM)**: two factors — `E(r_e) = R_f + β_G·(E(r_gm) − R_f) + β_C·(E(r_c) − R_f)`,
  adding a wealth-weighted **foreign-currency index** (r_c) to the global index (r_gm). β_C captures FX
  sensitivity of cash flows. No single accepted method once operations reach developing countries.

## Beta Estimation (15.a, 15.e)
- Regression beta is noisy for the subject firm; use **comparable (pure-play) companies**:
  1. Take comparable's **equity (levered) beta**; **unlever** (Hamada):
     `β_asset = β_equity / [1 + (1 − t)(D/E)]`.
  2. **Relever** to the subject firm's capital structure:
     `β_equity = β_asset × [1 + (1 − t)(D/E_subject)]`.
- Use the **project's** (not the firm's) risk for project cost of capital.

## Capital Structure & Peers (15.f)
- Evaluate a firm's WACC and structure **relative to peers**: leverage, debt maturity, cost of debt,
  coverage; identify whether the structure is optimal/sustainable.

## Exam Traps
- **Unlever then relever** beta when the comparable's leverage differs from the subject's (Hamada).
- **Expanded CAPM** = R_f + β·ERP + **SP + SCRP** (uses peer beta); **Build-up** = R_f + ERP + **SP + IP +
  SCRP** (NO beta — implicit β=1). Don't double-count beta in build-up. Illiquidity → marketability
  **discount on value**, not a premium in r_e.
- **Grinold-Kroner**: a rise in expected **inflation does NOT change ERP** (i added, R_f subtracted, cancel).
  Earnings growth term = i + g − ΔS; %ΔP/E is the repricing term.
- **DDM ERP** assumes a **constant P/E**; if P/E will change, add a repricing adjustment.
- Country risk premium (Damodaran) scales the sovereign spread by **equity-to-bond volatility ratio**.
- **Fama-French**: SMB = size, HML = value, RMW = profitability, CMA = investment. The market beta differs
  from the single-factor CAPM beta once extra factors are added.
- Use **project** risk, not company-average risk, for a project's discount rate.
- Cost of debt for an EM issuer: add a **country risk premium** from a country **risk rating (CRR)**, and
  match the **currency** of the cash flows.

## Q&A

### 2026-06-03 — Unlever and relever beta (pure-play / Hamada)
**Q:** A comparable has equity beta 1.4, D/E 0.5, tax 25%. The subject firm has D/E 1.0, tax 25%. What's the subject's equity beta?
**A:** Two steps. **Unlever** the comparable to its asset (unlevered) beta:
`β_asset = 1.4 / [1 + (1−0.25)(0.5)] = 1.4 / 1.375 = 1.018`. **Relever** to the subject's structure:
`β_equity = 1.018 × [1 + (1−0.25)(1.0)] = 1.018 × 1.75 = 1.78`. Then plug into CAPM `r_e = R_f + β·ERP`.
Trap: you strip out the comparable's financial risk, then add back the **subject's**; use the **project's**
risk for a project discount rate, not the company average.
Related: [[Dividends_and_Share_Repurchases]]

### 2026-06-03 — Country risk premium for an emerging market
**Q:** How do you build the country risk premium, and where does it go in CAPM?
**A:** `CRP = sovereign yield spread × (σ_equity / σ_bond)` — the sovereign bond spread (EM yield − developed
yield, same currency) scaled by the **relative volatility of the equity market to the bond market**. Then
`r_e = R_f + β × (mature-market ERP + CRP)`. Intuition: the bond spread captures default risk; multiplying
by equity/bond vol scales it up to equity-market risk.
Related: [[Equity_Valuation_Process]]

### 2026-06-04 — Grinold-Kroner forward-looking ERP
**Q:** Using Grinold-Kroner, find the ERP given R_f 2.5%, expected inflation 1.6%, real EPS growth 3.0%, no
P/E change, dividend yield 2.2%, and a −0.7% change in shares outstanding.
**A:** `ERP = [DY + %ΔP/E + i + g − ΔS] − E(R_f) = [2.2 + 0 + 1.6 + 3.0 − (−0.7)] − 2.5 = 5.0%`. The earnings
growth per share = i + g − ΔS = 1.6 + 3.0 + 0.7 = 5.3%; add DY (2.2%) and the repricing term (0); subtract
R_f. **Trap:** higher expected inflation leaves ERP unchanged (i is added and R_f rises equally), and the
model is invalid where the equity market is a small share of the economy (many EMs).
Related: [[Equity_Valuation_Process]]

### 2026-06-04 — Private-company cost of equity: expanded CAPM vs build-up
**Q:** How do the expanded CAPM and build-up approaches differ for a private firm's required return on equity?
**A:** **Expanded CAPM** keeps a beta (estimated from public peers, unlevered then relevered) and adds
private premiums: `r_e = R_f + β_peer·ERP + SP + SCRP`. **Build-up** uses **no beta** (ERP is not
beta-adjusted, implying β = 1.0 = average-risk large-cap) and stacks premiums:
`r_e = R_f + ERP + SP + IP + SCRP`, where SP = size, IP = industry, SCRP = specific-company risk. Use
build-up when comparable public companies are unavailable. **Trap:** illiquidity is reflected as a
**discount for lack of marketability on value**, not as an extra premium in r_e.
Related: [[Equity_Valuation_Process]]

### 2026-06-04 — Fama-French factors
**Q:** What are the factors in the Fama-French three- and five-factor models?
**A:** Three-factor: `r_e = R_f + β₁·ERP + β₂·SMB + β₃·HML`, where **SMB** = size premium (small − large cap)
and **HML** = value premium (high − low book-to-market). Five-factor adds `+ β₄·RMW + β₅·CMA`: **RMW** =
profitability premium (robust − weak) and **CMA** = investment premium (conservative − aggressive). These
extend CAPM; the estimated market beta typically differs from the single-factor CAPM beta because of the
added factors.
Related: [[Equity_Valuation_Process]]
