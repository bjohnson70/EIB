---
title: EIB Model Schema
document_id: MODEL-SCHEMA-001
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# Executive Intelligence Briefing Model Schema

## Purpose

This document defines the common structure, naming conventions, lifecycle requirements, and governance standards for data models used by the Executive Intelligence Briefing (EIB).

The model schema establishes a consistent contract between:

- Connectors
- Workflows
- Prompts
- Validation processes
- Storage systems
- Future application code

Every EIB model should conform to this schema unless a documented architectural decision authorizes an exception.

---

# Model Categories

EIB models are organized into three categories.

## Core Models

Core models represent foundational objects used across multiple domains.

Examples:

- `BriefingItem`
- `ActionItem`

Repository location:

```text
MODELS/CORE/
```

## Domain Models

Domain models represent information associated with a specific source, subject area, or business function.

Examples:

- `EmailSummary`
- `CalendarEvent`
- `SecurityAlert`
- `Risk`
- `ProjectUpdate`
- `ExecutiveDecision`

Repository location:

```text
MODELS/DOMAIN/
```

## Schema Documents

Schema documents define common model standards, validation rules, enumerations, and relationships.

Repository location:

```text
MODELS/SCHEMA/
```

---

# Required Model Metadata

Every model document must begin with YAML front matter containing the following fields:

| Field | Type | Description |
|---|---|---|
| title | String | Human-readable model title |
| model_id | String | Unique model identifier |
| version | String | Semantic version |
| status | Enum | Model lifecycle status |
| owner | String | Person or team responsible for the model |
| last_updated | Date | Date of the most recent approved change |

Example:

```yaml
---
title: Action Item Data Model
model_id: MODEL-002
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---
```

---

# Model Lifecycle Status

Allowed model status values are:

| Status | Meaning |
|---|---|
| Draft | Under development and not approved for production use |
| Review | Ready for stakeholder or technical review |
| Approved | Accepted as the authoritative model definition |
| Deprecated | Still supported but scheduled for replacement |
| Retired | No longer supported or used |

Production workflows should use only models with an `Approved` status unless explicitly operating in a development or testing environment.

---

# Standard Model Sections

Every model document should contain the following sections.

## Purpose

Explains why the model exists and how it is used.

## Required Fields

Defines fields that must be populated for every valid instance.

## Optional Fields

Defines fields that may be populated when relevant information is available.

## Enumerations

Defines controlled values for fields such as status, priority, category, or severity.

## Relationships

Identifies other models that may reference or be referenced by the model.

## Lifecycle

Describes how an instance progresses from creation through archival or retirement.

## Validation Rules

Defines conditions that must be satisfied before the model is considered valid.

## Example

Provides at least one representative instance in YAML or JSON.

## Future Enhancements

Documents planned capabilities without making them part of the current required contract.

---

# Common Fields

The following fields should be used consistently across models where applicable.

| Field | Type | Description |
|---|---|---|
| id | String | Unique identifier for the object |
| title | String | Short human-readable label |
| summary | Markdown/String | Concise description |
| source | String | Originating system or connector |
| source_reference | String | Source-specific identifier or reference |
| created_timestamp | DateTime | Time the object was created |
| updated_timestamp | DateTime | Time the object was most recently updated |
| effective_timestamp | DateTime | Time the underlying event or information became effective |
| category | String | High-level classification |
| tags | List[String] | Searchable classification terms |
| priority | Integer | Executive priority |
| confidence | Decimal | Confidence from `0.00` through `1.00` |
| status | Enum | Current lifecycle state |
| owner | String | Responsible or recommended owner |
| source_items | List[String] | Related `BriefingItem` identifiers |
| related_items | List[String] | Related EIB object identifiers |
| url | String | Source or supporting link |
| notes | Markdown/String | Additional context |

Models should reuse these field names rather than introducing synonyms.

For example, use `created_timestamp` instead of mixing:

- `created`
- `creation_time`
- `date_created`
- `generated_at`

---

# Naming Conventions

## Model Names

Model names use singular PascalCase.

Examples:

```text
BriefingItem
ActionItem
EmailSummary
CalendarEvent
```

## Field Names

Field names use lowercase snake_case.

Examples:

```text
created_timestamp
action_required
source_items
decision_required
```

## File Names

Model document filenames use lowercase snake_case.

Examples:

```text
briefing_item.md
action_item.md
email_summary.md
```

## Model Identifiers

Model identifiers use the following format:

```text
MODEL-###
```

Examples:

```text
MODEL-001
MODEL-002
MODEL-003
```

Schema documents may use:

```text
MODEL-SCHEMA-###
```

---

# Data Types

EIB models use the following standard type names.

| Type | Definition |
|---|---|
| String | Plain text value |
| Markdown | Text that may contain Markdown formatting |
| Integer | Whole number |
| Decimal | Numeric value that may include fractional values |
| Boolean | `true` or `false` |
| Date | ISO 8601 calendar date |
| DateTime | ISO 8601 date and time with timezone when available |
| UUID | Universally unique identifier |
| Enum | One value from a defined controlled list |
| List[Type] | Ordered collection of values |
| Map | Key-value collection |
| Object | Structured nested record |

Dates should use:

