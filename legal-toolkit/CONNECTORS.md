# Legal Toolkit — Connectors

Legal Toolkit works standalone out of the box. When connected to external services via MCP, skills can pull data directly from those systems rather than requiring manual file uploads.

## Connector Categories

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Call transcription | `~~call transcription` | Fireflies | Gong, Otter.ai, Chorus |
| Chat | `~~chat` | Slack | Microsoft Teams |
| Cloud storage | `~~cloud storage` | Box | Dropbox, Google Drive, Egnyte |
| CRM | `~~CRM` | HubSpot | Salesforce, Clio |
| Email | `~~email` | Microsoft 365 | Google Workspace (Gmail) |
| Knowledge base | `~~knowledge base` | Notion | Confluence, Clio Documents |
| Office suite | `~~office suite` | Microsoft 365 | Google Workspace |

## Skills Enhanced by Connectors

### Call Transcription (`~~call transcription`)
**Fireflies** is the default. Connect at: https://fireflies.ai

Skills that benefit:
- **score-intake** — Pull recent intake call transcripts by date, rep name, or keyword instead of uploading audio files
- **build-objection-playbook** — Analyze a batch of call recordings from Fireflies to extract real objection patterns
- **build-intake-script** — Learn from past call patterns to generate data-driven intake scripts

### Chat (`~~chat`)
**Slack** is the default.

Skills that benefit:
- **score-intake** — Post scorecards directly to a coaching channel after scoring
- **surface-performance** — Share KPI reports to a firm leadership channel
- **design-comm-cadence** — Preview and schedule client messages via Slack for team review
- **multiply-content** — Post generated social content to a review channel before publishing

### Cloud Storage (`~~cloud storage`)
**Box** is the default. Also works with Dropbox, Google Drive.

Skills that benefit:
- **build-case-playbook** — Pull case files directly from a matter folder
- **build-chronology** — Ingest documents from a cloud folder without uploading individually
- **analyze-discovery** — Pull discovery packages from a shared folder
- **draft-motion** — Pull case files and templates from cloud storage
- **summarize** — Pull documents from cloud storage for summarization

### CRM (`~~CRM`)
**HubSpot** is the default. Also works with Salesforce, Clio.

Skills that benefit:
- **surface-performance** — Pull lead and case data directly from CRM for KPI analysis
- **analyze-workload** — Pull active caseload from CRM to analyze attorney capacity
- **map-client-journey** — Pull client lifecycle data to map touchpoints accurately
- **calculate-pricing** — Look up comparable past cases and their fees

### Email (`~~email`)
**Microsoft 365** is the default. Also works with Google Workspace (Gmail).

Skills that benefit:
- **process-emails** — Connect directly to an email archive or inbox instead of uploading .eml/.mbox files
- **design-comm-cadence** — Draft and schedule client communication emails directly
- **request-reviews** — Send review request emails directly from Claude

### Knowledge Base (`~~knowledge base`)
**Notion** is the default. Also works with Confluence.

Skills that benefit:
- **build-case-playbook** — Save generated playbooks to a Notion database for future reference
- **build-chronology** — Save chronologies to a matter page in Notion
- **build-intake-script** — Pull existing scripts from a Notion playbook library

## Setup

All connectors are pre-configured in `.mcp.json`. To activate them:

1. Open Claude Desktop settings
2. Go to Connectors
3. Authenticate with the services you use

Skills degrade gracefully when connectors are not available — they will prompt you to provide files or paste data manually instead.
