---
title: Executive Priority Engine
component_id: ENGINE-001
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# Executive Priority Engine

## Purpose

The Executive Priority Engine determines the relative importance of every item considered for inclusion in an Executive Intelligence Briefing (EIB).

Its objective is to ensure the briefing presents the most valuable information first, reducing cognitive load while maximizing executive preparedness.

The Priority Engine answers a single question:

> **"If the executive only reads the first page, what must they know?"**

---

# Design Principles

The engine should be:

- Explainable
- Deterministic
- Consistent
- Configurable
- User-aware
- Transparent

Priority scores should never be random or opaque.

---

# Executive Priority Score (EPS)

Every briefing item receives an Executive Priority Score (EPS).

```
EPS = Σ(weight × factor)
```

Scores range from:

| Score | Priority |
|-------:|----------|
| 90–100 | Critical |
| 75–89 | High |
| 50–74 | Medium |
| 25–49 | Low |
| 0–24 | Informational |

---

# Scoring Factors

## Business Impact

How significant is the potential organizational effect?

| Value | Weight |
|------:|-------:|
| Minimal | 0 |
| Moderate | 10 |
| Significant | 20 |
| Enterprise | 30 |

---

## Time Sensitivity

How quickly does action become less valuable?

| Condition | Points |
|-----------|-------:|
| Immediate | 25 |
| Today | 20 |
| This Week | 10 |
| Future | 5 |
| None | 0 |

---

## Executive Relevance

Does the item require executive awareness or decision-making?

| Audience | Points |
|----------|-------:|
| Executive Decision | 25 |
| Executive Awareness | 15 |
| Team Awareness | 5 |
| Operational Only | 0 |

---

## Change Since Last Briefing

New information deserves attention.

| Condition | Points |
|-----------|-------:|
| Brand New | 20 |
| Significant Update | 15 |
| Minor Update | 5 |
| No Change | 0 |

---

## Risk Level

| Level | Points |
|-------|-------:|
| Critical | 25 |
| High | 18 |
| Medium | 10 |
| Low | 5 |
| None | 0 |

---

## User Context

Profile-driven modifiers may adjust the score.

Examples:

- Upcoming travel
- Calendar conflicts
- Active project ownership
- Preferred locations
- Current vacation
- Role-specific responsibilities

Typical adjustment:

±10 points

---

# Priority Bands

## Critical (90–100)

Always displayed.

Cannot be hidden.

Examples:

- Executive decision today
- Active cybersecurity incident
- Major operational outage
- Regulatory deadline

---

## High (75–89)

Displayed prominently.

Examples:

- Important meetings
- Escalated risks
- Upcoming deadlines
- Customer-impacting issues

---

## Medium (50–74)

Displayed in normal briefing order.

Examples:

- Informational updates
- Moderate risks
- Project milestones

---

## Low (25–49)

Included only if space permits.

---

## Informational (0–24)

Usually omitted from the executive summary.