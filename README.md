# Legal Toolkit

A Claude Code plugin with 31 legal productivity skills -- document processing, criminal defense workflows, firm operations, and client management. Covers everything from document summarization and audio transcription to motion drafting, intake call scoring, case strategy playbooks, and attorney workload analysis.

All processing is 100% local -- no data leaves your machine.

Works with both **Claude Code** (CLI) and **Claude Desktop / Cowork**.

## Prerequisites

### Claude Code (CLI)

1. **Node.js** (v18+) -- for generating Word documents
2. **Python 3** (v3.9+) -- for document processing, transcription, OCR, and analysis
3. **ffmpeg** (optional) -- for audio/video transcription and deposition indexing

Dependencies are auto-installed on first use of each skill.

#### macOS (with Homebrew)

```bash
brew install node python3 ffmpeg
```

#### Windows

- **Node.js**: Download from https://nodejs.org (LTS version). Check "Add to PATH" during install.
- **Python 3**: Download from https://www.python.org/downloads/. Check "Add Python to PATH" during install.
- **ffmpeg**: Download from https://ffmpeg.org/download.html and add the `bin/` folder to your system PATH.

#### Linux (Ubuntu/Debian)

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs python3 python3-pip ffmpeg poppler-utils
```

### Claude Desktop / Cowork

No prerequisites needed. Cowork's VM has Python and Node.js pre-installed. Dependencies are auto-installed on first run.

## Installing the Plugin

### Option A: Claude Code CLI

Install directly from within Claude Code:

```
/install-plugin https://github.com/jdrodriguez/legal-toolkit
```

Or clone and use locally:

```bash
git clone https://github.com/jdrodriguez/legal-toolkit.git
claude --plugin-dir /path/to/legal-toolkit
```

### Option B: Claude Desktop / Cowork

1. Download the plugin zip from this repository
2. Open Claude Desktop and start a Cowork session
3. Drag and drop the `.zip` file into the chat
4. Claude will install the plugin automatically

### Verify the installation

Type this in Claude Code or Cowork:
```
/legal-toolkit:summarize
```

If Claude recognizes the command, you're all set.

## Available Skills

### Document Processing

| Command | Description |
|---------|-------------|
| `/legal-toolkit:summarize` | Summarize documents (PDF, DOCX, TXT, Markdown) into professional Word reports |
| `/legal-toolkit:transcribe` | Transcribe audio/video recordings with timestamps and speaker labels |
| `/legal-toolkit:ocr` | OCR scanned PDFs and images (PaddleOCR + Tesseract) |
| `/legal-toolkit:compare-documents` | Compare documents with visual diff heatmaps |
| `/legal-toolkit:redline` | Generate tracked-changes redlines between document versions |

### Litigation & Case Work

| Command | Description |
|---------|-------------|
| `/legal-toolkit:calculate-deadlines` | Calculate court deadlines (FRCP Rule 6, state rules, .ics export) |
| `/legal-toolkit:build-chronology` | Build case chronologies from documents |
| `/legal-toolkit:index-deposition` | Index deposition video/audio recordings |
| `/legal-toolkit:map-entities` | NLP entity extraction and relationship mapping |
| `/legal-toolkit:analyze-photos` | Evidence photo EXIF/GPS analysis |
| `/legal-toolkit:analyze-video` | Forensic video frame analysis |
| `/legal-toolkit:search-records` | SEC EDGAR public filings research |

### Criminal Defense

| Command | Description |
|---------|-------------|
| `/legal-toolkit:analyze-discovery` | Analyze discovery packages with NHTSA cross-reference and defense memo |
| `/legal-toolkit:draft-motion` | Draft motions (suppress, dismiss, exclude, limine, compel, sentencing) |
| `/legal-toolkit:build-case-playbook` | Generate defense strategy playbook from case files |

### E-Discovery & Financial Analysis

| Command | Description |
|---------|-------------|
| `/legal-toolkit:process-emails` | E-discovery email processing |
| `/legal-toolkit:analyze-communications` | Communication pattern analysis |
| `/legal-toolkit:audit-billing` | Billing data audit (LEDES, Excel, CSV) |
| `/legal-toolkit:analyze-financials` | Forensic financial analysis |

### Intake & Client Management

| Command | Description |
|---------|-------------|
| `/legal-toolkit:process-intake` | Client intake processing |
| `/legal-toolkit:score-intake` | Score intake calls against coaching rubric (accepts audio or text) |
| `/legal-toolkit:build-intake-script` | Build adaptive intake call scripts with branching logic |
| `/legal-toolkit:build-objection-playbook` | Generate objection handling playbook from call recordings |
| `/legal-toolkit:calculate-pricing` | Calculate case retainer ranges with payment plan options |
| `/legal-toolkit:request-reviews` | Generate client review request scripts and timing strategy |
| `/legal-toolkit:map-client-journey` | Map and optimize the client experience journey |
| `/legal-toolkit:design-comm-cadence` | Design client communication calendars and templates |

### Firm Operations

| Command | Description |
|---------|-------------|
| `/legal-toolkit:multiply-content` | Multiply one piece of content into 12+ platform-native outputs |
| `/legal-toolkit:surface-performance` | Surface firm KPIs from case data exports |
| `/legal-toolkit:analyze-workload` | Analyze attorney caseload capacity and redistribution |
| `/legal-toolkit:model-decision` | Structured decision analysis for firm owners |

## Usage Examples

### Summarize a document

```
Summarize /path/to/my-report.pdf
```

Or point it at a folder:

```
Summarize everything in /path/to/contracts/
```

### Transcribe a recording

```
Transcribe /path/to/meeting-recording.mp3
```

The transcriber runs locally using faster-whisper. It launches as a background process and provides progress updates as it works. Output is a professional .docx with:
- Metadata table (duration, language, model, speakers)
- Executive summary and key topics
- Full timestamped transcript with speaker labels
- Speaker statistics and notable quotes

Optional speaker diarization requires [pyannote.audio](https://github.com/pyannote/pyannote-audio) and a free [HuggingFace token](https://huggingface.co/settings/tokens).

### Calculate court deadlines

```
Calculate deadlines from a complaint filed today in California Superior Court
```

### OCR a scanned document

```
OCR /path/to/scanned-contract.pdf
```

## Output

Each skill produces output files **in the same folder as your input document**:

| Skill | Output |
|-------|--------|
| Summarize | `{filename}_summary.docx` + `_summary_work/` directory |
| Transcribe | `{filename}_transcript.docx` + `_transcript_work/` directory |
| OCR | `{filename}_ocr.txt` or `.docx` |
| Redline | `{filename}_redline.docx` |
| Other skills | Varies -- each skill reports its output location |

## Supported File Types

| Format | Extension | Skills |
|--------|-----------|--------|
| PDF | `.pdf` | summarize, ocr, compare-documents, redline |
| Word | `.docx` | summarize, compare-documents, redline |
| Plain text | `.txt`, `.md` | summarize |
| Audio | `.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`, `.wma`, `.aac` | transcribe, index-deposition |
| Video | `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm` | transcribe, index-deposition |
| Images | `.jpg`, `.png`, `.tiff`, `.bmp` | ocr, analyze-photos |
| Email | `.eml`, `.msg`, `.mbox` | process-emails |
| Spreadsheets | `.csv`, `.xlsx` | audit-billing, analyze-financials, surface-performance, analyze-workload |

## Troubleshooting

### "command not found: node" or "command not found: python3"

Close and reopen your terminal. If that doesn't help:

**macOS/Linux**: Add this to your `~/.zshrc` or `~/.bashrc`:
```bash
export PATH="/usr/local/bin:$PATH"
```
Then run `source ~/.zshrc`.

**Windows**: Reinstall Node.js/Python and check "Add to PATH" during installation.

### "Cannot find module 'docx'"

```bash
npm install -g docx
```

If the error persists:
```bash
export NODE_PATH=$(npm root -g)
```
Add that line to your `~/.zshrc` or `~/.bashrc` to make it permanent.

### Python import errors

Dependencies auto-install on first use. To install manually:
```bash
pip3 install pdfplumber pymupdf python-docx faster-whisper pydub
```

### Transcription: "No speech detected"

The audio file may be corrupted, empty, or in an unsupported codec. Try converting it first:
```bash
ffmpeg -i input.m4a -acodec pcm_s16le -ar 16000 output.wav
```

### Uninstalling

```
/plugin uninstall legal-toolkit
```

## Architecture

```
legal-toolkit/
  .claude-plugin/plugin.json     # Plugin metadata
  install.sh                     # Dependency installer for all skills
  commands/                      # 31 slash command entry points
  skills/                        # 31 skill directories
    summarize/
      SKILL.md                   # Skill instructions
      scripts/                   # Python scripts
    transcribe/
      SKILL.md
      scripts/
        check_dependencies.py    # Verify/install dependencies
        resolve_path.py          # File path resolution
        transcribe_audio.py      # Background transcription with status.json polling
        create_document.py       # Generate .docx output
    ...
```

Each skill follows the same pattern: a `SKILL.md` with instructions and a `scripts/` directory with Python CLI tools. Scripts output JSON to stdout and progress to stderr.

## License

MIT
