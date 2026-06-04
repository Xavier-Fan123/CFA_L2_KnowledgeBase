---
aliases: [Market-Based Valuation, Price Multiples, EV/EBITDA, Justified Multiples, PEG, Method of Comparables]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-06-03
status: evergreen
source: Schweser Book 3, Module 20, LOS 20.a-20.r
---

# Market-Based (Relative) Valuation

## Two Approaches (20.a, 20.b)
- **Method of comparables**: compare a stock's multiple to a benchmark (peers, industry, own history).
  "Law of one price" — similar assets should trade at similar multiples.
- **Method based on forecasted fundamentals**: derive a **justified multiple** from a DCF/Gordon model.

## Justified Multiples (from fundamentals) (20.i)
- **Justified leading P/E** = `payout / (r − g)`; **trailing P/E** = `payout(1+g)/(r − g)`.
- **Justified P/B** = `(ROE − g) / (r − g)` (ties to residual income → [[Residual_Income]]).
- **Justified P/S** = `(net margin × payout × (1+g)) / (r − g)`.

## Earnings Issues (20.e, 20.f)
- **Normalize EPS** for cyclical firms: method of historical average EPS or average ROE × current BV.
- **Negative earnings** → P/E meaningless; use **earnings yield E/P** (high E/P = cheap) or normalized EPS.
- **Underlying/trailing earnings** strip out non-recurring items.

## PEG and Cross-Sectional P/E (20.h, 20.j)
- **PEG** = `(P/E) / g(%)`; lower PEG = relatively cheaper, but assumes a linear P/E-growth relation and
  ignores risk and differing growth durations.
- **Predicted P/E**: regress P/E on fundamentals (growth, payout, risk) cross-sectionally; limits —
  unstable out of sample, multicollinearity, time-period specific.

## Price/Cash Flow (P/CF) and Dividend Yield (20.c, 20.d)
Both are explicit curriculum multiples alongside P/E, P/B, P/S.

**Price/Cash Flow — four cash-flow definitions** (official LM4): the analyst must state *which* one.
| CF definition | How computed | Note |
|---|---|---|
| **CF** (earnings-plus-noncash-charges) | EPS + per-share Dep, Amort, Depletion | The default "P/CF"; simple but ignores WCInv and non-cash *revenue* |
| **CFO** | Cash flow from operations (statement of cash flows) | Adjust for non-persistent items; IFRS vs US GAAP interest/dividend classification differs |
| **FCFE** | CFO − FCInv + net borrowing | Strongest link to valuation theory; but more **volatile** / often **negative** |
| **EBITDA** | EBIT + Dep + Amort (a pre-interest, pre-tax operating-cash proxy) | Used in **EV/EBITDA**, not price/EBITDA (EBITDA is a firm-level, pre-debt flow) |
- Rationale for P/CF: cash flow is **harder to manipulate** and **more stable** than earnings, and sidesteps
  cross-firm differences in accounting conservatism.
- Drawback: the simple **CF** definition ignores working-capital changes and non-cash revenue (e.g.,
  front-end-loaded revenue is not caught); theory actually prefers **P/FCFE**.

**Dividend yield (P/D inverted)** — `D/P`. Reported as a yield (not P/D) because many firms pay no dividend
(then D/P = 0, but P/D is undefined).
- **Trailing dividend yield** = (annualized most-recent dividend, i.e. the *dividend rate*) / price.
- **Justified (leading) dividend yield (Gordon)**: `D0/P0 = (r − g)/(1 + g)`.
- Rationales: dividend yield is a **component of total return** and a **less risky** component than capital
  gains. Drawbacks: it is only **one** component of return (ignoring it elsewhere is suboptimal), and the
  **dividend displacement of earnings** means higher current dividends can trade off future growth.

## Enterprise Value Multiples (20.n-20.p)
- **EV** = market cap + total debt + preferred + minority interest − cash & equivalents (cash & short-term
  investments, a.k.a. *nonearning assets*, are subtracted because EV = net price an acquirer pays for the
  whole firm — the acquirer gains access to that cash).
- **EV/EBITDA**: numerator (total firm value) matches a pre-financing flow (EBITDA) → good for comparing
  firms with **different capital structures** and for capital-intensive firms.
- EV/Sales useful when earnings are negative or capital structures differ.

## Momentum & Averaging (20.q, 20.r)
- **Momentum indicators**: earnings surprise (standardized unexpected earnings = unexpected earnings ÷
  std-dev of past surprises), relative strength.
