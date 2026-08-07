---
title: Repository Migration Plan
document_id: GOV-007
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-08-06
---

# Executive Intelligence Briefing (EIB)

# Repository Migration Plan

## Purpose

This document defines the controlled process for reorganizing the EIB repository into its approved canonical structure.

The migration is intended to eliminate inconsistent paths, duplicate directories, malformed filenames, obsolete locations, and undocumented structural drift without losing valid project content.

---

# Objectives

The migration will:

- Consolidate duplicate directory structures.
- Standardize top-level directory capitalization.
- Preserve valid documents and document identifiers.
- Remove malformed or obsolete files.
- Update internal references.
- Refresh the document catalog.
- Confirm cross-platform Git compatibility.
- Prepare the repository for Codex-assisted development.

---

# Governing Standard

All migration activities must follow:

```text
DOCUMENTATION/REPOSITORY_STANDARDS.md
```

If this migration plan conflicts with the Repository Standards, the Repository Standards take precedence.

---

# Canonical Top-Level Structure

The target repository structure is:

```text
AI/
ARCHITECTURE/
CONFIG/
CONNECTORS/
DATA/
DEVELOPMENT/
DOCUMENTATION/
IMPLEMENTATION/
MODELS/
OPERATIONS/
PERSONALITY/
PROFILES/
PROMPTS/
ROADMAP/
TESTS/
TOOLS/
WORKFLOWS/
```

Repository-wide documents may remain at the root when appropriate.

Examples:

```text
README.md
LICENSE.md
MANIFESTO.md
CONSTITUTION.md
ROADMAP.md
```

---

# Migration Principles

## Preserve Before Removing

A file must not be deleted until its content has been evaluated.

Where duplicate files exist:

1. Compare content.
2. Identify the authoritative version.
3. Preserve unique valid information.
4. Establish one canonical copy.
5. Remove the duplicate only after verification.

---

## One Logical Change Per Commit

Migration changes should be divided into focused commits.

Examples:

```text
refactor(repo): consolidate architecture directories
docs(catalog): update architecture document paths
fix(repo): remove malformed repository path
```

Do not combine unrelated cleanup activities into a single large commit when they can reasonably be separated.

---

## Preserve Document IDs

Moving or renaming a document must not change its established document identifier unless an explicit governance decision requires it.

Example:

```text
Architecture/ADR-0002-Knowledge-vs-Intelligence.md
```

may become:

```text
ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
```

while remaining:

```text
ADR-0002
```

---

# Migration Sequence

## Phase 1 — Standards

Status: Complete

Required document:

```text
DOCUMENTATION/REPOSITORY_STANDARDS.md
```

---

## Phase 2 — Inventory

Create a complete inventory of current repository content.

Required document:

```text
DOCUMENTATION/REPOSITORY_INVENTORY.md
```

The inventory should identify:

- Current path
- Document identifier
- Document title
- Proposed canonical path
- Duplicate status
- Migration action
- Verification status

No major structural moves should occur until the relevant files appear in the inventory.

---

## Phase 3 — Architecture Consolidation

The repository currently contains both:

```text
ARCHITECTURE/
```

and:

```text
Architecture/
```

The approved canonical directory is:

```text
ARCHITECTURE/
```

Each document in `Architecture/` must be individually evaluated before migration.

Potential actions:

- Move
- Merge
- Replace
- Retire
- Delete duplicate
- Retain temporarily pending review

The `Architecture/` directory should be removed only after every valid document has been migrated or formally retired.

---

## Phase 4 — Root Document Review

Review repository-root documents for proper placement.

Possible outcomes:

- Remain at root
- Move to DOCUMENTATION
- Move to ARCHITECTURE
- Move to ROADMAP
- Retire as duplicate

Repository-root content should remain minimal and intentional.

---

## Phase 5 — Remaining Directory Review

Review all other top-level directories for:

- Naming consistency
- Duplicate content
- Obsolete structures
- Missing metadata
- Incorrect cross-references

Directories should be addressed one at a time.

---

# Cross-Reference Updates

Whenever a file is moved or renamed, references must be searched and updated.

Examples include:

- Markdown links
- Related Documents sections
- Catalog entries
- Architecture references
- Prompt dependencies
- Workflow dependencies
- Configuration references
- AI instruction documents

Path updates should occur in the same logical migration as the file move whenever practical.

---

# Document Catalog

The authoritative catalog must ultimately reflect the actual repository.

During migration, catalog entries may temporarily indicate:

```text
Migration Pending
```

or:

```text
Deprecated
```

Once migration is complete, every governed document should have one valid canonical catalog entry.

---

# Verification Requirements

Each migration step should be verified before proceeding.

Verification should include, where applicable:

- Destination file exists.
- Source file is removed when appropriate.
- Document content is complete.
- Document ID remains correct.
- Internal links are updated.
- Catalog entry is updated.
- No unintended files changed.
- Git status is understood.
- Commit is successfully pushed.

---

# Cross-Platform Validation

Before the Repository Foundation milestone is considered complete, the repository must successfully clone and check out on:

- Windows
- Linux
- macOS or equivalent compatibility validation
- Android GitSync

The repository should also open cleanly in:

- Visual Studio Code
- Codex

---

# AI-Assisted Migration

Once Codex is configured, it may assist with repository migration.

Codex should be instructed to:

1. Read `DOCUMENTATION/REPOSITORY_STANDARDS.md`.
2. Read this Migration Plan.
3. Inspect current repository state.
4. Make only approved migration changes.
5. Preserve document identifiers.
6. Update internal references.
7. Update catalog and inventory.
8. Show proposed changes before destructive operations when risk exists.
9. Run available validation checks.
10. Produce focused commit messages.

Human approval remains required for significant structural or destructive changes until the migration is complete.

---

# Rollback

Git history is the authoritative rollback mechanism.

Do not create manual backup copies such as:

```text
OLD/
BACKUP/
FINAL2/
```

If a migration causes an issue:

1. Stop further changes.
2. Identify the affected commit.
3. Revert or correct the commit.
4. Revalidate repository state.
5. Document any important lesson in the Decision Log.

---

# Migration Completion Criteria

The migration is complete when:

- Only approved canonical top-level directories remain.
- `Architecture/` no longer exists.
- `ARCHITECTURE/` contains all approved architecture content.
- No malformed filenames remain.
- Duplicate documents are resolved.
- Root directory is intentionally organized.
- Document Catalog matches repository reality.
- Cross-references are valid.
- Repository clones successfully on Windows.
- GitSync compatibility is confirmed.
- Codex can operate on the repository.
- Repository validation can be repeated reliably.

---

# Current Priority

The immediate next task after approval of this plan is:

> Build `DOCUMENTATION/REPOSITORY_INVENTORY.md` and inventory the contents of both `ARCHITECTURE/` and `Architecture/` before moving or deleting additional files.

---

# Guiding Rule

Move deliberately.

Verify before deleting.

Preserve valid information.

Leave one authoritative source.

The objective is not simply to make the repository cleaner.

The objective is to make the repository trustworthy.