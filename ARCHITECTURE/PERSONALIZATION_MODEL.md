---
title: Executive Personalization Model
document_id: PA-008
version: 3.0
status: Approved
owner: BSJ
last_updated: 2026-08-07
depends_on:
  - ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
  - ARCHITECTURE/SCORING_MODEL.md
  - ARCHITECTURE/REPORT_SPECIFICATION.md
  - IMPLEMENTATION/CONFIGURATION_AND_PROFILE_MODEL.md
---

# Executive Intelligence Briefing (EIB)

# Executive Personalization Model

## Purpose

This document defines how EIB personalizes intelligence for each user while preserving a consistent, explainable, and trustworthy briefing experience.

Personalization determines:

- Which relevant intelligence deserves greater emphasis.
- Which context matters to the user.
- How information should be presented.
- What level of detail is appropriate.
- Which strategic locations, topics, responsibilities, and preferences should influence the briefing.

Personalization must improve relevance without changing underlying facts.

---

# Design Philosophy

> Every user should receive the same truth, but not necessarily the same briefing.

Personalization occurs after information has been collected, validated, normalized, enriched, and scored.

It may influence relevance and presentation, but it must not manufacture facts, suppress critical intelligence, or silently alter source information.

---

# Objectives

The personalization model should:

- Increase relevance.
- Reduce cognitive load.
- Preserve factual consistency.
- Remain explainable.
- Support explicit user configuration.
- Adapt carefully over time.
- Support multiple executive and non-executive personas.
- Work internationally.
- Separate personal preferences from shared platform logic.
- Preserve user control.

---

# Personalization Pipeline

```text
Normalized Intelligence
        │
        ▼
Base Scoring
        │
        ▼
User Profile
        │
        ▼
Role and Responsibility Context
        │
        ▼
Interest and Priority Matching
        │
        ▼
Strategic Location Context
        │
        ▼
Personal Relevance Adjustment
        │
        ▼
Presentation Rules
        │
        ▼
Briefing Composition
```

---

# Core Principle

Personalization adjusts **relevance and presentation**.

It does not rewrite reality.

The architecture should preserve a conceptual separation between:

```text
Fact
   │
   ▼
Intelligence
   │
   ▼
Personal Relevance
   │
   ▼
Presentation
```

---

# User Profile

Each user profile may contain configurable attributes such as:

- Name
- Role
- Organization
- Business unit
- Areas of responsibility
- Strategic priorities
- Preferred topics
- Strategic locations
- Time zone
- Language
- Regional context
- Reading preferences
- Notification preferences
- Personality preference
- Historical interests
- Explicit exclusions
- Active projects

Profiles should be configuration-driven rather than hard-coded into EIB.

---

# Role-Based Personalization

Different roles require different perspectives.

Examples include:

## CIO

Potential emphasis:

- Enterprise technology
- Digital transformation
- Major initiatives
- IT operations
- Technology investment
- Vendor strategy
- Enterprise architecture

---

## CISO

Potential emphasis:

- Cybersecurity
- Privacy
- Threat intelligence
- Risk
- Compliance
- Vulnerability trends
- Security architecture

---

## Executive Director

Potential emphasis:

- Enterprise risk
- Organizational performance
- Legislative activity
- Public perception
- Strategic initiatives
- Workforce
- Budget

---

## Division Chief

Potential emphasis:

- Operational performance
- Staffing
- Budget
- Projects
- Service delivery
- Program risks

These are examples, not fixed product assumptions.

Role behavior should be configurable.

---

# Responsibility Context

Role title alone is insufficient.

Personalization should also consider explicit areas of responsibility.

Examples:

```text
Cybersecurity
Privacy
Cloud
Infrastructure
Budget
Operations
Human Resources
Property Management
Travel
Family Planning
Retirement
```

Two users with identical titles may therefore receive meaningfully different briefings.

---

# Strategic Locations

EIB must not hard-code concepts such as:

```text
Home
San Diego
Sacramento
United States
```

Users may define one or more **Strategic Locations**.

Examples include:

- Primary residence
- Secondary residence
- Office
- Rental property
- Vacation destination
- Family location
- Travel destination
- International business location

A strategic location may contain:

```text
location_id
label
city
region
country
time_zone
latitude
longitude
priority
comparison_enabled
weather_enabled
travel_relevance
```

