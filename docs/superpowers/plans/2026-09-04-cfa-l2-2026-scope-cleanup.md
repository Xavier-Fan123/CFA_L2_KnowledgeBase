# CFA Level II 2026 Exam-Scope Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the core knowledge base an accurate, low-noise study system for the November 2026 CFA Level II examination.

**Architecture:** Add one `exam_scope` metadata field so generated review tools distinguish core notes from useful reference-only notes. Remove expressly withdrawn and legacy-only teaching content, then add a hand-audited official-module manifest that maps all 45 current learning modules to the existing notes.

**Tech Stack:** Markdown, Python 3 standard library, `unittest`, Obsidian WikiLinks, CFA Institute 2026 official topic outline and September 2026 errata.

**Spec:** `docs/superpowers/specs/2026-09-04-cfa-l2-2026-scope-cleanup-design.md`

## Global Constraints

- The November 2026 examination uses the 2026 curriculum; do not introduce 2027 content.
- CFA Institute official curriculum and errata override Schweser when sources differ.
- All KB and Q&A content remains English-only.
- Do not copy official vignettes or large passages of copyrighted curriculum text.
- Preserve Standard III(D), the current VI(A) title, and the change-of-control contingent-put mechanism.
- Keep sound Level I foundations available as reference-only rather than deleting them.
- Do not commit or push without a separate explicit user request.

---

### Task 1: Make exam scope a tested generator concept

**Files:**

- Create: `scripts/test_generate_atlas.py`
- Modify: `scripts/generate_atlas.py`
- Modify: `scripts/kb_quality_check.py`

**Interfaces:**

- Consumes: optional frontmatter `exam_scope`, whose allowed values are `core` and `reference-only`.
- Produces: `Note.exam_scope: str`, `is_core_note(note: Note) -> bool`, core-only topic totals/recall/traps, and a Reference-Only section in the generated coverage matrix.

- [ ] **Step 1: Write failing generator tests**

Create `scripts/test_generate_atlas.py` with a small `make_note()` factory and these assertions:

```python
from pathlib import Path
import unittest

from scripts.generate_atlas import Note, is_core_note, render_active_recall, render_coverage, render_exam_traps


def make_note(*, stem: str, exam_scope: str, qa: list[str], traps: list[str]) -> Note:
    return Note(
        path=Path(f"14_Corporate_Issuers/{stem}.md"),
        rel=f"14_Corporate_Issuers/{stem}.md",
        stem=stem,
        title=stem.replace("_", " "),
        topic="14 Corporate Issuers",
        source="CFA Level II LOS 1.a" if exam_scope == "core" else "CFA Level I bridge",
        status="evergreen",
        exam_scope=exam_scope,
        level2=["Overview"],
        qa=qa,
        traps=traps,
        worked_count=0,
        los_tokens=["1.a"],
    )


class ExamScopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.core = make_note(stem="Core_Note", exam_scope="core", qa=["Core prompt"], traps=["Core trap"])
        self.reference = make_note(
            stem="Reference_Note",
            exam_scope="reference-only",
            qa=["Reference prompt"],
            traps=["Reference trap"],
        )

    def test_is_core_note(self) -> None:
        self.assertTrue(is_core_note(self.core))
        self.assertFalse(is_core_note(self.reference))

    def test_reference_note_is_excluded_from_active_recall_and_traps(self) -> None:
        notes = [self.core, self.reference]
        self.assertIn("Core prompt", render_active_recall(notes))
        self.assertNotIn("Reference prompt", render_active_recall(notes))
        self.assertIn("Core trap", render_exam_traps(notes))
        self.assertNotIn("Reference trap", render_exam_traps(notes))

    def test_coverage_counts_only_core_and_lists_reference_separately(self) -> None:
        rendered = render_coverage([self.core, self.reference])
        self.assertIn("| 14 Corporate Issuers | 1 | 1 | 1 | 1 | 1 | 0 |", rendered)
        self.assertIn("## Reference-Only Notes", rendered)
        self.assertIn("[[Reference_Note]]", rendered)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests and verify the new interface is absent**

Run: `python -m unittest scripts.test_generate_atlas -v`

Expected: import/construction failures because `Note.exam_scope` and `is_core_note` do not exist.

- [ ] **Step 3: Implement the minimal scope-aware generator**

In `scripts/generate_atlas.py`:

```python
VALID_EXAM_SCOPES = {"core", "reference-only"}


