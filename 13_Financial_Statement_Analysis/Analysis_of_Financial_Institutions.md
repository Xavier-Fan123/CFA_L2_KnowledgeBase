---
aliases: [Analysis of Financial Institutions, CAMELS, Bank Analysis, Insurance Company Analysis]
tags: [CFA-L2, fsa, concept, financials]
date: 2026-10-05
status: evergreen
source: Official Curriculum 2026 L2 V3 LM4 (October 2026 errata applied); Schweser Book 2, Module 10, LOS 10.a-10.f
---

# Analysis of Financial Institutions

## Why Banks Are Different (10.a, 10.b)
- Highly **levered**, balance-sheet-driven, mostly **financial assets** (loans, securities) whose values sit **relatively close to fair value** → direct exposure to **credit, liquidity, market, and interest-rate risk**; systemically important → heavily **regulated**.
- **Systemic risk** = impairment in one part of the financial system that can spread through the rest of the system and hurt the whole economy.
- The **Basel Committee** is a standing committee of the **Bank for International Settlements**; its framework sets **minimum capital, minimum liquidity, and stable-funding** requirements, but **national regulators** set the binding minimums.
- Key regulatory frameworks: **Basel III** — minimum capital, liquidity, and stable-funding requirements.
  - **Minimum capital ratios** (as a % of **risk-weighted assets**, RWA) — memorize the three numbers:

| Ratio | Basel III minimum |
|---|---|
| **Common Equity Tier 1 (CET1)** | **4.5% of RWA** |
| **Total Tier 1** (CET1 + additional Tier 1) | **6.0% of RWA** |
| **Total capital** (Tier 1 + Tier 2) | **8.0% of RWA** |

  - Riskier assets carry higher risk weights, so the **same** equity supports fewer risky assets. Other global bodies alongside the Basel Committee: **Financial Stability Board**, **IOSCO**, **IAIS**, and the International Association of Deposit Insurers.
  - **Liquidity Coverage Ratio (LCR)** = HQLA / 30-day net cash outflows (short-term resilience).
  - **Net Stable Funding Ratio (NSFR)** = available stable funding / required stable funding (≥ 100%).

## CAMELS Approach (10.c)
- An examiner rates each component **1 (best) to 5 (worst)**, then forms a **composite** rating that is **not a simple average** — the examiner weights the components by judgment, so two examiners with identical component ratings can reach different composites. Analysts reuse the framework for equity and debt analysis.

| Letter | Component | What to assess |
|------|------|------|
| **C** | Capital adequacy | Tier 1 / Total capital vs risk-weighted assets; cushion for losses |
| **A** | Asset quality | Loan quality, concentration, allowance for loan losses, NPLs |
| **M** | Management | Governance, controls, risk culture, accounting choices |
| **E** | Earnings | Quality, sustainability, composition (recurring vs one-off); heavy use of estimates — loan-loss provisions, securities valuation, goodwill impairment |
| **L** | Liquidity | LCR, NSFR, funding stability, deposit base |
| **S** | Sensitivity to market risk | Interest-rate, currency, and other market exposures (VaR) |

### Component detail (official text)
- **Capital adequacy** — proportion of assets funded with capital, measured against **risk-weighted assets**: cash 0%, corporate loans **100%**, high-volatility commercial real estate and loans **> 90 days past due above 100%**; off-balance-sheet exposures are risk-weighted too. *Example*: $10 cash, $1,000 performing loans, $10 non-performing loans at 150% → RWA = 0 + 1,000 + 15 = **$1,015**.
  - **CET1** = common stock + related surplus + retained earnings + **AOCI**, less deductions such as **intangible assets and deferred tax assets** (the most loss-absorbing capital). **Other Tier 1**: subordinated, **no fixed maturity**, payments **fully discretionary**. **Tier 2**: subordinated to depositors and general creditors, **original maturity ≥ 5 years**.