Strategic locations may support:

- Weather
- Sunrise and sunset
- Travel context
- Time-zone awareness
- Local events
- Regional risk
- Geographic comparisons

---

# International Support

Personalization must support users outside the United States.

The architecture must not assume:

- U.S. addresses
- Fahrenheit
- Miles
- U.S. dollars
- U.S. time zones
- English-only output
- U.S.-specific public agencies
- U.S.-specific weather providers

Localization should be profile- and configuration-driven.

Potential preferences include:

```text
temperature_unit
distance_unit
currency
locale
language
date_format
time_format
```

---

# Topic Preferences

Users may identify preferred topics.

Examples include:

- Artificial Intelligence
- Healthcare
- Cybersecurity
- Privacy
- Cloud
- Budget
- Workforce
- Infrastructure
- Legislation
- Travel
- Property
- Markets

Preferred topics may influence ranking.

They must not suppress critical intelligence merely because a subject is not ordinarily preferred.

---

# Priority Adjustment

Personalization may modify the base priority assessment.

Potential inputs include:

- User responsibilities
- Strategic priorities
- Active projects
- Current calendar
- Strategic locations
- Explicit interests
- Historical relevance
- Known deadlines

Conceptually:

```text
Base Priority
      +
Personal Relevance
      +
Current Context
      =
Personalized Priority
```

The base intelligence score should remain available for explainability.

---

# Critical Intelligence Protection

Personalization must not hide information that exceeds defined criticality thresholds.

Examples may include:

- Severe security incidents
- Immediate safety risks
- Major organizational disruptions
- Critical deadlines
- Significant regulatory events

A preference such as:

```text
Low interest in cybersecurity
```

must never suppress:

```text
Critical enterprise security incident
```

---

# Calendar Context

Calendar information may materially affect relevance.

Examples:

```text
Meeting with vendor today
        +
Vendor security news
        ↓
Higher relevance
```

```text
Travel tomorrow
        +
Destination weather disruption
        ↓
Higher relevance
```

Calendar context should therefore be available to personalization and prioritization.

---

# Reading Preferences

Users may prefer different briefing depths.

Potential profiles include:

```text
Concise
Standard
Detailed
```

The normal EIB daily briefing should remain concise enough to consume in approximately:

```text
5–7 minutes
```

unless the user explicitly requests additional detail.

---

# Presentation Preferences

Presentation preferences may include:

- Mobile-first
- Email-first
- Markdown
- Rich interface
- Detailed metrics
- Narrative emphasis
- Bullet emphasis
- Executive summary emphasis

Presentation behavior should remain separate from the underlying intelligence.

---

# Personality

Personality affects **how intelligence is communicated**, not what the facts are.

Examples may include:

- Executive balanced
- Concise
- Analytical
- Conversational

Personality rules should be managed separately from intelligence scoring.

Conceptually:

```text
Intelligence
     │
     ▼
Personalization
     │
     ▼
Personality
     │
     ▼
Presentation
```

---

# Human Experience

EIB should remain professional without becoming sterile.

A briefing may contain limited enjoyable elements such as:

- Weather comparisons
- Sunrise and sunset
- Travel countdowns
- Weekend context
- Relevant leadership observations
- Personal milestones
- A small humorous or human observation

These elements should remain relevant and restrained.

The objective is:

> useful enough for an executive briefing, but enjoyable enough that the user wants to read it every day.

---

# One Human Moment

A standard briefing may include approximately one small contextual personal element when appropriate.

Examples:

```text
Perfect evening weather for nine holes.
```

```text
Sunset is late enough tonight to squeeze in an outdoor project.
```

```text
Your destination is considerably cooler than home today.
```

The human element should never crowd out priority intelligence.

---

# Repetition Control

Personalization should avoid repeatedly surfacing the same optional content.

Examples include:

- Quotes
- Trivia
- Personal observations
- Recurring commentary

EIB should maintain sufficient history to avoid excessive repetition.

---

# Metrics Preferences

Users may prefer data-rich intelligence.

Where metrics are presented, personalization may affect:

- Which metrics appear.
- Desired level of explanation.
- Comparison periods.
- Directional indicators.

Metrics should still include interpretation.

