# CFA Level II 2026 Exam-Scope Cleanup Design

## Purpose

Align the core knowledge base with the curriculum applicable to the November 2026 CFA Level II examination. Remove obsolete or expressly withdrawn material from the exam-review path, preserve current concepts that support an examinable LOS, and make out-of-scope reference material visibly subordinate to the core curriculum.

## Authoritative Baseline

- CFA Institute, *2026 Level II Topic Outlines*, covering 10 topic areas and 45 examinable learning modules. The Quantitative Methods appendices are reference material rather than an additional examinable module.
- CFA Institute, *2026 Level II Curriculum Errata Notice*, September 2026 issue.
- The ten local official curriculum volumes, `../cfa-program2026L2V1.PDF` through `../cfa-program2026L2V10.PDF`.
- The five local 2026 Schweser Notes volumes as a secondary LOS-by-LOS completeness check. Where they differ, the CFA Institute curriculum and errata control.

The 2027 curriculum does not apply to this project because its changes first apply to examinations beginning in February 2027.

## Current-State Finding

Every one of the 45 official 2026 learning modules has a corresponding topic note. The existing August 2026 audit also accounts for all 370 Schweser LOS markers. No new topic note is required merely to close a module- or LOS-level omission.

This cleanup therefore focuses on scope accuracy, current errata, and removal of review noise. It does not claim that a vignette can never mention a non-LOS term as background; it classifies what the candidate can be directly required to know under the published 2026 curriculum.

## Classification Rules

### Core examinable

Keep material that directly teaches an official 2026 LOS or is necessary to apply that LOS. Core material remains in topic notes and all generated review indexes.

Examples that must remain include:

- Standard III(D) Performance Presentation, including the fact that following GIPS is one way to meet the standard.
- The change-of-control contingent put and related convertible-bond protection mechanics.
- Correct definitions and formulas confirmed by the September 2026 errata, including `R-squared = RSS / SST = 1 - SSE / SST`.

### Reference-only, not directly examinable

Keep current foundational material only when it remains useful for understanding an examinable LOS, but exclude it from the core exam-review indexes and label it prominently as reference-only.

- `Capital_Budgeting_Foundations.md` remains available as a Level I bridge, but it must not be counted as a Level II LOS note, appear in the active-recall or exam-trap review queues, or inflate Corporate Issuers coverage.
- GIPS detail beyond the Standard III(D) treatment remains reference-only. The core III(D) rule stays in `Code_and_Standards.md`; deep firm/composite/history/verification mechanics must not appear in the Level II formula sheet or core review queues.

### Remove from the exam knowledge base

Delete material that is explicitly withdrawn by current errata or retained solely from a legacy curriculum without supporting a current LOS:

- The pseudo-R-squared discussion in `Logistic_Regression.md`, which the 2026 errata removes from the curriculum.
- The Fed model and Yardeni model Q&A in `Market_Based_Valuation.md`.
- The legacy M&A taxonomy and Q&A on poison pills, horizontal/vertical mergers, crown jewels, Pac-Man, white knights, and white squires in `Corporate_Restructurings.md`.

When deleting legacy M&A material, retain the examinable change-of-control contingent-put mechanism in `Bonds_With_Embedded_Options.md`, but remove cross-links to the deleted legacy section and avoid teaching the non-curriculum label as required vocabulary.

## Scope Manifest

Create `10_Atlas/2026_Exam_Scope.md` as the durable audit record. It will contain:

- The ten official topic weights.
- All 45 official learning-module titles, grouped by topic.
- The corresponding KB note for each module.
- A status column showing `Core`, `Covered with another module in the same note`, or `Reference-only` where applicable.
- A dated September 2026 errata section distinguishing corrections already reflected in the KB from content removed during this cleanup.
- A clear warning that absence from the LOS means “not directly examinable,” not a guarantee that a term cannot appear as incidental vignette context.

Register the scope manifest in `Master_Index.md`.

## Index and History Handling

- Update `Master_Index.md` and the topic overview notes so core navigation does not present Level I capital budgeting or deep GIPS as Level II readings.
- Update `Formula_Cheat_Sheet.md` to remove non-Level-II GIPS mechanics while retaining the III(D) exam rule in the ethics note.
- Remove obsolete Q&A entries from their topic notes and from `QA_Log.md`.
- Regenerate `LOS_Coverage_Matrix.md`, `Active_Recall_Index.md`, and `Exam_Traps_Index.md` after reference-only notes are excluded by the generator.
- Preserve resolved historical audit entries in `knowledge_gaps.md`, but rewrite WikiLinks or completion wording where necessary so history remains accurate and no broken links are introduced.

## Generator Changes

Extend the note metadata and Atlas generator with one optional frontmatter field:

```yaml
exam_scope: core | reference-only
```

Topic notes default to `core`. The two reference-only notes use `exam_scope: reference-only`. The generator will:

- exclude reference-only notes from topic coverage totals, direct-LOS counts, Active Recall, and Exam Traps;
- list them in a separate Reference-Only section of the coverage matrix;
- never classify a Level I LOS token as a Level II direct LOS;
- continue validating their frontmatter and internal links.

This is deliberately limited to one field and three generated outputs; no archive directory or second knowledge-base hierarchy is introduced.

## Verification

Implementation is complete only when all of the following pass:

1. `python scripts\generate_atlas.py` regenerates all Atlas outputs.
2. `python scripts\kb_quality_check.py` reports no quality issues.
3. A full Markdown search finds no remaining pseudo-R-squared, Fed/Yardeni, or deleted legacy-M&A teaching content outside historical audit prose.
4. A full Markdown search finds no broken references to removed Q&A or sections.
5. The scope manifest contains exactly 45 core official learning modules and all ten topic areas.
6. Reference-only notes do not contribute to Level II coverage, Active Recall, Exam Traps, or the formula sheet.
7. The core notes still contain Standard III(D), the correct current VI(A) title, and the change-of-control contingent-put mechanism.
8. `git diff --check` reports no whitespace errors, and the final diff is reviewed for unrelated changes.

## Non-Goals

- Rewriting every existing note or worked example.
- Importing copyrighted curriculum prose or official question sets.
- Applying the 2027 curriculum to a November 2026 study plan.
- Deleting sound Level I foundations merely because they are not directly examinable at Level II.
- Committing or pushing changes without an explicit user request.