@dataclass
class Note:
    # existing fields...
    exam_scope: str
    # remaining existing fields...


def is_core_note(note: Note) -> bool:
    return note.exam_scope == "core"
```

Set `exam_scope=fm.get("exam_scope", "core")` in `parse_note()`. In `render_coverage()`, build topic summaries and Reading-Level Notes from `core_notes = [note for note in notes if is_core_note(note)]`, then add:

```python
reference_notes = [note for note in notes if not is_core_note(note)]
lines.extend(["", "## Reference-Only Notes", ""])
for note in reference_notes:
    lines.append(f"- {wiki(note.stem)} — {note.source}")
```

Filter `render_active_recall()` and `render_exam_traps()` with `is_core_note(note)`. Remove the source-string special case for GIPS from `coverage_confidence()` because metadata now owns the classification.

In `scripts/kb_quality_check.py`, validate any supplied topic-note field:

```python
exam_scope = fm.get("exam_scope", "core")
if path.parent.name in TOPIC_DIRS and exam_scope not in {"core", "reference-only"}:
    issues.append(f"{rel}: invalid frontmatter `exam_scope` value `{exam_scope}`")
```

- [ ] **Step 4: Run the focused test suite**

Run: `python -m unittest scripts.test_generate_atlas -v`

Expected: 3 tests pass.

- [ ] **Step 5: Review this task without committing**

Run: `git diff -- scripts/generate_atlas.py scripts/kb_quality_check.py scripts/test_generate_atlas.py`

Expected: only the optional metadata field, filtering behavior, validation, and tests described above.

---

### Task 2: Reclassify Level I and deep-GIPS material as reference-only

**Files:**

- Modify: `14_Corporate_Issuers/Capital_Budgeting_Foundations.md`
- Modify: `20_Ethics/GIPS.md`
- Modify: `20_Ethics/Ethics_Overview.md`
- Modify: `20_Ethics/Code_and_Standards.md`
- Modify: `10_Atlas/Master_Index.md`
- Modify: `10_Atlas/Formula_Cheat_Sheet.md`
- Modify: `CLAUDE.md`
- Modify: `README.md`

**Interfaces:**

- Consumes: `exam_scope: reference-only` from Task 1.
- Produces: two still-searchable reference notes that cannot inflate core Level II coverage or review queues.

- [ ] **Step 1: Add explicit metadata and scope warnings**

Add this frontmatter field to both reference notes:

```yaml
exam_scope: reference-only
```

Keep the current capital-budgeting scope warning. Tighten the GIPS warning so its first lines distinguish:

```markdown
> **Reference-only for the 2026 Level II exam:** detailed GIPS firm, composite,
> history, and verification mechanics are not a standalone 2026 Level II reading.
> The examinable core is Standard III(D): performance must be fair, accurate,
> and complete; following GIPS is one way to comply, and false compliance claims violate III(D).
```

- [ ] **Step 2: Keep the examinable III(D) rule in the core note**

In `Code_and_Standards.md`, make the III(D) bullet self-contained and label its link as optional reference:

```markdown
- **III(D) Performance Presentation**: presentations must be **fair, accurate, and complete**; do not cherry-pick accounts or periods. Following **GIPS** is one way to comply, and a false GIPS-compliance claim violates III(D). Detailed GIPS mechanics are reference-only: [[GIPS]].
```

In `Ethics_Overview.md`, move the GIPS link under a `## Reference-only foundation` heading and remove deep GIPS mechanics from the Cross-cutting Exam Traps section.

- [ ] **Step 3: Separate core and reference navigation**

In `Master_Index.md`:

- add `[[2026_Exam_Scope]]` to Review control;
- remove Capital Budgeting from the Corporate Issuers core list;
- remove GIPS from the Ethics core list;
- add a dedicated `## Reference-only foundations` section containing `[[Capital_Budgeting_Foundations]]` and `[[GIPS]]`;
- change Corporate Issuers and Ethics coverage counts to core-only counts.