- **Central tendency of a group of multiples** (4 measures in the LOS):
  - **Arithmetic mean** — biased **upward** by large outliers; overstates the group multiple.
  - **Median** — robust to outliers, but ignores magnitude.
  - **Harmonic mean** = `n / Σ(1/Xi)` (reciprocal of the arithmetic mean of the reciprocals) — the correct
    portfolio-equivalent average for price multiples; weights each stock by its yield.
  - **Weighted harmonic mean** = `1 / Σ(wi/Xi)` with portfolio value weights wi — matches a real
    cap-weighted portfolio's multiple. (Harmonic ≤ geometric ≤ arithmetic for positive values.)

## Exam Traps
- **EV subtracts cash** and adds debt/preferred/minority — a common error.
- **EV/EBITDA** is preferred when capital structures differ (P/E is distorted by leverage).
- Use the **harmonic mean** to average P/Es across firms, not the arithmetic mean; the arithmetic mean is
  biased **upward** by outliers.
- Justified P/B = `(ROE − g)/(r − g)`; P/B > 1 when ROE > r.
- **P/CF**: always pin down the cash-flow definition (CF vs CFO vs FCFE vs EBITDA). The simple **CF**
  (EPS + noncash charges) **ignores WCInv and non-cash revenue**. EBITDA pairs with **EV**, not price.
- **Justified dividend yield = (r − g)/(1 + g)** — it is the **inverse** orientation of P/E-type multiples,
  so *higher* yield = *cheaper*. Trailing yield uses the **dividend rate** (annualized latest dividend).

## Q&A

### 2026-06-03 — Why use the harmonic mean to average P/Es?
**Q:** A peer group has P/Es of 10, 15, and 60. Why not just average them?
**A:** The **arithmetic mean** (28.3) is dragged up by the high outlier and **overstates** the group
multiple. The **harmonic mean** = `n / Σ(1/Pi/E) = 3/(1/10 + 1/15 + 1/60) = 3/0.1833 = 16.4` weights each
stock by its earnings yield and is the correct way to average price multiples (equivalent to an
equal-dollar-weighted portfolio's multiple). Always use harmonic (or weighted harmonic) mean for P/Es.
Related: [[Dividend_Discount_Models]]

### 2026-06-03 — Why EV/EBITDA over P/E when capital structures differ?
**Q:** When is EV/EBITDA the better multiple, and how is EV built?
**A:** `EV = market cap + total debt + preferred + minority interest − cash & equivalents`. EBITDA is a
**pre-financing, pre-tax** flow available to **all** capital providers, and EV is total firm value — so
the pair is **capital-structure-neutral**, unlike P/E, which is distorted by leverage and by D&A policy.
Prefer EV/EBITDA for firms with **different leverage**, heavy D&A, or negative net income. Trap: EV
**subtracts cash** and **adds** debt/preferred/minority.
Related: [[Residual_Income]]

### 2026-06-04 — P/CF: which "cash flow" and a worked calc
**Q:** What cash-flow definitions feed P/CF, and how do you compute the basic P/CF?
**A:** Four definitions: (1) **CF** = EPS + per-share depreciation/amortization/depletion (the default
"P/CF"), (2) **CFO**, (3) **FCFE** (= CFO − FCInv + net borrowing; strongest theory link but volatile/often
negative), (4) **EBITDA** (firm-level, so used in **EV**/EBITDA). Worked (curriculum Philips example): EPS
€1.41 + per-share D&A €1.17 = **CF €2.58**; price €36.31 → `P/CF = 36.31/2.58 = 14.1`. Why P/CF over P/E:
cash flow is harder to manipulate and steadier; trap — the simple CF definition **ignores working-capital
changes and non-cash revenue**, so aggressive revenue recognition isn't caught.
Related: [[Free_Cash_Flow_Valuation]]

### 2026-06-04 — Justified dividend yield and the dividend rate
**Q:** What is the justified dividend yield, and how is a trailing dividend yield computed?
**A:** From Gordon: `D0/P0 = (r − g)/(1 + g)` — the justified (leading) dividend yield. **Trailing dividend
yield** = the *dividend rate* (annualized most recent dividend; for quarterly payers, 4 × latest quarterly
dividend) ÷ current price. Dividend yield is reported as a **yield** (not P/D) because non-payers give D/P
= 0 while P/D is undefined. Rationale: it is part of total return and a lower-risk part; drawback: it is
only **one** return component and ignores the **dividend displacement of earnings** (higher dividends now
can reduce future growth).
Related: [[Dividend_Discount_Models]]
