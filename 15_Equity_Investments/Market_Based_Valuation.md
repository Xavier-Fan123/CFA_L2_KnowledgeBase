---
aliases: [Market-Based Valuation, Price Multiples, EV/EBITDA, Justified Multiples, PEG, Method of Comparables]
tags: [CFA-L2, equity, concept, valuation]
date: 2026-08-25
status: evergreen
source: Schweser Book 3, Module 20, LOS 20.a-20.r
---

# Market-Based (Relative) Valuation

## Two Approaches (20.a, 20.b, 20.l, 20.m)
- **Method of comparables**: compare a stock's multiple to a benchmark (peers, industry, own history). "Law of one price" — similar assets should trade at similar multiples. Multiple **below** the benchmark → undervalued; **above** → overvalued (20.l).
- **But fundamentals decide (20.m)**: never read the comparison mechanically. A **high P/E can still be attractive** if growth is rapid, and a **high dividend yield can be unattractive** if earnings do not support the dividend and no growth is expected. Always ask whether the multiple gap is explained by differences in **growth, risk, and payout** — only the unexplained residual is mispricing.
- **Method based on forecasted fundamentals**: derive a **justified multiple** from a DCF/Gordon model.

## Justified Multiples (from fundamentals) (20.i)
All justified multiples share the form `[fundamental] / (r − g)` → **rise with g, fall with r**; they differ only in the anchoring fundamental.

| Multiple | Justified formula | **Anchor fundamental** | Value signal |
|----------|-------------------|------------------------|--------------|
| **Leading P/E** | `payout/(r−g)` = `(1−b)/(r−g)` | payout & g | — |
| **Trailing P/E** | `payout(1+g)/(r−g)` | payout & g | = Leading × (1+g) |
| **P/B** | `(ROE − g)/(r − g)` | **ROE** | **ROE > r ⟺ P/B > 1** |
| **P/S** | `net profit margin × payout × (1+g)/(r − g)` | **net profit margin** | high margin → high P/S |
| **P/CF** | ✗ no curriculum justified formula — comparables only | — | — |
| **Dividend yield** `D₀/P₀` | `(r − g)/(1 + g)` | inverse orientation | higher yield = cheaper |

- **P/B** derives from residual income: `P/B = 1 + (ROE−r)/(r−g) = (ROE−g)/(r−g)` → `ROE > r ⇒ P/B > 1`; `ROE = r ⇒ P/B = 1`. Ties to → [[Residual_Income]].
- **P/S** uses trailing sales S₀ (hence the `(1+g)`): from `P₀ = E₀(1+g)·payout/(r−g)` divide by S₀ and use `E₀/S₀ = net profit margin`.
- **P/E**: payout's effect on P/E is **ambiguous** — raising payout lifts the numerator but cuts retention b, lowering `g = b·ROE` (dividend displacement).
- **P/CF has no Gordon-derived justified formula** in the curriculum — it is a **method-of-comparables** multiple only (four CF definitions: CF, CFO, FCFE, EBITDA). *[My derivation, beyond curriculum: from the FCFE Gordon model `P₀ = FCFE₁/(r−g)`, leading `P/FCFE = 1/(r−g)`, trailing `P/FCFE = (1+g)/(r−g)` — same structure as P/E with payout = 1, which is why theory prefers P/FCFE; not curriculum text.]*

## Rationales and Drawbacks by Multiple (20.c)
The exam asks "why would an analyst prefer X here?" — these are list LOS.