In `Formula_Cheat_Sheet.md`, rename `## 20 — Ethics & GIPS` to `## 20 — Ethics`, link only `[[Code_and_Standards]]`, and delete the bullet teaching firm-wide compliance, five-to-ten-year history, and third-party verification.

- [ ] **Step 4: Document the metadata convention**

Add `exam_scope: core | reference-only` to the README note-format documentation and explain that omitted means `core`. In `CLAUDE.md`, change the Book 5 mapping from `+ GIPS` to a statement that GIPS is not a standalone Level II reading and only its Standard III(D) treatment belongs to core review.

- [ ] **Step 5: Run focused metadata and navigation checks**

Run:

```powershell
rg -n "exam_scope: reference-only" 14_Corporate_Issuers\Capital_Budgeting_Foundations.md 20_Ethics\GIPS.md
rg -n "Reference-only foundations|2026_Exam_Scope" 10_Atlas\Master_Index.md
rg -n "firm-wide|5 years|build to 10|verification recommended" 10_Atlas\Formula_Cheat_Sheet.md
```

Expected: two metadata matches; Master Index contains both navigation changes; the formula-sheet search returns no matches.

---

### Task 3: Remove withdrawn and legacy-only exam content

**Files:**

- Modify: `11_Quantitative_Methods/Logistic_Regression.md`
- Modify: `14_Corporate_Issuers/Corporate_Restructurings.md`
- Modify: `15_Equity_Investments/Market_Based_Valuation.md`
- Modify: `16_Fixed_Income/Bonds_With_Embedded_Options.md`
- Modify: `90_QA_Log/QA_Log.md`

**Interfaces:**

- Consumes: the September 2026 official errata and the approved classification rules.
- Produces: core topic notes containing only current 2026 teaching content, while retaining the current contingent-put LOS.

- [ ] **Step 1: Remove pseudo-R-squared from Logistic Regression**

Delete the third Testing item, the pseudo-R-squared Fit cell, and the related Exam Trap. In the saved Q&A answer, end after the likelihood-ratio-test example and the “LR test, not F-test” trap. Do not remove MLE, log-odds interpretation, pointwise marginal effects, or the LR test.

- [ ] **Step 2: Remove the legacy Equity Q&A**

Delete the entire `2026-07-12 — Fed model vs. Yardeni model (legacy curriculum)` Q&A entry from `Market_Based_Valuation.md` and its matching line in `QA_Log.md`.

- [ ] **Step 3: Remove the legacy M&A section and Q&A**

Delete `## Legacy M&A Vocabulary (NOT 2026 L2 curriculum)` through the line immediately before `## Exam Traps`. Delete these three Q&A entries:

- `2026-08-02 — Poison pill vs. poison put`
- `2026-07-11 — Horizontal vs. vertical merger`
- `2026-07-11 — Takeover defenses: crown jewel, Pac-Man, white knight`

Delete their matching `QA_Log.md` lines.

- [ ] **Step 4: Preserve only the current fixed-income mechanism**

In the convertible-bond paragraph in `Bonds_With_Embedded_Options.md`, retain:

- conversion-price/ratio adjustments;
- a change-of-control contingent put exercisable for a specified window;
- the alternative lowered conversion price;
- hard-versus-soft put settlement;
- forced conversion for a callable convertible.

Delete the market label “poison put,” the takeover-deterrent explanation, the par/101 generalization, and the cross-link to the removed Corporate Restructurings legacy section.

- [ ] **Step 5: Prove the removed content is absent from core notes**

Run:

```powershell
rg -n -i "pseudo-R|Fed model|Yardeni|Legacy M&A|poison pill|poison put|Pac-Man|white knight|white squire|horizontal merger|vertical merger" 11_Quantitative_Methods 12_Economics 13_Financial_Statement_Analysis 14_Corporate_Issuers 15_Equity_Investments 16_Fixed_Income 17_Derivatives 18_Alternative_Investments 19_Portfolio_Management 20_Ethics
```

Expected: no matches.

Run:

```powershell
rg -n -i "change-of-control|contingent put|hard.*put|soft.*put" 16_Fixed_Income\Bonds_With_Embedded_Options.md
```

Expected: the current convertible-bond protection mechanics remain.

---

### Task 4: Add the official 45-module exam-scope manifest

**Files:**

- Create: `10_Atlas/2026_Exam_Scope.md`

