---
title: ADR-0002 - Knowledge vs. Intelligence
document_id: ADR-0002
version: 1.0
status: Accepted
owner: BSJ
last_updated: 2026-08-06
---

# ADR-0002 — Knowledge vs. Intelligence

## Status

**Accepted**

---

# Purpose

Define the architectural distinction between **Knowledge**, **Reasoning**, **Intelligence**, and **Action** within the Executive Intelligence Briefing (EIB) ecosystem.

This Architecture Decision Record establishes the conceptual information model that guides how information is stored, interpreted, transformed, and acted upon throughout the platform.

---

# Context

Many knowledge management systems accumulate information without distinguishing between facts, analysis, and actionable outputs. As repositories grow, this causes valuable information to become increasingly difficult to retrieve and even harder to use for decision-making.

The Executive Intelligence Briefing (EIB) is intended to do more than store information—it transforms knowledge into actionable intelligence.

To accomplish this consistently, EIB requires a clear separation between:

- Knowledge
- Reasoning
- Intelligence
- Action

Each layer has a distinct purpose and lifecycle.

---

# Decision

EIB adopts the following four-layer information model:

```text
Knowledge
      │
      ▼
Reasoning
      │
      ▼
Intelligence
      │
      ▼
Action
```

Each layer builds upon the previous one while remaining conceptually independent.

---

# Knowledge

Knowledge consists of durable facts, observations, and reference information.

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

Knowledge changes slowly and forms the long-term memory of the system.

---

# Reasoning

Reasoning transforms knowledge into understanding.

It captures:

- Analysis
- Assumptions
- Trade-offs
- Context
- Relationships
- Patterns
- Decision logic

Reasoning answers:

> **Why does this matter?**

Reasoning should be documented whenever significant architectural, operational, or executive conclusions are reached.

---

# Intelligence

Intelligence is generated from knowledge through reasoning.

Intelligence answers:

> **What should I know right now?**

Examples include:

- Executive Intelligence Briefings
- Daily reports
- Weekly summaries
- Health summaries
- Retirement readiness reports
- Travel recommendations
- Cybersecurity summaries
- Meeting preparation briefs
- Risk assessments

Intelligence is time-sensitive and should indicate when it was generated.

---

# Action

Action represents decisions or work performed because of intelligence.

Action answers:

> **What should happen next?**

Examples include:

- Calendar updates
- Task creation
- Executive decisions
- Project prioritization
- Follow-up communications
- Workflow execution

Actions should be traceable back to the intelligence that produced them.

---

# Benefits

Separating these layers provides:

- Clear separation of responsibilities.
- Reusable knowledge.
- Transparent reasoning.
- Actionable intelligence.
- Better executive decision support.
- Improved traceability.
- Support for AI reasoning.
- Future automation opportunities.

---

# Consequences

## Positive

- Information becomes easier to maintain.
- Knowledge can support multiple intelligence products.
- Decision logic becomes transparent.
- Intelligence products become more consistent.
- Future AI agents can reason from a common model.

## Trade-offs

- Contributors must classify information correctly.
- Some documents may span multiple layers.
- Reasoning should be captured whenever practical.

These trade-offs are acceptable because they significantly improve the long-term quality and usefulness of the repository.

---

# Success Criteria

This decision is considered successful when:

- Knowledge remains durable and reusable.
- Reasoning explains important conclusions.
- Intelligence is timely and actionable.
- Actions can be traced to supporting intelligence.
- Contributors understand the progression from information to decision.

---

# Repository Foundation Impact

This ADR establishes the conceptual information architecture used throughout EIB.

It directly influences:

- Knowledge management
- Executive Intelligence Briefings
- AI reasoning workflows
- Prompt engineering
- Domain agent design
- Future intelligence pipelines

---

# Related Documents

- ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
- ARCHITECTURE/ARCHITECTURE.md
- ARCHITECTURE/GOVERNANCE.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md

---

# Guiding Principle

> Knowledge tells us what is true.

> Reasoning explains why it matters.

> Intelligence identifies what deserves attention.

> Action creates value.