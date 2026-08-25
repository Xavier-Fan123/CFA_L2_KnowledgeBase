---
aliases: [Commodities, Commodity Futures, Contango, Backwardation, Roll Return, Theories of Futures Returns, Commodity Swaps]
tags: [CFA-L2, alt, concept, commodities]
date: 2026-08-25
status: evergreen
source: Schweser Book 4, Module 30, LOS 30.a-30.j
---

# Commodities and Commodity Derivatives

## Sectors & Life Cycle (30.a, 30.b)
- Sectors: **energy, base/industrial metals, precious metals, agriculture (grains, softs), livestock**. Each has distinct seasonality, storability, and supply/demand cycles.
- Life cycle from production → storage/transport → consumption affects price behavior and the futures curve (e.g., harvest cycles, refinery turnarounds).

## Valuation vs Equities/Bonds (30.c, 30.d)
- Commodities generate **no cash flows** → cannot be valued by DCF. "Value" comes from supply/demand, storage economics, and **convenience yield** (benefit of holding the physical).
- Participants: **hedgers** (producers/consumers), **speculators/traders** (provide liquidity, take risk), **arbitrageurs**.

## Contango vs Backwardation (30.e)
- **Contango**: futures price **> spot** (upward curve) — typical when storage costs dominate, ample supply. In contango the **basis and calendar spread are negative** → **negative** roll return.
- **Backwardation**: futures price **< spot** (downward curve) — typical with high convenience yield / tight supply. Basis and calendar spread are **positive** → **positive** roll return (futures rise to meet spot as they converge).

## Theories of Futures Returns (30.f)

The curriculum names **three** distinct theories — keep them separate, because a vignette will name one:

| Theory | Claim | Implication for curve shape |
|---|---|---|
| **Insurance theory** (Keynes, normal backwardation) | Futures returns **compensate the buyer for providing price-risk insurance to the producer**, who is the natural **short** hedger | **Backwardation is the normal condition**; the long speculator earns the risk premium |
| **Hedging pressure hypothesis** | Extends insurance theory by admitting **long hedgers** (consumers) as well as short hedgers | **Short hedgers dominate → backwardation**; **long hedgers dominate → contango** |
| **Theory of storage** | Spot and futures are linked through **storage costs** and **convenience yield** | High storage cost / ample supply → **contango**; high convenience yield / tight supply → **backwardation** |

- Trap: insurance theory says backwardation is *normal*; only the **hedging pressure hypothesis** can produce **contango** from hedger behaviour (when consumers dominate the hedging). The theory of storage is the only one that is a **cost** argument rather than a **risk-premium** argument.

## Total Return Components (30.g, 30.h)
`Total return = spot (price) return + roll return + collateral return`.
- **Price (spot) return** = change in the price of the futures contract held.
- **Roll return**: gain/loss from rolling expiring futures to the next contract. **Accounting** figure only — you cannot build a portfolio of "pure roll return." Official formula: `Roll return = [(Near-term price − Farther-term price) / Near-term price] × % of position rolled`
  - **Backwardation → positive roll return** (near > far; roll into **cheaper** deferred contracts → buy **more** contracts to hold the same dollar exposure).
  - **Contango → negative roll return** (near < far; roll into **more expensive** contracts → buy **fewer**).
  - *Worked (official WTI, S&P GSCI 5-day roll = 20%/day):* March $52.64, April $53.00 → (52.64 − 53.00)/52.64 = −0.68% gross × 20% = **−0.13% net roll return** (negative, in contango).
- **Collateral return**: interest (≈ risk-free rate) on the cash backing a fully collateralized position.
- **Worked total return (official Example 18):** price 5% + roll 2.5% + collateral (2% × 100%) = **9.5%**.

## Swaps & Indexes (30.i, 30.j)
- **Commodity swaps** modify exposure without holding physicals:
  - **Total-return swap** — pay/receive the total return of a commodity (or index) vs a fixed/floating rate.
  - **Excess-return swap** — exchanges the **price (excess) return** only (no collateral leg).
  - **Basis swap** — exchanges cash flows based on the difference between two related prices/indexes.
  - **Variance / volatility swap** — payoff tied to realized **variance / volatility** of the commodity.
