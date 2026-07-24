---
title: Email Summary Data Model
model_id: MODEL-003
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# EmailSummary

## Purpose

The `EmailSummary` model represents an executive-focused summary of an email message or email thread.

Its purpose is to reduce inbox noise by extracting the information that matters most to executive decision-making while preserving links to the original source.

Each `EmailSummary` should reference one or more `BriefingItem` objects and may generate one or more `ActionItem` objects.

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | UUID/String | Unique identifier |
| source | String | Always "Gmail" unless another email connector is used |
| subject | String | Email subject |
| sender | String | Display name or email address |
| received_timestamp | DateTime | When the email was received |
| summary | Markdown | Executive summary |
| priority | Integer | Executive priority (1–5) |
| confidence | Decimal | Confidence score (0.00–1.00) |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| recipients | List[String] | Primary recipients |
| cc | List[String] | Carbon copy recipients |
| thread_id | String | Email conversation identifier |
| message_id | String | Original message identifier |
| category | String | Executive classification |
| labels | List[String] | Email labels |
| attachments | List[String] | Attachment filenames |
| due_date | Date | Deadline identified in the message |
| action_required | Boolean | Indicates follow-up is needed |
| url | String | Link to original message |
| source_items | List[String] | Related BriefingItem IDs |
| related_items | List[String] | Related EIB object IDs |

---

# Executive Categories

Email may be classified as:

- Executive Decision
- Action Required
- Calendar
- Project
- Security
- Incident
- Regulatory
- Financial
- Personnel
- Informational

---

# Executive Rules

The summary should answer:

- Why was this email sent?
- Why does it matter?
- Does it require action?
- Is there a deadline?
- Who owns the next step?

Long email threads should be summarized into a single executive narrative.

---

# Attachment Handling

Attachments should not be duplicated.

Instead record:

- filename
- type
- availability
- significance

Future versions may support AI-generated attachment summaries.

---

# Relationships

EmailSummary may reference:

- BriefingItem
- ActionItem
- CalendarEvent
- ProjectUpdate
- ExecutiveDecision

---

# Lifecycle

1. Retrieved
2. Normalized
3. Summarized
4. Classified
5. Prioritized
6. Published
7. Archived

---

# Validation Rules

A valid EmailSummary must:

- Include sender
- Include subject
- Include received timestamp
- Include executive summary
- Have a priority between 1 and 5
- Have confidence between 0.00 and 1.00
- Reference the original message

---

# Example

```yaml
id: email-001
source: Gmail
subject: Quarterly Security Steering Committee
sender: CIO
received_timestamp: 2026-07-24T08:05:00-07:00
priority: 2
confidence: 0.98
summary: >
  The CIO requested agenda items for next week's Security Steering
  Committee meeting. Responses are requested by Tuesday.
action_required: true
due_date: 2026-07-28
```

---

# Future Enhancements

Future releases may include:

- Thread summarization
- AI importance scoring
- Sentiment analysis
- Executive relationship scoring
- Auto-generated replies
- Attachment summarization
- Deadline extraction
- Cross-linking to calendar events

---

# Success Criteria

An EmailSummary is successful when an executive can determine, in less than 30 seconds:

- What the email is about
- Why it matters
- Whether action is required
- When action is due
- Where to find the original message

The EmailSummary model enables executives to process large volumes of email efficiently without losing important context.