---
description: Structure a firm decision into options analysis, financial impact, risk assessment, and recommendation
argument-hint: "<decision description, options, and constraints>"
---

# /decision-model -- Owner Decision Model

Analyze a business decision for a law firm owner. Produces a structured analysis with options comparison, financial summary, risk assessment, and a recommendation with stated confidence level. This is decision support — the owner makes the final call.

@$1

Examples:
- `/legal-toolkit:decision-model Should we hire a second associate or a paralegal?`
- `/legal-toolkit:decision-model Evaluate opening a satellite office in Tampa vs. staying single-location`
- `/legal-toolkit:decision-model Take on a complex federal case -- high profile but 200+ hours, no guarantee of payment`

## Workflow

- **Clarify** the decision and gather context — what is being decided, why now, and what constraints exist (budget, timeline, risk tolerance)
- **Identify** at least three options including "maintain status quo" as a baseline comparison
- **Analyze** each option across financial impact, pros/cons, and execution requirements
- **Assess risks** with specific failure scenarios, likelihood, impact, and mitigation strategies
- **Summarize financials** in a side-by-side comparison table with ranges where precision is not possible
- **Recommend** the option the analysis supports, with an explicit confidence level (high / moderate / low) and what additional data would increase confidence
- **Outline implementation** with immediate next steps, 30-day milestones, checkpoints, and success metrics
- Refer to the `model-decision` skill (SKILL.md) for decision frameworks and analysis templates
