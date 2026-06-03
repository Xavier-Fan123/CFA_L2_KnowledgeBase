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

## Enterprise Value Multiples (20.n-20.p)
- **EV** = market cap + total debt + preferred + minority interest − cash & equivalents.
- **EV/EBITDA**: numerator (total firm value) matches a pre-financing flow (EBITDA) → good for comparing
  firms with **different capital structures** and for capital-intensive firms.
- EV/Sales useful when earnings are negative or capital structures differ.

## Momentum & Averaging (20.q, 20.r)
- **Momentum indicators**: earnings surprise (standardized unexpected earnings), relative strength.
- Averaging multiples across a group: use the **harmonic mean** (or weighted harmonic mean) — the
  arithmetic mean **overweights high outliers** and overstates the group multiple.

## Exam Traps
- **EV subtracts cash** and adds debt/preferred/minority — a common error.
- **EV/EBITDA** is preferred when capital structures differ (P/E is distorted by leverage).
- Use the **harmonic mean** to average P/Es across firms, not the arithmetic mean.
- Justified P/B = `(ROE − g)/(r − g)`; P/B > 1 when ROE > r.

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
