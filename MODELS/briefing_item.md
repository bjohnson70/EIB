---
title: Briefing Item Data Model
model_id: MODEL-001
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# BriefingItem

## Purpose

The `BriefingItem` is the canonical information model used throughout the Executive Intelligence Briefing (EIB).

Every connector should normalize collected information into one or more `BriefingItem` objects before workflow processing begins.

This provides a common contract between connectors, workflows, prompts, and future application code.

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | UUID/String | Unique identifier |
| source | String | Originating connector (GitHub, Gmail, Web, etc.) |
| category | String | High-level topic classification |
| title | String | Short descriptive title |
| summary | Markdown | Executive summary of the item |
| timestamp | DateTime | When the information originated |
| priority | Integer | Executive priority (1–5) |
| confidence | Decimal | Confidence score (0.00–1.00) |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| url | String | Source URL or reference |
| author | String | Original author or publisher |
| tags | List | Classification tags |
| affected_systems | List | Systems or projects impacted |
| due_date | Date | Deadline if applicable |
| owner | String | Suggested owner |
| action_required | Boolean | Indicates follow-up is recommended |
| action_item | Markdown | Suggested executive action |
| related_items | List | IDs of related BriefingItems |

---

# Priority Scale

| Value | Meaning |
|------:|---------|
| 1 | Immediate action required |
| 2 | Executive decision needed |
| 3 | High importance |
| 4 | Informational |
| 5 | Background awareness |

---

# Confidence Scale

| Range | Meaning |
|---------|---------|
| 0.90–1.00 | High confidence |
| 0.75–0.89 | Good confidence |
| 0.50–0.74 | Moderate confidence |
| Below 0.50 | Low confidence; highlight uncertainty |

---

# Lifecycle

A `BriefingItem` progresses through these stages:

1. Collected
2. Normalized
3. Classified
4. Prioritized
5. Validated
6. Published
7. Archived

---

# Relationships

Other EIB models may reference a `BriefingItem`, including:

- EmailSummary
- CalendarEvent
- Risk
- ActionItem
- TechnologyNews
- SecurityAlert
- ExecutiveDecision

---

# Design Principles

Every `BriefingItem` should be:

- Atomic (one primary topic)
- Traceable to its source
- Easy to summarize
- Suitable for executive consumption
- Independent of the connector that created it

The `BriefingItem` serves as the common language spoken by every component of the Executive Intelligence Briefing platform.