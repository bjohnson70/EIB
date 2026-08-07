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
| Architecture/README.md | Unknown | ARCHITECTURE/README.md | Pending Review | Pending Review | Pending |
| Architecture/REPORT_SPECIFICATION.md | Unknown | ARCHITECTURE/REPORT_SPECIFICATION.md | Pending Review | Pending Review | Pending |
| Architecture/SCORING_MODEL.md | Unknown | ARCHITECTURE/SCORING_MODEL.md | Pending Review | Pending Review | Pending |

---

# Known Repository Governance Documents

| Current Path | Document ID | Proposed Canonical Path | Review Status | Migration Action | Verification |
|---|---|---|---|---|---|
| DOCUMENTATION/REPOSITORY_STANDARDS.md | GOV-006 | DOCUMENTATION/REPOSITORY_STANDARDS.md | Verified | Keep | Verified |
| DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md | GOV-007 | DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md | Verified | Keep | Verified |
| DOCUMENTATION/REPOSITORY_INVENTORY.md | GOV-008 | DOCUMENTATION/REPOSITORY_INVENTORY.md | Current | Keep | Pending |
| DOCUMENTATION/DOCUMENT_CATALOG.md | TBD | DOCUMENTATION/DOCUMENT_CATALOG.md | Pending Review | Keep/Update | Pending |
| DOCUMENTATION/REPOSITORY_STATUS.md | TBD | DOCUMENTATION/REPOSITORY_STATUS.md | Pending Review | Keep/Update | Pending |
| DOCUMENTATION/CHANGELOG.md | TBD | DOCUMENTATION/CHANGELOG.md | Pending Review | Keep/Update | Pending |
| DOCUMENTATION/TRACEABILITY_MATRIX.md | TBD | DOCUMENTATION/TRACEABILITY_MATRIX.md | Pending Review | Keep/Update | Pending |
| DOCUMENTATION/DECISION_LOG.md | GOV-001 or TBD | DOCUMENTATION/DECISION_LOG.md | Pending Review | Keep/Update | Pending |

---

# Known Duplicate or Competing Repository Documents

The following files are known to require later review because similar repository-management content may exist in more than one location.

| Current Path | Potential Conflict | Review Status | Action |
|---|---|---|---|
| DOCUMENT_CATALOG.md | DOCUMENTATION/DOCUMENT_CATALOG.md | Pending Review | Compare |
| CHANGELOG.md | DOCUMENTATION/CHANGELOG.md | Pending Review | Compare |
| DECISIONS.md | AI/DECISIONS.md and DOCUMENTATION/DECISION_LOG.md | Pending Review | Compare |
| AI/REPOSITORY_STATUS.md | DOCUMENTATION/REPOSITORY_STATUS.md | Pending Review | Compare |

No duplicate should be removed solely because of its filename. Content must be compared first.

---

# Malformed Filename Incident

A malformed ADR-0001 path previously existed containing an embedded newline character.

The malformed path prevented Windows Git checkout.

Status:

```text
Removed
```

Required follow-up:

- Recreate ADR-0001 under `ARCHITECTURE/`.
- Verify no additional malformed filenames exist.
- Add automated filename validation under `TOOLS/`.

---

# Migration Work Queue

The current migration sequence is:

1. Verify this inventory against GitHub.
2. Recreate ADR-0001 under `ARCHITECTURE/`.
3. Review ADR-0002.
4. Review ADR-0003.
5. Review ADR-0004.
6. Review ADR-0005.
7. Review remaining `Architecture/` documents individually.
8. Migrate approved documents into `ARCHITECTURE/`.
9. Update all affected cross-references.
10. Remove empty `Architecture/` directory.
11. Review duplicate repository-management documents.
12. Refresh Document Catalog.
13. Validate repository filenames.
14. Perform clean Windows clone.
15. Configure Codex against the clean local repository.

---

# Review Procedure

For each document:

1. Read the complete current document.
2. Identify its document ID.
3. Determine whether equivalent content already exists.
4. Compare versions when duplicates exist.
5. Preserve unique information.
6. Select one canonical destination.
7. Update this inventory.
8. Perform the approved migration.
9. Verify GitHub.
10. Update the Document Catalog.

---

# Rules During Migration

Do not:

- Bulk-delete unreviewed documents.
- Assume similarly named files are duplicates.
- Change document IDs solely because a file moves.
- Create backup copies inside the repository.
- Introduce another capitalization variant.
- Claim a migration is verified until the resulting GitHub state has been checked.

---

# Current Checkpoint

Repository Standards:

```text
Complete
```

Repository Migration Plan:

```text
Complete
```

Repository Inventory:

```text
In Progress
```

Architecture Consolidation:

```text
Not Started
```

Windows Clean Clone:

```text
Blocked pending architecture cleanup and filename validation
```

Codex Configuration:

```text
Pending
```

---

# Next Action

After this inventory is committed and verified:

> Recreate `ADR-0001` under the canonical `ARCHITECTURE/` directory and verify it before reviewing ADR-0002.

---

# Guiding Principle

Inventory first.

Compare second.

Move third.

Verify always.