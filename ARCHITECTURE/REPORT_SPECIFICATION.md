---
title: Executive Briefing Report Specification
document_id: PA-004
version: 3.0
status: Approved
owner: BSJ
last_updated: 2026-08-07
depends_on:
  - ARCHITECTURE/PRODUCT_ARCHITECTURE.md
  - ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
  - ARCHITECTURE/SCORING_MODEL.md
  - ARCHITECTURE/PERSONALIZATION_MODEL.md
  - IMPLEMENTATION/BRIEFING_ASSEMBLY_ENGINE.md
---

# Executive Intelligence Briefing (EIB)

# Executive Briefing Report Specification

## Purpose

This document defines the standard structure, content, behavior, and quality expectations for the Executive Intelligence Briefing.

It specifies how intelligence should be organized and presented so that the final briefing remains:

- Concise
- Relevant
- Actionable
- Personalized
- Evidence-based
- Easy to scan
- Enjoyable to read
- Consistent enough to become familiar
- Flexible enough to adapt to the user's actual day

The objective is not to maximize information.

The objective is to maximize useful understanding in the minimum practical amount of executive time.

---

# Standard Reading Time

The standard daily briefing should normally require approximately:

```text
5–7 minutes
```

to read.

The briefing should not gradually expand into a long-form morning report simply because additional information is available.

When additional detail is useful, EIB should:

- Summarize it.
- Link or reference supporting material.
- Make deeper detail available on demand.

---

# Executive Design Questions

The briefing should help answer:

1. What does my day look like?
2. What changed?
3. What matters most?
4. Why does it matter?
5. What should I consider doing?
6. What should I keep watching?

Not every section must answer every question.

The complete briefing should answer all of them collectively.

---

# Design Principles

## Calendar First

The briefing should begin with the user's actual day.

Calendar context influences the relevance of other intelligence.

Examples:

```text
Meeting today
     +
Related external development
     ↓
Higher priority
```

The user should not receive:

```text
Nothing on the calendar
```

when calendar information was simply unavailable.

Source unavailability must be distinguishable from an empty schedule.

---

## Intelligence Before Information

Do not include an item merely because it is interesting.

An item should earn space by contributing:

- Context
- Relevance
- Risk
- Opportunity
- Preparation
- Decision support
- Action

---

## Recommendations Near the Intelligence

Recommended actions should normally appear adjacent to the intelligence that generated them.

Avoid creating a disconnected list of actions whose rationale is unclear.

---

## Metrics With Meaning

Important metrics should include:

1. Current value
2. Change or comparison
3. Interpretation

Example:

```text
Medical Vesting

85%

+5 percentage points

Progress continues toward the next vesting milestone.
```

A number without context is not executive intelligence.

---

## Direction Matters

Where meaningful, risk or performance should indicate trajectory.

Examples:

```text
Increasing
Stable
Decreasing
```

The user should be able to understand whether conditions are improving or deteriorating.

---

## Confidence Is Visible

When information is uncertain, the briefing should say so.

Possible labels include:

```text
Verified
Developing
Estimated
```

The system must not create false certainty for presentation purposes.

---

## Personalized, Not Distorted

The briefing should reflect the user's:

- Role
- Responsibilities
- Calendar
- Strategic locations
- Preferences
- Active projects
- Reading style

Personalization must not alter underlying facts or hide critical intelligence.

---

## Useful but Human

The briefing should remain professional without becoming sterile.

The desired balance is:

> Data-rich, concise, useful—and still a little fun.

The product must not devolve into:

> "Just the facts, ma'am."

A small amount of human context can improve the daily experience without reducing executive value.

---

# Standard Briefing Structure

The exact presentation may evolve, but the standard daily briefing should generally follow this sequence.

---

## 1. Daily Orientation

Provide immediate context for the day.

Potential elements include:

- Date
- Day of week
- Current location or profile context
- Brief opening observation when appropriate

This section should be extremely brief.

---

## 2. Calendar and Schedule

Calendar information should appear near the beginning.

Include:

- Important meetings
- Appointments
- Deadlines
- Travel
- Preparation needs
- Schedule conflicts
- Relevant meeting context

Avoid reproducing every low-value event merely because it exists.

---

## 3. Weather and Strategic Locations

When enabled, provide weather for the user's configured strategic location or locations.

