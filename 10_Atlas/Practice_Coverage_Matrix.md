---
aliases: [Practice Coverage Matrix, EOC Coverage Matrix, Mock Coverage Matrix]
tags: [CFA-L2, atlas, practice]
date: 2026-08-27
status: evergreen
source: Local practice-source inventory, re-verified 2026-08-27 by Glob against the KB's parent directory
---

# Practice Coverage Matrix

Tracks the practice sources available locally and how much of each has been distilled into the notes. It does **not** mean full official vignettes have been copied in. Working rule: keep the original question PDFs as source files, and distill only personal errors, formula triggers, traps, and original paraphrased Q&A into topic notes.

## Correction Log

**2026-08-27 — every source previously marked "NOT present on this machine" is in fact present.** The 2026-08-25 audit searched two hardcoded paths (`../notes/` and `../*.PDF`), neither of which exists here, and concluded the EOC volumes, module quizzes and mock sets were gone. They were simply one directory level deeper. All counts below were re-verified by Glob and `find`. See [[knowledge_gaps]] for the full entry.

## How to Find the Sources

Source folder names contain non-ASCII characters and must never be transcribed into a note. Discover files at runtime by passing the KB's **parent directory** as Glob's `path` and matching on the ASCII file names. Bracketed numbers are the hit counts verified on 2026-08-27:

```text
**/cfa-program2026L2V*.PDF                     -> official curriculum volumes V1-V10   [10]
**/cfa-program2026L2glossary.PDF               -> official L2 glossary                  [1]
**/CFA 2026 Level II SchweserNotes Book *.pdf  -> Schweser Books 1-5                    [5]
**/*Quicksheet*.pdf                            -> Schweser formula Quicksheet           [1]
**/Volume *.pdf                                -> official EOC practice problems        [10]
**/Module * Quiz - Questions.pdf               -> Schweser module quizzes               [143]
**/Module * Quiz - Answers.pdf                 -> matching answer keys                  [143]
**/mock*/*                                     -> 2025 mock sets (mock1-3, mockA-B)     [20]
**/pack/*                                      -> 2025 topic practice packs             [23]
```

Always use `**/` — the sources sit in separate subfolders at different depths.

## Source Inventory (verified 2026-08-27)

| Source | Contents | Status |
|---|---|---|
| Official curriculum | 10 volumes V1-V10 + glossary | **Present** |
| Schweser Notes | Books 1-5 + Quicksheet | **Present** |
| Official EOC practice problems | 10 volumes, vignette problems **with full solutions** | **Present — not yet distilled** |
| Schweser module quizzes | 143 question PDFs + 143 answer PDFs | **Present — not yet distilled** |
| 2025 mock sets | mock1, mock2, mock3, mockA, mockB (20 files) | **Present — not yet distilled** |
| 2025 topic practice packs | 23 files (questions + answers) | **Present — not yet distilled** |

## Official EOC Volume Coverage

Each volume carries the official `PRACTICE PROBLEMS` section for its topic, followed by `SOLUTIONS`.
Discover with `**/Volume *.pdf`.

| Volume | Topic | Distilled |
|---:|---|---|
| 1 | Quantitative Methods | Not started |
| 2 | Economics | Not started |
| 3 | Financial Statement Analysis | Not started |
| 4 | Corporate Issuers | Not started |
| 5 | Equity Investments | Not started |
| 6 | Fixed Income | Not started |
| 7 | Derivatives | Not started |
| 8 | Alternative Investments | Not started |
| 9 | Portfolio Management | Not started |
| 10 | Ethical and Professional Standards | Not started |

## Module Quiz Coverage

143 question/answer pairs, one folder per topic. Quiz file names carry the **module number** (e.g. `Module 25.8 Quiz - Questions.pdf`), so each quiz maps directly onto a KB note via the module number in that note's `source:` field.

| Topic | Q/A pairs | Distilled |
|---|---:|---|
| Quantitative Methods | 15 | Not started |
| Economics | 5 | Not started |
| Financial Statement Analysis | 26 | Not started |
| Corporate Issuers | 8 | Not started |
| Equity Valuation | 17 | Not started |
| Fixed Income | 21 | Not started |
| Derivatives | 10 | Not started |
| Alternative Investments | 10 | Not started |
| Portfolio Management | 20 | Not started |
| Ethical and Professional Standards | 11 | Not started |
| **Total** | **143** | **0** |

## Distillation Priority

Agreed order (2026-08-27): **highest exam weight first**.

1. **Financial Statement Analysis** (10-15%) — also the largest quiz set at 26 pairs
2. **Equity Investments** (10-15%) — 17 pairs
3. **Fixed Income** (10-15%) — 21 pairs
4. Portfolio Management and Ethics (also 10-15%), then the 5-10% topics: Quant, Economics, Corporate Issuers, Derivatives, Alternative Investments

Within a topic, prioritize the modules whose notes are thinnest by lines-per-LOS — currently [[Arbitrage_Free_Valuation]], [[Bonds_With_Embedded_Options]], [[Quality_of_Financial_Reports]], and [[Dividend_Discount_Models]].

## Import Policy

- Never paste full official vignettes or long answer explanations into notes — copyright and review value both argue against it.
- Per practice session, add only derived artifacts: the missed LOS, the formula trigger, the trap, an original paraphrased Q&A, and the module number that locates the source PDF.
- Prioritize the official EOC volumes and the Schweser module quizzes over the 2025 mock/pack PDFs.
- Record each completed batch by flipping the "Distilled" cell in the tables above.
