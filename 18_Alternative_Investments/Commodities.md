---
aliases: [Commodities, Commodity Futures, Contango, Backwardation, Roll Return, Theories of Futures Returns, Commodity Swaps]
tags: [CFA-L2, alt, concept, commodities]
date: 2026-06-03
status: evergreen
source: Schweser Book 4, Module 30, LOS 30.a-30.j
---

# Commodities and Commodity Derivatives

## Sectors & Life Cycle (30.a, 30.b)
- Sectors: **energy, base/industrial metals, precious metals, agriculture (grains, softs), livestock**.
  Each has distinct seasonality, storability, and supply/demand cycles.
- Life cycle from production → storage/transport → consumption affects price behavior and the futures
  curve (e.g., harvest cycles, refinery turnarounds).

## Valuation vs Equities/Bonds (30.c, 30.d)
- Commodities generate **no cash flows** → cannot be valued by DCF. "Value" comes from supply/demand,
  storage economics, and **convenience yield** (benefit of holding the physical).
- Participants: **hedgers** (producers/consumers), **speculators/traders** (provide liquidity, take
  risk), **arbitrageurs**.

## Contango vs Backwardation (30.e)
- **Contango**: futures price **> spot** (upward curve) — typical when storage costs dominate, ample
  supply. In contango the **basis and calendar spread are negative** → **negative** roll return.
- **Backwardation**: futures price **< spot** (downward curve) — typical with high convenience yield /
  tight supply. Basis and calendar spread are **positive** → **positive** roll return (futures rise to
  meet spot as they converge).

## Theories of Futures Returns (30.f)
| Theory | Idea |
|------|------|
| **Insurance / hedging pressure (Keynes – normal backwardation)** | Producers hedge by selling futures; speculators require a risk premium → futures below expected spot → backwardation |
| **Theory of storage** | Futures-spot relationship set by storage costs vs **convenience yield**; high convenience yield → backwardation |
| **Hedging pressure hypothesis** | Net hedging position (producers short vs consumers long) determines whether the curve is in contango or backwardation |

## Total Return Components (30.g, 30.h)
`Total return = spot (price) return + roll return + collateral return`.
- **Roll return**: gain/loss from rolling expiring futures to the next contract.
  - **Backwardation → positive roll return** (roll down to cheaper deferred contracts).
  - **Contango → negative roll return** (roll up to more expensive contracts).
- **Collateral return**: interest on the cash backing a fully collateralized futures position.

## Swaps & Indexes (30.i, 30.j)
- **Commodity swaps**: exchange exposure (e.g., total-return swap, basis swap, variance swap) to gain or
  modify commodity exposure without holding physicals.
- **Index construction** drives returns: **weighting** scheme (production-weighted vs fixed), the
  **roll** methodology and timing, and **rebalancing** frequency materially affect index performance.

## Exam Traps
- **Backwardation → positive roll return; contango → negative roll return.**
- Commodities have **no cash flows** → no DCF; convenience yield is central.
- Keynes's **normal backwardation**: speculators earn a risk premium for bearing producers' price risk.
- Total return = spot + **roll** + collateral.

## Q&A

### 2026-06-03 — Roll return in contango vs backwardation
**Q:** A fully collateralized long futures position rolls monthly. How does the curve shape drive the roll return?
**A:** `Total return = spot return + roll return + collateral return`. In **backwardation** (futures <
spot, downward curve) you sell the expiring contract and buy a **cheaper** deferred one, and as it
converges up to spot you earn a **positive roll return**. In **contango** (futures > spot) you roll into
a **more expensive** contract → **negative roll return** (a persistent drag, e.g., commodity ETFs in
contango). Mnemonic: **backwardation = positive roll, contango = negative roll**.
Related: [[Real_Estate]]

### 2026-06-03 — Theories of futures returns
**Q:** What does "normal backwardation" claim, and how does the theory of storage explain curve shape?
**A:** **Keynes's normal backwardation (insurance/hedging-pressure):** producers hedge by **selling**
futures, so speculators who take the long side demand a **risk premium** → futures price sits **below**
the expected future spot (backwardation), and speculators earn that premium. **Theory of storage:** the
futures-spot gap reflects **storage costs minus convenience yield** — high convenience yield (tight
supply, valuable to hold physical) pushes the market into **backwardation**; abundant supply / high
storage cost → **contango**.
Related: [[Hedge_Fund_Strategies]]
