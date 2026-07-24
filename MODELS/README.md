---
title: EIB Model Layer
document_id: MODELS-README-001
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# Executive Intelligence Briefing Model Layer

## Purpose

The `MODELS` directory defines the standardized data structures used by the Executive Intelligence Briefing (EIB).

Models provide the shared contract between:

- Connectors
- Workflows
- Prompts
- Validation processes
- Runtime storage
- Future application code

The model layer allows EIB to process information consistently regardless of where the information originated.

---

# Why Models Matter

Each connector retrieves data in a different format.

For example:

- Gmail returns messages and threads.
- Google Calendar returns events.
- GitHub returns issues, commits, pull requests, and files.
- Web sources return articles and pages.
- Security sources return alerts and advisories.

EIB should not require every workflow or prompt to understand every source-specific format.

Instead, connectors normalize source data into approved EIB models.

```text
Source Data
    ↓
Connector
    ↓
EIB Model
    ↓
Workflow Processing
    ↓
Prompt Analysis
    ↓
Executive Briefing
```

This creates a stable boundary between data collection and intelligence generation.

---

# Repository Structure

```text
MODELS/
├── README.md
├── CORE/
│   ├── briefing_item.md
│   └── action_item.md
├── DOMAIN/
│   ├── email_summary.md
│   ├── calendar_event.md
│   ├── security_alert.md
│   ├── risk.md
│   ├── project_update.md
│   └── executive_decision.md
└── SCHEMA/
    └── model_schema.md
```

---

# Model Categories

## Core Models

Core models are foundational objects used across multiple EIB domains.

Repository location:

```text
MODELS/CORE/
```

### BriefingItem

The canonical unit of information processed by EIB.

A `BriefingItem` represents one meaningful topic, event, update, risk, opportunity, or communication.

All connectors should produce one or more `BriefingItem` objects.

### ActionItem

Represents a recommended task, decision, follow-up, or delegated activity.

An `ActionItem` should remain traceable to the information that generated it.

---

## Domain Models

Domain models represent specialized information associated with a particular source or business function.

Repository location:

```text
MODELS/DOMAIN/
```

### EmailSummary

Provides an executive-focused summary of an email message or thread.

### CalendarEvent

Represents a calendar event enriched with executive context, preparation requirements, conflicts, and follow-up needs.

### SecurityAlert

Represents a cybersecurity threat, vulnerability, incident, advisory, or defensive concern.

### Risk

Represents a condition that may negatively affect objectives, operations, compliance, security, finances, or reputation.

### ProjectUpdate

Represents a meaningful change in project status, schedule, scope, cost, dependency, or delivery risk.

### ExecutiveDecision

Represents a decision requiring executive awareness, approval, direction, or accountability.

---

## Schema Documents

Schema documents define standards that apply across the model layer.

Repository location:

```text
MODELS/SCHEMA/
```

### Model Schema

Defines:

- Required metadata
- Standard sections
- Naming conventions
- Common field names
- Data types
- Priority and confidence scales
- Validation rules
- Versioning
- Security requirements
- Governance expectations

All models should conform to the approved model schema.

---

# Current Model Inventory

| Model | Identifier | Category | Status |
|---|---|---|---|
| BriefingItem | MODEL-001 | Core | Approved |
| ActionItem | MODEL-002 | Core | Approved |
| EmailSummary | MODEL-003 | Domain | Approved |
| CalendarEvent | MODEL-004 | Domain | Planned |
| SecurityAlert | MODEL-005 | Domain | Planned |
| Risk | MODEL-006 | Domain | Planned |
| ProjectUpdate | MODEL-007 | Domain | Planned |
| ExecutiveDecision | MODEL-008 | Domain | Planned |

Model identifiers should remain stable even when files are renamed or reorganized.

---

# Processing Contract

The normal EIB processing flow is:

1. A connector retrieves source information.
2. The connector preserves source traceability.
3. The connector creates one or more `BriefingItem` objects.
4. Domain-specific objects are created when appropriate.
5. Workflows classify, prioritize, deduplicate, and validate the objects.
6. Prompts transform validated objects into executive intelligence.
7. Recommended actions become `ActionItem` objects.
8. Final outputs are published and archived.

---

# Connector Responsibilities

Each connector should:

- Retrieve only authorized information.
- Preserve source identifiers and links.
- Record relevant timestamps.
- Normalize data into approved EIB fields.
- Assign an initial confidence value.
- Avoid embedding connector-specific assumptions in shared models.
- Report source failures without fabricating missing data.
- Produce atomic records whenever practical.

A connector may populate a specialized domain model in addition to a `BriefingItem`.

Example:

```text
Gmail Message
    ↓
EmailSummary
    ↓
BriefingItem
    ↓
ActionItem, when follow-up is required
```

---

# Workflow Responsibilities

Workflows should operate primarily on normalized models rather than raw source payloads.

Workflow responsibilities include:

- Deduplication
- Classification
- Priority scoring
- Confidence adjustment
- Relationship creation
- Deadline detection
- Risk identification
- Action-item generation
- Validation
- Publication

Workflows should not rename standard model fields or introduce alternate interpretations of shared scales.

---

# Prompt Responsibilities

Prompts should consume predictable model inputs.

Prompts may:

- Summarize
- Compare
- Rank
- Explain
- Identify implications
- Recommend supported actions
- Assemble briefing sections

Prompts should not:

- Invent missing source information
- Remove traceability
- Convert uncertainty into false certainty
- Change model definitions dynamically
- Treat source-specific fields as universal standards

---

# Core Relationships

The following relationships are expected.