| Multiple | Rationales | Drawbacks |
|---|---|---|
| **P/E** | EPS (earnings power) is the primary driver of investment value; **most widely used** in practice; P/E differences are significantly related to **long-run average returns** | Earnings can be **negative**; the **transitory/volatile** part of earnings makes interpretation hard; **management discretion** distorts reported earnings |
| **P/B** | Book value is usually **positive even when EPS is negative**; **more stable** than EPS; a good net-asset proxy for firms holding mostly **liquid assets** (banks, insurers, finance/investment firms); useful for firms **expected to go out of business**; explains long-run return differences | Ignores **non-physical (intangible) assets**; misleads across firms of very **different size**; **accounting conventions** obscure true shareholder investment; **inflation and technological change** drive book away from market value |
| **P/S** | Meaningful even for **distressed** firms; sales are **harder to manipulate** than EPS or book value; **less volatile** than P/E; suits **mature, cyclical, and start-up** firms with no earnings record; related to long-run returns | Higher sales ≠ higher **operating profit**; ignores **cost-structure** differences; **revenue-recognition** practices can still distort sales |
| **P/CF** | Cash flow is **harder to manipulate** than earnings; **more stable** than P/E; sidesteps earnings-quality differences; related to long-run returns | The "EPS + noncash charges" definition **ignores items that actually affect CFO**; **FCFE** is theoretically better but **more volatile** |
| **Dividend yield** | Dividends are a **component of total return**, and a **less risky** component than capital appreciation | Only **one** component of return; **dividend displacement** — higher dividends today mean slower growth, hurting the other component |

## Earnings Issues (20.e, 20.f)
- **Normalize EPS** for cyclical firms by (1) the **method of historical average EPS** or (2) the **method of average ROE** (average ROE × current book value per share). The curriculum **prefers the method of average ROE**, because it reflects the firm's current asset base rather than an EPS history from a different-sized company.
- **Underlying earnings** (a.k.a. core/persistent/continuing) = earnings with **non-recurring components removed**; **normalized earnings** = earnings adjusted for the **business cycle**. Different fixes for different problems.
- **Negative earnings** → P/E meaningless; use **earnings yield E/P** (high E/P = cheap) or normalized EPS.
- **Underlying/trailing earnings** strip out non-recurring items.

## PEG and Cross-Sectional P/E (20.h, 20.j)
- **PEG** = `(P/E) / g(%)`; lower PEG = relatively cheaper, but assumes a linear P/E-growth relation and ignores risk and differing growth durations.
- **Predicted P/E**: regress P/E on fundamentals (growth, payout, risk) cross-sectionally; limits — unstable out of sample, multicollinearity, time-period specific.

## Price/Cash Flow (P/CF) and Dividend Yield (20.c, 20.d)
Both are explicit curriculum multiples alongside P/E, P/B, P/S.

**Price/Cash Flow — four cash-flow definitions** (official LM4): the analyst must state *which* one.

| CF definition | How computed | Note |
|---|---|---|
| **CF** (earnings-plus-noncash-charges) | EPS + per-share Dep, Amort, Depletion | The default "P/CF"; simple but ignores WCInv and non-cash *revenue* |
| **CFO** | Cash flow from operations (statement of cash flows) | Adjust for non-persistent items; IFRS vs US GAAP interest/dividend classification differs |
| **FCFE** | CFO − FCInv + net borrowing | Strongest link to valuation theory; but more **volatile** / often **negative** |
| **EBITDA** | EBIT + Dep + Amort (a pre-interest, pre-tax operating-cash proxy) | Used in **EV/EBITDA**, not price/EBITDA (EBITDA is a firm-level, pre-debt flow) |

- Rationale for P/CF: cash flow is **harder to manipulate** and **more stable** than earnings, and sidesteps cross-firm differences in accounting conservatism.
- Drawback: the simple **CF** definition ignores working-capital changes and non-cash revenue (e.g., front-end-loaded revenue is not caught); theory actually prefers **P/FCFE**.

**Dividend yield (P/D inverted)** — `D/P`. Reported as a yield (not P/D) because many firms pay no dividend (then D/P = 0, but P/D is undefined).
- **Trailing dividend yield** = (annualized most-recent dividend, i.e. the *dividend rate*) / price.
- **Justified (leading) dividend yield (Gordon)**: `D0/P0 = (r − g)/(1 + g)`.
- Rationales: dividend yield is a **component of total return** and a **less risky** component than capital gains. Drawbacks: it is only **one** component of return (ignoring it elsewhere is suboptimal), and the **dividend displacement of earnings** means higher current dividends can trade off future growth.

