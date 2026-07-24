---
title: Executive Confidence Engine
component_id: ENGINE-004
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# Executive Confidence Engine

## Purpose

The Executive Confidence Engine evaluates the reliability of every piece of intelligence produced by EIB.

Confidence represents how certain EIB is that its information, correlations, and recommendations are accurate and complete.

Unlike priority, which measures importance, confidence measures certainty.

Both are essential for sound executive decision-making.

---

# Guiding Principle

High priority does not always mean high confidence.

Likewise, high confidence does not always indicate high priority.

Executives should understand both.

Example:

Critical Security Alert

Priority: 98

Confidence: 62%

Meaning:

This issue appears extremely important, but additional verification is recommended.

---

# Objectives

The Confidence Engine should:

- Measure reliability
- Increase transparency
- Prevent overconfidence
- Explain uncertainty
- Build long-term trust

---

# Confidence Pipeline

```
Collect Evidence
        ↓
Evaluate Sources
        ↓
Measure Agreement
        ↓
Assess Freshness
        ↓
Calculate Confidence
        ↓
Generate Explanation
```

---

# Confidence Factors

## Source Reliability

How trustworthy is the originating source?

Example weights:

| Source Type | Score |
|------------|------:|
| Official System | 100 |
| Verified API | 95 |
| Enterprise Application | 90 |
| Internal Document | 80 |
| Public News | 70 |
| Social Media | 40 |
| Unknown Source | 20 |

---

## Multiple Source Agreement

Independent confirmation increases confidence.

Examples:

- Email and Calendar agree.
- GitHub and Change Management agree.
- Security platform and vulnerability scanner agree.

More corroboration generally results in higher confidence.

---

## Data Freshness

Newer information is generally more reliable.

Suggested guidance:

| Age | Score |
|-----|------:|
| <1 hour | 100 |
| Same day | 95 |
| 1–3 days | 85 |
| 1 week | 70 |
| Older | 50 |

Organizations may configure freshness thresholds.

---

## Completeness

Confidence decreases when important context is missing.

Examples:

- Missing meeting agenda.
- Partial email thread