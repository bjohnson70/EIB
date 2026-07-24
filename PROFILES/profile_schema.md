---
title: User Profile Schema
schema_id: PROFILE-001
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# User Profile Schema

## Purpose

The User Profile defines the information that personalizes the Executive Intelligence Briefing (EIB).

Rather than hard-coding assumptions into prompts or workflows, all user-specific preferences, routines, locations, interests, and personalization settings should reside within the profile.

The profile answers a single question:

> **"Who is this briefing being prepared for?"**

---

# Design Principles

Profiles should be:

- Portable
- Human readable
- Version controlled
- Extensible
- Independent of connectors
- Independent of prompts

A workflow should be able to generate a personalized briefing simply by reading the profile.

---

# High-Level Structure

```yaml
profile:
  identity:
  organization:
  preferences:
  locations:
  schedule:
  interests:
  communications:
  personalization:
```

---

# Identity

Defines the individual receiving the briefing.

Example fields:

```yaml
identity:
  full_name:
  preferred_name:
  title:
  organization:
  department:
  timezone:
  locale:
```

---

# Organization

Defines organizational context.

```yaml
organization:
  role:
  manager:
  executive_level:
  business_unit:
```

---

# Preferences

General user preferences.

```yaml
preferences:

  units:
    temperature:
    distance:
    currency:

  language:

  work_style:

  briefing_length:

  personality:

  quote_frequency:
```

---

# Strategic Locations

Strategic Locations are reusable places that matter to the user.

Examples include:

- Home
- Office
- Frequent destination
- Regional office
- Customer
- Family
- Vacation home

Example:

```yaml
locations:

  - name: Elk Grove
    role: Home

  - name: San Diego
    role: Vacation Home

  - name: London
    role: Regional Office

  - name: Tokyo
    role: Supplier
```

Workflows may use these locations for:

- Weather
- Time zones
- News
- Travel
- Security alerts
- Regional events
- Market intelligence

---

# Schedule

Typical working preferences.

```yaml
schedule:

  work_days:

  office_days:

  preferred_meeting_hours:

  focus_time:

  travel_preferences:
```

---

# Interests

Personal interests used only when they enhance the briefing.

Examples:

```yaml
interests:

- Golf
- Camping
- Travel
- Technology
- Aviation
- Photography
```

These should never dominate the briefing.

They simply provide opportunities for occasional personalization.

---

# Communication

Defines communication preferences.

```yaml
communications:

  greeting:

  closing:

  humor_level:

  detail_level:

  quote_style:
```

---

# Personalization

Controls optional enhancements.

```yaml
personalization:

  weather: true

  countdowns: true

  birthdays: true

  anniversaries: true

  travel: true

  leadership_quotes: true

  weekend_preview: true
```

Organizations may disable individual features while retaining the same workflows.

---

# Extensibility

Future versions may include:

- Family members
- Pets
- Sports teams
- Favorite restaurants
- Professional certifications
- Retirement planning
- Health goals
- Reading lists
- Learning objectives

Extensions should never require breaking changes.

---

# Validation Rules

A valid profile should include:

- Identity
- Time zone
- Locale
- Personality
- At least one Strategic Location

Everything else is optional.

---

# Relationship to Other Components

The profile influences:

- Connectors
- Workflows
- Prompts
- Personality profiles
- Weather
- News
- Travel
- Executive summaries

The profile should never contain transient data such as email messages or calendar events.

It defines the user—not today's briefing.

---

# Success Criteria

A successful profile allows EIB to answer:

- Who am I preparing this briefing for?
- What matters most to this person?
- How should I communicate with them?
- What information is most relevant?
- How can I make the briefing both useful and enjoyable?

The User Profile is the personalization foundation of EIB and should remain stable as new capabilities are added.