- **Index construction** drives returns via three levers: **weighting** scheme, **roll** methodology/timing, and **rebalancing** frequency.
  - **Five major indexes:** **S&P GSCI** (24 commodities, world-production value weighting → energy-heavy, up to ~80%); **BCOM / Bloomberg Commodity** (23 commodities, liquidity-weighted + committee, capped to diversify); **DBLCI** (fixed weights, distinctive **optimized roll**); **TR/CC CRB** (fixed, committee, **monthly** rebalance); **RICI** (38 commodities, fixed, committee, **monthly** rebalance).
  - **Weighting:** production/value-weighted (floating) drifts with prices → **smaller rebalancing trades**; **fixed-weight** forces larger buy-low/sell-high rebalancing.
  - **Rebalancing:** **frequent (monthly)** rebalancing helps in **mean-reverting** markets (sell peaks/buy valleys) but **hurts in trending** markets; annual rebalancing favors persistent trends.
  - **Roll methodology** matters most where roll cost is large (e.g., **natural gas** ~19% annual roll cost — its higher weight in BCOM is a drag the index must overcome with price/rebalance return).

## Commodity Trading Extension (Beyond Curriculum)
This section is a professional trading application, not CFA curriculum text.

- A commodity desk usually separates **outright price risk**, **calendar-spread risk**, and **basis risk**. A long physical cargo hedged with exchange futures may be flat in outright price but still exposed to grade, location, timing, freight, and pricing-index differences.
- **Contango** is not automatically a bearish forecast. It often reflects financing, storage, insurance, quality-loss, and logistics costs. A merchant with available tankage or warehouse capacity can monetize a cash-and-carry only if the spread exceeds the full carry cost and the physical leg is executable.
- **Backwardation** often signals scarce prompt supply and high convenience yield. The economic value may sit in inventory optionality: being able to deliver or consume prompt barrels/tons when paper markets cannot create physical availability.
- Persistent contango hurts a long-only futures investor through negative roll return, but it can still be attractive for a physical trader with cheap storage and funding. The same curve shape can be bad for an index investor and useful for a merchant balance sheet.
- Do not read the futures curve as a pure forecast. It mixes no-arbitrage carry, inventory scarcity, hedging pressure, funding constraints, and risk premia.

## Exam Traps
- **Backwardation → positive roll return; contango → negative roll return.** In backwardation you buy **more** (cheaper) deferred contracts to keep dollar exposure; in contango you buy **fewer**.
- Commodities have **no cash flows** → no DCF; convenience yield is central.
- Keynes's **normal backwardation**: speculators earn a risk premium for bearing producers' price risk.
- Total return = spot + **roll** + collateral; roll return = (near − far)/near × % rolled (an **accounting** figure — cannot be isolated into a tradable portfolio).
- Index returns hinge on **weighting + roll + rebalancing**: floating/production weights → small rebalancing trades; **frequent rebalancing helps mean-reverting, hurts trending** markets.

## Q&A

### 2026-06-03 — Roll return in contango vs backwardation
**Q:** A fully collateralized long futures position rolls monthly. How does the curve shape drive the roll return?
**A:** `Total return = spot return + roll return + collateral return`. In **backwardation** (futures < spot, downward curve) you sell the expiring contract and buy a **cheaper** deferred one, and as it converges up to spot you earn a **positive roll return**. In **contango** (futures > spot) you roll into a **more expensive** contract → **negative roll return** (a persistent drag, e.g., commodity ETFs in contango). Mnemonic: **backwardation = positive roll, contango = negative roll**.
Related: [[Real_Estate]]

### 2026-06-03 — Theories of futures returns
**Q:** What does "normal backwardation" claim, and how does the theory of storage explain curve shape?
**A:** **Keynes's normal backwardation (insurance/hedging-pressure):** producers hedge by **selling** futures, so speculators who take the long side demand a **risk premium** → futures price sits **below** the expected future spot (backwardation), and speculators earn that premium. **Theory of storage:** the futures-spot gap reflects **storage costs minus convenience yield** — high convenience yield (tight supply, valuable to hold physical) pushes the market into **backwardation**; abundant supply / high storage cost → **contango**.
Related: [[Hedge_Fund_Strategies]]

### 2026-06-04 — How does commodity index construction affect returns?
**Q:** Which design choices make two commodity indexes (e.g., S&P GSCI vs BCOM) perform differently?
**A:** Three levers: **weighting**, **roll methodology**, and **rebalancing frequency**. **Weighting:** the S&P GSCI uses **world-production value** weighting → very energy-heavy (up to ~80%), while **BCOM** caps weights for diversification (energy ~30%, but more natural gas). Because natural gas has a huge (~19%) annual **roll cost** in contango, an index overweight it must overcome that drag with price and rebalance return. **Roll methodology** (which contracts, over how many days) sets the roll return — DBLCI uses an optimized roll. **Rebalancing:** monthly rebalancers (TR/CC CRB, RICI) buy-low/sell-high and win in **mean-reverting** markets but **lag in trending** markets; annual rebalancers favor persistent trends. Floating (production) weights drift with prices, so they need **smaller** rebalancing trades than fixed-weight schemes.
Related: [[Alternative_Investments_Overview]]
