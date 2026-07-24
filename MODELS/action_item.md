---
title: Action Item Data Model
model_id: MODEL-002
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# ActionItem

## Purpose

The `ActionItem` represents a recommended task, decision, follow-up, or activity identified during Executive Intelligence Briefing (EIB) processing.

ActionItems may originate from:

- Email
- Calendar
- GitHub
- Cybersecurity events
- News
- Project updates
- AI analysis
- Executive decisions

Every ActionItem should be traceable back to one or more originating BriefingItems.

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | UUID/String | Unique identifier |
| title | String | Short action description |
| summary | Markdown | Description of the recommended action |
| priority | Integer | Executive priority (1–5) |
| owner | String | Recommended owner |
| status | Enum | Current lifecycle state |
| created_timestamp | DateTime | Time ActionItem was generated |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| due_date | Date | Recommended completion date |
| source_items | List | Related BriefingItem IDs |
| category | String | Security, Project, Calendar, Finance, etc. |
| estimated_effort | Enum | Small, Medium, Large |
| delegation_candidate | Boolean | Suitable for delegation |
| decision_required | Boolean | Executive decision required |
| notes | Markdown | Additional supporting information |
| url | String | Supporting reference |

---

# Status Values

| Status | Meaning |
|---------|---------|
| Proposed | Newly generated recommendation |
| Accepted | Reviewed and approved |
| Delegated | Assigned to another individual |
| In Progress | Work has begun |
| Waiting | Blocked or awaiting input |
| Completed | Finished |
| Cancelled | No longer required |

---

# Priority Scale

| Value | Meaning |
|------:|---------|
| 1 | Immediate |
| 2 | High |
| 3 | Normal |
| 4 | Low |
| 5 | Future Consideration |

---

# Executive Rules

An ActionItem should:

- Recommend a specific action.
- Be concise.
- Be measurable.
- Be understandable without reading the entire briefing.
- Reference supporting information.

Avoid vague recommendations such as:

- "Look into..."
- "Consider..."
- "Maybe..."

Prefer:

- Review...
- Approve...
- Contact...
- Schedule...
- Escalate...
- Respond...
- Complete...

---

# Relationships

ActionItems may reference:

- BriefingItem
- EmailSummary
- CalendarEvent
- SecurityAlert
- Risk
- ExecutiveDecision

---

# Lifecycle

An ActionItem progresses through:

1. Generated
2. Reviewed
3. Accepted
4. Assigned
5. Executed
6. Completed
7. Archived

---

# Future Enhancements

Future versions may include:

- Automatic task creation
- Microsoft Planner integration
- Google Tasks integration
- Jira integration
- GitHub Issues integration
- Due date prediction
- AI effort estimation
- AI owner recommendation
- Reminder scheduling
- Progress tracking

---

# Success Criteria

A high-quality ActionItem should answer:

- What needs to be done?
- Why does it matter?
- Who should do it?
- When should it be completed?
- What information supports the recommendation?

The ActionItem model transforms intelligence into execution, ensuring the Executive Intelligence Briefing not only informs decision-makers but also drives meaningful action.