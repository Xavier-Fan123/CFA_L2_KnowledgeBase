---
aliases: [Economics and Investment Markets, Discount Rate Framework, Taylor Rule, Business Cycle and Markets, Credit Spreads, Equity Risk Premium]
tags: [CFA-L2, pm, concept, macro]
date: 2026-08-25
status: evergreen
source: Schweser Book 5, Module 34, LOS 34.a-34.k
---

# Economics and Investment Markets

## The Discount-Rate Framework (34.a, 34.b)
- Asset value = `PV of expected future cash flows`. To affect value, an economic factor must change one of: (1) **default-free interest rates** across maturities, (2) **timing/magnitude of expected cash flows**, or (3) the **risk premium**.
- **Expectations** drive prices; only the **unexpected** (surprise) part of news moves markets.

### The Inter-Temporal Rate of Substitution — the engine behind the whole reading (34.a, 34.b)
The reading builds every result from one idea: an investor decides between **consuming now** and **consuming later**.

- **Inter-temporal rate of substitution** = the **marginal utility of future consumption ÷ the marginal utility of current consumption**. It is how much future consumption an investor values relative to consumption today.
- **Diminishing marginal utility** makes it move: when future income is expected to be **high**, an extra unit of future consumption is worth **less** → the inter-temporal rate of substitution **falls** → investors **save less** → the **real interest rate rises** to clear the market.
- Hence **real rates are positively correlated with expected real GDP growth** (why fast-growing economies show high real rates), and also positively related to the **expected volatility** of that growth (a higher risk premium).
- **Risk premium = the covariance between an asset's future payoff and the investor's inter-temporal rate of substitution.**
  - **Risky assets (equities)**: the covariance is **negative** — payoffs are high exactly when incomes are high and the marginal utility of future consumption is low. A negative covariance lowers today's price (P₀), which **raises** expected return → a **positive risk premium**.
  - **Single-period risk-free bond**: terminal value is certain, so the covariance is **zero** → **no risk premium**.
- **Risk aversion**: the utility lost on a loss exceeds the utility gained on an equal-sized gain. **Absolute risk aversion declines with wealth** (richer investors accept more risk), but in **equilibrium** the marginal utility of holding more risky assets declines, so wealthy and poorer investors end up with the **same willingness to hold risky assets** at the margin.

## Real Rates & Growth (34.c)
- Average level of **real short-term rates** is tied to the economy's **long-term real growth rate** and the **volatility** of that growth. Higher trend growth → higher real rates; higher growth volatility → investors demand more → can lower the equilibrium rate (precautionary saving).
- Policy rates often described by a **Taylor rule**: `policy rate = neutral + inflation + 0.5(inflation gap) + 0.5(output gap)`.

## Business Cycle Effects (34.d, 34.f, 34.i, 34.j)
- **Term structure**: short rates rise into late expansion; the **yield curve flattens/inverts** late cycle and **steepens** in early recovery (policy easing).
- **Credit spreads**: **widen in contractions** (higher default risk), **tighten in expansions**. Credit-sensitive bonds underperform in downturns.
- **Equity earnings**: cyclical expectations swing earnings growth; **valuation multiples** compress in downturns and expand in recoveries (pro-cyclical).

## Inflation-Indexed Bonds (34.e)
- **Breakeven inflation rate** = nominal yield − real (TIPS) yield = expected inflation + an inflation risk premium. The spread between nominal and inflation-indexed bonds reflects inflation expectations and uncertainty.

## Equity Risk Premium & Consumption (34.h, 34.g)
- Equities pay off poorly in **bad times** (low consumption) → poor consumption hedge → investors demand a **positive equity risk premium**. Assets that hedge bad times (e.g., government bonds) command lower premiums.
- A company's **credit quality** depends on the cyclicality and stability of demand for its products.

## Commercial Real Estate (34.k)
- CRE combines **bond-like** (lease income) and **equity-like** (residual value, vacancy/cyclicality) characteristics; sensitive to growth, rates, and credit conditions.

## Exam Traps
- A factor affects markets only via **rates, cash flows, or the risk premium**; only **surprises** move prices.
- **Credit spreads widen in recessions, tighten in expansions**; yield curve flattens/inverts late cycle.
- **Breakeven inflation = nominal − real yield**.
- Equity risk premium exists because stocks are a **poor consumption hedge** (pay off badly in bad times) — formally, the **negative covariance between the payoff and the inter-temporal rate of substitution** is the risk premium.
- **Higher expected GDP growth → lower inter-temporal rate of substitution → less saving → HIGHER real rates.** The chain runs through diminishing marginal utility; getting the direction backwards is the classic error.
- A **single-period risk-free bond has zero covariance → zero risk premium**; the premium appears only once the terminal value is uncertain.

## Q&A

### 2026-06-03 — The discount-rate framework: how can an economic factor move asset prices?
**Q:** Through what channels does any piece of economic news affect asset values?
**A:** Value = PV of expected cash flows, so a factor matters only if it changes one of three things: (1) **default-free rates** across maturities (the discounting), (2) the **timing/magnitude of expected cash flows**, or (3) the **risk premium**. And only the **unexpected (surprise)** component moves prices — anything already expected is in the price. (Policy rates are often summarized by a **Taylor rule**: neutral + inflation + 0.5·inflation gap + 0.5·output gap.)
Related: [[Measuring_Managing_Market_Risk]]

### 2026-06-03 — Breakeven inflation and credit spreads over the cycle
**Q:** What does breakeven inflation measure, and how do credit spreads behave across the business cycle?
**A:** **Breakeven inflation = nominal yield − real (TIPS) yield = expected inflation + an inflation risk premium**, so the nominal-vs-indexed spread reflects both inflation expectations and uncertainty. **Credit spreads widen in contractions** (higher default probability, lower recovery) and **tighten in expansions**; the yield curve tends to **flatten/invert late cycle** and **steepen in early recovery**. Equities carry a positive risk premium because they pay off **poorly in bad times** (low consumption) — a poor consumption hedge.
Related: [[Multifactor_Models]]