```text
YYYY-MM-DD
```

Date and time values should use ISO 8601:

```text
2026-07-24T09:30:00-07:00
```

---

# Identifier Rules

Every model instance must have an identifier that is:

- Unique within the EIB environment
- Stable throughout the object lifecycle
- Safe for storage and transmission
- Independent of its display title

UUIDs are preferred for runtime-generated objects.

Source identifiers may be preserved in `source_reference`, but they should not replace the EIB object identifier unless uniqueness and stability are guaranteed.

---

# Priority Standard

Models using executive priority should follow this common scale:

| Value | Meaning |
|---:|---|
| 1 | Immediate action or attention required |
| 2 | High priority or executive decision needed |
| 3 | Normal priority |
| 4 | Low priority |
| 5 | Background or future consideration |

Priority values must be interpreted consistently across connectors, workflows, and briefing output.

Domain-specific severity values may exist separately but should not replace executive priority.

---

# Confidence Standard

Models using confidence should store a decimal value from `0.00` through `1.00`.

| Range | Meaning |
|---|---|
| 0.90–1.00 | High confidence |
| 0.75–0.89 | Good confidence |
| 0.50–0.74 | Moderate confidence |
| Below 0.50 | Low confidence |

Confidence should reflect the reliability and completeness of the information, not the importance of the item.

A high-priority item may have low confidence, and a low-priority item may have high confidence.

---

# Source Traceability

Every model derived from external information should preserve sufficient source information to support verification.

Where applicable, include:

- `source`
- `source_reference`
- `url`
- `effective_timestamp`
- `source_items`

Derived models such as `ActionItem`, `Risk`, or `ExecutiveDecision` should reference the `BriefingItem` objects that support them.

No generated recommendation should become detached from its underlying evidence.

---

# Relationships

Relationships between models should use identifiers rather than embedding complete copies of related objects.

Example:

```yaml
source_items:
  - "briefing-item-123"
  - "briefing-item-456"
```

This approach:

- Reduces duplication
- Preserves referential integrity
- Supports independent updates
- Simplifies storage
- Improves traceability

Nested objects may be used when the data is inseparable from the parent and has no independent lifecycle.

---

# Validation Rules

A model instance is valid when:

1. All required fields are present.
2. Field values use the documented data types.
3. Enum values match the defined allowed values.
4. Priority is between `1` and `5`, when used.
5. Confidence is between `0.00` and `1.00`, when used.
6. Dates and timestamps use ISO 8601 formats.
7. Referenced objects use valid identifiers.
8. Source-derived information is traceable.
9. Sensitive information is handled according to EIB security rules.
10. The object represents one clear primary concept.

Invalid objects should not proceed to final briefing publication unless the validation issue is explicitly documented.

---

# Model Versioning

EIB models use semantic versioning.

## Major Version

Increase the major version when:

- Removing a field
- Renaming a field
- Changing a field type incompatibly
- Changing the meaning of an existing value
- Introducing a breaking relationship change

Example:

```text
1.0 → 2.0
```

## Minor Version

Increase the minor version when:

- Adding an optional field
- Adding a backward-compatible enumeration
- Clarifying validation rules
- Adding examples or documentation

Example:

```text
1.0 → 1.1
```

Breaking changes should include a documented migration path.

---

# Security and Privacy

Models must not store credentials, API keys, authentication tokens, or secrets.

Sensitive content should be:

- Minimized
- Redacted when appropriate
- Classified when required
- Retained only as long as necessary
- Protected according to applicable organizational policy

Models should store references to sensitive source content rather than duplicating full content when the briefing only requires a summary.

---

# Example Model Definition

The following is a simplified example of a compliant model instance:

```yaml
id: "briefing-item-123"
source: "Gmail"
source_reference: "gmail-message-reference"
category: "Cybersecurity"
title: "Incident response review requested"
summary: >
  Security leadership requested review of the current incident
  response escalation process before the next governance meeting.
effective_timestamp: "2026-07-24T08:15:00-07:00"
priority: 2
confidence: 0.98
action_required: true
tags:
  - incident-response
  - governance
```

---

# Repository Structure

The approved model structure is:

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

Existing model files should be moved as follows:

```text
MODELS/briefing_item.md
→ MODELS/CORE/briefing_item.md
```

```text
MODELS/action_item.md
→ MODELS/CORE/action_item.md
```

No content changes are required solely because of the move, although internal repository references should be updated.

---

# Governance

Changes to approved models should:

1. Identify the reason for the change.
2. Evaluate compatibility with existing connectors and workflows.
3. Update the model version.
4. Update dependent documentation.
5. Record significant decisions in `AI/DECISIONS.md`.
6. Perform validation or regression testing.
7. Update `AI/REPOSITORY_STATUS.md` when the change affects repository readiness.

---

# Success Criteria

The EIB model schema is successful when:

- Connectors produce consistent objects.
- Workflows process data without source-specific assumptions.
- Prompts receive predictable inputs.
- Recommendations remain traceable to evidence.
- Model changes are governed and versioned.
- New domains can be added without redesigning the core architecture.
- Future application code can implement the documented contracts directly.

The model layer is the shared language of the Executive Intelligence Briefing platform.