## Enterprise Value Multiples (20.n, 20.o, 20.p)
- **EV** = market cap + total debt + preferred + minority interest − cash & equivalents (cash & short-term investments, a.k.a. *nonearning assets*, are subtracted because EV = net price an acquirer pays for the whole firm — the acquirer gains access to that cash).
- **EV/EBITDA advantages**: (1) numerator (total firm value) matches a pre-financing flow, so it is **useful across firms with different leverage**; (2) EBITDA suits **capital-intensive businesses with heavy depreciation**; (3) EBITDA is usually **positive even when EPS is not**.
- **EV/EBITDA disadvantages**: (1) when **working capital is growing, EBITDA overstates CFO** (it ignores WCInv entirely); (2) **FCFF is more strongly linked to valuation theory** than EBITDA.
- EV/Sales useful when earnings are negative or capital structures differ.

## International Comparables (20.p)
Cross-border relative valuation is harder because comparable firms differ in:
- **Accounting methods** (recognition, depreciation, inventory, lease and pension treatment) — multiples are not on a like-for-like basis.
- **Cultures** and business/reporting conventions.
- **Risk** (country, currency, political, and liquidity differences).
- **Growth opportunities** (different macro and industry stages).

Practical fix: restate to a common accounting basis where possible, and prefer multiples that are **less sensitive to accounting choice** (e.g., **EV/Sales**, **EV/EBITDA**) over P/E and P/B.

## Momentum & Averaging (20.q, 20.r)
- **Momentum indicators**: earnings surprise (standardized unexpected earnings = unexpected earnings ÷ std-dev of past surprises), relative strength.
- **Central tendency of a group of multiples** (4 measures in the LOS):
  - **Arithmetic mean** — biased **upward** by large outliers; overstates the group multiple.
  - **Median** — robust to outliers, but ignores magnitude.
  - **Harmonic mean** = `n / Σ(1/Xi)` (reciprocal of the arithmetic mean of the reciprocals) — the correct portfolio-equivalent average for price multiples; weights each stock by its yield.
  - **Weighted harmonic mean** = `1 / Σ(wi/Xi)` with portfolio value weights wi — matches a real cap-weighted portfolio's multiple. (Harmonic ≤ geometric ≤ arithmetic for positive values.)

## Exam Traps
- **EV subtracts cash** and adds debt/preferred/minority — a common error.
- **EV/EBITDA's two drawbacks**: EBITDA **overstates CFO when working capital grows**, and **FCFF ties to theory better** than EBITDA. Advantages ≠ the whole answer.
- Normalizing cyclical EPS: the **method of average ROE is preferred** over the method of historical average EPS.
- **P/B is the multiple for firms holding liquid assets** (banks/insurers) and for firms **expected to be wound up**; its weakness is **intangibles**, size effects, accounting conventions, and inflation.
- **EV/EBITDA** is preferred when capital structures differ (P/E is distorted by leverage).
- Use the **harmonic mean** to average P/Es across firms, not the arithmetic mean; the arithmetic mean is biased **upward** by outliers.
- Justified P/B = `(ROE − g)/(r − g)`; P/B > 1 when ROE > r.
- **P/CF**: always pin down the cash-flow definition (CF vs CFO vs FCFE vs EBITDA). The simple **CF** (EPS + noncash charges) **ignores WCInv and non-cash revenue**. EBITDA pairs with **EV**, not price.
- **Justified dividend yield = (r − g)/(1 + g)** — it is the **inverse** orientation of P/E-type multiples, so *higher* yield = *cheaper*. Trailing yield uses the **dividend rate** (annualized latest dividend).

## Q&A

