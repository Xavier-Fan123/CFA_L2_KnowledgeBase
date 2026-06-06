---
aliases: [Dividends and Share Repurchases, Dividend Policy, Buybacks, Dividend Theories, Payout Policy]
tags: [CFA-L2, corp, concept]
date: 2026-06-03
status: evergreen
source: Official Curriculum 2026 L2 V4, Reading "Analysis of Dividends and Share Repurchases" (Schweser Book 2, Module 13); LOS a-n
---

# Analysis of Dividends and Share Repurchases

## Effects on Wealth & Ratios (13.a)
- **Cash dividend**: assets and equity fall by the dividend; **liquidity ratios decline**, leverage (D/E) **rises**. Shareholder wealth unchanged (cash moves from firm to holder).
- **Stock dividend / stock split**: no change to total equity or wealth; lowers price proportionally, raises share count. Ratios per share change, but value does not.
- **Reverse split**: raises price, lowers share count; no wealth effect.

## Dividend Theories (13.b)

| Theory | Claim |
|------|------|
| **MM dividend irrelevance** | In perfect markets, payout policy does not affect value (homemade dividends) |
| **Bird-in-hand** | Investors prefer (less risky) dividends → higher payout raises value, lowers cost of equity |
| **Tax aversion** | If dividends taxed higher than capital gains, investors prefer low/no payout |

## Signaling, Clientele, Agency (13.c, 13.d, 13.e)
- **Signaling**: dividend **initiations/increases** signal confidence (positive); **cuts/omissions** signal trouble (strongly negative) — managers are reluctant to cut.
- **Clientele effect**: different investor groups prefer different payout levels (tax brackets, institutions).
- **Agency**: paying out free cash flow **reduces agency costs** of overinvestment.

## Dividend Tax Systems (13.f)
- **Double taxation**: taxed at corporate level, then again at investor level. Effective rate = `corporate rate + (1 − corporate rate) × dividend tax rate`.
- **Dividend imputation**: shareholder receives credit for taxes paid by the firm → effectively taxed once at the investor's rate.
- **Split-rate**: lower corporate tax on distributed than retained earnings.

## Stable vs Constant Payout (13.g)
- **Stable dividend** policy (most common): smooth dividends, grow gradually toward a long-run target; **target payout adjustment model**: `expected ΔDividend = (expected EPS × target payout − previous dividend) × adjustment factor`.
- **Constant payout ratio**: dividend is a fixed % of earnings → volatile dividends.

## Share Repurchases (13.i-13.l)
- Methods: **open-market**, **fixed-price tender offer**, **Dutch auction**, **direct negotiation**.
- **EPS effect** of a buyback: if **earnings yield (E/P) > after-tax cost of funds** used → EPS **increases**; if E/P < after-tax cost → EPS **falls**. (Cash-financed: compare E/P to after-tax return forgone on cash.)
- **Worked example (Schweser – JetFun):** 10m shares, NI $50m, EPS $5; buy back 2m shares at a 25% premium over $40 = **$50/share** ($100m).
  - **Surplus cash**: 8m shares left → EPS = `50/8 = $6.25` (**+25%**).
  - **New debt** at 3% after-tax: cost = `3% × $100m = $3m` → NI $47m → EPS = `47/8 = $5.875` (**+17.5%**).
  - Earnings yield = `5/50 = 10% > 3%` after-tax cost → **accretive in both cases**. (But leverage rises, so higher EPS ≠ automatically higher share price.)
- **BVPS effect**: if repurchase price **> BVPS** → BVPS **falls**; if price **< BVPS** → BVPS rises.
- Buybacks vs dividends: tax timing flexibility, signaling, offsetting option dilution, financial flexibility. Equivalent to dividends **only** under no-tax, full-information assumptions.

## Coverage / Sustainability (13.m, 13.n)
- **Dividend coverage** = net income / dividends; **FCFE coverage** = FCFE / (dividends + buybacks).
- Low coverage, high payout, declining FCFE, and high leverage flag an **unsustainable** dividend.

## Exam Traps
- Buyback EPS test: compare **E/P (earnings yield)** to the **after-tax cost** of the funds — above → accretive, below → dilutive.
- BVPS rises only if shares are repurchased **below** book value per share.
- Dividend **cuts** carry the strongest negative signal; cash dividends raise D/E and cut liquidity.

## Q&A

### 2026-06-03 — Is a buyback accretive or dilutive to EPS?
**Q:** What determines whether a share repurchase raises or lowers EPS?
**A:** Compare the **earnings yield E/P** (= EPS ÷ repurchase price) to the **after-tax cost of the funds** used. If E/P > after-tax cost → **accretive** (EPS rises); if E/P < after-tax cost → **dilutive**. For surplus cash, the "cost" is the after-tax return forgone on that cash; for debt-financed buybacks, it's the after-tax interest rate. Caveat: accretion ≠ value creation — leverage rises, so a higher EPS does not automatically mean a higher share price. (JetFun: E/P = 10% > 3% after-tax cost → accretive both ways.)
Related: [[Corporate_Restructurings]]

### 2026-06-03 — Effective tax rate under double taxation
**Q:** Corporate tax 30%, dividend tax 20%. What's the effective tax on a dividend under double taxation?
**A:** `Effective rate = corporate rate + (1 − corporate rate) × dividend tax rate = 0.30 + 0.70×0.20 = 0.44 = 44%`. The profit is taxed once at the corporate level, then the after-corporate-tax distribution is taxed again at the investor level. Contrast: **imputation** systems give the shareholder a credit for corporate tax (taxed once, at the investor's rate); **split-rate** systems tax distributed earnings at a lower corporate rate than retained earnings.
Related: [[Equity_Investments_Overview]]
