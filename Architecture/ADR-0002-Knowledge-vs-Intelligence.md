---
Title: ADR-0002 – Knowledge vs. Intelligence
Status: Accepted
Version: Foundation (v0.1)
Date: 2026-07-21
Author: EIB Project
---

# ADR-0002 – Knowledge vs. Intelligence

## Status

Accepted

---

# Context

Many knowledge management systems store information without distinguishing between facts, analysis, and actionable outputs. As a result, notes become difficult to use for decision-making and often require repeated interpretation.

The Executive Intelligence Briefing (EIB) is intended to do more than store information—it is designed to transform knowledge into actionable intelligence.

To achieve this, the project requires a clear distinction between **Knowledge** and **Intelligence**, with **Reasoning** providing the bridge between them.

---

# Decision

EIB adopts a four-layer information model:

```text
Knowledge
      ↓
Reasoning
      ↓
Intelligence
      ↓
Action
```

---

## Knowledge

Knowledge consists of long-lived facts and reference information.

Knowledge answers:

> **What do we know?**

Examples include:

- Personal profiles
- Family information
- Health history
- Retirement plans
- Financial information
- Work responsibilities
- Policies
- Procedures
- Lessons learned
- Personal operating principles

Knowledge changes slowly and serves as the foundation for future analysis.

---

## Reasoning

Reasoning connects knowledge to intelligence.

It captures:

- Analysis
- Assumptions
- Trade-offs
- Context
- Patterns
- Relationships
- Decision logic

Reasoning answers:

> **Why does this matter?**

Reasoning should be documented whenever significant conclusions or architectural decisions are made.

---

## Intelligence

Intelligence is generated from knowledge through reasoning.

Intelligence answers:

> **What should I know right now?**

Examples include:

- Executive Intelligence Briefings
- Daily reports
- Weekly summaries
- Health summaries
- Retirement readiness reports
- Meeting preparation briefs
- Risk assessments
- Travel recommendations

Intelligence is time-sensitive and should indicate when it was generated.

---

## Action

Action represents decisions or work performed as a result of intelligence.

Action answers:

> **What should happen next?**

Examples include:

- Calendar updates
- Task lists
- Project priorities
- Executive decisions
- Follow-up activities
- Communications

---

# Benefits

Separating these layers provides several advantages:

- Prevents facts from being confused with conclusions.
- Makes reasoning transparent.
- Allows multiple intelligence products to be generated from the same knowledge.
- Improves traceability.
- Encourages better decision-making.
- Supports future automation.

---

# Consequences

Positive:

- Clear separation of concerns.
- Reusable knowledge.
- Better executive reporting.
- Easier maintenance.
- Stronger auditability.

Trade-offs:

- Requires discipline when classifying information.
- Some documents may span multiple layers.
- Reasoning should be documented whenever practical.

These trade-offs are acceptable because they improve the quality and long-term usefulness of the system.

---

# Success Criteria

This decision is successful when:

- Knowledge remains accurate and reusable.
- Intelligence is timely and actionable.
- Reasoning explains how conclusions were reached.
- Actions can be traced back to supporting intelligence.
- Future maintainers understand the flow from information to decision.

---

# Related Documents

- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md
- ADR-0001 – Public vs. Private Repository Strategy

---

## Guiding Principle

> Every solution should leave behind a better starting point for the next person.