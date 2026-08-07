---
title: Executive Intelligence Scoring Model
document_id: PA-007
version: 3.0
status: Approved
owner: BSJ
last_updated: 2026-08-07
depends_on:
  - ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
  - ARCHITECTURE/REPORT_SPECIFICATION.md
  - ARCHITECTURE/PERSONALIZATION_MODEL.md
  - ARCHITECTURE/DATA_SOURCE_STRATEGY.md
  - IMPLEMENTATION/PRIORITY_ENGINE.md
  - IMPLEMENTATION/CONFIDENCE_ENGINE.md
---

# Executive Intelligence Briefing (EIB)

# Executive Intelligence Scoring Model

## Purpose

This document defines how EIB evaluates, ranks, and prioritizes candidate intelligence before personalization and briefing composition.

The scoring model does not determine whether something is true.

Validation and confidence assessment address evidence quality.

Scoring answers a different question:

> How much executive attention does this deserve?

---

# Objectives

The scoring model should:

- Prioritize executive value.
- Remain explainable.
- Produce reasonably consistent results.
- Support changing priorities.
- Adapt to different user profiles.
- Reward useful novelty.
- Penalize unnecessary repetition.
- Protect critical intelligence from accidental suppression.
- Support configuration rather than hard-coded user behavior.

No single scoring factor should determine the final result.

---

# Conceptual Flow

```text
Validated Intelligence
        │
        ▼
Base Scoring
        │
        ▼
Priority Classification
        │
        ▼
Personal Relevance Adjustment
        │
        ▼
Briefing Selection
```

Scoring and personalization are related but distinct.

Base scoring should remain available for explainability even after personalization is applied.

---

# Multi-Factor Scoring Framework

Candidate intelligence may be evaluated across the following dimensions.

| Factor | Purpose |
|---|---|
| Business / Mission Impact | Measures organizational or personal consequence |
| Executive Relevance | Measures alignment with user responsibilities |
| Urgency | Measures how quickly attention or action is needed |
| Confidence | Measures strength of supporting evidence |
| Timeliness | Measures freshness |
| Strategic Alignment | Measures relationship to defined priorities |
| Source Credibility | Measures trustworthiness of supporting sources |
| Novelty | Rewards meaningful new information |
| Actionability | Measures whether useful action can follow |
| Trend Direction | Measures whether risk or opportunity is changing |
| Calendar Relevance | Measures relationship to imminent schedule |
| Location Relevance | Measures relationship to configured strategic locations |

Actual implementations may use a subset or expansion of these factors.

---

# Scoring Philosophy

Balanced scoring is more reliable than simplistic ranking.

Examples:

- A highly urgent rumor with poor evidence should not automatically outrank a verified high-impact issue.
- A trusted source does not make an irrelevant event important.
- An old issue may remain important if risk is increasing.
- A repeated story should normally decline in prominence unless something materially changes.
- A moderate issue may become highly relevant because of today's calendar.

The model should reward **meaningful context**, not merely dramatic language.

---

# Conceptual Formula

A conceptual base score may be represented as:

```text
Base Priority =
  Impact
+ Relevance
+ Urgency
+ Confidence
+ Timeliness
+ Strategic Alignment
+ Source Credibility
+ Novelty
+ Actionability
```

Contextual modifiers may then apply:

```text
Personalized Priority =
  Base Priority
+ Calendar Relevance
+ Strategic Location Relevance
+ Explicit User Priority
```

Actual implementation may use:

- Weighted values
- Normalization
- Thresholds
- Rules
- Statistical models
- AI-assisted classification

Implementation must remain explainable.

---

# Factor Definitions

## Business / Mission Impact

Measures the potential effect of the issue.

Examples include:

- Financial consequence
- Service disruption
- Regulatory exposure
- Security impact
- Reputation
- Public trust
- Mission delivery
- Strategic opportunity
- Personal consequence

Impact should reflect consequence, not merely topic importance.

---

## Executive Relevance

Measures the relationship between the intelligence and the recipient's responsibilities.

Inputs may include:

- Role
- Areas of responsibility
- Active projects
- Strategic priorities
- Explicit profile settings

The same intelligence may therefore receive different relevance scores for different users.

---

## Urgency

Measures how quickly awareness or action is required.

Potential categories include:

```text
Immediate
Today
This Week
Monitor
Informational
```

Urgency should not be confused with impact.

A high-impact issue may develop slowly.

A low-impact issue may require an immediate minor action.

---

## Confidence

Represents the strength of supporting evidence.

Confidence may consider:

- Number of independent sources
- Source quality
- Corroboration
- Freshness
- Internal consistency
- Validation results

