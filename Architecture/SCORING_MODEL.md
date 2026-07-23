---
title: Executive Intelligence Scoring Model
document_id: PA-0005
version: 1.0
status: Approved
owner: Bryan Johnson
author: Bryan Johnson & ChatGPT
last_updated: 2026-07-23
depends_on:
  - ../VISION.md
  - PRODUCT_ARCHITECTURE.md
  - INTELLIGENCE_ARCHITECTURE.md
---

# Executive Intelligence Scoring Model

## Purpose

This document defines the scoring methodology used by the Executive Intelligence Briefing (EIB) to determine which information is included, how it is prioritized, and how it is presented.

The objective is to consistently identify the information that provides the greatest executive value.

---

# Design Goals

The scoring model shall:

- Prioritize executive decision-making.
- Reduce cognitive load.
- Promote consistency.
- Support explainable rankings.
- Minimize omission of high-impact events.
- Continuously improve through feedback.

---

# Executive Intelligence Equation

Every intelligence item receives an Executive Intelligence Score (EIS).

The score represents the combined executive value of an intelligence item.

Higher scores indicate greater briefing priority.

---

# Scoring Dimensions

Each item is evaluated across the following dimensions.

## Importance

How significant is the event?

Scale:

1–10

Examples:

- Local outage = 3
- State legislation = 7
- Global cyber campaign = 10

---

## Urgency

How quickly must an executive respond?

Scale:

1–10

Examples:

- Informational article = 2
- Active ransomware campaign = 10

---

## Executive Impact

How much could this influence executive decisions?

Scale:

1–10

---

## Organizational Impact

Does the event affect the executive's organization?

Scale:

1–10

---

## Personal Relevance

Does this directly affect the executive?

Examples:

- Calendar
- Travel
- Projects
- Retirement
- Weather
- Health (if enabled)

Scale:

1–10

---

## Geographic Relevance

Priority order:

1. Local
2. California
3. United States
4. International

Scores should reflect the executive's operating environment.

---

## Decision Value

Will this information likely change an executive decision?

Scale:

1–10

This is one of the highest weighted dimensions.

---

## Operational Impact

Does this influence today's operations?

Examples:

- Major outage
- Travel disruption
- Security incident
- Legislative deadline

Scale:

1–10

---

## Confidence

How reliable is the information?

Confidence levels:

- Verified
- High
- Moderate
- Developing
- Unverified

Lower confidence reduces ranking.

---

## Time Sensitivity

How quickly does the value of the information decline?

Examples:

Breaking events receive higher scores than historical analysis.

---

# Priority Bands

## Critical

Immediate executive attention.

Displayed first.

---

## High

Likely requires awareness today.

---

## Medium

Useful executive context.

---

## Low

Optional awareness.

May be omitted if briefing length constraints require.

---

# Coverage Override

Coverage Assurance may elevate an item regardless of score.

Examples:

- Major cybersecurity incident
- Governor's emergency declaration
- Critical vulnerability
- Significant AI announcement
- Major financial disruption

Coverage completeness always takes precedence over algorithmic optimization.

---

# Personalization Adjustment

The base score may be adjusted based upon:

- Executive role
- Organization
- Calendar
- Projects
- Geographic location
- Standing interests

Personalization affects ranking—not factual accuracy.

---

# Diversity Adjustment

The briefing should avoid overrepresentation of a single topic.

If numerous items have similar scores, diversity should be favored.

Example:

Instead of ten cybersecurity stories, provide:

- Three cybersecurity
- Two technology
- Two government
- Two markets
- One leadership

unless a major event justifies otherwise.

---

# Explainability

Every intelligence item should be explainable.

The platform should