Potential metrics include:

- Current conditions
- High / low
- Precipitation
- Wind
- Sunrise
- Sunset

Where a comparison location is configured, provide a useful comparison.

Example:

```text
Home
78°F

San Diego
71°F

Seven degrees cooler at the coast today.
```

The comparison should include both useful metrics and a brief human interpretation.

---

# Strategic Location Requirements

The report specification must not assume the user lives in a particular city, state, or country.

Users should be able to configure:

- Primary location
- Secondary location
- Favorite comparison location
- Travel destinations
- Other strategic places

Locations may be anywhere in the world.

Localization should support appropriate:

- Units
- Time zones
- Date formats
- Currency
- Language

---

## 4. Executive Priorities

Present the most important intelligence requiring attention.

The number of top priorities should remain limited.

Each priority may include:

```text
Title
What changed
Why it matters
Risk or opportunity
Confidence
Recommendation
```

Avoid forcing every item into the same verbose template when a shorter presentation is sufficient.

---

## 5. Domain Intelligence

Relevant domain sections may include:

- Cybersecurity
- Technology
- Government / Regulatory
- Organization
- Workforce
- Finance
- Projects
- Travel
- Property
- Other configured domains

Domains should appear based on relevance rather than merely because they are available.

---

# Cybersecurity

Cybersecurity intelligence should emphasize:

- Material vulnerabilities
- Active exploitation
- Significant compromises
- Emerging AI/security issues
- Vendor or platform exposure
- Regulatory implications
- Internal relevance when known

Important developments should not be omitted simply because they do not fit a narrow traditional cybersecurity category.

Where appropriate, include:

```text
What happened
Enterprise relevance
Risk direction
Recommended action
Confidence
```

---

# Technology and AI

Technology intelligence should focus on:

- Material platform developments
- Enterprise AI implications
- Vendor changes
- Architecture implications
- Relevant market shifts
- Emerging risks and opportunities

Avoid generic technology-news aggregation.

---

# Government and Regulatory

Include only developments with meaningful relevance.

Potential content includes:

- Legislation
- Regulation
- Government technology policy
- Security requirements
- Privacy requirements
- Funding or budget implications

---

# Metrics and Operational Intelligence

Metrics should be presented compactly.

Preferred conceptual pattern:

```text
Metric

Current value

Change

Interpretation
```

Example:

```text
Critical Vulnerabilities

24

-12%

Improving from the prior reporting period.
```

Metric commentary should remain brief.

---

## 6. Recommendations

Recommendations should normally accompany the relevant intelligence.

A short consolidated action summary may also appear when useful.

Recommendations should communicate:

- Suggested action
- Urgency
- Reason
- Owner when appropriate

The system should distinguish:

```text
Recommendation
```

from:

```text
Automated action already taken
```

---

## 7. Forward Look

Briefly identify what deserves monitoring beyond today.

Examples:

- Upcoming deadlines
- Developing risks
- Expected announcements
- Travel
- Major meetings
- Events within the next several days

This should remain concise.

---

## 8. Human Moment

The briefing may include approximately one optional human element when context makes it worthwhile.

Examples:

- Outdoor-weather observation
- Travel comparison
- Relevant leadership thought
- Personal milestone
- Weekend context
- Brief humor

The human element should:

- Be relevant.
- Be short.
- Avoid excessive repetition.
- Never crowd out intelligence.

---

# Quote and Repetition Control

Quotes, leadership principles, trivia, or recurring commentary should not appear merely because there is a slot available.

The system should avoid repeatedly presenting the same content.

Recent-history awareness should prevent overuse of:

- The same quote
- The same leadership observation
- The same joke
- The same narrative framing

Optional content should remain genuinely optional.

---

# Briefing Density

The briefing should optimize for information density without sacrificing readability.

Prefer:

```text
Metric + interpretation
```

over:

```text
Several paragraphs explaining a simple number
```

Prefer:

```text
Short contextual recommendation
```

over:

```text
A disconnected action section requiring the reader to reconstruct the rationale
```

---

# Mobile-First Presentation

The briefing should work well on:

- Phones
- Tablets
- Desktop browsers
- Email
- Markdown viewers

Presentation should therefore favor:

- Short sections
- Scannable headings
- Compact tables
- Limited horizontal width
- Avoidance of overly complex layouts

