---
aliases: [Knowledge Gaps]
tags: [CFA-L2, inbox, gaps]
date: 2026-06-03
status: evergreen
---

# Knowledge Gaps

Auto-detected topics not yet covered by the KB. Resolve by creating or enriching notes.

### 2026-09-04 — 2026 exam-scope audit and errata reconciliation (RESOLVED)
- Official 45-module mapping found no missing current 2026 learning module in the knowledge base.
- September errata review removed pseudo-R-squared; Fed/Yardeni and legacy M&A vocabulary were removed from core notes.
- [[Capital_Budgeting_Foundations]] and deep [[GIPS]] mechanics were reclassified as reference-only.
- Current Standard III(D) and change-of-control contingent-put mechanics were retained; final review consolidated current III(D) non-GIPS procedures into the core [[Code_and_Standards]] note.
- Priority: resolved

### 2026-08-27 - All local practice sources were wrongly recorded as missing (RESOLVED)
- Triggered by: user question - "is there anything still worth adding to the KB?" A coverage audit found concept coverage complete (42/42 readings, 370/370 LOS, spot-checked against the notes), so the search moved to what was *not* covered: practice material.
- **Finding:** [[Practice_Coverage_Matrix]] recorded the official EOC volumes, the module-quiz PDFs and the 2025 mock sets as **"NOT present on this machine."** All of them are present. Re-verified by Glob and `find` on 2026-08-27:
  - **10 official EOC volumes** (`**/Volume *.pdf`) with vignette `PRACTICE PROBLEMS` + full `SOLUTIONS`
  - **143 module-quiz question PDFs + 143 answer PDFs** (`**/Module * Quiz - Questions.pdf`) - matching the per-topic counts the old "prior inventory" table already listed (15/5/26/8/17/21/10/10/20/11)
  - **20 mock files** (mock1-3, mockA-B) and **23 topic-pack files**
  - **Schweser Quicksheet** (`**/*Quicksheet*.pdf`) - a formula condensation the KB has never referenced
- **Root cause:** `CLAUDE.md` Rule 2 asserted the Schweser books sit in `../notes/` and the official volumes sit directly in `../`. Neither is true here - `../notes/` does not exist and the parent contains no PDFs at all; everything is one level deeper, inside a single 2026 source folder whose name is non-ASCII. The 2026-08-25 audit searched those two hardcoded paths, found nothing, and wrote the "not present" conclusion into the matrix.
- **Fixed:** Rule 2 rewritten around **ASCII file-name Glob patterns** with the KB's parent passed as `path` and `**/` for depth, each with its verified hit count, plus an explicit warning against hardcoding depth. [[Practice_Coverage_Matrix]] rewritten with the true inventory, a correction log, per-topic distillation tables, and the agreed priority order.
- **Consequence still open:** the KB's ~168 Q&A entries are all self-authored; **zero** derive from official EOC or module-quiz questions, because the source was believed missing. Level II is a vignette exam, so this is now the largest remaining gap - a gap in *kind*, not in LOS coverage.
- Suggested action: distill practice questions into the notes, highest exam weight first (FSA -> Equity -> Fixed Income), per the priority table in [[Practice_Coverage_Matrix]]. Derived artifacts only - never full vignettes.
- Priority: **infrastructure resolved; distillation high**

### 2026-08-27 - Q&A headings written with a hyphen vanish from the review indexes (RESOLVED)
- Triggered by: the Atlas reported Economics at 12 Q&A while the notes actually held 18.
- Finding: `scripts/generate_atlas.py:119` only counts a `## Q&A` heading if it contains an **em-dash**. Six entries in [[Currency_Exchange_Rates]] and [[Economic_Growth]] used a plain hyphen, so they were invisible to [[LOS_Coverage_Matrix]] **and** to [[Active_Recall_Index]] - the review prompts existed but never appeared in the index used to revise from.
- Fixed: the six headings normalized to the template separator; Atlas regenerated (Economics now reads 18). KB-wide total is now **168 topic-note Q&A entries, all indexed**; a 169th sits in [[Statistical_Tests_Master_Table]], which lives in `10_Atlas/` and is outside the generator's topic scan by design.
- **Standing rule for future write-backs:** the Q&A heading separator must be an em-dash, exactly as the CLAUDE.md template shows - `### YYYY-MM-DD - <summary>` written with a hyphen silently drops the entry from both indexes.
- Priority: resolved