**Interfaces:**

- Consumes: official 2026 topic outline, official topic weights, September 2026 errata, and existing note WikiLinks.
- Produces: a human-auditable one-row-per-module scope baseline.

- [ ] **Step 1: Create the manifest header and topic-weight table**

Use frontmatter aliases `2026 Exam Scope`, `2026 Curriculum Map`, tags `[CFA-L2, atlas, scope, 2026]`, date `2026-09-04`, status `evergreen`, and source `CFA Institute 2026 Level II Topic Outlines and September 2026 Curriculum Errata Notice`.

The weight table must contain:

| KB topic | Official page label | Weight |
|---|---|---:|
| Quantitative Methods | Quantitative Methods | 5-10% |
| Economics | Economics | 5-10% |
| Financial Statement Analysis | Financial Statement Analysis | 10-15% |
| Corporate Issuers | Corporate Finance | 5-10% |
| Equity Investments | Equities | 10-15% |
| Fixed Income | Fixed Income | 10-15% |
| Derivatives | Derivatives and Risk Management | 5-10% |
| Alternative Investments | Alternative Investments | 5-10% |
| Portfolio Management | Portfolio Construction | 10-15% |
| Ethics | Ethical and Professional Standards | 10-15% |

- [ ] **Step 2: Add exactly 45 module rows**

Use one table with columns `Topic`, `LM`, `Official 2026 learning module`, `Primary KB note`, and `Status`. Add these mappings:

```text
Quantitative Methods | 1 | Basics of Multiple Regression and Underlying Assumptions | [[Multiple_Regression]] | Core
Quantitative Methods | 2 | Evaluating Regression Model Fit and Interpreting Model Results | [[Multiple_Regression]] | Core; shared note
Quantitative Methods | 3 | Model Misspecification | [[Model_Misspecification]]; [[Regression_Assumption_Violations]]; [[Breusch_Pagan_Test]] | Core; split notes
Quantitative Methods | 4 | Extensions of Multiple Regression | [[Multiple_Regression]]; [[Logistic_Regression]] | Core; split notes
Quantitative Methods | 5 | Time-Series Analysis | [[Time_Series_Analysis]] | Core
Quantitative Methods | 6 | Machine Learning | [[Machine_Learning]] | Core
Quantitative Methods | 7 | Big Data Projects | [[Big_Data_Projects]] | Core
Economics | 1 | Currency Exchange Rates: Understanding Equilibrium Value | [[Currency_Exchange_Rates]] | Core
Economics | 2 | Economic Growth | [[Economic_Growth]] | Core
Financial Statement Analysis | 1 | Intercorporate Investments | [[Intercorporate_Investments]] | Core
Financial Statement Analysis | 2 | Employee Compensation: Post-Employment and Share-Based | [[Employee_Compensation]] | Core
Financial Statement Analysis | 3 | Multinational Operations | [[Multinational_Operations]] | Core
Financial Statement Analysis | 4 | Analysis of Financial Institutions | [[Analysis_of_Financial_Institutions]] | Core
Financial Statement Analysis | 5 | Evaluating Quality of Financial Reports | [[Quality_of_Financial_Reports]] | Core
Financial Statement Analysis | 6 | Integration of Financial Statement Analysis Techniques | [[Integration_of_FSA_Techniques]] | Core
Corporate Issuers | 1 | Analysis of Dividends and Share Repurchases | [[Dividends_and_Share_Repurchases]] | Core
Corporate Issuers | 2 | Environmental, Social, and Governance (ESG) Considerations in Investment Analysis | [[ESG_and_Corporate_Governance]] | Core
Corporate Issuers | 3 | Cost of Capital: Advanced Topics | [[Cost_of_Capital]] | Core
Corporate Issuers | 4 | Corporate Restructuring | [[Corporate_Restructurings]] | Core
Equity Valuation | 1 | Equity Valuation: Applications and Processes | [[Equity_Valuation_Process]] | Core
Equity Valuation | 2 | Discounted Dividend Valuation | [[Dividend_Discount_Models]] | Core
Equity Valuation | 3 | Free Cash Flow Valuation | [[Free_Cash_Flow_Valuation]] | Core
Equity Valuation | 4 | Market-Based Valuation: Price and Enterprise Value Multiples | [[Market_Based_Valuation]] | Core
Equity Valuation | 5 | Residual Income Valuation | [[Residual_Income]] | Core
Equity Valuation | 6 | Private Company Valuation | [[Private_Company_Valuation]] | Core
Fixed Income | 1 | The Term Structure and Interest Rate Dynamics | [[Term_Structure]] | Core
Fixed Income | 2 | The Arbitrage-Free Valuation Framework | [[Arbitrage_Free_Valuation]] | Core
Fixed Income | 3 | Valuation and Analysis of Bonds with Embedded Options | [[Bonds_With_Embedded_Options]] | Core
Fixed Income | 4 | Credit Analysis Models | [[Credit_Analysis_Models]] | Core
Fixed Income | 5 | Credit Default Swaps | [[Credit_Default_Swaps]] | Core
Derivatives | 1 | Pricing and Valuation of Forward Commitments | [[Forward_Commitments]] | Core
Derivatives | 2 | Valuation of Contingent Claims | [[Options_Valuation]] | Core
Alternative Investments | 1 | Introduction to Commodities and Commodity Derivatives | [[Commodities]] | Core
Alternative Investments | 2 | Overview of Types of Real Estate Investment | [[Real_Estate]] | Core
Alternative Investments | 3 | Investments in Real Estate through Publicly Traded Securities | [[Publicly_Traded_Real_Estate]] | Core
Alternative Investments | 4 | Hedge Fund Strategies | [[Hedge_Fund_Strategies]] | Core
Portfolio Management | 1 | Economics and Investment Markets | [[Economics_and_Investment_Markets]] | Core
Portfolio Management | 2 | Analysis of Active Portfolio Management | [[Active_Portfolio_Management]] | Core
Portfolio Management | 3 | Exchange-Traded Funds: Mechanics and Applications | [[Exchange_Traded_Funds]] | Core
Portfolio Management | 4 | Using Multifactor Models | [[Multifactor_Models]] | Core
Portfolio Management | 5 | Measuring and Managing Market Risk | [[Measuring_Managing_Market_Risk]] | Core
Portfolio Management | 6 | Backtesting and Simulation | [[Backtesting_and_Simulation]] | Core
Ethical and Professional Standards | 1 | Code of Ethics and Standards of Professional Conduct | [[Code_and_Standards]] | Core
Ethical and Professional Standards | 2 | Guidance for Standards I-VII | [[Code_and_Standards]] | Core; shared note
Ethical and Professional Standards | 3 | Application of the Code and Standards: Level II | [[Application_of_the_Code_and_Standards]] | Core
```

