---
aliases: [Dividends and Share Repurchases, Dividend Policy, Buybacks, Dividend Theories, Payout Policy]
tags: [CFA-L2, corp, concept]
date: 2026-08-25
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
- **Agency (13.d) — two distinct conflicts**:
  1. **Shareholders vs managers**: paying out a higher proportion of FCFE **reduces** the cash managers could sink into **negative-NPV** projects (empire building) — so a higher payout is a governance tool.
  2. **Shareholders vs bondholders**: shareholders can **expropriate bondholder wealth** by voting themselves a large dividend, shrinking the asset base that collateralizes the debt. This conflict is normally resolved **contractually — through covenants in the bond indenture** (dividend restrictions, minimum coverage/net-worth tests), not by dividend policy itself.

## Six Factors Affecting Payout Policy (13.e)
The curriculum lists exactly six. Vignettes give you a fact pattern and ask which way payout should move.

| Factor | Effect on payout |
|---|---|
| **1. Investment opportunities** | More positive-NPV projects → less residual cash → **lower** payout |
| **2. Expected volatility of future earnings** | Volatile earnings → managers change dividends **cautiously** (reluctant to raise a dividend they may have to cut) |
| **3. Financial flexibility** | Firms avoid raising the dividend even with ample FCF, because dividends are **sticky**; they pay out via **repurchases** instead to keep flexibility |
| **4. Tax considerations** | Where capital gains are taxed more favorably than dividends, structure payout to maximize investors' **after-tax** income |
| **5. Flotation costs** | External equity costs more than retained earnings, so **high flotation costs → lower payout** (retain instead of paying out and re-issuing) |
| **6. Contractual and legal restrictions** | **Debt covenants** and jurisdictional rules (e.g., impairment-of-capital rules) can cap dividends outright |

## Global Payout Trends (13.h)
- The **proportion of companies paying cash dividends has trended downwards globally**.
- **Share repurchases have trended upwards** — in the **US since the 1980s**, and in the **UK and continental Europe since the 1990s**.
- Direction of travel: cash dividends give way to buybacks, consistent with the flexibility and tax rationales above.

## Dividend Tax Systems (13.f)
- **Double taxation**: taxed at corporate level, then again at investor level. Effective rate = `corporate rate + (1 − corporate rate) × dividend tax rate`.
- **Dividend imputation**: shareholder receives credit for taxes paid by the firm → effectively taxed once at the investor's rate.
- **Split-rate**: lower corporate tax on distributed than retained earnings.

## Stable vs Constant Payout (13.g)
- **Stable dividend** policy (most common): smooth dividends, grow gradually toward a long-run target; **target payout adjustment model**: `expected ΔDividend = (expected EPS × target payout − previous dividend) × adjustment factor`.
- **Constant payout ratio**: dividend is a fixed % of earnings → volatile dividends.

## Share Repurchases (13.i-13.l)
- **Four repurchase methods (13.i)** — know the mechanics, not just the names:

| Method | Mechanics |
|---|---|
| **Open-market transactions** | The firm simply buys its own shares in the market. Most common; most **flexible** (no obligation to complete) |
| **Fixed-price tender offer** | Firm offers to buy a **preset number of shares at one fixed price**, usually at a **premium** to market, within a set window |
| **Dutch auction** | A tender offer that names a **range of prices**. Shareholders bid; the firm accepts bids **lowest price first** until the desired quantity is filled, then pays **every accepted bid the same (highest accepted) price** |
| **Direct negotiation** | Buying a block from a **major shareholder**, often at a premium — used to clear a **market overhang**, or in a **greenmail** situation (paying off a hostile accumulator) |

- **EPS effect** of a buyback: if **earnings yield (E/P) > after-tax cost of funds** used → EPS **increases**; if E/P < after-tax cost → EPS **falls**. (Cash-financed: compare E/P to after-tax return forgone on cash.)
- **Worked example (Schweser – JetFun):** 10m shares, NI $50m, EPS $5; buy back 2m shares at a 25% premium over $40 = **$50/share** ($100m).
  - **Surplus cash**: 8m shares left → EPS = `50/8 = $6.25` (**+25%**).
  - **New debt** at 3% after-tax: cost = `3% × $100m = $3m` → NI $47m → EPS = `47/8 = $5.875` (**+17.5%**).
  - Earnings yield = `5/50 = 10% > 3%` after-tax cost → **accretive in both cases**. (But leverage rises, so higher EPS ≠ automatically higher share price.)
- **BVPS effect**: if repurchase price **> BVPS** → BVPS **falls**; if price **< BVPS** → BVPS rises.
- **Five rationales for repurchasing rather than paying a dividend (13.l)**: (1) potential **tax advantage** when capital gains are taxed more favorably; (2) **share-price support / signaling** of management confidence; (3) **added flexibility** — avoids committing to a "sticky" future dividend; (4) **offsets dilution** from employee stock options; (5) **increases financial leverage** by reducing balance-sheet equity. Buybacks are equivalent to dividends **only** under no-tax, full-information assumptions.

## Coverage / Sustainability (13.m, 13.n)
- **Dividend coverage** = net income / dividends; **FCFE coverage** = FCFE / (dividends + buybacks).
- Low coverage, high payout, declining FCFE, and high leverage flag an **unsustainable** dividend.

## Exam Traps
- Buyback EPS test: compare **E/P (earnings yield)** to the **after-tax cost** of the funds — above → accretive, below → dilutive.
- BVPS rises only if shares are repurchased **below** book value per share.
- Dividend **cuts** carry the strongest negative signal; cash dividends raise D/E and cut liquidity.
- **13.e list of six** — investment opportunities, earnings volatility, financial flexibility, taxes, **flotation costs**, contractual/legal restrictions. Flotation costs push payout **down**, not up.
- **Dutch auction**: bids filled **lowest-first**, but everyone accepted is paid the **single highest accepted price** — not their own bid.
- **Agency runs two ways**: higher payout fixes the shareholder-manager conflict but **worsens** the shareholder-bondholder conflict; the latter is controlled by **indenture covenants**.
- Global trend: **fewer** dividend payers, **more** repurchases (US since the 1980s; UK/Europe since the 1990s).

## Q&A

### 2026-06-03 — Is a buyback accretive or dilutive to EPS?
**Q:** What determines whether a share repurchase raises or lowers EPS?
**A:** Compare the **earnings yield E/P** (= EPS ÷ repurchase price) to the **after-tax cost of the funds** used. If E/P > after-tax cost → **accretive** (EPS rises); if E/P < after-tax cost → **dilutive**. For surplus cash, the "cost" is the after-tax return forgone on that cash; for debt-financed buybacks, it's the after-tax interest rate. Caveat: accretion ≠ value creation — leverage rises, so a higher EPS does not automatically mean a higher share price. (JetFun: E/P = 10% > 3% after-tax cost → accretive both ways.)
Related: [[Corporate_Restructurings]]

### 2026-06-03 — Effective tax rate under double taxation
**Q:** Corporate tax 30%, dividend tax 20%. What's the effective tax on a dividend under double taxation?
**A:** `Effective rate = corporate rate + (1 − corporate rate) × dividend tax rate = 0.30 + 0.70×0.20 = 0.44 = 44%`. The profit is taxed once at the corporate level, then the after-corporate-tax distribution is taxed again at the investor level. Contrast: **imputation** systems give the shareholder a credit for corporate tax (taxed once, at the investor's rate); **split-rate** systems tax distributed earnings at a lower corporate rate than retained earnings.
Related: [[Equity_Investments_Overview]]
