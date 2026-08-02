---
aliases: [Corporate Restructurings, Mergers and Acquisitions, Divestitures, Spin-off, Takeover Premium, Net Debt to EBITDA, Pro Forma WACC, Sum of the Parts, LBO, Equity Carve-out, Comparable Transaction Analysis]
tags: [CFA-L2, corp, concept]
date: 2026-06-03
status: evergreen
source: Official Curriculum 2026 L2 V4, Reading "Corporate Restructuring" (Schweser Book 2, Module 16); LOS a-g
---

# Corporate Restructurings

## Corporate Life Cycle (16.a)
Actions track the life cycle: **start-up/growth** → invest (expand); **maturity** → invest (acquire to re-accelerate) or divest (shed low-growth lines); **decline** → restructure or liquidate. Empirically, all restructuring activity is **pro-cyclical** (rises with equity prices), yet **weak-economy deals create more value** on average than strong-economy deals.

## Three Categories of Structural Change & Motivations (16.a)
- **Investment** (increase size/scope) — three forms:
  - **Equity investment**: buy a material stake **< 50%**; both firms stay independent; may get a board seat.
  - **Joint venture**: two+ firms jointly **control a new, separate** company (technically a type of equity investment); common for entering new/foreign markets.
  - **Acquisition**: buy **most/all** shares to gain **control**; target is **consolidated** (one set of financials, line-by-line aggregation). Distinct from equity investment/JV because of control + consolidation.
- **Divestment** (decrease size/scope) — two main forms in the curriculum:
  - **Sale (divestiture)**: sell a unit/segment/assets for **cash**; control transfers to the acquirer.
  - **Spin-off**: separate a unit into a **new independent company** via a **stock dividend** to existing holders (pro-rata new shares); **no cash** to the parent; faces little regulatory scrutiny (reduces, not increases, market power). (Curriculum also recognizes split-off and equity carve-out as related forms.)

### Divestiture Forms Compared

| Dimension | **Equity carve-out** | **Spin-off** | **Split-off** |
|---|---|---|---|
| Mechanism | Sell a stake via **IPO** to new outside investors | Distribute sub shares **pro rata** as a stock dividend | Shareholders **swap** parent shares for sub shares |
| **Cash to parent** | ✅ **YES** | ❌ No | ❌ No |
| Who receives sub shares | New outside investors | **All** existing holders, pro rata | Only those who **elect** to swap |
| Voluntary? | — | **No** — automatic | **Yes** — shareholder chooses |
| Parent share count | Unchanged | Unchanged | ⬇️ **Decreases** (tendered shares retired) |
| Parent retains a stake? | Yes — usually keeps control | No | No |
| Consolidation | **Still consolidated**; minority interest appears | Deconsolidated | Deconsolidated |
| Resulting shareholder base | Unchanged + new sub investors | Same people own **both** firms | Base **splits into two groups** |

- **Spin-off vs. split-off in one line:** spin-off = *everyone gets both*; split-off = *you pick one*.
- **Sharpest framing:** a **split-off is economically a share repurchase funded with subsidiary stock instead of cash** — which is why the parent's share count falls.
- **Carve-outs keep control**: only a minority stake is sold, so the parent still consolidates and books a **non-controlling interest**. Often a **first step**, later completed by a full spin-off or sale.
- Mnemonic: **C**arve-out → **C**ash · **Spin** → **s**tock dividend sprayed to all · **S**plit → **s**wap, base **s**plits, share count **s**hrinks.
- **Restructuring** (same size/scope, better cost/financing): **cost** restructuring (e.g., franchising, sale-leaseback), **balance-sheet** restructuring (recapitalization, leveraged recap), **reorganization** (Chapter 11 — renegotiate debt) and **liquidation** (Chapter 7).
- Motivations (Exhibit 3): **Investment** → realize synergies, growth, capabilities/resources, acquire an undervalued target; **Divestment** → focus, valuation (unlock a **conglomerate discount**), liquidity, regulatory; **Restructuring** → improve returns on capital, financial distress/bankruptcy.
- **LBO** (special case = invest + divest + restructure): PE buyer uses heavy debt to take a target private, restructures, then exits via sale/IPO. Returns driven by **purchase price, leverage, FCF generated (debt paydown), and exit price**.