State explicitly that the Quantitative Methods appendices are references and are not counted as a 46th core module.

- [ ] **Step 3: Add the scope-exclusion and errata record**

Add three concise sections:

- `Not directly examinable in 2026`: Capital Budgeting is Level I; deep GIPS mechanics are reference-only; Fed/Yardeni, pseudo-R-squared, and legacy M&A defense vocabulary were removed from core review.
- `Still examinable despite nearby deletions`: Standard III(D), VI(A) Avoid or Disclose Conflicts, and change-of-control contingent-put protection.
- `September 2026 errata check`: the 24 August R-squared correction is already reflected; two 13 August Machine Learning entries are accessibility-only; stale pseudo-R-squared prose was removed; previously corrected pooling-of-interests residue, private-company-premium wording, SOFR transition wording, and VI(A) naming remain aligned.

Include links to the official Level II page, the official combined 2026 topic outline, the official September 2026 errata, and the CFA Institute announcement that 2027 changes apply from February 2027.

- [ ] **Step 4: Count and validate the manifest**

Run:

```powershell
$moduleRows = Get-Content -LiteralPath '10_Atlas\2026_Exam_Scope.md' | Where-Object { $_ -match '^\| (Quantitative Methods|Economics|Financial Statement Analysis|Corporate Issuers|Equity Valuation|Fixed Income|Derivatives|Alternative Investments|Portfolio Management|Ethical and Professional Standards) \| [0-9]+ \|' }
$moduleRows.Count
```

Expected: `45`.

---

### Task 5: Reconcile audit history and regenerate review artifacts

**Files:**

