---
title: Repository Inventory
document_id: GOV-008
version: 1.0
status: Active
owner: BSJ
last_updated: 2026-08-06
---

# Executive Intelligence Briefing (EIB)

# Repository Inventory

## Purpose

This document is the authoritative working inventory used during the EIB Repository Foundation migration.

It records the current location of governed repository content, the intended canonical location, required migration action, and verification status.

This inventory is a migration-control document and should reflect actual repository state rather than intended architecture.

---

# Governing Documents

Repository migration activities are governed by:

```text
DOCUMENTATION/REPOSITORY_STANDARDS.md
DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
```

---

# Status Values

## Review Status

- Pending Review
- Reviewed
- Duplicate
- Obsolete
- Missing
- Verified

## Migration Action

- Keep
- Move
- Merge
- Replace
- Recreate
- Retire
- Delete Duplicate
- Pending Review

## Verification

- Pending
- Verified
- Failed

---

# Architecture Migration Inventory

The repository currently contains two architecture directory structures:

```text
ARCHITECTURE/
Architecture/
```

The approved canonical directory is:

```text
ARCHITECTURE/
```

No remaining Title Case `Architecture/` document should be deleted until its content has been reviewed and any unique information has been preserved.

---

## Canonical ARCHITECTURE Directory

| Current Path | Document ID | Proposed Canonical Path | Review Status | Migration Action | Verification |
|---|---|---|---|---|---|
| ARCHITECTURE/DESIGN_PHILOSOPHY.md | ARCH-001 | ARCHITECTURE/DESIGN_PHILOSOPHY.md | Pending Review | Keep | Pending |
| ARCHITECTURE/SYSTEM_ARCHITECTURE.md | ARCH-002 | ARCHITECTURE/SYSTEM_ARCHITECTURE.md | Pending Review | Keep | Pending |
| ARCHITECTURE/EDITORIAL_GUIDELINES.md | ARCH-003 | ARCHITECTURE/EDITORIAL_GUIDELINES.md | Pending Review | Keep | Pending |
| ARCHITECTURE/QUALITY_STANDARDS.md | ARCH-004 | ARCHITECTURE/QUALITY_STANDARDS.md | Pending Review | Keep | Pending |
| ARCHITECTURE/PRODUCT_VISION.md | ARCH-005 | ARCHITECTURE/PRODUCT_VISION.md | Pending Review | Keep | Pending |
| ARCHITECTURE/INTELLIGENCE_ENGINE.md | ARCH-006 | ARCHITECTURE/INTELLIGENCE_ENGINE.md | Pending Review | Keep | Pending |

---

## Legacy Architecture Directory

| Current Path | Document ID | Proposed Canonical Path | Review Status | Migration Action | Verification |
|---|---|---|---|---|---|
| Architecture/ADR-0001-Public-vs-Private-Repositories.md | ADR-0001 | ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md | Recreate Required | Recreate | Pending |
| Architecture/ADR-0002-Knowledge-vs-Intelligence.md | ADR-0002 | ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md | Pending Review | Pending Review | Pending |
| Architecture/ADR-0003-Document-Lifecycle.md | ADR-0003 | ARCHITECTURE/ADR-0003-Document-Lifecycle.md | Pending Review | Pending Review | Pending |
| Architecture/ADR-0004-Definition-of-Done.md | ADR-0004 | ARCHITECTURE/ADR-0004-Definition-of-Done.md | Pending Review | Pending Review | Pending |
| Architecture/ADR-0005-Versioning-Strategy.md | ADR-0005 | ARCHITECTURE/ADR-0005-Versioning-Strategy.md | Pending Review | Pending Review | Pending |
| Architecture/ARCHITECTURE.md | Unknown | ARCHITECTURE/ARCHITECTURE.md or merge target | Pending Review | Pending Review | Pending |
| Architecture/DATA_SOURCE_STRATEGY.md | Unknown | ARCHITECTURE/DATA_SOURCE_STRATEGY.md | Pending Review | Pending Review | Pending |
| Architecture/GOVERNANCE.md | Unknown | ARCHITECTURE/GOVERNANCE.md | Pending Review | Pending Review | Pending |
| Architecture/INTELLIGENCE_ARCHITECTURE.md | Unknown | ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md or merge target | Pending Review | Pending Review | Pending |
| Architecture/PERSONALIZATION_MODEL.md | Unknown | ARCHITECTURE/PERSONALIZATION_MODEL.md | Pending Review | Pending Review | Pending |
| Architecture/PRODUCT_ARCHITECTURE.md | Unknown | ARCHITECTURE/PRODUCT_ARCHITECTURE.md | Pending Review | Pending Review | Pending |
| Architecture/README.md