### 2026-07-11 — Why use E/P instead of P/E when diluted EPS is negative
**Q:** If a company's diluted EPS is negative, why look at E/P (earnings yield) instead of P/E?
**A:** (1) A negative P/E has **no economic meaning** ("pay −5 dollars per dollar of earnings"). (2) P/E is **discontinuous at E = 0** and its ranking reverses across it: as EPS falls, P/E → +∞, jumps to −∞, then rises toward zero — so a deeply loss-making firm (P/E = −5) "looks cheaper" than a healthy firm at P/E = 20, and P/E screens put the worst firms on top. (3) **E/P is monotonic** because the denominator (price) is always positive: highest E/P = cheapest, most negative E/P = worst — every stock ranks consistently. Alternatives: normalized/average EPS or robust-denominator multiples (P/B, P/S, EV/EBITDA). Same yield-space logic underlies the **harmonic mean** for averaging P/Es.
Related: [[Dividend_Discount_Models]]

### 2026-07-12 — Standardized unexpected earnings (SUE)
**Q:** What is standardized unexpected earnings and what is it used for?
**A:** `SUE = (actual EPS − expected EPS) / σ(past earnings surprises)` — the earnings surprise scaled by that firm's own historical surprise variability, making it a **signal-to-noise z-score** comparable across firms. Example: a stable firm beating by $0.05 with σ = $0.02 (SUE +2.5) is a far stronger signal than a volatile firm beating by $0.20 with σ = $0.40 (SUE +0.5). Uses: ranking stocks in **momentum strategies** exploiting **post-earnings-announcement drift** (high-SUE stocks keep drifting up after the announcement), and cross-firm comparability of surprises. Traps: denominator = std-dev of **past surprises** (not of EPS, not analyst-forecast dispersion); SUE is fundamental **momentum**, not a value measure.
Related: [[Multifactor_Models]]

### 2026-07-12 — Relative strength indicators: what they are and what they're for
**Q:** What are relative strength indicators and what is their role?
**A:** **RSTR compares a stock's recent performance either (1) to its own past performance or (2) to a group of comparable stocks/an index** over the same period (up 8% vs sector +15% → negative relative strength). It is a **momentum indicator** (price momentum), alongside **earnings surprise/SUE** (fundamental momentum; SUE = unexpected earnings ÷ std-dev of past surprises, scaling the surprise by its historical variability). Role: a **timing/confirmation overlay and screening factor** — momentum says recent winners tend to keep winning (the Carhart **WML** factor is a relative-strength construct). Traps: momentum indicators are **not value measures** (high RSTR ≠ undervalued); momentum = "going with the market," the opposite of contrarian value.
Related: [[Multifactor_Models]]