```text
BriefingItem
├── may originate from EmailSummary
├── may originate from CalendarEvent
├── may originate from SecurityAlert
├── may originate from ProjectUpdate
├── may support Risk
├── may support ExecutiveDecision
└── may generate ActionItem
```

Relationships should use stable object identifiers.

Example:

```yaml
source_items:
  - "briefing-item-123"
```

Complete related objects should not be duplicated unless the nested data has no independent lifecycle.

---

# Shared Standards

## Priority

All models using executive priority should use:

| Value | Meaning |
|---:|---|
| 1 | Immediate action or attention required |
| 2 | High priority or executive decision needed |
| 3 | Normal priority |
| 4 | Low priority |
| 5 | Background or future consideration |

Priority represents executive importance, not source urgency alone.

---

## Confidence

All models using confidence should store a decimal from `0.00` through `1.00`.

| Range | Meaning |
|---|---|
| 0.90–1.00 | High confidence |
| 0.75–0.89 | Good confidence |
| 0.50–0.74 | Moderate confidence |
| Below 0.50 | Low confidence |

Confidence reflects evidence quality, reliability, consistency, and completeness.

---

## Dates and Times

Dates should use ISO 8601:

```text
2026-07-24
```

Date and time values should include timezone information whenever available:

```text
2026-07-24T09:30:00-07:00
```

The default EIB timezone is defined in:

```text
CONFIG/application.yaml
```

---

## Naming

Model names:

```text
PascalCase
```

Examples:

```text
BriefingItem
ActionItem
EmailSummary
```

Field names:

```text
lowercase_snake_case
```

Examples:

```text
created_timestamp
source_reference
action_required
```

File names:

```text
lowercase_snake_case.md
```

---

# Model Development Process

When adding a new model:

1. Confirm that an existing model cannot represent the requirement.
2. Assign the next approved model identifier.
3. Place the model in `CORE` or `DOMAIN`.
4. Follow `MODELS/SCHEMA/model_schema.md`.
5. Define required and optional fields.
6. Define all enumerations.
7. Define relationships.
8. Add validation rules.
9. Include at least one example.
10. Update the model inventory in this README.
11. Update dependent connectors and workflows.
12. Record significant architectural decisions in `AI/DECISIONS.md`.

---

# Model Change Process

For an approved model change:

1. Identify affected connectors.
2. Identify affected workflows.
3. Identify affected prompts.
4. Determine whether the change is breaking.
5. Increment the model version.
6. Document any migration requirements.
7. Update examples and validation rules.
8. Perform regression testing.
9. Update repository status documentation.

Breaking changes should not be introduced solely for convenience.

---

# Validation Expectations

A model instance should not proceed to final publication unless:

- Required fields are present.
- Data types are valid.
- Enumerations use approved values.
- Priority is between `1` and `5`, when applicable.
- Confidence is between `0.00` and `1.00`, when applicable.
- Dates use approved formats.
- Source-derived claims remain traceable.
- Relationships reference valid identifiers.
- Sensitive information is appropriately handled.
- The object represents one clear primary concept.

Validation failures should be logged and either corrected or explicitly disclosed.

---

# Security and Privacy

Models must never contain:

- Passwords
- API keys
- Authentication tokens
- Private cryptographic keys
- Connector secrets

Sensitive source content should be minimized.

Whenever a summary is sufficient, models should preserve a source reference instead of duplicating the complete source content.

Retention, redaction, classification, and access controls should follow applicable organizational requirements.

---

# Implementation Guidance

The current Markdown model documents are authoritative design specifications.

Future runtime implementations may represent these models using:

- YAML Schema
- JSON Schema
- Python classes
- TypeScript interfaces
- Database tables
- Data validation libraries

Runtime implementations must preserve the meaning, required fields, relationships, and validation rules documented here.

Markdown remains the human-readable source of truth until a formal schema implementation is approved.

---

# Example Processing Sequence

```yaml
email_summary:
  id: "email-summary-001"
  subject: "Security Steering Committee agenda"
  sender: "CIO"
  received_timestamp: "2026-07-24T08:05:00-07:00"
  summary: >
    Agenda items are requested for next week's committee meeting.
  priority: 2
  confidence: 0.98
  action_required: true

briefing_item:
  id: "briefing-item-001"
  source: "Gmail"
  category: "Governance"
  title: "Steering Committee agenda items due"
  summary: >
    The CIO requested proposed agenda items for the upcoming
    Security Steering Committee meeting.
  timestamp: "2026-07-24T08:05:00-07:00"
  priority: 2
  confidence: 0.98
  source_reference: "email-summary-001"

action_item:
  id: "action-item-001"
  title: "Submit Steering Committee agenda items"
  summary: >
    Review current security governance priorities and send proposed
    agenda items to the CIO before the stated deadline.
  priority: 2
  owner: "Bryan Johnson"
  status: "Proposed"
  created_timestamp: "2026-07-24T09:00:00-07:00"
  source_items:
    - "briefing-item-001"
```

---

# Planned Work

The next planned domain models are:

1. `MODELS/DOMAIN/calendar_event.md`
2. `MODELS/DOMAIN/security_alert.md`
3. `MODELS/DOMAIN/risk.md`
4. `MODELS/DOMAIN/project_update.md`
5. `MODELS/DOMAIN/executive_decision.md`

After the initial model library is complete, the repository should add machine-readable schemas and model validation tests.

---

# Success Criteria

The model layer is successful when:

- Every connector produces predictable data.
- Workflows remain independent of raw source formats.
- Prompts receive stable and traceable inputs.
- Risks and actions remain connected to supporting evidence.
- New connectors can be added without redesigning existing workflows.
- Model changes are versioned and governed.
- Runtime code can be implemented directly from the documented contracts.

The `MODELS` directory is the common language of the Executive Intelligence Briefing platform.