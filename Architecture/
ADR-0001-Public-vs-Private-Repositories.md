---
Title: ADR-0001 – Public vs. Private Repository Strategy
Status: Accepted
Version: Foundation (v0.1)
Date: 2026-07-21
Author: EIB Project
Repository: Public Candidate
---

# ADR-0001 – Public vs. Private Repository Strategy

## Status

Accepted

---

# Context

The Executive Intelligence Briefing (EIB) is intended to serve two complementary purposes:

1. Capture and organize personal knowledge.
2. Create reusable guidance that can benefit others.

These goals create an architectural challenge. Personal knowledge often contains confidential information, while reusable guidance should be openly shareable.

A single repository would either expose personal information or require continual redaction, making long-term maintenance difficult.

---

# Decision

The EIB will be maintained as two complementary repositories.

## Public Repository

Purpose:

Provide reusable knowledge that anyone can adopt.

Contents include:

- Documentation
- Templates
- Prompt Library
- Playbooks
- Setup Guides
- Examples
- Sample Data
- Architecture Decision Records

The Public Repository shall never contain personal or confidential information.

---

## Private Repository

Purpose:

Capture personal knowledge and individualized implementations.

Examples include:

- Health
- Retirement
- Financial Planning
- Family
- Work
- Executive Briefings
- Projects
- Reports

The Private Repository may contain confidential or sensitive information.

---

# Relationship

The Public Repository defines reusable structure.

The Private Repository provides personalized implementation.

Whenever a reusable improvement is discovered while working in the Private Repository, it should be evaluated for promotion into the Public Repository.

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.

This principle governs all architectural decisions.

---

# Consequences

Benefits include:

- Protection of personal information.
- Reusable templates for others.
- Simplified maintenance.
- Clear separation of responsibilities.
- Easier collaboration.
- Long-term sustainability.

Tradeoffs include:

- Two repositories must be maintained.
- Reusable improvements require deliberate promotion from Private to Public.

These tradeoffs are acceptable because they reinforce the project's mission while preserving privacy.

---

# Alternatives Considered

## Single Repository

Rejected.

Reason:
Mixes reusable content with personal information and creates unnecessary maintenance.

---

## Branch-Based Separation

Rejected.

Reason:
Introduces unnecessary complexity and increases the risk of accidentally publishing personal information.

---

# Success Criteria

This decision is successful when:

- Personal information remains protected.
- Public knowledge continues to grow.
- Templates become increasingly reusable.
- Improvements discovered privately regularly strengthen the Public Repository.

---

# Related Documents

- MANIFESTO.md
- ARCHITECTURE.md
- README.md
- ROADMAP.md

---

*"Every solution should leave behind a better starting point for the next person."*