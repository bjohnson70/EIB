---
title: ADR-0004 - Definition of Done
document_id: ADR-0004
version: 1.0
status: Accepted
owner: BSJ
last_updated: 2026-08-06
---

# ADR-0004 — Definition of Done

## Status

**Accepted**

---

# Purpose

Establish a consistent definition of "Done" for work performed within the Executive Intelligence Briefing (EIB) project.

This Architecture Decision Record defines the minimum quality criteria that must be satisfied before work is considered complete.

---

# Context

Simply completing a document or writing code does not ensure that work is usable, maintainable, or trustworthy.

Without a shared definition of completion:

- Incomplete work may be mistaken for finished work.
- Repository quality degrades over time.
- Cross-references become inaccurate.
- Documentation becomes inconsistent.
- AI-generated content becomes difficult to maintain.

A consistent Definition of Done ensures that repository quality continually improves.

---

# Decision

A task is considered **Done** only when all applicable quality requirements have been satisfied.

Completion is measured by quality—not merely by creation.

---

# Definition of Done

Unless specifically exempted, a completed repository change should satisfy the following checklist.

## Repository

- File exists in the approved canonical location.
- Repository naming standards are followed.
- Directory structure complies with Repository Standards.
- No duplicate files are introduced.

---

## Document

- YAML metadata is complete.
- Document identifier is assigned.
- Version information is updated.
- Status is appropriate.
- Formatting is consistent.

---

## Content

- Purpose is clearly stated.
- Context is documented.
- Decision is explicit.
- Benefits and consequences are identified.
- Related documents are referenced.
- Guiding principle is included where appropriate.

---

## Cross-References

- Internal links are valid.
- Related document references are current.
- No broken references remain.

---

## Governance

- Repository Standards followed.
- Migration Plan followed (when applicable).
- Inventory updated (when applicable).
- Document Catalog updated (when applicable).

---

## Verification

Where applicable:

- GitHub commit verified.
- Repository status reviewed.
- No unintended file changes.
- Repository remains portable across supported platforms.

---

# Benefits

Using a shared Definition of Done:

- Improves consistency.
- Reduces technical debt.
- Supports AI-assisted development.
- Simplifies reviews.
- Produces higher quality documentation.
- Makes repository evolution predictable.

---

# Repository Foundation Impact

During the Repository Foundation Project, each migrated document must satisfy this Definition of Done before migration is considered complete.

Future contributors should apply this checklist before marking any repository task as finished.

---

# Related Documents

- ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
- ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
- ARCHITECTURE/ADR-0003-Document-Lifecycle.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
- DOCUMENTATION/REPOSITORY_INVENTORY.md

---

# Guiding Principle

> Work is not complete when it is written.

> Work is complete when it is trusted, verified, and ready for the next contributor.