- **Asset quality** — credit risk of the assets **plus** the strength of risk management. Loans at **amortized cost net of the allowance for loan losses**; securities by category (IFRS 9: amortized cost / FVOCI / FVTPL; US GAAP: equity at fair value through net income, debt as held-to-maturity, trading, or available-for-sale). Check asset **composition** (liquid assets, investments, loans incl. reverse repos as % of assets), **credit-quality distribution**, whether the **allowance moves with impaired assets**, off-balance-sheet credit exposure (guarantees, unused commitments, letters of credit), and **diversification**.
- **Management capabilities** — compliance, an **independent board** without excessive pay or self-dealing, internal controls, transparent reporting; for banks above all, the ability to **identify and control risk**. Overall performance is the most reliable indicator.
- **Earnings** — adequate return on capital, **high quality** (unbiased estimates, sustainable sources) and trending up. Big estimates: **loan impairment allowances** and **fair values** (see hierarchy below).
- **Liquidity** — liquid assets vs near-term cash needs **and**, under Basel III, the **stability of funding**: LCR and NSFR (target **≥ 100%**).
- **Sensitivity to market risk** — mismatches in **maturity, repricing frequency, reference rate, or currency** of assets vs liabilities, plus off-balance-sheet derivatives and guarantees. Banks disclose the earnings effect of rate shifts (and VaR). Assets repricing **faster** than liabilities benefit from **rising** rates; because banks have more assets than liabilities, a rate rise lifts net interest income even with matched terms.

### Fair-Value Hierarchy inside "E" (10.c)
Earnings quality depends on **how** the securities portfolio is valued:

| Level | Input | Reliability |
|---|---|---|
| **Level 1** | **Quoted prices** in active markets for **identical** assets | Highest |
| **Level 2** | **Observable** inputs other than quoted prices for identical assets (quoted prices for similar assets, observable rates/spreads) | Medium |
| **Level 3** | **Unobservable** inputs — the bank's own model assumptions | Lowest — the earnings-quality red flag |

A rising share of **Level 3** assets is a warning sign: management effectively marks its own book.

## Limitations of CAMELS and Other Bank Factors (10.c, 10.e)
- **Limitations**: CAMELS is **neither comprehensive nor integrated**, and the **order of the letters does not signal importance** — capital ("C") and liquidity ("L") are equally important under Basel III.
- **Bank-specific factors CAMELS misses**:
  - **Government support** — size ("too big to fail", **SIFIs**), health of the country's banking system, and **government ownership** (a "development" view vs a sign of a weak system).
  - **Mission** of the banking entity (e.g., community or development objectives rather than profit maximization).
  - **Corporate culture** — risk-averse or risk-taking? Warning signs: outsized concentrated exposures, restatements from control failures, above-average equity-based pay, a history of slow loss provisioning followed by large write-downs.
- **Factors relevant to any company**: **competitive environment**; **off-balance-sheet items** (credit derivatives, **unconsolidated VIEs**, benefit plans, **assets under management** of trust departments); **segment information**; **currency exposure** (transaction exposure, and translation adjustments that can **reduce capital** when the home currency strengthens); **risk factors** in the annual filing; **Basel III (Pillar 3) disclosures** that promote market discipline.
- *Errata (2 Jun 2026)*: the curriculum sentence calling operating leases a "low-risk off-balance-sheet liability" was **deleted** — leases are on the balance sheet under current standards.

## Insurance Companies (10.f)
- **Business model**: revenue = **premiums** + **investment income on the float** (premiums collected but not yet paid out as claims). Analyze **business profile, earnings characteristics, investment returns, liquidity, and capitalization**; for P&C also **loss reserves** and the **combined ratio**.
- **Property & casualty (P&C)**: shorter-tail, less predictable claims. Personal vs commercial lines; **direct writers** (in-house sales staff → higher **fixed** costs) vs **agency writers** (commissions → **variable** costs). **Loss reserves** are a large, discretionary estimate — optimistic reserving underprices policies and can lead to insolvency, and long-dated obligations (e.g., asbestos) are hardest to estimate. Investment income is less volatile than underwriting income (low-risk, low-return portfolios). Key ratios: **loss & loss-adjustment expense ratio** (= (loss expense + loss-adjustment expense) / net premiums earned), **underwriting expense ratio** (= underwriting expense / net premiums written), **combined ratio** (= loss ratio + expense ratio; **< 100% = underwriting profit**), **dividends-to-policyholders ratio**, **combined ratio after dividends** (= combined ratio + policyholder-dividends ratio), and the **total investment return ratio**.
- **P&C pricing cycle — hard vs soft market (10.f)**: P&C premiums are **cyclical**, and the curriculum reads the cycle straight off the industry **combined ratio**:
  - **Low** combined ratio → **hard** market (premium rates are high relative to claims, so underwriting is profitable).
  - **High** combined ratio → **soft** market (rates have been competed down relative to claims).
  - Trap: learn it as a **mapping, not a story** — **low combined ratio = hard market**, **high combined ratio = soft market**.