### 2026-08-27 - Arbitrage_Free_Valuation carries no worked calculation
- Triggered by: the same coverage audit - a lines-per-LOS and worked-example sweep across all 57 topic notes.
- Finding: [[Arbitrage_Free_Valuation]] is 59 lines covering LOS 24.a-24.i with **zero numbers** - no calibrated binomial tree, no backward-induction node values, no pathwise example. The prose is complete and correct (value additivity **and** dominance, lognormal `e^(2σ)` node spacing, CIR/Vasicek/Ho-Lee/KWF), but the exam tests this reading almost entirely as calculation. Every comparable computational note ([[Time_Series_Analysis]], [[Options_Valuation]], [[Multifactor_Models]], [[Real_Estate]]) carries worked examples.
- Checked and cleared: the other zero-example notes are genuinely qualitative or already complete - [[Exchange_Traded_Funds]], [[Quality_of_Financial_Reports]] (Beneish, all 8 indices + the -1.78 cutoff), [[Economics_and_Investment_Markets]] (Taylor rule, breakeven inflation), [[Big_Data_Projects]] (confusion matrix worked through). Not gaps.
- Suggested action: add a calibrated two-period tree, a backward-induction walk-through for a coupon bond, and a pathwise valuation that reconciles to the same price, from Schweser Book 4 Module 24.
- Priority: medium-high


### 2026-08-25 - Reading-level "KEY CONCEPTS" audit: 47 detail-level LOS points were missing or thin (RESOLVED)
- Triggered by: user request - "can this KB be made more detailed; are any exam points missing?"
- **Method (new, reusable):** every Schweser reading ends with a `KEY CONCEPTS` block that restates the reading **LOS by LOS**. Extracted all 40 such blocks (readings 1-40) plus the full **370-LOS** list from Books 1-5, then compared each block line-by-line against its KB note. This finds *detail inside a covered LOS*, which the earlier note-level and module-level audits could not.
- **Calibration used:** lines-per-LOS density flagged the thin notes first (DDM 4.2, Economics & Investment Markets 4.5, Dividends 4.8, Bonds w/ Embedded Options 5.2, Equity Valuation Process 5.4, Arbitrage-Free 5.8, ETFs 6.0 vs ~8 for notes judged genuinely deep).
- **Findings fixed (47 items), by topic:**
  - **Economics**: the three current-account mechanisms (**flow supply/demand, portfolio composition, debt sustainability**) plus capital-account dominance (5.j) were absent; labor **quantity vs quality** drivers and the resource curse (6.f-6.h) were one line.
  - **FSA**: **proportionate consolidation** (7.a); **tax windfall/shortfall** IFRS-vs-US-GAAP and the **treasury stock method** (8.b); **Basel III minima 4.5%/6%/8% of RWA** and the **Level 1/2/3 fair-value hierarchy** (10.c); **P&C hard vs soft market** and the L&H interest-rate-risk contrast (10.f); only **5 of the 8 Beneish variables** were listed, with no cutoff and no limitations (11.d).
  - **Corporate**: the **six factors affecting payout policy** (13.e); the **shareholder-bondholder** agency conflict and indenture covenants (13.d); **global payout trends** (13.h); **Dutch auction / direct-negotiation mechanics** (13.i); the **five repurchase rationales** (13.l); **rate implicit in the lease (RIIL)** as the finance-lease cost of debt (15.b).
  - **Equity**: **investment value vs fair market value** (17.c); Porter's five forces and the QoE categories enumerated (17.e); one-/two-period DDM, the **three GGM assumptions**, GGM and **multistage strengths/limitations**, **spreadsheet modeling steps**, SGR assumptions + beginning-of-period values (18.b-18.p); **P/E and P/B rationales & drawbacks**, "average ROE preferred", **EV/EBITDA disadvantages**, **international comparables**, fundamentals-in-comparables (20.c-20.p); private-company **FCF forecasting issues**, the **five discount-rate considerations** (incl. *use the target's WACC, not the acquirer's*), **DLOM estimation methods**, and the **prior transaction method** (22.c-22.i).
  - **Fixed income**: **dominance** as the second arbitrage condition (24.a); the **Kalotay-Williams-Fabozzi** model (24.i); **sinking funds and estate puts** (25.a); **naked CDS, long/short and curve trades, synthetic-vs-cash CDO arbitrage** (27.d, 27.e).
  - **Derivatives**: American-vs-European call/put value rule (29.d).
  - **Alternatives**: the **three** futures-return theories kept separate, with hedging pressure able to produce **contango** (30.f); **specialist strategies were WRONG** - the note said "volatility, reinsurance/ILS" but the 2026 reading names **volatility trading and life settlements** (33.f); **netting risk** in funds-of-funds (33.g); the **20% HF in a 60/40** result - lower sigma, higher Sharpe **and Sortino**, lower **max drawdown** (33.i); short-bias and convertible-arb position sizings (33.b, 33.d).
  - **Portfolio management**: the **inter-temporal rate of substitution** - the concept the whole Economics & Investment Markets reading is built on - was absent (34.a-34.c); **IC of a market timer = 2(% correct) - 1** and sector rotation (35.e); **tracking difference vs tracking error** and the curriculum's source list, **iNAV**, the liquidity metric, **expectation-related risk**, and the **three** portfolio-use buckets (36.c-36.h); **factor portfolio vs tracking portfolio** (37.e); **reverse stress test** (38.h); **tail dependence** and the **multivariate skewed Student t** sensitivity analysis (39.f, 39.h).
  - **Ethics**: named application cases absent - **issuer-paid research** I(B), **independent practice** IV(A), **front running** VI(B), **client brokerage / best price and execution** III(A).
