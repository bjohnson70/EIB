---
title: Calendar Event Data Model
model_id: MODEL-004
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# CalendarEvent

## Purpose

The `CalendarEvent` model represents a scheduled meeting, appointment, reminder, travel event, or blocked time that is relevant to an executive.

Unlike a raw calendar entry, a CalendarEvent enriches scheduling information with executive context, preparation guidance, potential conflicts, follow-up actions, and business significance.

Each CalendarEvent should remain traceable to the originating calendar system while providing actionable intelligence.

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | UUID/String | Unique EIB identifier |
| source | String | Originating calendar connector |
| title | String | Event title |
| start_timestamp | DateTime | Event start time |
| end_timestamp | DateTime | Event end time |
| organizer | String | Meeting organizer |
| priority | Integer | Executive priority (1–5) |
| confidence | Decimal | Confidence score |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| attendees | List[String] | Meeting attendees |
| optional_attendees | List[String] | Optional invitees |
| location | String | Physical or virtual location |
| meeting_url | String | Online meeting link |
| description | Markdown | Calendar description |
| agenda | Markdown | Executive agenda summary |
| preparation_notes | Markdown | Suggested preparation |
| expected_decisions | List[String] | Decisions expected |
| follow_up_required | Boolean | Indicates follow-up is expected |
| follow_up_notes | Markdown | Suggested follow-up |
| related_items | List[String] | Related EIB object IDs |
| source_reference | String | Calendar event identifier |

---

# Event Categories

Calendar events may be classified as:

- Executive Meeting
- Leadership
- One-on-One
- Project Review
- Security
- Governance
- Board Meeting
- Travel
- Training
- Personal
- Focus Time
- Reminder

---

# Executive Intelligence

Each CalendarEvent should answer:

- Why is this meeting important?
- What preparation is recommended?
- Who are the key participants?
- What decisions may be required?
- Are there related risks or dependencies?

---

# Conflict Analysis

Workflows may identify:

- Double bookings
- Travel conflicts
- Insufficient preparation time
- Consecutive high-priority meetings
- Missing agendas
- Missing required attendees

Detected conflicts should generate supporting `BriefingItem` objects and may generate `ActionItem` recommendations.

---

# Preparation Guidance

Preparation notes may include:

- Documents to review
- Previous meeting decisions
- Outstanding action items
- Recent project updates
- Relevant risks
- Questions requiring executive input

Preparation guidance should be concise and directly relevant to the meeting.

---

# Relationships

CalendarEvent may reference:

- BriefingItem
- ActionItem
- EmailSummary
- ProjectUpdate
- ExecutiveDecision
- Risk

---

# Lifecycle

1. Retrieved
2. Normalized
3. Enriched
4. Prioritized
5. Conflict Analysis
6. Published
7. Archived

---

# Validation Rules

A valid CalendarEvent must:

- Include a title
- Include start and end timestamps
- Include an organizer
- Have a valid priority
- Have a confidence value between 0.00 and 1.00
- Preserve a reference to the originating calendar event

---

# Example

```yaml
id: calendar-event-001
source: Google Calendar
title: Security Steering Committee
start_timestamp: 2026-07-28T13:30:00-07:00
end_timestamp: 2026-07-28T14:30:00-07:00
organizer: CIO
priority: 2
confidence: 0.99
attendees:
  - CIO
  - CISO
  - Privacy Officer
preparation_notes: >
  Review current cybersecurity metrics, outstanding risks,
  and proposed governance agenda items.
expected_decisions:
  - Approve quarterly security priorities
  - Review incident response metrics
```

---

# Future Enhancements

Future releases may include:

- AI-generated meeting briefs
- Automatic agenda creation
- Preparation checklists
- Travel time estimation
- Meeting effectiveness scoring
- Historical meeting context
- Suggested briefing documents
- Automatic follow-up generation

---

# Success Criteria

A CalendarEvent is successful when an executive can understand in less than one minute:

- Why the meeting matters
- What preparation is needed
- What decisions are expected
- Who the key participants are
- What follow-up is likely to result

The CalendarEvent model transforms a schedule into executive decision support rather than simply displaying appointments.