### 2026-07-12 — Fed model vs. Yardeni model (legacy curriculum)
**Q:** What are the Fed model and the Yardeni model?
**A:** Both are **aggregate-market** earnings-yield valuation tools from the **legacy** Equity Market Valuation reading (not in the 2026 LOS). **Fed model**: market fairly valued when forward **E/P = 10Y Treasury yield** (E/P higher → stocks cheap). Criticisms: ignores the **equity risk premium**, ignores **earnings growth**, and suffers **money illusion** (real asset vs nominal yield). **Yardeni model**: fair `E/P = y_B − d × LTEG`, where y_B = **A-rated corporate bond yield** (adds a risk premium), LTEG = consensus 5-yr market earnings growth, d ≈ **0.10** (market's weight on growth); undervalued if actual E/P exceeds this. Its flaws: corporate spread captures **default** risk not equity risk, **d assumed constant**, and **LTEG is optimistically biased** consensus.
Related: [[Dividend_Discount_Models]]

### 2026-07-12 — What "sales" means in the price-to-sales ratio
**Q:** In the P/S ratio, is "sales" the same as revenue?
**A:** Yes — **net revenue (net sales)**: the top line after returns, allowances, and trade discounts, used as trailing-12-month **sales per share** (= market cap ÷ annual net revenue). Strengths: nearly always **positive** (works when P/E fails), more **stable** than EPS, **harder to manipulate** than earnings — but not immune: watch **channel stuffing** and **bill-and-hold** revenue games. Weakness: ignores profitability — justified `P/S = (net margin × payout × (1+g))/(r−g)`, so a high P/S is only warranted by high margin/growth; always read P/S with the net margin. Mismatch trap: price is an **equity** claim but sales accrue to the **whole firm** → prefer **EV/Sales** when leverage differs.
Related: [[Dividend_Discount_Models]]

### 2026-07-11 — What the forward PEG ratio measures and its three limitations
**Q:** What kind of indicator is the forward P/E-to-growth (PEG) ratio?
**A:** **PEG = forward P/E ÷ expected EPS growth (as a whole number, 12% → 12)** — it standardizes the multiple **per unit of expected growth** so high-growth and low-growth stocks become comparable; **lower PEG = relatively cheaper** (e.g., P/E 30 / g 25 → PEG 1.2 beats P/E 15 / g 8 → PEG 1.9). Forward P/E is the clean pairing (expected earnings with expected growth). Three tested limitations: (1) assumes a **linear** P/E–growth relation (true relation is convex as g → r); (2) **ignores risk** (a low PEG may just compensate for high r); (3) **ignores growth duration** (20% for 20 years ≠ 20% for 3 years). Also meaningless when g ≤ 0. Only compare PEGs within similar-risk, similar-duration groups.
**Convexity demo** (justified leading P/E = (1−b)/(r−g), r = 10%, payout 40% — all four stocks fairly priced): g = 2/5/8/9% → P/E = 5/8/20/40 → PEG = 2.50/1.60/2.50/4.44. PEG differs ~3× (and isn't even monotonic) across correctly priced stocks because g sits in the denominator (r−g): P/E accelerates as g → r. So "lowest PEG = most undervalued" systematically flags fairly priced high-growth stocks as expensive; positive correlation ≠ proportionality.
Related: [[Dividend_Discount_Models]]

### 2026-07-11 — Underlying EPS vs. diluted EPS
**Q:** What is the difference between underlying EPS and diluted EPS?
**A:** They adjust **different parts of the fraction**. **Diluted EPS** fixes the **denominator**: a standardized, audited GAAP/IFRS measure assuming all dilutive securities convert (options/warrants via treasury-stock method; convertibles with mechanical numerator add-backs). **Underlying EPS** (core/adjusted/persistent) fixes the **numerator**: an analyst-defined, non-standardized measure stripping nonrecurring items (restructuring, impairments, asset-sale gains/losses) to show sustainable earning power. They are **complements**: the best P/E denominator = underlying earnings on a diluted share count. Traps: management's "adjusted EPS" can be self-serving (recurring "one-offs") — make your own adjustments; don't confuse underlying (one period, remove transitory items) with **normalized** EPS (cycle average, for cyclicals).
Related: [[Employee_Compensation]]

### 2026-07-11 — When to use P/E rather than E/P
**Q:** When should you look at P/E instead of E/P?
**A:** **P/E is the default when all earnings in the comparison set are positive**: it matches market convention (index/peer multiples, historical averages), anchors to the **justified P/E** from fundamentals (trailing = (1−b)(1+g)/(r−g); leading = (1−b)/(r−g)), and gives the intuitive "years of earnings paid" framing (also the basis of PEG). Switch to **E/P** when: any EPS in the sample is negative/near zero (only E/P ranks monotonically), you are screening a large universe, comparing equity yields to bond yields, or averaging multiples (harmonic mean = averaging in E/P space). The two are informationally equivalent for positive earnings — the choice is about sign-robustness and what you're comparing against.
Related: [[Dividend_Discount_Models]]

### 2026-06-03 — Why use the harmonic mean to average P/Es?
**Q:** A peer group has P/Es of 10, 15, and 60. Why not just average them?
**A:** The **arithmetic mean** (28.3) is dragged up by the high outlier and **overstates** the group multiple. The **harmonic mean** = `n / Σ(1/Pi/E) = 3/(1/10 + 1/15 + 1/60) = 3/0.1833 = 16.4` weights each stock by its earnings yield and is the correct way to average price multiples (equivalent to an equal-dollar-weighted portfolio's multiple). Always use harmonic (or weighted harmonic) mean for P/Es.
Related: [[Dividend_Discount_Models]]

### 2026-06-03 — Why EV/EBITDA over P/E when capital structures differ?
**Q:** When is EV/EBITDA the better multiple, and how is EV built?
**A:** `EV = market cap + total debt + preferred + minority interest − cash & equivalents`. EBITDA is a **pre-financing, pre-tax** flow available to **all** capital providers, and EV is total firm value — so the pair is **capital-structure-neutral**, unlike P/E, which is distorted by leverage and by D&A policy. Prefer EV/EBITDA for firms with **different leverage**, heavy D&A, or negative net income. Trap: EV **subtracts cash** and **adds** debt/preferred/minority.
Related: [[Residual_Income]]

### 2026-06-04 — P/CF: which "cash flow" and a worked calc
**Q:** What cash-flow definitions feed P/CF, and how do you compute the basic P/CF?
**A:** Four definitions: (1) **CF** = EPS + per-share depreciation/amortization/depletion (the default "P/CF"), (2) **CFO**, (3) **FCFE** (= CFO − FCInv + net borrowing; strongest theory link but volatile/often negative), (4) **EBITDA** (firm-level, so used in **EV**/EBITDA). Worked (curriculum Philips example): EPS €1.41 + per-share D&A €1.17 = **CF €2.58**; price €36.31 → `P/CF = 36.31/2.58 = 14.1`. Why P/CF over P/E: cash flow is harder to manipulate and steadier; trap — the simple CF definition **ignores working-capital changes and non-cash revenue**, so aggressive revenue recognition isn't caught.
Related: [[Free_Cash_Flow_Valuation]]

### 2026-07-25 — Justified leading vs trailing P/E (the (1+g) bridge)
**Q:** What is the difference between justified leading P/E and trailing P/E?
**A:** Two layers. **(1) Which EPS:** *trailing* (current) P/E divides price by **past 12-month realized EPS (E₀)**; *leading* (forward/prospective) P/E divides by **forecast next-period EPS (E₁)**. **(2) Justified formulas** (both from Gordon `P₀ = D₁/(r−g)`): leading `P₀/E₁ = payout/(r−g) = (1−b)/(r−g)`; trailing `P₀/E₀ = payout(1+g)/(r−g) = (1−b)(1+g)/(r−g)`. The trailing form carries an extra **(1+g)** because `E₁ = E₀(1+g)`, giving the bridge **Trailing P/E = Leading P/E × (1+g)** — so with g > 0, trailing P/E is always the larger. Example: payout 40% (b=0.6), ROE 15% → g = 9%, r = 12% → leading = 0.40/0.03 = **13.33×**, trailing = 0.436/0.03 = **14.53×** (=13.33×1.09 ✓). Traps: never pair E₁ with the trailing formula (or omit the (1+g)); normalize trailing EPS for transitory items; "justified" = derived from fundamentals, not from comparables.
Related: [[Free_Cash_Flow_Valuation]], [[Dividend_Discount_Models]]

### 2026-06-04 — Justified dividend yield and the dividend rate
**Q:** What is the justified dividend yield, and how is a trailing dividend yield computed?
**A:** From Gordon: `D0/P0 = (r − g)/(1 + g)` — the justified (leading) dividend yield. **Trailing dividend yield** = the *dividend rate* (annualized most recent dividend; for quarterly payers, 4 × latest quarterly dividend) ÷ current price. Dividend yield is reported as a **yield** (not P/D) because non-payers give D/P = 0 while P/D is undefined. Rationale: it is part of total return and a lower-risk part; drawback: it is only **one** return component and ignores the **dividend displacement of earnings** (higher dividends now can reduce future growth).
Related: [[Dividend_Discount_Models]]
