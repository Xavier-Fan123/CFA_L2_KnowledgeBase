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
