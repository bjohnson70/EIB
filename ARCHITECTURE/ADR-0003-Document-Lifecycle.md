---
title: ADR-0003 - Document Lifecycle
document_id: ADR-0003
version: 1.0
status: Accepted
owner: BSJ
last_updated: 2026-08-06
---

# ADR-0003 — Document Lifecycle

## Status

**Accepted**

---

# Purpose

Define the lifecycle of governed documents within the Executive Intelligence Briefing (EIB) repository to ensure that documentation remains accurate, traceable, and maintainable throughout its existence.

This Architecture Decision Record establishes the states through which governed documents progress, from initial creation through retirement.

---

# Context

As the EIB repository grows, documents will continually evolve. Without a consistent lifecycle, obsolete information may remain in active use, duplicate documents may emerge, and contributors may struggle to determine which version is authoritative.

A documented lifecycle provides clear governance and supports both human contributors and AI-assisted development.

---

# Decision

Every governed document shall progress through a defined lifecycle.

```text
Draft
   │
   ▼
Review
   │
   ▼
Approved
   │
   ▼
Active
   │
   ▼
Revised
   │
   ▼
Deprecated
   │
   ▼
Archived or Removed
```

---

# Lifecycle States

## Draft

The document is under initial development.

Characteristics:

- Content may be incomplete.
- Subject to significant revision.
- Not considered authoritative.

---

## Review

The document has reached sufficient maturity for technical or architectural review.

Characteristics:

- Major concepts are present.
- Feedback is expected.
- Structure should be largely complete.

---

## Approved

The document has been formally accepted.

Characteristics:

- Architecture decision accepted.
- Repository standards satisfied.
- Ready for operational use.

---

## Active

The document represents the current authoritative guidance.

Characteristics:

- Used by contributors.
- Referenced by related documentation.
- Maintained as the source of truth.

---

## Revised

Updates have been made to improve accuracy or reflect evolving architecture.

Characteristics:

- Document identifier remains unchanged.
- Version number increases.
- Revision history is maintained through Git.

---

## Deprecated

The document remains available for historical context but should no longer guide new work.

Characteristics:

- Replacement identified where applicable.
- Existing references should be updated over time.

---

## Archived or Removed

A document reaches this state only after careful review.

Removal is appropriate when:

- The information is obsolete.
- Another authoritative document replaces it.
- Git history provides sufficient historical preservation.

Manual backup copies should not be retained inside the repository.

---

# Lifecycle Principles

The lifecycle is governed by the following principles:

- One authoritative copy.
- Stable document identifiers.
- Git provides revision history.
- Repository standards apply throughout every lifecycle stage.
- Significant architectural changes should be captured through ADRs or governance documents.

---

# Benefits

This lifecycle:

- Improves repository quality.
- Prevents duplicate documentation.
- Supports AI-assisted maintenance.
- Simplifies repository governance.
- Improves long-term maintainability.

---

# Repository Foundation Impact

The Repository Foundation Project uses this lifecycle to guide migration decisions.

Documents migrated during repository cleanup move directly into the **Active** state unless otherwise identified.

Future work should follow the lifecycle from Draft through Active.

---

# Related Documents

- ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
- ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
- DOCUMENTATION/REPOSITORY_INVENTORY.md

---

# Guiding Principle

> Documentation is not finished when it is written.

> It is finished only when it is trusted, maintained, and no longer needed.