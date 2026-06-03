---
aliases: [Knowledge Gaps]
tags: [CFA-L2, inbox, gaps]
date: 2026-06-03
status: evergreen
---

# Knowledge Gaps

Auto-detected topics not yet covered by the KB. Resolve by creating or enriching notes.

## Prose Verification Status (deep-dive against Schweser)
Tracks which topics have had formulas verified line-by-line against the book + worked examples added,
vs. those still scaffolded from the LOS map + general knowledge.

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

**All ten topics deep-verified against Schweser prose.** Every formula checked was already correct; the
deep-dive added the book's exact worked examples, mnemonics, and edition details. One correction was made
during review: the CDS cheapest-to-deliver example (a senior CDS delivers the cheapest *senior* obligation,
not a subordinated one).

## Enrichment status (updated 2026-06-03)
**Bulk enrichment pass complete.** Every detail note across the nine non-Quant topic areas now carries:
worked numeric example(s) and a populated `## Q&A` section (2–3 exam-style questions each), all spot-checked
against the 2026 Schweser Notes (Books 1–5). The `_None yet._` Q&A placeholders have been cleared KB-wide.
See [[QA_Log]] for the per-note index.

### Metadata fix needed (CLAUDE.md)
- The CLAUDE.md "Topic ↔ Schweser Book" mapping says **Book 3 = Corporate Issuers + Equity**, but the actual
  2026 Schweser layout is **Book 2 = FSA + Corporate Issuers** (modules 7–16) and **Book 3 = Equity only**
  (modules 17–22). The Corporate Issuers notes' `source: Book 2` tags are therefore **correct**; CLAUDE.md's
  table is the thing to correct. Priority: low (cosmetic, but affects future PDF lookups).

## Remaining enrichment opportunities (optional)
- Quant: seasonality, ARCH, RMSE, cointegration sub-readings not yet noted.
- Pull actual end-of-chapter practice questions from the official EOC folder (`02 CFA二级课后题/Volume 1–10`)
  and mock exams into each note's Q&A section as real vignette practice.
- Add a cross-topic **formula cheat-sheet** note (final-review aggregation) and a personal **error log**
  (distinct from this coverage-gap file) — both flagged in the earlier KB review as high-value additions.


### 2026-06-03 — Nine topic areas are seed-only
- Triggered by: initial KB build (only Quantitative Methods has real content so far)
- Suggested action: create notes as questions arrive, or proactively from the curriculum PDFs
- Priority: medium

### 2026-06-03 — Quant: time-series topics not yet covered
- Triggered by: Time_Series_Analysis covers stationarity/unit root but not seasonality, ARCH, RMSE, AR(p) forecasting, cointegration
- Suggested action: enrich [[Time_Series_Analysis]] or split into dedicated notes (Seasonality, ARCH)
- Priority: medium