Detailed confidence behavior belongs to:

```text
IMPLEMENTATION/CONFIDENCE_ENGINE.md
```

---

## Timeliness

Measures freshness relative to the subject.

Freshness is domain-dependent.

Examples:

```text
Breaking security alert   Hours
Weather                    Hours
Calendar event             Minutes to days
Project update             Days
Policy                     Months
Historical trend           Years
```

Older information should not automatically receive a low score when historical context remains meaningful.

---

## Strategic Alignment

Measures relationship to defined priorities.

Examples:

- Enterprise initiatives
- Active projects
- Major policy goals
- Retirement milestones
- Travel objectives
- Organizational priorities
- Security programs

Strategic alignment should be configuration-driven.

---

## Source Credibility

Measures the historical and contextual reliability of the source.

Source credibility should contribute to confidence and ranking without becoming a substitute for corroboration.

Source classification is governed by:

```text
ARCHITECTURE/DATA_SOURCE_STRATEGY.md
```

---

## Novelty

Measures whether the intelligence materially adds something new.

Repeated information should gradually decline in priority unless:

- Circumstances materially change.
- Risk increases.
- New evidence appears.
- A deadline approaches.
- User action remains outstanding.
- The issue becomes newly relevant to today's context.

Novelty helps control briefing fatigue.

---

## Actionability

Measures whether the intelligence can support a useful decision or action.

Examples:

```text
High actionability:
A deadline requires a decision today.

Low actionability:
Interesting industry commentary with no foreseeable consequence.
```

Actionability should increase priority when other factors also justify attention.

---

## Trend Direction

Where possible, EIB should evaluate whether the condition is:

```text
Increasing
Stable
Decreasing
```

Trend can materially change priority.

Example:

```text
Moderate risk + rapidly increasing
```

may deserve more attention than:

```text
High risk + steadily decreasing
```

depending on context.

---

## Calendar Relevance

Calendar proximity may materially increase relevance.

Examples:

```text
Meeting with Vendor A today
        +
Material Vendor A development
        ↓
Priority increase
```

```text
Travel tomorrow
        +
Destination disruption
        ↓
Priority increase
```

Calendar relevance should influence ranking without replacing the base score.

---

## Strategic Location Relevance

Configured locations may affect priority.

Examples:

- Weather disruption
- Wildfire
- Utility outage
- Local event
- Travel issue
- Regulatory development
- Property concern

The model must support locations anywhere in the world.

---

# Base Priority Categories

The resulting base score may map into qualitative categories.

| Category | Meaning |
|---|---|
| Critical | Immediate attention required |
| High | Review today |
| Medium | Include when relevant |
| Low | Include if space or context supports it |
| Background | Retain for context or history |

Thresholds should remain configurable.

---

# Critical Intelligence Protection

Certain intelligence should bypass normal personalization suppression.

Potential examples include:

- Severe security incident
- Immediate safety risk
- Major operational disruption
- Critical legal deadline
- Significant regulatory event
- High-confidence urgent risk

Conceptually:

```text
if criticality >= protection_threshold:
    include
```

Personal preference must not hide genuinely critical intelligence.

---

# Briefing Budget

Priority scoring exists partly because the briefing has a limited attention budget.

The standard daily briefing targets approximately:

```text
5–7 minutes
```

Therefore:

> A high-quality scoring model must be willing to leave interesting information out.

Not every worthy item belongs in today's briefing.

Some may be:

- Deferred
- Summarized
- Retained as background
- Available on demand

---

# Diversity Control

A briefing composed solely of the highest numerical scores may become dominated by one domain.

EIB may therefore apply diversity rules to maintain useful coverage.

Example:

```text
10 cyber stories
1 calendar item
1 major financial issue
```

should not automatically produce:

```text
10 cyber stories
```

in the final briefing.

Diversity rules should not suppress genuinely critical intelligence.

---

# Repetition Penalty

Repeated optional content should lose priority over time.

Examples:

- Same news story
- Same recommendation
- Same leadership quote
- Same optional observation

However, repetition penalties should reset or diminish when:

- New evidence appears.
- Risk changes.
- User action remains overdue.
- Context materially changes.

---

# Recommendation Relationship

Scoring should help determine whether an item deserves a recommendation.

Potential conceptual logic:

```text
High Priority
+ Sufficient Confidence
+ Meaningful Actionability
        ↓
Recommendation Candidate
```

Recommendation logic remains owned by the Recommendation Engine.

---

# Explainability

Every important ranked item should be explainable.

EIB should be able to answer:

> Why is this ranked this highly?

Possible explanation:

