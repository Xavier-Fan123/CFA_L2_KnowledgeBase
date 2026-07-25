---
aliases: [Knowledge Gaps]
tags: [CFA-L2, inbox, gaps]
date: 2026-06-03
status: evergreen
---

# Knowledge Gaps

Auto-detected topics not yet covered by the KB. Resolve by creating or enriching notes.

### 2026-07-18 — Independent regulators vs SROs (out of 2026 L2 scope)
- Triggered by: user question on structural and funding differences between independent regulators and SROs — not found in the KB, the five 2026 Schweser L2 books, or the official L2 glossary; this is the Level I "Economics of Regulation" LOS. Answered from general/L1 knowledge: independent regulator = government-recognized authority + self-funded via levies on regulated entities (funding independence → political independence); SRO = private member body funded by dues/commercial revenue (conflict-of-interest risk); overlap case = FINRA (SRO with delegated authority); SRO delegation more common in common-law than civil-law countries.
- Suggested action: none for L2 notes; if the user's practice sources keep testing it, add a short "Legacy/L1 Regulation Vocabulary" stub.
- Priority: low (Level I material, not a 2026 L2 LOS)

### 2026-07-11 — Legacy M&A vocabulary (merger types, takeover defenses) absent from KB
- Triggered by: user questions on horizontal vs. vertical mergers and on crown jewel / Pac-Man / white knight defenses — the current 2026 restructuring reading does not define these, so answers came from legacy-curriculum/general knowledge.
- Suggested action: if the user's practice questions keep touching legacy M&A terms, add a short "Legacy M&A Vocabulary" section to [[Corporate_Restructurings]] (merger types, pre-/post-offer defenses: poison pill, staggered board, greenmail, leveraged recap, litigation, etc.); otherwise leave as Q&A entries only.
- Priority: low (out of 2026 LOS scope; useful vignette vocabulary)

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

### Metadata fix needed (CLAUDE.md)
- The CLAUDE.md "Topic ↔ Schweser Book" mapping says **Book 3 = Corporate Issuers + Equity**, but the actual 2026 Schweser layout is **Book 2 = FSA + Corporate Issuers** (modules 7–16) and **Book 3 = Equity only** (modules 17–22). The Corporate Issuers notes' `source: Book 2` tags are therefore **correct**; CLAUDE.md's table is the thing to correct. Priority: low (cosmetic, but affects future PDF lookups).

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