- **Also fixed (infrastructure):**
  - `Practice_Coverage_Matrix` listed source PDFs under **another machine's user profile** (`C:\Users\chenx\...`) with Chinese folder names - violating the KB's English-only rule and, worse, **the EOC volumes, module-quiz PDFs and 2025 mock PDFs do not exist on this machine**. Table rewritten with the verified inventory (only the 10 official volumes + Schweser Books 1-5 are present) and the missing sets marked as a prior inventory, not as available material.
  - `CLAUDE.md` Rule 2 described a non-ASCII sibling source folder that no longer exists; rewritten to the real layout (Schweser in `../notes/`, official volumes in `../`), with `-layout` extraction and a pointer to the `KEY CONCEPTS` blocks as the per-reading checklist.
- **Verification:** all **370 of 370** LOS are now tagged in the topic notes, either as an explicit token (346) or inside a heading range such as `25.i-25.l` (24); `kb_quality_check.py` reports no issues; zero CJK characters remain in any KB markdown file.
- **Not audited at content level:** Quant readings 1-4 and Derivatives 28 were checked against KEY CONCEPTS and found complete, but their *worked examples* were not re-derived; and the whole audit is anchored on **Schweser**, which is a condensation of the official curriculum. Where Schweser and the official volumes have diverged before (Real Estate LM2, Publicly Traded RE LM3, Ethics LM1-3), the official text won. A future pass should re-run this same KEY-CONCEPTS method against `cfa-program2026L2V*.PDF` learning-outcome lists.
- Priority: resolved