## Three-Step Evaluation Process (16.b–16.d)
**Step 1 Initial evaluation → Step 2 Preliminary valuation → Step 3 Modeling & valuation.**

### Step 1 — Initial Evaluation (16.b): four questions
**What? Why? Is it material? When?** Apply professional skepticism (management always frames it positively).
- **Materiality = size + fit.**
  - **Size**: for a transaction, value = (cash paid + stock issued + target debt assumed) ÷ acquirer **EV**. Rule of thumb: **"large" if total transaction value > 10% of the acquirer's pre-deal EV.** (Most deals are immaterial for large caps; >95% of deals are < $1bn and >80% of targets are private.) For non-transaction restructurings, use the scale (e.g., cost cut as % of revenue/opex).
  - **Fit**: how it fits prior actions/strategy — a small off-strategy deal can still signal a strategy shift (Farfetch's ~8%-of-EV acquisition still dropped the stock 45%).
- **Announcement-day stock reaction** is a common but **unreliable** value gauge — research finds **no correlation** with long-run returns; >½ of negative initial reactions later earned excess returns.
- **When/timing**: closing can be **12+ months** out (shareholder, creditor, antitrust approvals); the deal hits the acquirer's financials only **at closing**. Markets discount the expected impact (incl. break risk) at announcement.

### Step 2 — Preliminary (relative) Valuation (16.c)
Three relative methods (DCF comes in Step 3):

- **Comparable company**: trading multiples of listed peers (EV/EBITDA, EV/sales, P/E).
  - Premium: **must ADD** a takeover premium because trading multiples have none.
  - Best for: **spin-offs** (no control premium).
- **Comparable transaction**: multiples paid in past similar deals.
  - Premium: **embedded** because transaction multiples already include it.
  - Best for: acquisitions/sales.
- **Premium-paid**: apply historical takeover premiums to the unaffected price.
  - Premium: the method itself is the premium.
  - Best for: listed targets.

- **Enterprise multiples** (EV/EBITDA) are preferred — less sensitive to capital structure.
- **Sum-of-the-parts (spin-off) — worked example (official):** a firm with EV €96,380m (10× consolidated EBITDA of €9,638m). Connectivity EBITDA €7,638m at peer 13× = €99,294m; Media EBITDA €2,000m at peer 6× = €12,000m → parts = **€111,294m, ~15% above** the €96,380m whole ⇒ a spin-off could **unlock value**.
- **Comparable-transaction — worked example (official):** apply mean multiples paid (P/E, P/CF, P/BV, P/S) to the target's per-share metrics, then take a **weighted average** (e.g., weight P/CF 40%, others 20%) → estimated fair takeover value $47.65 vs $55.00 paid ⇒ acquirer **overpaid** by ~13%.
- **Takeover premium (16.c)**: `PRM = (DP − SP) / SP`, DP = deal price/share, SP = **unaffected** (pre-announcement) price/share. Exclude any pre-announcement run-up from rumors — use a price **one week+ prior** or a VWAP. Historical median premium (1990–2018) ≈ **30%** (range ~20–40%). The control premium is what holders require to relinquish control.

### Step 3 — Modeling & Valuation: Effects on EPS, Net Debt/EBITDA, WACC (16.d)
Build **pro forma** statements, then read off EPS, net debt/EBITDA, FCF, and a pro forma WACC for DCF.

**Pro forma income statement (acquisition) — build order:**
1. **Revenue** = acquirer + target ± revenue synergies/dis-synergies.
2. **Operating expense / COGS** = acquirer + target ∓ cost synergies.
3. **D&A** = acquirer + target + amortization of acquired intangibles (PPA step-up).
4. **Interest** = acquirer's current interest + new-debt interest (at the revised rate).
5. **Taxes** = EBT-weighted blend of the two firms' tax rates.
6. **Shares** = acquirer's shares + any newly issued shares.

- **EPS effect**: depends on financing and **relative P/E**. Stock-financed and acquirer P/E **>** target P/E → typically **accretive**; acquirer P/E < target P/E → dilutive. Cash/debt-financed → **accretive if target earnings yield (E/P) > after-tax cost of debt**, dilutive if below. (Accretion ≠ value creation.)
- **Net debt / EBITDA** = (total debt − cash) ÷ EBITDA. Debt-financed deals raise it (more credit risk, possible covenant/rating pressure); divestitures that pay down debt lower it. (Six Flags hit ~13× pre-bankruptcy; emerged at < 3×.)
- **Pro forma WACC**: a restructuring changes both the **weights** (w_d, w_p, w_e) AND the **costs** (r_d, r_e) of capital. A cash/debt-funded acquisition shifts weights toward debt; a deal that raises leverage and cuts profitability **raises** WACC. Crossing from **investment- to speculative-grade** adds several hundred bps to WACC — hence acquirers often structure deals to **defend an IG rating**.
- **Capital-structure-weight worked example (official, CN/KCS):** acquirer pre-deal debt $10.2bn, equity 713m × $105 = $74.9bn → **12% / 88%**. Post-deal: debt $33bn, equity (713m + 103m new) × $105 = $85.7bn → **~28% / 72%**. (Higher combined leverage 4.6× vs a rival's 4.0× debt/EBITDA = the less attractive offer.)

## Evaluating Investment, Divestment & Restructuring Actions (16.e, 16.f, 16.g)
- **Equity investments (16.e)**: accounted for by the **equity method** if significant influence; the investee is **not consolidated**. Evaluate strategic fit and whether the stake is a strategic partnership/toehold to a future acquisition.
- **Joint ventures (16.e)**: equity-method/proportionate; evaluate shared **control**, resource contributions, and market-access rationale.
- **Acquisitions (16.e)**: target is **consolidated** (control). Evaluate **value creation = synergies − premium paid**, financing mix, accretion/dilution, and post-deal leverage/WACC and rating.
- **Divestitures — sale vs spin-off (16.f)**: both can unlock a **conglomerate discount** (sum-of-parts > whole) by improving focus/management attention. A **sale** brings cash (often at a lower valuation if forced by liquidity/regulators); a **spin-off** gives holders equity in the separated firm and is slower but faces little antitrust scrutiny. Choice often hinges on **valuation** (many interested buyers → sale fetches more).
- **Cost & balance-sheet restructurings (16.g)**: cost (franchising, sale-leaseback) lifts margins/returns; balance-sheet (recap, leveraged recap) rebalances leverage; reorganization renegotiates debt. Watch one-off charges and earnings-quality effects.

## Legacy M&A Vocabulary (NOT 2026 L2 curriculum)

> ⚠️ **Scope:** the terms below are **absent from the 2026 L2 curriculum** — "poison" returns **zero hits across all five 2026 Schweser books**. This is legacy-curriculum / general M&A vocabulary, retained only because practice sources keep testing it. Do not spend L2 review time here; recognize the words and move on.

**Takeover defense taxonomy:**

| **Pre-offer (preventive)** — installed in advance | **Post-offer (reactive)** — deployed after a bid |
|---|---|
| Poison **pill**, poison **put**, staggered/classified board, restricted voting rights, supermajority provisions, fair price amendments, golden parachutes | "Just say no," litigation, greenmail, share repurchase, leveraged recapitalization, crown jewel, Pac-Man, white knight, white squire |

**Poison pill vs. poison put:**

| Dimension | **Poison pill** | **Poison put** |
|---|---|---|
| Right held by | **Shareholders** (excluding the acquirer) | **Bondholders** |
| Instrument | Shareholder rights plan (**equity**) | Bond covenant (**debt**) |
| Trigger | Acquirer crosses ~10–20% ownership | **Change of control** |
| Mechanism | Buy new shares at a deep discount (~50%) | Put bonds back at **par / 101** |
| Damage to acquirer | **Dilution** — raider's stake destroyed | **Cash drain** — must refinance all debt at once |
| Board can cancel? | ✅ **Yes** — redeemable at will | ❌ **No** — contractual covenant |

- **Mnemonic: pill poisons the share count; put poisons the cash balance.**
- **Pill variants:** *flip-in* (buy target shares at a discount — most common); *flip-over* (buy the acquirer's shares post-merger); *dead-hand* (only incumbent directors may redeem — often struck down).
- **A pill's real purpose is leverage, not blockade.** The board can redeem it, so it forces the bidder to negotiate **with the board** instead of going straight to shareholders — raising the final premium.
- **The poison put is genuinely credit-protective**, not just an anti-raider device: without it, an LBO acquirer loads the target with debt and structurally subordinates existing bondholders (event risk).

> 🔗 **The poison put IS examinable — under a different name.** Schweser Book 4, Module 25.8, LOS 25.n covers it as a **"contingent put option in the event of change-of-control events,"** exercisable for a limited window, with a lowered conversion price as the alternative protection, and the **hard put** (cash) vs. **soft put** (issuer chooses cash/stock/debentures) distinction. See [[Bonds_With_Embedded_Options]].

## Exam Traps
- **Materiality** rule of thumb: transaction is "large" if value > **10% of acquirer's pre-deal EV** (size + fit). Announcement-day price reaction is a **poor** predictor of long-run value.
- **Comparable-company** multiples have **no** control premium → **add** one (best for spin-offs); **comparable-transaction** multiples **embed** the premium.
- **Takeover premium** = (DP − SP)/SP, using the **pre-announcement (unaffected)** price as denominator (exclude rumor run-up; use ~1 week prior or VWAP). Historical median ≈ 30%.
- **EPS** stock-financed accretion/dilution hinges on **relative P/E** (acquirer P/E > target → accretive); cash/debt-financed → compare **target E/P vs after-tax cost of debt**. Accretion ≠ value creation.
- **Pro forma WACC** changes both **weights and costs** of capital; defend an **investment-grade** rating to avoid a several-hundred-bp WACC jump.
- **Spin-off** = pro-rata new shares via stock dividend, **no cash** to parent; **carve-out** = sell a stake via IPO for **cash**; **split-off** = holders swap parent shares for subsidiary shares.

## Q&A

### 2026-08-02 — Poison pill vs. poison put
**Q:** What are a poison put and a poison pill, and when is each used?
**A:** **Poison pill** = a **shareholder rights plan**: once a hostile acquirer crosses ~10–20% ownership, all *other* shareholders may buy new shares at a ~50% discount → **massive dilution** of the raider. **Poison put** = a **bond covenant** letting **bondholders** put their bonds back at **par/101 on a change of control** → the acquirer must **refinance the entire debt stack at once**. Mnemonic: **pill poisons the share count, put poisons the cash balance.** Both are **pre-offer (preventive)** defenses installed in advance, not deployed reactively. Critical asymmetry: a **pill is board-redeemable at will** (so its real function is forcing the bidder to negotiate with the board, raising the premium), while a **put is a contract the board cannot undo**. The put is also genuinely credit-protective against LBO event risk, not merely an anti-raider device. ⚠️ **Scope:** "poison" has **zero hits in all five 2026 Schweser L2 books** — pill is legacy vocabulary; the **put's mechanism IS examinable** as the change-of-control **contingent put** in Book 4, Module 25.8, LOS 25.n.
Related: [[Bonds_With_Embedded_Options]]

### 2026-07-11 — Horizontal vs. vertical merger
**Q:** How do you distinguish a horizontal merger from a vertical merger?
**A:** **Horizontal** = combining with a firm at the **same stage of the same industry** (a competitor) — motives: economies of scale, market/pricing power, cost synergies; attracts the **most antitrust scrutiny** (raises concentration). **Vertical** = combining with a firm at a **different stage of your own value chain** (a supplier or customer) — motives: secure inputs, capture chain margins, cut transaction costs. Vertical splits into **backward integration** (buy upstream, e.g., automaker → battery maker) and **forward integration** (buy downstream, e.g., manufacturer → retailer). Test: could one firm be the other's supplier/customer? Yes → vertical; same product to same customers → horizontal; unrelated → **conglomerate**. (Legacy M&A curriculum / general knowledge — the 2026 restructuring reading does not formally define these.)
Related: [[Corporate_Issuers_Overview]]

### 2026-07-11 — Takeover defenses: crown jewel, Pac-Man, white knight
**Q:** In M&A, what do crown jewel, Pac-Man, and white knight mean?
**A:** Three **post-offer takeover defenses** (legacy M&A curriculum / general knowledge). **Crown jewel**: target sells its most valuable asset — usually what the bidder wants — to a third party, making itself unattractive (may be ruled illegal if done after a hostile bid). **Pac-Man**: target counter-bids to **acquire the hostile acquirer**; rare (needs size/financing). **White knight**: target invites a **friendly third party to outbid** the hostile bidder — the ensuing bidding war often triggers the **winner's curse** (knight overpays, benefiting target shareholders). Don't confuse white knight (buys the whole company) with **white squire** (buys only a minority blocking stake, no control).
Related: [[Corporate_Issuers_Overview]]

### 2026-06-03 — Spin-off vs split-off vs equity carve-out
**Q:** Distinguish the three main divestiture forms and which raise cash for the parent.
**A:** **Spin-off** — existing shareholders receive **pro-rata shares** of the new standalone entity; **no cash** to the parent. **Split-off** — shareholders **exchange** some parent shares for subsidiary shares (reduces parent share count); no cash raised. **Equity carve-out** — parent **sells a stake via IPO** to outside investors → **raises cash**. All three can unlock value by reducing a conglomerate discount and improving focus. Trap: only the carve-out (and an outright asset sale) brings cash into the parent.
Related: [[Dividends_and_Share_Repurchases]]

### 2026-06-03 — Computing the takeover premium
**Q:** A target trades at $30 a week before any rumor; the deal is announced at $42. What's the premium?
**A:** `Premium = (DP − UP) / UP = (42 − 30)/30 = 40%`, where DP = deal price and UP = **unaffected** (pre-announcement) price. Always use a price from **before** rumors leaked (e.g., a week prior or a VWAP), not the price right before announcement, which already reflects speculation. Comparable-**transaction** multiples already embed a premium; comparable-**company** multiples require adding an estimated premium.
Related: [[Equity_Valuation_Process]]

### 2026-06-04 — Sum-of-the-parts spin-off value
**Q:** A firm trades at EV €96,380m (10× total EBITDA €9,638m). Its Connectivity segment (EBITDA €7,638m) and Media segment (EBITDA €2,000m) have peer EV/EBITDA multiples of 13× and 6×. Could a Media spin-off add value?
**A:** Value the parts at peer multiples: Connectivity 13 × 7,638 = €99,294m; Media 6 × 2,000 = €12,000m → sum-of-parts = **€111,294m**, about **15% above** the €96,380m consolidated EV. So the market appears to be undervaluing the segments together (a conglomerate discount), and a spin-off has the **potential to unlock value** — subject to confirming peers and prospects are truly comparable. This is **comparable-company** analysis, which is favored for spin-offs because no control premium is involved.
Related: [[Equity_Valuation_Process]]

### 2026-06-04 — Is the restructuring material? (10% of EV)
**Q:** How do analysts decide whether an acquisition is "material" enough to model?
**A:** Materiality has two dimensions — **size** and **fit**. For size, compute transaction value (cash + stock issued + target debt assumed) ÷ the acquirer's **pre-deal enterprise value**; a common rule of thumb is **"large" if that ratio exceeds 10%**. For non-transaction restructurings, use the scale (e.g., announced cost cut as % of revenue). Even a small deal can matter for **fit** if it signals a strategy shift. Trap: the **announcement-day stock reaction is an unreliable** gauge of long-run value creation.
Related: [[Cost_of_Capital]]

### 2026-06-04 — How a debt-funded acquisition shifts the WACC weights
**Q:** An acquirer has $10.2bn debt and 713m shares at $105. It buys a target by issuing $19bn of new debt (bringing total debt to $33bn) plus 103m new shares. How do its capital-structure weights change (constant price)?
**A:** Pre-deal: equity = 713m × $105 = $74.9bn, debt $10.2bn → **12% debt / 88% equity**. Post-deal: debt $33bn; equity = (713 + 103)m × $105 = $85.7bn → total $118.7bn → **~28% debt / 72% equity**. The mix shifts toward debt, raising financial risk and net debt/EBITDA. A pro forma WACC must also re-estimate the **costs** r_d and r_e; if higher leverage threatens the investment-grade rating, WACC can jump several hundred bps, so acquirers often structure deals to **preserve an IG rating**.
Related: [[Cost_of_Capital]]
