# CFA Level II Knowledge Base

A structured, Claude Code-powered knowledge base for the CFA Level II exam — covering all ten topic areas, turning every Q&A into searchable, reviewable wiki notes.

Built on the same logic as the LPG Trading Knowledge Base, but with a **zero-dependency adaptation**: search, citation, and Q&A write-back are all done with native Claude Code tools (Grep / Read / Edit) — **no Python, no API key required**. Pure Markdown, openable directly in [Obsidian](https://obsidian.md/) for graph view and full-text search.

## Architecture

```
User asks a CFA question
  │
  ▼
CLAUDE.md (behavioral rules)
  │
  ├─ Rule 1: Search KB first ──► Grep/Glob over this KB's .md notes
  │                                   │
  │                                   ▼
  │                             Read relevant notes → Answer with citations
  │
  ├─ Rule 2: Authoritative fallback ─► Not in KB → pdftotext the Schweser PDFs (sibling source folder)
  │
  ├─ Rule 3: Write back Q&A ──► Append valuable Q&A to the topic note's ## Q&A section + 90_QA_Log
  │
  ├─ Rule 4: Cite sources ──► Clearly separate "from KB / curriculum" vs "from general knowledge"
  │
  └─ Rule 5: Gap detection ──► Uncovered topics logged to 00_Inbox/knowledge_gaps.md
```

## Directory Structure

```
CFA_L2_KnowledgeBase/
├── 00_Inbox/                       # Inbox: knowledge gaps, incoming material
│   └── knowledge_gaps.md
├── 10_Atlas/                       # Index
│   ├── Master_Index.md             # Map of Content with all WikiLinks
│   ├── LOS_Coverage_Matrix.md      # Generated coverage/maintenance matrix
│   ├── Active_Recall_Index.md      # Generated Q&A prompt index
│   └── Exam_Traps_Index.md         # Generated trap index
│
├── 11_Quantitative_Methods/        # Quantitative Methods
├── 12_Economics/                   # Economics
├── 13_Financial_Statement_Analysis/# Financial Statement Analysis
├── 14_Corporate_Issuers/           # Corporate Issuers
├── 15_Equity_Investments/          # Equity Investments
├── 16_Fixed_Income/                # Fixed Income
├── 17_Derivatives/                 # Derivatives
├── 18_Alternative_Investments/     # Alternative Investments
├── 19_Portfolio_Management/        # Portfolio Management
├── 20_Ethics/                      # Ethical and Professional Standards
│
├── 90_QA_Log/                      # Chronological Q&A log across all topics
│   └── QA_Log.md
├── scripts/                        # Optional maintenance scripts
│
├── CLAUDE.md                       # Claude Code behavioral rules (auto-loaded)
└── README.md
```

## Sources

The authoritative basis for this KB is the official / Schweser material that lives in a **sibling
source folder** under the parent CFA directory (`../`). That folder's on-disk name contains non-ASCII
characters, so do not hardcode it — discover the real paths at runtime with Glob, e.g.
`Glob(pattern="../**/SchweserNotes Book *.pdf")`. The folder contains:

- Schweser Notes Book 1-5 + Quicksheet (`*SchweserNotes Book *.pdf`)
- CFA Institute official curriculum (`cfa-program2026L2V*.PDF`)
- End-of-chapter questions and answers

PDFs are read with `pdftotext` (available on this machine at `/mingw64/bin/pdftotext`). Each note's
`source:` field records its origin (e.g. `Schweser Book 1, Module 2, LOS 2.c`).

## Note Format

Every wiki note follows a standardized structure:

- **YAML frontmatter**: `aliases`, `tags`, `date`, `status` (`seed` → `incubating` → `evergreen`), `source` (curriculum reference)
- **Body**: concept explanation
- **Exam Traps**: high-frequency mistakes
- **Q&A**: question-answer pairs distilled from conversations (dated)

## status Lifecycle

| status | Meaning |
|--------|---------|
| `seed` | Placeholder skeleton — title/outline only, awaiting content |
| `incubating` | Has real content but does not yet fully cover the LOS |
| `evergreen` | Complete, aligned to curriculum, ready to review |

## How to Use

1. Open this folder in Claude Code — `CLAUDE.md` loads automatically; just ask questions.
2. Each time you ask a CFA question, Claude searches this KB first, answers with `[[WikiLink]]` citations, and writes valuable Q&A back into the relevant note.
3. (Optional) Open this folder in Obsidian for the WikiLink graph and full-text search.

## Maintenance

Optional generated review indexes live in `10_Atlas/`:

- `LOS_Coverage_Matrix.md`: coverage and maintenance view by topic/note.
- `Active_Recall_Index.md`: every saved Q&A heading as a review prompt.
- `Exam_Traps_Index.md`: all `## Exam Traps` bullets in one final-review sheet.

Regenerate and check them with:

```powershell
python scripts\generate_atlas.py
python scripts\kb_quality_check.py
```

## Inspired By

Follows the "LLM Knowledge Base" pattern of the LPG Trading Knowledge Base — use an LLM to ingest source material, compile structured wikis, answer complex questions, and grow the KB incrementally through use.