### 2026-08-02 — Capital budgeting (TNOCF / NWC recovery / tax shields) absent from KB and from the 2026 L2 curriculum (RESOLVED)
- Triggered by: user's four-part self-diagnosis after a practice set — TNOCF & NWC recovery, incremental capex vs. depreciation tax shield, annuity↔geometric-series mapping, and nominal-vs-real direction on shields and interest.
- Finding: **"TNOCF" returns zero hits across all five 2026 Schweser L2 books**; there is no capital budgeting reading in 2026 L2. This is **Level I** (Corporate Issuers — Capital Investments). The user's practice source is testing L1 foundation material.
- Suggested action: **done** — created [[Capital_Budgeting_Foundations]] with an explicit scope warning, plus L2 bridges for each concept (NWC↔WCInv in [[Free_Cash_Flow_Valuation]]; tax shield↔after-tax cost of debt in [[Cost_of_Capital]]; geometric series↔Gordon Growth in [[Dividend_Discount_Models]]; nominal-vs-real↔temporal method in [[Multinational_Operations]]).
- Priority: resolved (kept as foundation, flagged as non-LOS so it doesn't consume L2 review time)

### 2026-07-26 — No critical-value / test-statistic reference anywhere in the KB (RESOLVED)
- Triggered by: user asked which multiplier to use for 90/95/99% confidence intervals, one- vs two-tailed. Grep found no z/t critical values in any note or in the Formula Cheat Sheet — every note assumed the reader already had them.
- Suggested action: **done** — added a "Coefficient t-test and Confidence Intervals" section with the full critical-value table to [[Multiple_Regression]] and a one-line summary to [[Formula_Cheat_Sheet]]. Follow-up **also done (2026-07-26)**: built [[Statistical_Tests_Master_Table]] in `10_Atlas/` — all 12 L2 hypothesis tests (statistic / distribution / df / tails / decision rule), the non-test diagnostics (VIF, leverage, AIC/BIC/RMSE), a df decoder, a "which test do I use" flow, and the violation→Type I/II direction table. Registered in [[Master_Index]] and back-linked from all six quant detail notes.
- Priority: resolved

### 2026-07-18 — Independent regulators vs SROs (out of 2026 L2 scope)
- Triggered by: user question on structural and funding differences between independent regulators and SROs — not found in the KB, the five 2026 Schweser L2 books, or the official L2 glossary; this is the Level I "Economics of Regulation" LOS. Answered from general/L1 knowledge: independent regulator = government-recognized authority + self-funded via levies on regulated entities (funding independence → political independence); SRO = private member body funded by dues/commercial revenue (conflict-of-interest risk); overlap case = FINRA (SRO with delegated authority); SRO delegation more common in common-law than civil-law countries.
- Suggested action: none for L2 notes; if the user's practice sources keep testing it, add a short "Legacy/L1 Regulation Vocabulary" stub.
- Priority: low (Level I material, not a 2026 L2 LOS)

### 2026-07-11 — Legacy M&A vocabulary (merger types, takeover defenses) absent from KB
- Triggered by: user questions on horizontal vs. vertical mergers and on crown jewel / Pac-Man / white knight defenses — the current 2026 restructuring reading does not define these, so answers came from legacy-curriculum/general knowledge.
- Suggested action: if the user's practice questions keep touching legacy M&A terms, add a short "Legacy M&A Vocabulary" section to [[Corporate_Restructurings]] (merger types, pre-/post-offer defenses: poison pill, staggered board, greenmail, leveraged recap, litigation, etc.); otherwise leave as Q&A entries only.
- **2026-08-02 — triggered a second time** (poison pill / poison put) → **section built.** [[Corporate_Restructurings]] now has a "Legacy M&A Vocabulary" block with the pre-/post-offer defense taxonomy and a pill-vs-put table, explicitly flagged as non-LOS. Notable finding: "poison" has **zero hits in all five 2026 Schweser books**, but the **poison put's mechanism IS examinable** as the change-of-control contingent put in Book 4 Module 25.8 (LOS 25.n) — [[Bonds_With_Embedded_Options]] updated to carry the market name.
- **2026-09-04 — resolved in the core note:** the optional Legacy M&A Vocabulary section and its related Q&A entries were removed from [[Corporate_Restructurings]]; this discovery history is retained for audit evidence.
- Priority: resolved (was low — out of 2026 LOS scope; useful vignette vocabulary)

### 2026-06-05 - 2026 errata / LOS metadata / practice-source sync (RESOLVED for concept metadata)
- Triggered by: user audit against current CFA Institute Level II page and 2026 errata.
- Fixed: [[Intercorporate_Investments]] VIE primary beneficiary definition, removed pooling-of-interests curriculum residue, tightened contingent-liability/goodwill impairment language; [[Cost_of_Capital]] private-company premium wording; [[Dividend_Discount_Models]] MSEX PVGO no-growth value; [[Real_Estate]] official LOS 31.a-31.e metadata.
- Added: [[Practice_Coverage_Matrix]] inventory for local 2026 EOC volumes, module quiz Q&A PDFs, and 2025 mock/pack sources.
- Remaining practice work: distill missed questions into original flashcards/traps after practice sessions; do not copy full official vignettes into notes.
- Priority: concept/metadata gap resolved; practice distillation is ongoing.

### 2026-06-05 — Ten-agent deep module-level audit vs. OFFICIAL curriculum (RESOLVED)
- Triggered by: user request — set up 10 agents (one per topic), deep-verify every module against the original/official curriculum volumes (`cfa-program2026L2V1–V10.PDF`), and supplement as needed.
- Method: 10 parallel agents, each scoped to one topic folder, grounded in the official volume + Schweser.
- **Findings (notes were incomplete/incorrect despite `status: evergreen` — confirms labels can't be trusted):**
  - **Derivatives**: [[Options_Valuation]] was **missing BSM d₁/d₂ entirely**; FRA/swap valuation, Black model, swaptions, and Greek formulas + delta-hedge sizing were thin → all added.
  - **Equity**: [[Market_Based_Valuation]] was **missing P/CF and dividend yield** (both explicit LOS) → added.
  - **Ethics**: [[Code_and_Standards]] was on the **old edition** — missing **Standard I(E) Competence** (2024 revision), VI(A) mislabeled; no Application-cases note existed → created [[Application_of_the_Code_and_Standards]]; [[GIPS]] source corrected (no standalone 2026 GIPS reading — it sits under Standard III(D)).
  - **Alternatives**: [[Real_Estate]] used a non-official example and omitted most of LM2 → **rewritten** to the official private-RE reading (NOI, RE cycle, 3 valuation approaches, indexes).
  - **Corporate**: [[Cost_of_Capital]] missing DDM/BYPRP/Fama-French/Grinold-Kroner; [[Corporate_Restructurings]] missing pro-forma/sum-of-parts/LBO → added.
  - Smaller gaps filled across Quant (ANOVA MSR/MSE/SEE; AR residual-autocorrelation test), Economics (forward points, real-rate parity, endogenous growth), FSA (SPE/VIE, pension & translation worked examples, sources of risk info), FI (macro rate views 23.k, convertibles, VND/CVA, DM, CDS spread), PM (APT arbitrage, parametric VaR worked example).
- **Result: every LOS across all ten topics now verified against the official curriculum and at evergreen depth.**
- Priority: resolved.

### 2026-06-04 — Full reading-level build-out (RESOLVED)
- Triggered by: user request — "cover every chapter of all ten CFA L2 topics perfectly."
- Audited all 42 Schweser readings vs. KB. Found 6 integer-level gaps + Time-Series module holes.
- **Done**: created [[Multiple_Regression]] (R1 basics/fit/dummies/influence), [[Machine_Learning]] (R3), [[Big_Data_Projects]] (R4), [[Integration_of_FSA_Techniques]] (R12), [[Publicly_Traded_Real_Estate]] (R32); completed [[Time_Series_Analysis]] (trend, seasonality, chain-rule/RMSE, cointegration).
- Module-level audit of high-module-count existing notes (R23/25/26/28/29/41) — all confirmed complete.
- **Result: all 42 readings now have evergreen notes; no `seed`/`incubating`/`(to add)` notes remain.**
- Priority: resolved.

### 2026-06-04 — ARCH not covered (RESOLVED)
- Triggered by: "What is ARCH?"
- Suggested action: enrich note — **done**, folded ARCH section + Q&A into [[Time_Series_Analysis]].
- Priority: medium

## Prose Verification Status (deep-dive against Schweser)
Tracks which topics have had formulas verified line-by-line against the book + worked examples added, vs. those still scaffolded from the LOS map + general knowledge.

| Topic | Status |
|------|------|
| 11 Quantitative Methods | ✅ Deep (extracted prose, examples) |
| 12 Economics | ✅ Deep-verified 2026-06-03 (mnemonic + 5 examples) |
| 13 Financial Statement Analysis | ✅ Deep-verified 2026-06-03 (goodwill, pension flags) |
| 14 Corporate Issuers | ✅ Deep-verified 2026-06-03 (JetFun buyback example) |
| 15 Equity Investments | ✅ Deep-verified 2026-06-03 (EVA, justified P/B examples) |
| 16 Fixed Income | ✅ Deep-verified 2026-06-03 (CVA, OAS, convertible, CDS examples) |
| 17 Derivatives | ✅ Deep-verified 2026-06-03 (binomial π_U, BSM put replication) |
| 18 Alternative Investments | ✅ Deep-verified 2026-06-03 (RE max-loan/return, contango basis) |
| 19 Portfolio Management | ✅ Deep-verified 2026-06-03 (breadth, TC², VaR statement) |
| 20 Ethics | ✅ Deep-verified 2026-06-03 (12th-ed Handbook, stricter-law) |

**All ten topics deep-verified against Schweser prose.** Every formula checked was already correct; the deep-dive added the book's exact worked examples, mnemonics, and edition details. One correction was made during review: the CDS cheapest-to-deliver example (a senior CDS delivers the cheapest *senior* obligation, not a subordinated one).

## Enrichment status (updated 2026-06-03)
**Bulk enrichment pass complete.** Every detail note across the nine non-Quant topic areas now carries: worked numeric example(s) and a populated `## Q&A` section (2–3 exam-style questions each), all spot-checked against the 2026 Schweser Notes (Books 1–5). The `_None yet._` Q&A placeholders have been cleared KB-wide. See [[QA_Log]] for the per-note index.

### Metadata fix needed (CLAUDE.md) - RESOLVED
- ~~The CLAUDE.md "Topic ↔ Schweser Book" mapping says **Book 3 = Corporate Issuers + Equity**~~ - **verified 2026-08-25: CLAUDE.md already reads "Book 2: FSA (modules 7-12) + Corporate Issuers (modules 13-16)" and "Book 3: Equity Valuation only (modules 17-22)", which matches the actual 2026 Schweser layout.** No change needed. Separately fixed on the same date: Rule 2's description of the source-PDF folder, which pointed at a non-ASCII sibling folder that does not exist on this machine.

## Remaining enrichment opportunities (optional)
- ~~Quant: seasonality, ARCH, RMSE, cointegration~~ — **DONE 2026-06-04** (folded into [[Time_Series_Analysis]]).
- Official EOC/module quiz/mock sources are now indexed in [[Practice_Coverage_Matrix]]; next step is practice-session distillation into original flashcards/traps, not full vignette copying.
- Add a cross-topic **formula cheat-sheet** note (final-review aggregation) and a personal **error log** (distinct from this coverage-gap file) — both flagged in the earlier KB review as high-value additions.


### 2026-06-03 — Nine topic areas are seed-only
- Triggered by: initial KB build (only Quantitative Methods has real content so far)
- Suggested action: create notes as questions arrive, or proactively from the curriculum PDFs
- Priority: medium

### 2026-06-03 — Quant: time-series topics not yet covered
- Triggered by: Time_Series_Analysis covers stationarity/unit root but not seasonality, ARCH, RMSE, AR(p) forecasting, cointegration
- Suggested action: enrich [[Time_Series_Analysis]] or split into dedicated notes (Seasonality, ARCH)
- Priority: medium
