---
aliases: [Exchange-Traded Funds, ETFs, Creation Redemption, Authorized Participants, Tracking Error, Premium Discount to NAV]
tags: [CFA-L2, pm, concept, etf]
date: 2026-06-03
status: evergreen
source: Schweser Book 5, Module 36, LOS 36.a-36.h
---

# Exchange-Traded Funds (ETFs)

## Creation / Redemption (36.a)
- **Authorized participants (APs)** — large institutions — create ETF shares by delivering the **creation basket** of securities **in-kind** to the issuer, and redeem by returning ETF shares for the basket. Usually **in-kind** (no cash) → tax-efficient (few realized gains).
- This **arbitrage mechanism** keeps the ETF price close to NAV: if price > NAV, APs create and sell; if price < NAV, APs buy and redeem.

## Trading & Markets (36.b)
- **Primary market**: AP ↔ issuer (creation/redemption). **Secondary market**: investors trade existing shares on exchange — most volume; provides liquidity without affecting the underlying.

## Tracking Error (36.c)
Sources: **fees/expenses**, **sampling/optimization** (not full replication), **cash drag**, index **rebalancing/reconstitution**, dividend reinvestment timing, withholding taxes, currency hedging.

## Bid-Ask Spread & Premium/Discount (36.d, 36.e)
- **Spread** drivers: liquidity and spread of the **underlying**, creation/redemption costs, competition among market makers, hedging cost/risk. Wider for less-liquid/foreign underlyings.
- **Premium/discount to NAV**: arises from **stale NAV** (e.g., foreign markets closed), supply/demand imbalances, and underlying liquidity. Persistent large premiums/discounts signal frictions in arbitrage.

## Costs & Risks (36.f, 36.g)
- **Total cost of ownership** = expense ratio + trading costs (commissions, bid-ask) + premium/discount + tracking error. Holding period matters: long holders care about TER; short-term traders about spreads.
- **Risks**: counterparty risk (esp. **ETNs** = unsecured debt; synthetic/swap-based ETFs), settlement, fund closure, security-lending, and underlying market risk.

## Portfolio Uses (36.h)
Core-satellite exposure, tactical tilts, cash equitization, rebalancing, liquidity sleeve, thematic/factor exposure, tax-loss harvesting, hedging.

## Exam Traps
- The **AP in-kind creation/redemption arbitrage** keeps price ≈ NAV and drives tax efficiency.
- **ETNs carry issuer counterparty (credit) risk** (unsecured debt), unlike physically-backed ETFs.
- Premiums/discounts often reflect **stale NAV** (closed underlying markets), not mispricing.
- Total cost of ownership ≠ just the expense ratio — include spreads, premium/discount, tracking error.

## Q&A

### 2026-06-03 — How does creation/redemption keep ETF price ≈ NAV (and cut taxes)?
**Q:** Explain the AP arbitrage and why ETFs are tax-efficient.
**A:** **Authorized participants** can swap the **creation basket** of securities for ETF shares (and back) **in-kind** with the issuer. If the ETF trades **above** NAV, APs create new shares (deliver basket, sell shares) → supply up, price down; if **below** NAV, they redeem (buy cheap shares, return basket) → price up. This arbitrage anchors price to NAV. Because redemptions are **in-kind** (hand over low-basis securities rather than selling them), the fund rarely realizes capital gains → **tax efficiency** vs mutual funds.
Related: [[Backtesting_and_Simulation]]

### 2026-06-03 — Premiums/discounts and ETN counterparty risk
**Q:** Why might an ETF trade at a premium/discount to NAV, and how do ETNs differ in risk?
**A:** Premiums/discounts arise mainly from **stale NAV** (e.g., foreign underlying markets are closed so the NAV is hours old while the ETF still trades), plus supply/demand imbalances and illiquid underlyings; persistent large gaps signal arbitrage frictions. **ETNs** are **unsecured debt** of the issuer, so they carry **issuer counterparty (credit) risk** — unlike physically-backed ETFs that hold the securities. Total cost of ownership = expense ratio + spreads + premium/discount + tracking error, not just the TER.
Related: [[Backtesting_and_Simulation]]
