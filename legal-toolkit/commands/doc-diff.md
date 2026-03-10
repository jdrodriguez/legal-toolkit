---
description: Compare two documents side-by-side with color-coded visual diffs and change heatmaps
argument-hint: "<original file> <revised file>"
---

# /doc-diff -- Legal Document Comparison

Compare two legal documents (PDF, DOCX, TXT) and generate detailed visual diffs with color-coded changes, change heatmaps, and structured change logs. Supports cross-format comparison.

@$1

Examples:
- `/legal-toolkit:doc-diff ~/contracts/lease-v1.pdf ~/contracts/lease-v2.pdf`
- `/legal-toolkit:doc-diff ~/cases/johnson/original-report.docx ~/cases/johnson/amended-report.docx`
- `/legal-toolkit:doc-diff ~/agreements/settlement-draft.docx ~/agreements/settlement-final.docx`

## Workflow

- **Validate** two document paths (original and revised) with supported formats (.pdf, .docx, .txt)
- **Compare** using the `compare-documents` skill's Python script, generating a detailed diff analysis
- **Present** change statistics: additions, deletions, modifications, percentage changed, and the 5 most significant changes
- **Generate** output files: comparison.html (side-by-side visual diff), change_heatmap.html, change_log.json, comparison_summary.txt
- Refer to the `compare-documents` skill (SKILL.md) for labeling options and next-step actions like redline generation