- Modify: `00_Inbox/knowledge_gaps.md`
- Regenerate: `10_Atlas/LOS_Coverage_Matrix.md`
- Regenerate: `10_Atlas/Active_Recall_Index.md`
- Regenerate: `10_Atlas/Exam_Traps_Index.md`

**Interfaces:**

- Consumes: cleaned topic notes and scope-aware generator.
- Produces: internally consistent audit history and core-only review artifacts.

- [ ] **Step 1: Reconcile the historical gap record**

Add a top entry dated `2026-09-04` recording:

- the official 45-module mapping found no missing current module;
- the September errata review removed pseudo-R-squared;
- Fed/Yardeni and legacy M&A vocabulary were removed from core notes;
- Capital Budgeting and deep GIPS were reclassified as reference-only;
- current III(D) and contingent-put mechanics were retained.

In the earlier legacy-M&A entry, preserve the discovery history but append that the optional section was removed from the core note on 2026-09-04. Do not delete historical evidence merely because the resulting content was later pruned.

- [ ] **Step 2: Regenerate all three Atlas files**

Run: `python scripts\generate_atlas.py`

Expected:

```text
wrote 10_Atlas/LOS_Coverage_Matrix.md
wrote 10_Atlas/Active_Recall_Index.md
wrote 10_Atlas/Exam_Traps_Index.md
```

- [ ] **Step 3: Verify the generated scope behavior**

Run:

```powershell
rg -n "Reference-Only Notes|Capital_Budgeting_Foundations|GIPS" 10_Atlas\LOS_Coverage_Matrix.md
rg -n "Capital_Budgeting_Foundations|\[\[GIPS\]\]" 10_Atlas\Active_Recall_Index.md 10_Atlas\Exam_Traps_Index.md
```

Expected: the coverage matrix has a Reference-Only section containing both notes; Active Recall and Exam Traps return no matches.

---

### Task 6: Run full verification and review the final diff

**Files:**

- Verify all changed files; no additional file is created solely for this task.

**Interfaces:**

- Consumes: Tasks 1-5.
- Produces: evidence that the KB is structurally valid, core-scope clean, and still retains the required current concepts.

- [ ] **Step 1: Run all unit tests**

Run: `python -m unittest discover -s scripts -p 'test_*.py' -v`

Expected: all discovered tests pass with zero errors and failures.

- [ ] **Step 2: Run the KB quality checker**

Run: `python scripts\kb_quality_check.py`

Expected: `No quality issues found.`

- [ ] **Step 3: Re-run the module count**

Run the `$moduleRows` command from Task 4.

Expected: exactly `45`.

- [ ] **Step 4: Verify removed and retained concepts**

Run:

```powershell
rg -n -i "pseudo-R|Fed model|Yardeni|Legacy M&A|poison pill|poison put|Pac-Man|white knight|white squire|horizontal merger|vertical merger" 11_Quantitative_Methods 12_Economics 13_Financial_Statement_Analysis 14_Corporate_Issuers 15_Equity_Investments 16_Fixed_Income 17_Derivatives 18_Alternative_Investments 19_Portfolio_Management 20_Ethics
rg -n "III\(D\) Performance Presentation|Avoid or Disclose Conflicts|change-of-control|contingent put" 20_Ethics 16_Fixed_Income\Bonds_With_Embedded_Options.md
```

Expected: the obsolete-content search returns no matches; the retained-content search finds all three current concepts.

- [ ] **Step 5: Check language, links, whitespace, and scope metadata**

Run:

```powershell
rg -n '[\p{Han}]' . --glob '*.md'
git diff --check
git status --short
git diff --stat
```

Expected: no CJK matches, no whitespace errors, and only the approved spec/plan, scope metadata/generator/tests, scope manifest, cleaned notes, reconciled indexes/history, README, and CLAUDE manual appear as changes.

- [ ] **Step 6: Review the complete diff without committing**

Run: `git diff -- . ':(exclude)10_Atlas/Active_Recall_Index.md' ':(exclude)10_Atlas/Exam_Traps_Index.md' ':(exclude)10_Atlas/LOS_Coverage_Matrix.md'`, then review the three generated files separately with `git diff --stat` and focused searches.

Expected: no unrelated edits, no accidental deletion of current LOS material, and no commit or push.
