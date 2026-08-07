---
title: Repository Inventory
document_id: GOV-008
version: 1.1
status: Active
owner: BSJ
last_updated: 2026-08-07
---

# Executive Intelligence Briefing (EIB)

# Repository Inventory

## Purpose

This document is the authoritative working inventory used during the EIB Repository Foundation migration.

It records current repository state, canonical locations, migration actions, and verification status.

This inventory must reflect actual repository state rather than intended architecture.

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

```text
Pending Review
Reviewed
Duplicate
Obsolete
Missing
Verified
```

## Migration Action

```text
Keep
Move
Merge
Replace
Recreate
Retire
Delete Duplicate
Pending Review
```

## Verification

```text
Pending
Verified
Failed
```

---

# Architecture Migration Summary

The repository historically contained two architecture directory structures:

```text
ARCHITECTURE/
Architecture/
```

The approved canonical directory is:

```text
ARCHITECTURE/
```

All known documents in the legacy `Architecture/` directory have now been reviewed and migrated or replaced with canonical versions under `ARCHITECTURE/`.

The remaining legacy copies may now be removed after confirming their canonical replacements exist.

---

# Canonical Architecture Foundation

| Canonical Path | Document ID | Status | Verification |
|---|---|---|---|
| ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md | ADR-0001 | Migrated | Verified |
| ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md | ADR-0002 | Migrated | Verified |
| ARCHITECTURE/ADR-0003-Document-Lifecycle.md | ADR-0003 | Migrated | Verified |
| ARCHITECTURE/ADR-0004-Definition-of-Done.md | ADR-0004 | Migrated | Verified |
| ARCHITECTURE/ADR-0005-Versioning-Strategy.md | ADR-0005 | Migrated | Verified |
| ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md | ARCH-007 | Migrated | Pending Final Verification |
| ARCHITECTURE/GOVERNANCE.md | GOV-002 | Migrated | Pending Final Verification |
| ARCHITECTURE/DATA_SOURCE_STRATEGY.md | PA-006 | Migrated | Pending Final Verification |
| ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md | PA-005 | Migrated | Pending Final Verification |
| ARCHITECTURE/PERSONALIZATION_MODEL.md | PA-008 | Migrated | Pending Final Verification |
| ARCHITECTURE/PRODUCT_ARCHITECTURE.md | PA-003 | Migrated | Pending Final Verification |
| ARCHITECTURE/REPORT_SPECIFICATION.md | PA-004 | Migrated | Pending Final Verification |
| ARCHITECTURE/SCORING_MODEL.md | PA-007 | Migrated | Pending Final Verification |
| ARCHITECTURE/README.md | ARCH-008 | Migrated | Pending Final Verification |

---

# Existing Canonical Architecture Documents

These documents already existed under the approved canonical directory before the legacy-directory migration.

| Path | Document ID | Review Status | Migration Action | Verification |
|---|---|---|---|---|
| ARCHITECTURE/DESIGN_PHILOSOPHY.md | ARCH-001 | Pending Review | Keep | Pending |
| ARCHITECTURE/SYSTEM_ARCHITECTURE.md | ARCH-002 | Pending Review | Keep | Pending |
| ARCHITECTURE/EDITORIAL_GUIDELINES.md | ARCH-003 | Pending Review | Keep | Pending |
| ARCHITECTURE/QUALITY_STANDARDS.md | ARCH-004 | Pending Review | Keep | Pending |
| ARCHITECTURE/PRODUCT_VISION.md | ARCH-005 | Pending Review | Keep | Pending |
| ARCHITECTURE/INTELLIGENCE_ENGINE.md | ARCH-006 | Pending Review | Keep | Pending |

These documents still require content review after the legacy `Architecture/` directory has been retired.

---

# Legacy Architecture Directory

All known legacy documents have been reviewed.

| Legacy Path | Canonical Replacement | Review Status | Action |
|---|---|---|---|
| Architecture/ADR-0001-Public-vs-Private-Repositories.md | ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md | Verified | Delete Legacy Copy |
| Architecture/ADR-0002-Knowledge-vs-Intelligence.md | ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md | Verified | Delete Legacy Copy |
| Architecture/ADR-0003-Document-Lifecycle.md | ARCHITECTURE/ADR-0003-Document-Lifecycle.md | Verified | Delete Legacy Copy |
| Architecture/ADR-0004-Definition-of-Done.md | ARCHITECTURE/ADR-0004-Definition-of-Done.md | Verified | Delete Legacy Copy |
| Architecture/ADR-0005-Versioning-Strategy.md | ARCHITECTURE/ADR-0005-Versioning-Strategy.md | Verified | Delete Legacy Copy |
| Architecture/ARCHITECTURE.md | ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md | Reviewed | Delete Legacy Copy |
| Architecture/DATA_SOURCE_STRATEGY.md | ARCHITECTURE/DATA_SOURCE_STRATEGY.md | Reviewed | Delete Legacy Copy |
| Architecture/GOVERNANCE.md | ARCHITECTURE/GOVERNANCE.md | Reviewed | Delete Legacy Copy |
| Architecture/INTELLIGENCE_ARCHITECTURE.md | ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md | Reviewed | Delete Legacy Copy |
| Architecture/PERSONALIZATION_MODEL.md | ARCHITECTURE/PERSONALIZATION_MODEL.md | Reviewed | Delete Legacy Copy |
| Architecture/PRODUCT_ARCHITECTURE.md | ARCHITECTURE/PRODUCT_ARCHITECTURE.md | Reviewed | Delete Legacy Copy |
| Architecture/README.md | ARCHITECTURE/README.md | Reviewed | Delete Legacy Copy |
| Architecture/REPORT_SPECIFICATION.md | ARCHITECTURE/REPORT_SPECIFICATION.md | Reviewed | Delete Legacy Copy |
| Architecture/SCORING_MODEL.md | ARCHITECTURE/SCORING_MODEL.md | Reviewed | Delete Legacy Copy |

