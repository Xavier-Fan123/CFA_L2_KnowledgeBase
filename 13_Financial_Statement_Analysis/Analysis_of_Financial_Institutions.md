---
aliases: [Analysis of Financial Institutions, CAMELS, Bank Analysis, Insurance Company Analysis]
tags: [CFA-L2, fsa, concept, financials]
date: 2026-08-25
status: evergreen
source: Schweser Book 2, Module 10, LOS 10.a-10.f
---

# Analysis of Financial Institutions

## Why Banks Are Different (10.a, 10.b)
- Highly **levered**, balance-sheet-driven, mostly **financial assets** (mark-to-market sensitive), systemically important → heavily **regulated**.
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

| Letter | Component | What to assess |
|------|------|------|
| **C** | Capital adequacy | Tier 1 / Total capital vs risk-weighted assets; cushion for losses |
| **A** | Asset quality | Loan quality, concentration, allowance for loan losses, NPLs |
| **M** | Management | Governance, controls, risk culture, accounting choices |
| **E** | Earnings | Quality, sustainability, composition (recurring vs one-off); heavy use of estimates — loan-loss provisions, securities valuation, goodwill impairment |
| **L** | Liquidity | LCR, NSFR, funding stability, deposit base |
| **S** | Sensitivity to market risk | Interest-rate, currency, and other market exposures (VaR) |

### Fair-Value Hierarchy inside "E" (10.c)
Earnings quality depends on **how** the securities portfolio is valued:

| Level | Input | Reliability |
|---|---|---|
| **Level 1** | **Quoted prices** in active markets for **identical** assets | Highest |
| **Level 2** | **Observable** inputs other than quoted prices for identical assets (quoted prices for similar assets, observable rates/spreads) | Medium |
| **Level 3** | **Unobservable** inputs — the bank's own model assumptions | Lowest — the earnings-quality red flag |

A rising share of **Level 3** assets is a warning sign: management effectively marks its own book.

## Other Bank Factors (10.d, 10.e)
- Government support / systemic importance, mission, culture; off-balance-sheet items; competitive environment; quality of capital. Not all captured by CAMELS.

## Insurance Companies (10.f)
- **Property & casualty (P&C)**: shorter-tail, less predictable claims. Key ratios: **loss & loss-adjustment expense ratio** (= (loss expense + loss-adjustment expense) / net premiums earned), **underwriting expense ratio** (= underwriting expense / net premiums written), **combined ratio** (= loss ratio + expense ratio; **< 100% = underwriting profit**), **dividends-to-policyholders ratio**, **combined ratio after dividends** (= combined ratio + policyholder-dividends ratio), and the **total investment return ratio**.
- **P&C pricing cycle — hard vs soft market (10.f)**: P&C premiums are **cyclical**, and the curriculum reads the cycle straight off the industry **combined ratio**:
  - **Low** combined ratio → **hard** market (premium rates are high relative to claims, so underwriting is profitable).
  - **High** combined ratio → **soft** market (rates have been competed down relative to claims).
  - Trap: learn it as a **mapping, not a story** — **low combined ratio = hard market**, **high combined ratio = soft market**.
- **Life & health (L&H)**: longer contract periods, **higher float**, and therefore **higher interest-rate risk** than P&C; more predictable claims. Focus on reserves, the investment spread, and persistency.
- Analyze: profitability (underwriting + investment), capitalization, liquidity, reserve adequacy.

## Exam Traps
- **CAMELS** order: Capital, Asset quality, Management, Earnings, Liquidity, Sensitivity.
- **Combined ratio < 100%** = underwriting profit; > 100% = underwriting loss (insurer relies on investment income).
- **Basel III minima: CET1 4.5%, Tier 1 6%, Total capital 8%** of risk-weighted assets; LCR and NSFR both ≥ **100%**.
- **Hard vs soft P&C market**: a **low** combined ratio marks a **hard** (profitable, high-rate) market; a **high** combined ratio marks a **soft** market. L&H carries **more interest-rate risk** than P&C because of its longer contracts and larger float.
- A growing share of **Level 3** (unobservable-input) assets is a bank earnings-quality red flag.
- LCR addresses **short-term (30-day)** liquidity; NSFR addresses **structural/long-term** funding.

## Q&A

### 2026-06-03 — Combined ratio: what does it tell you about a P&C insurer?
**Q:** A P&C insurer reports a combined ratio of 97%. Is that good, and what is it?
**A:** `Combined ratio = loss & loss-adjustment expense ratio + underwriting expense ratio`. **Below 100% = underwriting profit** (premiums cover claims + expenses), so 97% is good — the insurer made money on underwriting *before* investment income. Above 100% = underwriting loss, meaning the insurer relies on **investment income** to be profitable overall. P&C is shorter-tail/less predictable than life & health.
Related: [[Quality_of_Financial_Reports]]

### 2026-06-03 — LCR vs NSFR: what does each capture?
**Q:** Distinguish the two Basel III liquidity ratios.
**A:** **LCR = high-quality liquid assets ÷ 30-day net cash outflows** — **short-term** (30-day stress) resilience. **NSFR = available stable funding ÷ required stable funding (≥ 100%)** — **structural / long-term** funding stability (are long-dated assets funded with stable liabilities?). Both ≥ minimums. These sit under the **L** (liquidity) and complement the capital ratios (CET1/Tier 1/Total vs risk-weighted assets) that sit under **C** in CAMELS.
Related: [[Quality_of_Financial_Reports]]
