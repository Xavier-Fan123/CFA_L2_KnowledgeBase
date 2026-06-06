from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK_DIRS = (
    "00_Inbox",
    "10_Atlas",
    "11_Quantitative_Methods",
    "12_Economics",
    "13_Financial_Statement_Analysis",
    "14_Corporate_Issuers",
    "15_Equity_Investments",
    "16_Fixed_Income",
    "17_Derivatives",
    "18_Alternative_Investments",
    "19_Portfolio_Management",
    "20_Ethics",
    "90_QA_Log",
)
TOPIC_DIRS = tuple(d for d in CHECK_DIRS if re.match(r"^[0-9]{2}_", d) and d not in {"00_Inbox", "10_Atlas", "90_QA_Log"})
REQUIRED_FRONTMATTER = ("aliases", "tags", "date", "status")


def md_files() -> list[Path]:
    files: list[Path] = []
    for dirname in CHECK_DIRS:
        base = ROOT / dirname
        if base.exists():
            files.extend(sorted(base.glob("*.md")))
    return files


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return {}


def is_overview(path: Path) -> bool:
    return path.stem.endswith("_Overview") or path.stem in {"Master_Index", "Formula_Cheat_Sheet", "QA_Log", "knowledge_gaps"}


def strip_code_blocks(text: str) -> str:
    out: list[str] = []
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    return "\n".join(out)


def wikilink_targets(text: str) -> list[str]:
    targets = []
    visible_text = re.sub(r"`[^`]*`", "", strip_code_blocks(text))
    for raw in re.findall(r"\[\[([^\]]+)\]\]", visible_text):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            targets.append(target)
    return targets


def suspicious_hard_wrap(text: str) -> list[int]:
    lines = text.splitlines()
    hits: list[int] = []
    in_code = False
    for idx, line in enumerate(lines[:-1], 1):
        stripped = line.strip()
        nxt = lines[idx].strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not stripped or not nxt:
            continue
        if stripped.startswith(("#", "|", "---")) or nxt.startswith(("#", "|", "---")):
            continue
        if re.match(r"^(\s*)(([-*])|(\d+[.)]))\s+", line) and re.match(r"^(\s*)(([-*])|(\d+[.)]))\s+", lines[idx]):
            continue
        if stripped.endswith((".", ":", ";", "?", "!", "`", "]", ")")):
            continue
        if re.match(r"^(\s*)(([-*])|(\d+[.)]))\s+", lines[idx]):
            continue
        if nxt.startswith(("**Q:**", "**A:**", "Related:")):
            continue
        if len(stripped) > 40:
            hits.append(idx)
    return hits


def is_table_line(line: str) -> bool:
    return line.lstrip().startswith("|")


def split_table_cells(line: str) -> list[str]:
    stripped = line.strip()
    cells: list[str] = []
    current: list[str] = []
    in_code = False
    in_wikilink = False
    i = 1 if stripped.startswith("|") else 0

    while i < len(stripped):
        char = stripped[i]
        nxt = stripped[i + 1] if i + 1 < len(stripped) else ""

        if char == "\\" and nxt:
            current.append(char)
            current.append(nxt)
            i += 2
            continue
        if char == "`":
            in_code = not in_code
            current.append(char)
        elif not in_code and char == "[" and nxt == "[":
            in_wikilink = True
            current.append(char)
            current.append(nxt)
            i += 1
        elif not in_code and char == "]" and nxt == "]":
            in_wikilink = False
            current.append(char)
            current.append(nxt)
            i += 1
        elif char == "|" and not in_code and not in_wikilink:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        i += 1

    tail = "".join(current).strip()
    if tail or not stripped.endswith("|"):
        cells.append(tail)
    return cells


def is_table_separator(line: str) -> bool:
    cells = split_table_cells(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def markdown_table_issues(text: str) -> list[str]:
    lines = text.splitlines()
    issues: list[str] = []
    in_code = False
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code or not is_table_line(lines[i]):
            i += 1
            continue

        start = i
        block: list[tuple[int, str]] = []
        while i < len(lines) and is_table_line(lines[i]):
            block.append((i + 1, lines[i]))
            i += 1

        if start > 0 and lines[start - 1].strip():
            issues.append(f"line {start + 1}: table should be preceded by a blank line")
        if i < len(lines) and lines[i].strip():
            issues.append(f"line {i}: table should be followed by a blank line")

        for line_no, line in block:
            if line[:1].isspace():
                issues.append(f"line {line_no}: table line is indented")

        if len(block) < 2:
            issues.append(f"line {block[0][0]}: table-like line is missing a separator row")
            continue

        header_cells = split_table_cells(block[0][1])
        expected = len(header_cells)
        if any(cell == "" for cell in header_cells):
            issues.append(f"line {block[0][0]}: table header has an empty cell")
        if not is_table_separator(block[1][1]):
            issues.append(f"line {block[1][0]}: table separator row is invalid")
        elif len(split_table_cells(block[1][1])) != expected:
            issues.append(f"line {block[1][0]}: table separator column count does not match header")

        for line_no, line in block[2:]:
            actual = len(split_table_cells(line))
            if actual != expected:
                issues.append(f"line {line_no}: table row has {actual} cells, expected {expected}")

    return issues


def main() -> int:
    files = md_files()
    stems = [path.stem for path in files]
    stem_counts = Counter(stems)
    note_names = set(stems)
    issues: list[str] = []

    for stem, count in stem_counts.items():
        if count > 1:
            issues.append(f"duplicate note stem `{stem}` appears {count} times")

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        text = read_text(path)
        fm = parse_frontmatter(text)
        lines = text.splitlines()

        if not text.strip():
            issues.append(f"{rel}: empty file")
            continue

        if sum(1 for line in lines if line.strip().startswith("```")) % 2:
            issues.append(f"{rel}: unbalanced code fence")

        for key in REQUIRED_FRONTMATTER:
            if key not in fm:
                issues.append(f"{rel}: missing frontmatter `{key}`")

        if path.parent.name in TOPIC_DIRS:
            if "source" not in fm:
                issues.append(f"{rel}: missing frontmatter `source`")
            if not is_overview(path):
                if "## Exam Traps" not in text:
                    issues.append(f"{rel}: missing `## Exam Traps`")
                if "## Q&A" not in text:
                    issues.append(f"{rel}: missing `## Q&A`")

        for target in wikilink_targets(text):
            if target not in note_names:
                issues.append(f"{rel}: broken wikilink `[[{target}]]`")

        hard_wraps = suspicious_hard_wrap(text)
        if hard_wraps:
            shown = ", ".join(str(n) for n in hard_wraps[:5])
            issues.append(f"{rel}: suspicious hard-wrap candidate line(s) {shown}")

        for table_issue in markdown_table_issues(text):
            issues.append(f"{rel}: {table_issue}")

    print(f"Checked {len(files)} markdown files.")
    if issues:
        print(f"Found {len(issues)} issue(s):")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("No quality issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
