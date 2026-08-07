---
title: ADR-0001 - Public vs. Private Repository Strategy
document_id: ADR-0001
version: 2.0
status: Accepted
owner: BSJ
last_updated: 2026-08-06
---

# ADR-0001 — Public vs. Private Repository Strategy

## Status

**Accepted**

---

# Context

The Executive Intelligence Briefing (EIB) project has two complementary goals:

1. Capture and organize personal knowledge to improve executive decision-making.
2. Share reusable architecture, documentation, templates, prompts, and implementation guidance with the broader community.

These objectives have different security and governance requirements.

A single repository containing both reusable content and personal information would:

- Increase the risk of exposing sensitive information.
- Require continual manual redaction.
- Make open collaboration difficult.
- Reduce long-term maintainability.

---

# Decision

The EIB ecosystem shall consist of **two complementary repositories**.

## Public Repository

The Public Repository contains reusable intellectual property intended for anyone to learn from or adopt.

Examples include:

- Architecture
- Design documents
- Governance
- Templates
- Prompt libraries
- Playbooks
- Sample configurations
- Reference implementations
- Documentation
- AI development guidance

The Public Repository **must never contain personal, confidential, proprietary, or restricted information.**

---

## Private Repository

The Private Repository contains personalized implementations of the public architecture.

Examples include:

- Executive briefings
- Personal knowledge
- Family information
- Retirement planning
- Financial planning
- Health information
- Work products
- Connected data
- Personal AI profiles
- Production configuration

The Private Repository may contain confidential information and shall be appropriately protected.

---

# Relationship

The Public Repository defines the framework.

The Private Repository demonstrates its application.

Whenever improvements are discovered while working in the Private Repository, they should be generalized, stripped of sensitive information, and promoted into the Public Repository.

This creates a continuous improvement cycle.

```text
Private Experience
        │
        ▼
Generalize
        │
        ▼
Remove Sensitive Information
        │
        ▼
Improve Public Repository
        │
        ▼
Future Users Benefit
```

---

# Benefits

This strategy provides:

- Protection of sensitive information.
- A reusable public knowledge base.
- Clear separation of concerns.
- Easier collaboration.
- Cleaner governance.
- Better long-term maintenance.
- A repeatable architecture that others can adopt.

---

# Trade-offs

Maintaining two repositories requires:

- Synchronizing improvements.
- Managing two release cycles.
- Periodically promoting reusable content.

These trade-offs are acceptable because they preserve privacy while maximizing reuse.

---

# Alternatives Considered

## Single Repository

**Rejected**

Reason:

Mixing public and private information creates unnecessary security and maintenance risks.

---

## Branch-Based Separation

**Rejected**

Reason:

Git branches are not a security boundary and increase the risk of accidental publication.

---

## Manual Redaction

**Rejected**

Reason:

Manual redaction is time-consuming, error-prone, and difficult to sustain over the life of the project.

---

# Success Criteria

This decision is considered successful when:

- Personal information remains private.
- Public documentation grows over time.
- Improvements routinely flow from the Private Repository to the Public Repository.
- Contributors clearly understand where information belongs.
- The repository can be cloned and used on Windows, macOS, Linux, Android, and AI tooling without compatibility issues.

---

# Related Documents

- README.md
- DOCUMENTATION/DECISION_LOG.md
- DOCUMENTATION/PRODUCT_DECISIONS.md
- DOCUMENTATION/DOCUMENT_CATALOG.md
- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.

This principle governs both the architecture of EIB and the way knowledge is shared with the community.