---

# Output Formats

EIB should support or evolve toward:

- Markdown
- HTML
- Mobile-friendly presentation
- Email
- PDF
- Interactive interfaces
- Voice briefing

The intelligence structure should remain independent of output format.

---

# Briefing Versioning

Generated briefings should include sufficient metadata to identify:

- Generation date
- Generation time
- User profile
- Applicable configuration
- Briefing version when needed

Generated daily briefings are intelligence products and should not require manual document-version maintenance like governed architecture documents.

---

# Quality Standards

Every briefing should strive to be:

- Accurate
- Timely
- Relevant
- Traceable
- Concise
- Personalized
- Explainable
- Free from unnecessary duplication
- Clear about uncertainty
- Useful for action

---

# Content Exclusion

An item should normally be omitted when:

- It does not materially affect the user.
- It merely repeats previously covered information.
- It cannot be reasonably verified.
- It adds detail without increasing understanding.
- It exists only to fill a section.
- It makes the briefing materially longer without sufficient value.

Empty sections should generally disappear rather than announce that nothing was found.

---

# Exception: Source Failure

Source failure is different from no findings.

Examples:

```text
No meetings scheduled
```

is different from:

```text
Calendar unavailable
```

Likewise:

```text
No material cyber developments
```

is different from:

```text
Cybersecurity sources could not be verified
```

The briefing should communicate that distinction when it matters.

---

# Personalization

Briefing content may adapt based on:

- Role
- Responsibilities
- Strategic priorities
- User preferences
- Current calendar
- Strategic locations
- Reading preferences
- Active projects
- Explicit feedback

The core structure should remain familiar enough that users know where to look for important information.

---

# Learning and Feedback

Future briefings may improve through:

- User corrections
- Accepted recommendations
- Dismissed recommendations
- Explicit preference changes
- Requests for more or less detail
- Repetition feedback

Explicit user feedback should take precedence over weak inferred preferences.

---

# Standard Briefing Success Criteria

The standard report succeeds when:

- It normally takes approximately 5–7 minutes to read.
- The user quickly understands the day ahead.
- The most important intelligence is easy to identify.
- Metrics include useful interpretation.
- Risks communicate direction where possible.
- Recommendations explain why they exist.
- Strategic-location information is configurable.
- The briefing remains professional but not sterile.
- Optional human elements do not become repetitive.
- Important source failures are clearly distinguished from empty results.
- Supporting detail remains available without overwhelming the briefing.

---

# Future Enhancements

Potential capabilities include:

- Interactive drill-down
- Voice briefing generation
- Executive question-and-answer mode
- Multi-language briefings
- Dynamic briefing depth
- Comparative intelligence
- Personalized dashboards
- User-configurable section ordering
- Additional strategic-location comparisons
- Proactive recommendation tracking

These enhancements must preserve the core principle of concise executive intelligence.

---

# Repository Foundation Impact

During Repository Foundation migration:

- This document moves from `Architecture/` to canonical `ARCHITECTURE/`.
- Existing identifier `PA-004` is preserved pending broader identifier reconciliation.
- Dependencies are updated to canonical paths.
- The standard reading target is refined from "less than ten minutes" to approximately 5–7 minutes.
- Calendar-first context is formalized.
- Weather now includes configurable sunrise and sunset.
- Strategic locations are generalized for any user and country.
- Metrics require both measurement and interpretation.
- Repetition control is formalized.
- The briefing's professional-but-fun character becomes an explicit product requirement.

---

# Related Documents

- ARCHITECTURE/PRODUCT_ARCHITECTURE.md
- ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
- ARCHITECTURE/PERSONALIZATION_MODEL.md
- ARCHITECTURE/SCORING_MODEL.md
- ARCHITECTURE/DATA_SOURCE_STRATEGY.md
- IMPLEMENTATION/BRIEFING_ASSEMBLY_ENGINE.md
- IMPLEMENTATION/PRIORITY_ENGINE.md
- IMPLEMENTATION/RECOMMENDATION_ENGINE.md
- PERSONALITY/executive_balanced.md
- PROFILES/profile_schema.md

---

# Guiding Principle

> The briefing should be short enough to read every day, useful enough to influence decisions, and human enough that the user actually wants to read it.