After these files are removed, Git should automatically cease tracking the empty `Architecture/` directory.

---

# Known Repository Governance Documents

| Current Path | Document ID | Review Status | Migration Action | Verification |
|---|---|---|---|---|
| DOCUMENTATION/REPOSITORY_STANDARDS.md | GOV-006 | Verified | Keep | Verified |
| DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md | GOV-007 | Verified | Keep | Verified |
| DOCUMENTATION/REPOSITORY_INVENTORY.md | GOV-008 | Active | Keep / Update | Active |
| DOCUMENTATION/DOCUMENT_CATALOG.md | TBD | Pending Review | Keep / Update | Pending |
| DOCUMENTATION/REPOSITORY_STATUS.md | TBD | Pending Review | Keep / Update | Pending |
| DOCUMENTATION/CHANGELOG.md | TBD | Pending Review | Keep / Update | Pending |
| DOCUMENTATION/TRACEABILITY_MATRIX.md | TBD | Pending Review | Keep / Update | Pending |
| DOCUMENTATION/DECISION_LOG.md | TBD | Pending Review | Keep / Update | Pending |

---

# Known Duplicate or Competing Repository Documents

The following files require later content comparison.

| Current Path | Potential Conflict | Review Status | Action |
|---|---|---|---|
| DOCUMENT_CATALOG.md | DOCUMENTATION/DOCUMENT_CATALOG.md | Pending Review | Compare |
| CHANGELOG.md | DOCUMENTATION/CHANGELOG.md | Pending Review | Compare |
| DECISIONS.md | AI/DECISIONS.md and DOCUMENTATION/DECISION_LOG.md | Pending Review | Compare |
| AI/REPOSITORY_STATUS.md | DOCUMENTATION/REPOSITORY_STATUS.md | Pending Review | Compare |

No duplicate should be removed solely because of its filename.

Content must be compared first.

---

# Malformed Filename Incident

A malformed ADR-0001 path previously existed containing an embedded newline character.

The malformed path prevented Windows Git checkout.

Status:

```text
Removed
```

ADR-0001 has subsequently been recreated at:

```text
ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
```

Remaining follow-up:

```text
Verify no additional malformed filenames exist.
Add automated filename validation under TOOLS/.
Perform clean Windows clone.
```

---

# Architecture Migration Decisions

The migration established several canonical architecture decisions.

The master architecture document previously located at:

```text
Architecture/ARCHITECTURE.md
```

was migrated to:

```text
ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md
```

with canonical document identifier:

```text
ARCH-007
```

The Architecture Overview is located at:

```text
ARCHITECTURE/README.md
```

with document identifier:

```text
ARCH-008
```

Existing `PA-*` identifiers were preserved during migration pending a broader identifier review through the Document Catalog.

---

# Migration Work Queue

Current sequence:

```text
1. Repository Standards                              COMPLETE
2. Repository Migration Plan                         COMPLETE
3. Initial Repository Inventory                      COMPLETE
4. Recreate ADR-0001                                COMPLETE
5. Migrate ADR-0002 through ADR-0005                COMPLETE
6. Review legacy Architecture documents              COMPLETE
7. Create canonical ARCHITECTURE replacements        COMPLETE
8. Update Repository Inventory                       CURRENT
9. Remove legacy Architecture files                  NEXT
10. Verify Architecture directory is retired
11. Review existing ARCHITECTURE documents ARCH-001 through ARCH-006
12. Review duplicate repository-management documents
13. Refresh Document Catalog
14. Validate repository filenames
15. Validate internal references
16. Perform clean Windows clone
17. Verify VS Code repository
18. Configure Codex
19. Perform first Codex-assisted repository change
```

---

# Review Procedure

For each remaining document:

```text
Read
Compare
Preserve
Standardize
Migrate
Verify
Catalog
```

No destructive change should occur before a valid replacement has been established.

---

# Rules During Migration

Do not:

```text
Bulk-delete unreviewed documents.
Assume similarly named documents are duplicates.
Create manual backup copies inside the repository.
Introduce alternate capitalization.
Reuse document identifiers for unrelated documents.
Claim verification without inspecting actual repository state.
```

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
Updated through legacy architecture migration
```

ADR Migration:

```text
Complete
```

Legacy Architecture Content Review:

```text
Complete
```

Legacy Architecture Deletion:

```text
Ready
```

Canonical Architecture Review:

```text
ARCH-001 through ARCH-006 still pending
```

Document Catalog Refresh:

```text
Pending
```

Filename Validation:

```text
Pending
```

Windows Clean Clone:

```text
Pending legacy-directory removal
```

Codex Configuration:

```text
Pending successful clean clone
```

---

# Next Action

The immediate next action is:

> Delete the reviewed legacy files under `Architecture/`, leaving `ARCHITECTURE/` as the only architecture directory.

After deletion:

1. Verify the `Architecture/` directory no longer exists.
2. Verify all canonical replacements remain accessible.
3. Attempt a clean Windows clone before continuing broader repository cleanup.

---

# Guiding Principle

> Inventory first. Compare second. Move third. Verify always.

The Repository Foundation effort succeeds when repository structure can be trusted without needing historical chat context to understand where authoritative information belongs.