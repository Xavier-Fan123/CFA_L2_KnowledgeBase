from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS_DIR = ROOT / "10_Atlas"
TOPIC_DIRS = {
    "11_Quantitative_Methods": "11 Quantitative Methods",
    "12_Economics": "12 Economics",
    "13_Financial_Statement_Analysis": "13 Financial Statement Analysis",
    "14_Corporate_Issuers": "14 Corporate Issuers",
    "15_Equity_Investments": "15 Equity Investments",
    "16_Fixed_Income": "16 Fixed Income",
    "17_Derivatives": "17 Derivatives",
    "18_Alternative_Investments": "18 Alternative Investments",
    "19_Portfolio_Management": "19 Portfolio Management",
    "20_Ethics": "20 Ethics",
}


@dataclass
class Note:
    path: Path
    rel: str
    stem: str
    title: str
    topic: str
    source: str
    status: str
    level2: list[str]
    qa: list[str]
    traps: list[str]
    worked_count: int
    los_tokens: list[str]


def wiki(stem: str) -> str:
    return f"[[{stem}]]"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def first_h1(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback.replace("_", " ")


def section_body(lines: list[str], heading: str) -> list[str]:
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    if start is None:
        return []
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break
    return lines[start:end]


def extract_los_tokens(text: str) -> list[str]:
    tokens: set[str] = set()
    for match in re.finditer(r"\bLOS\s+([0-9]+)\.([a-z])\s*[–-]\s*([0-9]+)\.([a-z])\b", text):
        a_num, a_chr, b_num, b_chr = match.groups()
        if a_num == b_num:
            for code in range(ord(a_chr), ord(b_chr) + 1):
                tokens.add(f"{a_num}.{chr(code)}")
    for match in re.finditer(r"\bLOS\s+([0-9]+)\.([a-z])\s*[–-]\s*\.\s*([a-z])\b", text):
        num, a_chr, b_chr = match.groups()
        for code in range(ord(a_chr), ord(b_chr) + 1):
            tokens.add(f"{num}.{chr(code)}")
    for match in re.finditer(r"\bLOS\s+([0-9]+)\.([a-z])\b", text):
        tokens.add(f"{match.group(1)}.{match.group(2)}")
    for match in re.finditer(r"\(([0-9]+)\.([a-z])(?:\s*[–-]\s*([0-9]+)\.([a-z])|\s*[–-]\s*([a-z]))?\)", text):
        num, start, end_num, end_chr, short_end = match.groups()
        if end_chr and end_num == num:
            for code in range(ord(start), ord(end_chr) + 1):
                tokens.add(f"{num}.{chr(code)}")
        elif short_end:
            for code in range(ord(start), ord(short_end) + 1):
                tokens.add(f"{num}.{chr(code)}")
        else:
            tokens.add(f"{num}.{start}")
    return sorted(tokens, key=lambda token: (int(token.split(".")[0]), token.split(".")[1]))


def parse_note(path: Path) -> Note:
    text = read_text(path)
    lines = text.splitlines()
    fm = parse_frontmatter(text)
    rel = path.relative_to(ROOT).as_posix()
    topic = TOPIC_DIRS.get(path.parent.name, path.parent.name)
    level2 = [line[3:].strip() for line in lines if line.startswith("## ")]
    qa = [line[4:].strip() for line in section_body(lines, "## Q&A") if line.startswith("### ") and "—" in line]
    trap_lines = []
    for line in section_body(lines, "## Exam Traps"):
        stripped = line.strip()
        if stripped.startswith("- "):
            trap_lines.append(stripped[2:].strip())
    worked_count = sum(1 for line in lines if "worked" in line.lower() or "example" in line.lower())
    return Note(
        path=path,
        rel=rel,
        stem=path.stem,
        title=first_h1(text, path.stem),
        topic=topic,
        source=fm.get("source", ""),
        status=fm.get("status", ""),
        level2=level2,
        qa=qa,
        traps=trap_lines,
        worked_count=worked_count,
        los_tokens=extract_los_tokens(text),
    )


def load_notes() -> list[Note]:
    notes: list[Note] = []
    for dirname in TOPIC_DIRS:
        for path in sorted((ROOT / dirname).glob("*.md")):
            notes.append(parse_note(path))
    return notes


def coverage_confidence(note: Note) -> str:
    if "Overview" in note.stem or note.stem.endswith("_Overview"):
        return "Overview map"
    if "No standalone GIPS reading" in note.source:
        return "Reference-only"
    if note.los_tokens:
        return "Direct LOS"
    if "LOS" in note.source:
        return "Source LOS"
    return "Needs source detail"


def is_overview_note(note: Note) -> bool:
    return "Overview" in note.stem or note.stem.endswith("_Overview")


def render_coverage(notes: list[Note]) -> str:
    by_topic: dict[str, list[Note]] = defaultdict(list)
    for note in notes:
        by_topic[note.topic].append(note)

    lines = [
        "---",
        "aliases: [LOS Coverage Matrix, Coverage Matrix]",
        "tags: [CFA-L2, atlas, coverage]",
        "date: 2026-06-05",
        "status: evergreen",
        "source: Generated from note frontmatter and section headings by scripts/generate_atlas.py",
        "---",
        "",
        "# LOS Coverage Matrix",
        "",
        "Generated from each note's `source` field, headings, `## Exam Traps`, and `## Q&A` sections. Use this as a maintenance map: it verifies that every reading has a home note, not that every official vignette has been imported.",
        "",
        "## Topic Summary",
        "",
        "| Topic | Notes | Evergreen | Q&A | Trap bullets | Direct LOS notes | Review flags |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for topic in TOPIC_DIRS.values():
        topic_notes = by_topic[topic]
        evergreen = sum(1 for note in topic_notes if note.status == "evergreen")
        qa_count = sum(len(note.qa) for note in topic_notes)
        trap_count = sum(len(note.traps) for note in topic_notes)
        direct_los = sum(1 for note in topic_notes if coverage_confidence(note) == "Direct LOS")
        flags = sum(1 for note in topic_notes if coverage_confidence(note) == "Needs source detail")
        lines.append(f"| {topic} | {len(topic_notes)} | {evergreen} | {qa_count} | {trap_count} | {direct_los} | {flags} |")

    lines.extend(["", "## Reading-Level Notes", ""])
    for topic in TOPIC_DIRS.values():
        lines.extend([f"### {topic}", ""])
        for note in by_topic[topic]:
            source = note.source or "No `source` field"
            evidence = f"{len(note.level2)} sections; {len(note.qa)} Q&A; {len(note.traps)} traps; {note.worked_count} worked/example markers"
            if note.los_tokens:
                evidence += f"; LOS tokens: {', '.join(note.los_tokens[:12])}"
                if len(note.los_tokens) > 12:
                    evidence += ", ..."
            lines.append(f"- {wiki(note.stem)} — **{coverage_confidence(note)}**")
            lines.append(f"  - Source / LOS: {source}")
            lines.append(f"  - Evidence: {evidence}")
        lines.append("")

    flags = [
        note
        for note in notes
        if not is_overview_note(note)
        and coverage_confidence(note) != "Reference-only"
        and (coverage_confidence(note) == "Needs source detail" or not note.qa or not note.traps)
    ]
    lines.extend(["", "## Maintenance Flags", ""])
    if not flags:
        lines.append("No generated maintenance flags.")
    else:
        for note in flags:
            reasons = []
            if coverage_confidence(note) == "Needs source detail":
                reasons.append("source lacks parseable LOS/detail")
            if not note.qa:
                reasons.append("no Q&A")
            if not note.traps:
                reasons.append("no Exam Traps")
            lines.append(f"- {wiki(note.stem)}: {', '.join(reasons)}.")
    lines.append("")
    return "\n".join(lines)


def render_active_recall(notes: list[Note]) -> str:
    by_topic: dict[str, list[tuple[Note, str]]] = defaultdict(list)
    for note in notes:
        for qa in note.qa:
            by_topic[note.topic].append((note, qa))
    lines = [
        "---",
        "aliases: [Active Recall Index, Q&A Index]",
        "tags: [CFA-L2, atlas, active-recall]",
        "date: 2026-06-05",
        "status: evergreen",
        "source: Generated from note Q&A headings by scripts/generate_atlas.py",
        "---",
        "",
        "# Active Recall Index",
        "",
        "Each prompt links back to the note that contains the full answer. Use this as a compact review queue before drilling the underlying note.",
        "",
    ]
    total = sum(len(items) for items in by_topic.values())
    lines.append(f"Total prompts: **{total}**.")
    for topic in TOPIC_DIRS.values():
        items = by_topic.get(topic, [])
        lines.extend(["", f"## {topic}", ""])
        if not items:
            lines.append("- No Q&A prompts found.")
            continue
        for note, qa in items:
            lines.append(f"- {qa} -> {wiki(note.stem)}")
    lines.append("")
    return "\n".join(lines)


def render_exam_traps(notes: list[Note]) -> str:
    by_topic: dict[str, list[Note]] = defaultdict(list)
    for note in notes:
        if note.traps:
            by_topic[note.topic].append(note)
    lines = [
        "---",
        "aliases: [Exam Traps Index, Trap Index]",
        "tags: [CFA-L2, atlas, exam-traps]",
        "date: 2026-06-05",
        "status: evergreen",
        "source: Generated from note Exam Traps sections by scripts/generate_atlas.py",
        "---",
        "",
        "# Exam Traps Index",
        "",
        "Cross-topic collection of `## Exam Traps` bullets. Use it for final-pass review and to identify repeated confusion patterns.",
        "",
    ]
    for topic in TOPIC_DIRS.values():
        topic_notes = by_topic.get(topic, [])
        lines.extend(["", f"## {topic}", ""])
        if not topic_notes:
            lines.append("- No exam traps found.")
            continue
        for note in topic_notes:
            lines.append(f"### {note.title} -> {wiki(note.stem)}")
            for trap in note.traps:
                lines.append(f"- {trap}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    notes = load_notes()
    outputs = {
        "LOS_Coverage_Matrix.md": render_coverage(notes),
        "Active_Recall_Index.md": render_active_recall(notes),
        "Exam_Traps_Index.md": render_exam_traps(notes),
    }
    ATLAS_DIR.mkdir(exist_ok=True)
    for filename, content in outputs.items():
        (ATLAS_DIR / filename).write_text(content, encoding="utf-8")
        print(f"wrote 10_Atlas/{filename}")


if __name__ == "__main__":
    main()