- **Life & health (L&H)**: longer contract periods, **higher float**, and therefore **higher interest-rate risk** than P&C; more predictable claims, so L&H insurers can take **more investment risk**. Focus on reserves, the investment spread, and persistency.
  - **Earnings**: heavy estimates — future policyholder benefits (actuarial assumptions such as life expectancy) and **capitalized acquisition costs** amortized on expected profits; **contract surrenders** (early cancellation for cash value) add expense and liquidity risk; an asset-liability **valuation mismatch** (assets at market, liabilities at historical assumptions) distorts earnings when rates move.
  - **A.M. Best L&H profitability ratios**: (1) **total benefits paid ÷ (net premiums written + deposits)**; (2) **commissions and expenses incurred ÷ (net premiums written + deposits)**; plus ROA, ROE, operating margin, operating ROA/ROE.
  - **Investment returns**: diversification vs liabilities, performance = investment income (± realized, ± unrealized gains) ÷ invested assets, and interest-rate risk = **asset duration vs liability duration**.
- **Capitalization**: unlike banks (Basel since 1988) there is **no global risk-based capital standard** for insurers (the IAIS is developing one); jurisdictional regimes exist — EU **Solvency II**, US **NAIC risk-based capital**.
- Analyze: profitability (underwriting + investment), capitalization, liquidity, reserve adequacy.

## Exam Traps
- **CAMELS** order: Capital, Asset quality, Management, Earnings, Liquidity, Sensitivity.
- **Combined ratio < 100%** = underwriting profit; > 100% = underwriting loss (insurer relies on investment income).
- **Basel III minima: CET1 4.5%, Tier 1 6%, Total capital 8%** of risk-weighted assets; LCR and NSFR both ≥ **100%**.
- **Hard vs soft P&C market**: a **low** combined ratio marks a **hard** (profitable, high-rate) market; a **high** combined ratio marks a **soft** market. L&H carries **more interest-rate risk** than P&C because of its longer contracts and larger float.
- A growing share of **Level 3** (unobservable-input) assets is a bank earnings-quality red flag.
- LCR addresses **short-term (30-day)** liquidity; NSFR addresses **structural/long-term** funding.
- CAMELS ratings run **1 = best to 5 = worst**, and the composite is a **judgment-weighted**, not arithmetic, average. CAMELS order ≠ importance.
- **CET1 deducts intangibles and deferred tax assets**; Tier 2 needs an original maturity of at least five years.
- **Direct writers** carry fixed distribution costs; **agency writers** carry variable commission costs.

## Q&A

### 2026-06-03 — Combined ratio: what does it tell you about a P&C insurer?
**Q:** A P&C insurer reports a combined ratio of 97%. Is that good, and what is it?
**A:** `Combined ratio = loss & loss-adjustment expense ratio + underwriting expense ratio`. **Below 100% = underwriting profit** (premiums cover claims + expenses), so 97% is good — the insurer made money on underwriting *before* investment income. Above 100% = underwriting loss, meaning the insurer relies on **investment income** to be profitable overall. P&C is shorter-tail/less predictable than life & health.
Related: [[Quality_of_Financial_Reports]]

### 2026-06-03 — LCR vs NSFR: what does each capture?
**Q:** Distinguish the two Basel III liquidity ratios.
**A:** **LCR = high-quality liquid assets ÷ 30-day net cash outflows** — **short-term** (30-day stress) resilience. **NSFR = available stable funding ÷ required stable funding (≥ 100%)** — **structural / long-term** funding stability (are long-dated assets funded with stable liabilities?). Both ≥ minimums. These sit under the **L** (liquidity) and complement the capital ratios (CET1/Tier 1/Total vs risk-weighted assets) that sit under **C** in CAMELS.
Related: [[Quality_of_Financial_Reports]]