```text
High Impact
+ High CISO Relevance
+ Immediate Urgency
+ Verified Sources
+ Related meeting today
```

Explainability is a product requirement, not merely a debugging feature.

---

# Personalization Boundary

Base scoring should remain logically separate from user personalization.

Example:

```text
Base Priority: 72
Personal Relevance Adjustment: +12
Final User Priority: 84
```

The exact numeric implementation is illustrative.

The architectural requirement is that personalization adjustments remain distinguishable from the underlying intelligence score.

---

# Confidence Boundary

Priority and confidence are not the same thing.

An item may be:

```text
High Priority / Moderate Confidence
```

or:

```text
Medium Priority / High Confidence
```

The interface should not collapse these into one ambiguous number.

---

# Metrics and Scoring

Metrics should not receive priority merely because they are quantitative.

A metric becomes intelligence when it includes interpretation.

Example:

```text
Critical Vulnerabilities: 24
Change: -12%
Direction: Improving
```

This may rank differently from:

```text
Critical Vulnerabilities: 24
Change: +50%
Direction: Worsening
```

The absolute value alone is insufficient.

---

# Learning and Feedback

Scoring may improve over time through:

- Explicit user feedback
- Accepted recommendations
- Dismissed recommendations
- Manual corrections
- Source performance
- Repeated user requests
- Historical outcomes

Explicit feedback should generally carry more weight than weak behavioral inference.

---

# Guardrails

Learning must not:

- Hide critical information.
- Make scoring impossible to explain.
- Permanently encode accidental behavior.
- Replace explicit user preferences.
- Create uncontrolled user-specific architecture.

Users should be able to override learned preferences.

---

# Configuration

Scoring should increasingly be configuration-driven.

Potential parameters include:

```text
factor_weights
priority_thresholds
criticality_threshold
novelty_decay
repetition_window
calendar_boost
location_boost
domain_caps
diversity_rules
confidence_floor
```

Public repositories should contain reusable schemas and examples.

Private implementations may contain actual user-specific values.

---

# International Design

Scoring must not assume that relevance is U.S.-centric.

Geographic and regulatory relevance may vary by:

- Country
- Region
- Time zone
- Currency
- Local authorities
- Strategic location

Location and jurisdiction should therefore be inputs rather than hard-coded assumptions.

---

# Failure Behavior

If personalization or contextual scoring inputs are unavailable:

```text
Base scoring remains available.
```

EIB should prefer a reliable generic priority score over inventing context.

Example:

```text
Calendar unavailable
→ Do not apply calendar boost.
```

The system should not assume:

```text
No meetings
```

when calendar data was not retrieved.

---

# Implementation Boundary

This document defines scoring architecture and product behavior.

Detailed implementation belongs in:

```text
IMPLEMENTATION/PRIORITY_ENGINE.md
IMPLEMENTATION/CONFIDENCE_ENGINE.md
IMPLEMENTATION/INTELLIGENCE_PIPELINE_SPECIFICATION.md
```

---

# Repository Foundation Impact

During Repository Foundation migration:

- This document moves from `Architecture/` to canonical `ARCHITECTURE/`.
- Existing identifier `PA-007` is preserved pending identifier reconciliation.
- Dependencies are updated to canonical paths.
- Calendar relevance becomes an explicit scoring factor.
- Strategic-location relevance becomes an explicit scoring factor.
- Repetition control is strengthened.
- Briefing-length constraints become part of prioritization.
- Critical-intelligence protection is formalized.
- Priority and confidence are explicitly separated.

---

# Success Criteria

The scoring model succeeds when:

- Important intelligence consistently rises toward the top.
- Low-value repetition declines.
- Calendar and strategic context improve relevance.
- Critical intelligence cannot be hidden by preference.
- Ranking remains explainable.
- Confidence remains distinct from priority.
- The model supports a concise 5–7 minute briefing.
- Users can understand why items were emphasized.
- Scoring can evolve without becoming unstable or opaque.

---

# Related Documents

- ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
- ARCHITECTURE/PERSONALIZATION_MODEL.md
- ARCHITECTURE/REPORT_SPECIFICATION.md
- ARCHITECTURE/DATA_SOURCE_STRATEGY.md
- IMPLEMENTATION/PRIORITY_ENGINE.md
- IMPLEMENTATION/CONFIDENCE_ENGINE.md
- IMPLEMENTATION/RECOMMENDATION_ENGINE.md
- IMPLEMENTATION/INTELLIGENCE_PIPELINE_SPECIFICATION.md

---

# Guiding Principle

> Priority is not a measure of how interesting something is.

> Priority is a measure of how much attention it deserves now.