Example:

```text
Critical Vulnerabilities

24

(-12%)

Improving from the previous reporting period.
```

---

# Explainability

EIB should be able to explain why an item received personalized emphasis.

Example:

> Included because this issue relates to your cybersecurity responsibilities, affects a current strategic initiative, and has high urgency.

Explainability may include:

- Base priority
- Personal relevance
- Current context
- Strategic-location relevance
- Calendar relevance
- Explicit user preference

---

# Learning Model

EIB may improve personalization over time.

Potential signals include:

- Explicit feedback
- Topics repeatedly opened
- Recommendations accepted
- Recommendations dismissed
- User preference changes
- Manual corrections
- Repeated requests for more or less detail

Implicit behavioral signals should have less authority than explicit user configuration.

---

# User Control

Users should be able to:

- View important personalization settings.
- Change preferences.
- Override learned behavior.
- Disable optional personalization.
- Add or remove strategic locations.
- Reset learned preferences.

AI-generated learning must not become an invisible permanent policy.

---

# Privacy

Personalization must follow purpose limitation.

EIB should:

- Collect only information needed for legitimate personalization.
- Avoid unnecessary behavioral profiling.
- Protect private profile information.
- Keep personal profiles out of public repositories.
- Respect public/private repository boundaries established in ADR-0001.

---

# Profile Separation

Public EIB architecture should contain:

- Profile schemas
- Example profiles
- Fictional sample configurations

Private implementations may contain:

- Actual user profiles
- Real strategic locations
- Personal preferences
- Private connected-source configuration

This separation allows EIB to remain reusable without exposing personal information.

---

# Configuration

Profile behavior should increasingly be represented through structured configuration.

Example conceptual profile:

```yaml
profile:
  role: executive
  briefing_length: standard
  personality: executive_balanced

preferences:
  topics:
    - cybersecurity
    - technology
    - leadership

locations:
  - label: primary
    weather_enabled: true

units:
  temperature: fahrenheit
  distance: miles
```

Actual schema is defined by:

```text
IMPLEMENTATION/CONFIGURATION_AND_PROFILE_MODEL.md
```

---

# Personalization Engine

The Personalization Engine should eventually provide a dedicated implementation for:

- Role matching
- Responsibility matching
- Topic affinity
- Strategic-location relevance
- Calendar context
- Priority adjustment
- Presentation preferences
- Learning signals

The engine should expose its adjustments for explainability.

---

# Failure Behavior

Personalization failure should not prevent the core briefing from being generated.

Example:

```text
Profile unavailable
       ↓
Use safe default briefing profile
       ↓
Preserve critical intelligence
```

The system should prefer a neutral briefing over inventing user preferences.

---

# Repository Foundation Impact

During Repository Foundation migration:

- This document moves from `Architecture/` to canonical `ARCHITECTURE/`.
- Existing identifier `PA-008` is preserved pending broader identifier reconciliation.
- Dependencies are updated to canonical paths.
- Strategic Locations are generalized beyond any specific user's home or favorite location.
- International support becomes an explicit requirement.
- Personality is explicitly separated from intelligence.
- The standard briefing remains concise while retaining an enjoyable human element.

---

# Success Criteria

The personalization model succeeds when:

- Users consistently receive relevant intelligence.
- Critical information remains visible.
- Personalization reduces cognitive load.
- Facts remain unchanged by presentation preferences.
- Users can understand why content was emphasized.
- Profiles remain configurable.
- Strategic locations work internationally.
- Users retain control over learned preferences.
- The briefing remains both useful and enjoyable.
- Personalization can evolve without creating user-specific source-code branches.

---

# Related Documents

- ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
- ARCHITECTURE/SCORING_MODEL.md
- ARCHITECTURE/REPORT_SPECIFICATION.md
- ARCHITECTURE/PRODUCT_ARCHITECTURE.md
- ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
- IMPLEMENTATION/CONFIGURATION_AND_PROFILE_MODEL.md
- IMPLEMENTATION/PRIORITY_ENGINE.md
- PERSONALITY/executive_balanced.md
- PROFILES/profile_schema.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md

---

# Guiding Principle

> Same truth. Different relevance. Appropriate presentation.

Personalization should make EIB feel built for the user without making the underlying intelligence less objective.