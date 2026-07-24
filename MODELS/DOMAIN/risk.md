---
title: Risk Data Model
model_id: MODEL-006
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# Risk

## Purpose

The `Risk` model represents a condition, event, trend, dependency, or uncertainty that could negatively impact the organization's mission, operations, finances, security, compliance, reputation, or strategic objectives.

Unlike a `SecurityAlert`, which reports an event, a `Risk` represents an executive assessment of potential business impact. Risks may be derived from one or many supporting `BriefingItem` objects and are intended to guide executive attention and decision-making.

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | UUID/String | Unique EIB identifier |
| title | String | Short risk title |
| summary | Markdown | Executive description of the risk |
| category | Enum | Risk classification |
| likelihood | Enum | Probability of occurrence |
| impact | Enum | Business impact if realized |
| priority | Integer | Executive priority (1–5) |
| confidence | Decimal | Confidence score |
| status | Enum | Current lifecycle status |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| owner | String | Recommended risk owner |
| mitigation | Markdown | Recommended mitigation strategy |
| contingency | Markdown | Response if risk occurs |
| affected_business_units | List[String] | Impacted organizations |
| affected_systems | List[String] | Impacted systems |
| due_date | Date | Planned review or mitigation date |
| source_items | List[String] | Supporting BriefingItem IDs |
| related_items | List[String] | Related EIB object IDs |
| source_reference | String | External reference if applicable |
| notes | Markdown | Additional context |

---

# Risk Categories

Risks may be classified as:

- Cybersecurity
- Privacy
- Compliance
- Operational
- Financial
- Technology
- Vendor
- Personnel
- Project
- Strategic
- Legal
- Reputational

---

# Likelihood Scale

| Value | Meaning |
|---------|---------|
| Very High | Expected or already occurring |
| High | Likely |
| Moderate | Possible |
| Low | Unlikely |
| Very Low | Rare |

---

# Impact Scale

| Value | Meaning |
|---------|---------|
| Critical | Mission failure or severe organizational impact |
| High | Significant disruption |
| Moderate | Noticeable operational impact |
| Low | Limited impact |
| Minimal | Minor inconvenience |

---

# Executive Intelligence

Each Risk should answer:

- What could happen?
- Why does it matter?
- What is the business impact?
- How likely is it?
- What should leadership do?
- Who owns the response?

---

# Relationships

A Risk may reference:

- BriefingItem
- SecurityAlert
- ProjectUpdate
- EmailSummary
- ExecutiveDecision
- CalendarEvent
- ActionItem

Multiple BriefingItems may contribute to a single Risk.

---

# Lifecycle

1. Identified
2. Assessed
3. Prioritized
4. Assigned
5. Mitigated
6. Monitored
7. Closed

Closed risks remain archived for historical reporting and trend analysis.

---

# Validation Rules

A valid Risk must:

- Include a title
- Include a summary
- Include a category
- Include likelihood and impact ratings
- Include executive priority
- Include confidence between 0.00 and 1.00
- Reference at least one supporting BriefingItem

---

# Example

```yaml
id: risk-001
title: Delayed Critical Security Patching
summary: >
  Multiple critical vulnerabilities remain unpatched on internet-facing
  systems, increasing the likelihood of successful exploitation.
category: Cybersecurity
likelihood: High
impact: Critical
priority: 1
confidence: 0.96
status: Identified
owner: Infrastructure Services
mitigation: >
  Complete emergency patch deployment within 72 hours and verify
  successful installation.
source_items:
  - briefing-item-104
  - briefing-item-107
```

---

# Future Enhancements

Future releases may include:

- Quantitative risk scoring
- Risk heat maps
- Risk trend analysis
- AI-generated mitigation recommendations
- FAIR risk methodology support
- NIST CSF and ISO 31000 mappings
- Automatic risk aggregation
- Executive risk dashboard integration

---

# Success Criteria

A Risk is successful when an executive can quickly understand:

- The nature of the risk
- Its likelihood and potential impact
- The recommended mitigation
- Who owns the response
- The evidence supporting the assessment

The Risk model serves as the executive bridge between operational events and strategic decision-making, allowing EIB to synthesize diverse information into actionable organizational risk intelligence.