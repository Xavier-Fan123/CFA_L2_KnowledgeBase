---
aliases: [Exchange-Traded Funds, ETFs, Creation Redemption, Authorized Participants, Tracking Error, Premium Discount to NAV]
tags: [CFA-L2, pm, concept, etf]
date: 2026-08-25
status: evergreen
source: Schweser Book 5, Module 36, LOS 36.a-36.h
---

# Exchange-Traded Funds (ETFs)

## Creation / Redemption (36.a)
- **Authorized participants (APs)** — large institutions — create ETF shares by delivering the **creation basket** of securities **in-kind** to the issuer, and redeem by tendering ETF shares for the **redemption basket**. These **primary-market** transactions are in-kind and carry a **service fee payable to the ETF issuer**, which **shields non-transacting shareholders** from the costs and tax consequences of creation/redemption — the structural reason ETFs are more tax-efficient than mutual funds.
- This **arbitrage mechanism** keeps the ETF price close to NAV: if price > NAV, APs create and sell; if price < NAV, APs buy and redeem.

## Trading & Markets (36.b)
- **Primary market**: AP ↔ issuer (creation/redemption). **Secondary market**: investors trade existing shares on exchange — most volume; provides liquidity without affecting the underlying.

## Tracking Difference vs Tracking Error (36.c)
Two different things — the exam separates them:
- **Tracking difference** = fund return − index return over a period (a **level**: how far behind, and in which direction).
- **Tracking error** = the **annualized standard deviation of the DAILY tracking differences** (a **volatility**: how consistent the gap is). A fund can have a large tracking difference with tiny tracking error (a steady drag from fees) or the reverse.

**Curriculum sources of tracking error**: (1) **fees and expenses** of the fund (the single most persistent source); (2) **sampling and optimization** instead of full replication; (3) holding **depository receipts (DRs)** rather than the underlying local shares; (4) **changes in the index** (rebalancing/reconstitution); (5) **regulatory and tax requirements**; (6) **fund accounting practices**; (7) **asset manager operations** (securities lending revenue, dividend reinvestment timing, currency hedging, cash drag).

## Bid-Ask Spread & Premium/Discount (36.d, 36.e)
- **Spread** drivers: liquidity and spread of the **underlying**, creation/redemption costs, competition among market makers, hedging cost/risk. Wider for less-liquid/foreign underlyings.
- **Premium/discount to NAV**: `ETF premium (discount) % = (ETF price − NAV) / NAV`. Two curriculum sources: **timing differences** for ETFs holding foreign securities that trade in a **different time zone** (the NAV is stale while the ETF keeps trading), and **stale pricing** for **infrequently traded** ETFs. Supply/demand imbalances and illiquid underlyings add to it; persistent large gaps signal frictions in the arbitrage.
- **iNAV (indicated NAV)**: exchanges publish **intraday indicated NAVs** — fair-value estimates of the basket during the trading day — so the premium/discount can be judged without waiting for the closing NAV. Counterintuitive curriculum point: **the ETF price can be MORE informative than NAV or iNAV** when (1) the market for the underlying is **closed**, (2) the underlying securities are **highly volatile or illiquid**, or (3) there is a **time lag** between the pricing of the ETF and of the underlying. When the ETF and its underlying trade on the **same exchange**, closing prices are contemporaneous and timing noise disappears.
- **Spread drivers (36.d)** — ETF spreads are **positively** related to the **cost of creation/redemption**, the **spread on the underlying securities**, the **risk premium for carrying the position until the trade closes**, and the AP's **normal profit margin**; they are **negatively** related to the **probability of completing an offsetting trade in the secondary market** (i.e., more secondary liquidity → tighter spreads).

## Costs & Risks (36.f, 36.g)
- **Total cost of ownership** = expense ratio + trading costs (commissions, bid-ask) + premium/discount + tracking error. Holding period matters: **short-term investors focus on trading costs; long-term buy-and-hold investors focus on management fees**.
- **ETF liquidity metric (36.f)**: judge trading cost by the ratio of **average dollar volume to average assets** — **higher is better**. Note that an ETF's true liquidity also rests on the **underlying** basket, not just its own screen volume.
- **Three risks of investing in ETFs (36.g)**:
  1. **Counterparty risk** — acute for **ETNs** (unsecured debt of the issuer) and swap-based/synthetic ETFs.
  2. **Fund closures** — a sub-scale ETF can be liquidated, forcing an unwanted taxable exit and reinvestment. Causes include regulatory change, competition, and corporate actions.
  3. **Expectation-related risk** — the investor misunderstands what the product actually does (e.g., **leveraged and inverse ETFs reset daily**, so multi-period returns diverge from the stated multiple of the index; commodity ETFs deliver **roll** rather than spot returns).

## Portfolio Uses (36.h)
The curriculum groups them into **three** buckets — answer in this structure:

| Bucket | Uses |
|---|---|
| **1. Efficient portfolio management** | **Liquidity management** (cash equitization), **portfolio rebalancing**, **portfolio completion** (filling a missing exposure), **transition management** (bridging between managers) |
| **2. Asset class exposure management** | **Core exposure** to an asset class or sub-asset class, plus **tactical** strategies |
| **3. Active investing** | **Smart beta / alternatively weighted** ETFs, **risk management**, **discretionary active** ETFs, **dynamic asset allocation** |

## Exam Traps
- The **AP in-kind creation/redemption arbitrage** keeps price ≈ NAV and drives tax efficiency.
- **ETNs carry issuer counterparty (credit) risk** (unsecured debt), unlike physically-backed ETFs.
- Premiums/discounts often reflect **stale NAV** (closed underlying markets), not mispricing.
- Total cost of ownership ≠ just the expense ratio — include spreads, premium/discount, tracking error. **Short-term traders optimize spreads; long-term holders optimize the management fee.**
- **Tracking DIFFERENCE is a level; tracking ERROR is the annualized SD of daily tracking differences.** A steady fee drag gives a big difference with a small error.
- The three named ETF risks are **counterparty, fund closure, and expectation-related** risk — the third one covers daily-reset leveraged/inverse products.
- Portfolio uses come in **three** curriculum buckets: **efficient portfolio management**, **asset class exposure management**, **active investing**.

## Q&A

### 2026-06-03 — How does creation/redemption keep ETF price ≈ NAV (and cut taxes)?
**Q:** Explain the AP arbitrage and why ETFs are tax-efficient.
**A:** **Authorized participants** can swap the **creation basket** of securities for ETF shares (and back) **in-kind** with the issuer. If the ETF trades **above** NAV, APs create new shares (deliver basket, sell shares) → supply up, price down; if **below** NAV, they redeem (buy cheap shares, return basket) → price up. This arbitrage anchors price to NAV. Because redemptions are **in-kind** (hand over low-basis securities rather than selling them), the fund rarely realizes capital gains → **tax efficiency** vs mutual funds.
Related: [[Backtesting_and_Simulation]]

### 2026-06-03 — Premiums/discounts and ETN counterparty risk
**Q:** Why might an ETF trade at a premium/discount to NAV, and how do ETNs differ in risk?
**A:** Premiums/discounts arise mainly from **stale NAV** (e.g., foreign underlying markets are closed so the NAV is hours old while the ETF still trades), plus supply/demand imbalances and illiquid underlyings; persistent large gaps signal arbitrage frictions. **ETNs** are **unsecured debt** of the issuer, so they carry **issuer counterparty (credit) risk** — unlike physically-backed ETFs that hold the securities. Total cost of ownership = expense ratio + spreads + premium/discount + tracking error, not just the TER.
Related: [[Backtesting_and_Simulation]]
