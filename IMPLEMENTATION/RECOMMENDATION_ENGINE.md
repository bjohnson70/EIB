---
title: Executive Recommendation Engine
component_id: ENGINE-003
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# Executive Recommendation Engine

## Purpose

The Executive Recommendation Engine transforms prioritized intelligence into practical, actionable guidance.

Rather than merely identifying what is happening, the engine answers the executive's most important question:

> **"What should I do next?"**

Recommendations are advisory, transparent, and proportionate to the situation. They assist decision-making without replacing human judgment.

---

# Guiding Principles

Recommendations should always be:

- Actionable
- Explainable
- Timely
- Proportionate
- User-aware
- Evidence-based

The engine should never recommend action without sufficient supporting intelligence.

---

# Recommendation Pipeline

```
Prioritized Intelligence
          ↓
Determine Intent
          ↓
Evaluate Context
          ↓
Generate Candidate Actions
          ↓
Rank Recommendations
          ↓
Explain Reasoning
          ↓
Deliver to Briefing Composer
```

---

# Recommendation Categories

## Immediate Action

Requires prompt attention.

Examples:

- Approve a critical request.
- Respond to an executive email.
- Review a security incident.
- Join an active bridge call.

---

## Preparation

Improve readiness before an upcoming event.

Examples:

- Review briefing material.
- Read attached documentation.
- Contact meeting participants.
- Verify presentation materials.

---

## Decision

Executive judgment is required.

Examples:

- Approve funding.
- Accept project risk.
- Select implementation option.
- Escalate issue.

---

## Monitoring

No action required today.

Continue observation.

Examples:

- Vendor outage.
- Developing weather event.
- Regulatory proposal.
- Market trend.

---

## Follow-Up

Previously identified work requiring closure.

Examples:

- Outstanding action item.
- Awaiting approval.
- Unanswered request.
- Aging task.

---

# Recommendation Priority

Each recommendation receives its own score.

Factors include:

- Executive Priority Score
- Correlation Strength
- Risk Level
- Time Sensitivity
- Organizational Impact
- User Context
- Confidence

Recommendations should inherit—but not blindly mirror—the priority of the underlying intelligence.

---

# Recommendation Format

Every recommendation should answer five questions.

## 1. What?

What action is recommended?

---

## 2. Why?

Why is this recommendation being made?

---

## 3. When?

When should action occur?

Examples:

- Now
- Today
- Before today's meeting
- This week
- Monitor only

---

## 4. Impact

What happens if action is delayed?

Possible impacts:

- Missed deadline
- Increased operational risk
- Customer impact
- Regulatory exposure
- No significant impact

---

## 5. Confidence

How confident is EIB?

Example:

```
Recommendation Confidence

High (92%)

Reason:

Multiple independent sources support this recommendation.
```

---

# Recommendation Types

Examples include:

- Review
- Approve
- Escalate
- Delegate
- Schedule
- Respond
- Monitor
- Investigate
- Prepare
- Communicate
- No Action Required

"No Action Required" is a valid recommendation when supported by evidence.

---

# Recommendation Limits

Avoid overwhelming the executive.

Suggested defaults:

- Critical: Unlimited
- High: Top 5
- Medium: Top 10
- Low: Available in expanded view

Focus on quality over quantity.

---

# Explainability

Every recommendation should retain:

- Supporting sources
- Correlated events
- Priority score
- Confidence score
- Triggering conditions
- Reasoning summary

Users should always understand why a recommendation exists.

---

# Feedback Loop

Future versions may capture user responses.

Possible outcomes:

- Accepted
- Ignored
- Deferred
- Dismissed
- Completed

These signals should improve future recommendation quality while remaining transparent and user-controlled.

---

# Configuration

Organizations should be able to configure:

- Recommendation thresholds
- Maximum recommendations
- Category preferences
- Escalation rules
- Organizational policies

Behavior should be driven by configuration rather than code.

---

# Future Enhancements

Potential capabilities include:

- Predictive recommendations.
- Calendar-aware preparation.
- Organizational workload balancing.
- Team-level recommendations.
- Cross-project optimization.
- AI-generated alternative actions.

Recommendations should always remain explainable and user-controlled.

---

# Success Criteria

The Recommendation Engine succeeds when users consistently say:

- "That saved me time."
- "I was going to do that anyway."
- "I'm glad it reminded me."
- "That helped me avoid a problem."
- "Those