---
title: Repository Standards
document_id: GOV-006
version: 1.0
lifecycle_status: Approved
owner: BSJ
last_updated: 2026-09-13
---

# Executive Intelligence Briefing (EIB)

# Repository Standards

## Purpose

This document defines the authoritative repository standards for the Executive Intelligence Briefing (EIB).

Its purpose is to ensure that repository content remains:

- Consistent
- Portable
- Maintainable
- Version controlled
- AI readable
- Human readable
- Compatible across supported platforms

These standards apply to all future repository changes unless superseded by an approved architectural decision.

---

# Guiding Principle

The repository is the authoritative source of truth for the EIB project.

Reusable repository organization, repository hygiene, reference stability, and workflow execution are governed by the pinned COG Repository Standard and GitHub Development Workflow identified in the [COG Adoption Profile](COG_ADOPTION_PROFILE.md). This EIB standard retains the project-specific repository authority, platform compatibility, identity, lifecycle, catalog, migration, and AI governance requirements that are not generic COG baselines.

---

# Platform Compatibility

The repository must remain usable on:

- Windows
- macOS
- Linux
- Android Git clients such as GitSync
- GitHub
- Visual Studio Code
- Codex
- GitHub Copilot

A repository change is not considered complete if it introduces paths that prevent a supported platform from cloning or checking out the repository.

---

# Top-Level Directory Standard

Top-level project directories use **UPPERCASE** names.

Approved examples include:

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

Do not create alternate capitalization such as:

```text
Architecture/
architecture/
Documentation/
Implementation/
```

Git may treat these as different directories even when the local operating system does not.

Only one canonical capitalization may exist.

---

# Reserved Root Files

Only documents with repository-wide significance should remain at the repository root.

Examples include:

```text
README.md
LICENSE.md
MANIFESTO.md
CONSTITUTION.md
ROADMAP.md
```

Operational, architectural, implementation, and supporting documents should normally reside in their appropriate directory.

---

# File Naming

File names should:

- Use only characters valid across supported operating systems.
- Avoid leading or trailing spaces.
- Avoid embedded control characters.
- Avoid newline or tab characters.
- Avoid Windows-reserved characters.
- Use stable and descriptive names.
- Preserve established identifiers when documents already have assigned IDs.

Allowed examples:

```text
PRODUCT_ARCHITECTURE.md
REPOSITORY_STANDARDS.md
ADR-0001-Public-vs-Private-Repositories.md
run_eib.yaml
```

Prohibited examples include:

```text
ADR-0001?.md
ADR-0001 .md
<newline>ADR-0001.md
file:name.md
file*.md
```

---

# Windows Compatibility

Repository paths must not contain:

```text
< > : " / \ | ? *
```

within a filename.

Repository files must also avoid:

- Names ending in a period
- Names ending in a space
- Hidden control characters
- Newline characters
- Tab characters
- Windows reserved device names

Examples of reserved Windows names include:

```text
CON
PRN
AUX
NUL
COM1
LPT1
```

Compatibility must be considered even when GitHub or Linux permits a filename.

---

# Case Sensitivity

Case is significant in Git.

Therefore:

```text
ARCHITECTURE/
```

and

```text
Architecture/
```

must be treated as two different paths.

EIB uses the uppercase form for top-level directories.

Duplicate directories differing only by capitalization are prohibited.

---

# Markdown Document Metadata

Governed Markdown documents should begin with YAML front matter.

Standard fields are:

```yaml
---
title:
document_id: # exactly one of document_id, component_id, or model_id
# component_id:
# model_id:
version:
lifecycle_status:
owner:
last_updated:
---
```

Controlled artifacts must use exactly one type-appropriate identity field.
Component and model specifications may use `component_id` or `model_id` rather
than adding a redundant `document_id`.

The following fields are optional when applicable:

```yaml
effective_date:
decision_status:
operational_state:
review_status:
supersedes:
superseded_by:
```

Generic ambiguous `status` fields should be phased out during reconciliation;
they must not silently override lifecycle, decision, operational, or review
semantics. Dates use `YYYY-MM-DD`.

---

# Document Identifiers

Document identifiers must be:

- Unique
- Stable
- Human readable
- Never reused for another controlled identity, including after retirement,
  decontrol, or removal

Examples include:

```text
ADR-0001
ARCH-001
ENGINE-001
MODEL-001
GOV-006
```

Moving or renaming a document does not change its identifier.

Approved identity assignments and reservations include:

- `DEV-001` - `DEVELOPMENT/REPOSITORY_STRUCTURE.md`
- `DEV-002` - `DEVELOPMENT/ENGINEERING_STANDARDS.md`
- `IA-0036` - `REFERENCE_ARCHITECTURE.md`
- `MODEL-007` - Reserved / Never Assigned

Implementation engines use `component_id`; model specifications use `model_id`.
No identity gap may be reused without checking current and historical registry
evidence.

---

# One Authoritative Copy

Each governed document should have one authoritative location.

Avoid:

```text
FINAL
FINAL2
OLD
COPY
BACKUP
v2-final
```

Git provides revision history and replaces the need for manually preserved historical copies.

Obsolete documents should be explicitly deprecated or removed through version control.

---

# Cross-References

Internal repository references should use relative repository paths whenever practical.

Example:

```text
ARCHITECTURE/PRODUCT_ARCHITECTURE.md
```

When files are moved or renamed, affected references must be updated as part of the same logical change.

---

# Directory Moves

Directory renames and moves must be deliberate.

Before moving a directory:

1. Identify all files contained within it.
2. Identify references to those files.
3. Confirm the canonical destination.
4. Move the files.
5. Update references.
6. Update the document catalog.
7. Verify the repository clones successfully.

Case-only renames must be handled carefully because Windows filesystems are commonly case-insensitive.

---

# Repository Catalog

`DOCUMENT_CATALOG.md` or its approved successor serves as the repository configuration-management inventory.

`DOCUMENT_CATALOG.md` is the authoritative registry for controlled-artifact
identity allocation, canonical paths, registration, and disposition, including
active, reserved, retired, and historical identities. Artifact metadata is
authoritative for intrinsic attributes such as title, version, lifecycle, owner,
and effective date. A mismatch is a governance error and must not be silently
resolved by automation.

The catalog should record:

- Document identifier
- Document title
- Repository path
- Status
- Purpose or category

The catalog must be updated when governed documents are created, moved, renamed, deprecated, or removed.

Identity-affecting artifact and catalog changes must be made in the same atomic
commit. Routine content edits do not require catalog changes unless a cataloged
attribute or disposition changes. Directory inventory rows do not replace
individual controlled-artifact registration.

`MODEL-007` must remain recorded as `Reserved / Never Assigned`. Controlled IDs
must never be reused.

---

# Lifecycle and Authority Semantics

Lifecycle states are:

- Draft
- Review
- Approved
- Active
- Revised
- Deprecated
- Archived
- Removed

ADR decision disposition is separate and uses `Proposed`, `Accepted`,
`Rejected`, or `Superseded`. `Accepted` is not lifecycle `Active`.

Operational state is separate from lifecycle; `Production` is not lifecycle
`Active`. Review workflow values such as `Pending Review` and `Planned Review`
belong to the review register or `review_status`, not lifecycle.

`Approved` means formally approved but not necessarily in force. `Active` means
current authoritative/in-force. `Revised` is transitional and returns to
`Active` when the approved revision becomes authoritative. `Deprecated`,
`Archived`, and `Removed` are distinct. Supersession requires bidirectional
traceability, and a removed or retired identity remains permanently unavailable.

The owner is accountable for stewardship, accuracy, maintenance, and initiating
review. Ownership does not by itself confer approval authority; lifecycle,
identity, and disposition decisions remain with BSJ or explicitly delegated
governance authority.

---

# Classification and Automation Boundaries

Control is determined by authoritative function. Directory location, filename,
extension, inventory presence, historical metadata, README naming, template
naming, or an existing ID does not by itself make an artifact controlled.

Automation may validate and report repository conditions. It may not independently
assign, reserve, renumber, retire, decontrol, approve, supersede, or change the
lifecycle of a controlled artifact, nor resolve governance conflicts.

---

# Repository Validation

Repository validation should follow the reusable repository hygiene and validation expectations defined by the pinned COG Repository Standard and GitHub Development Workflow. EIB-specific validation obligations remain in this document, including platform compatibility, catalog integrity, controlled identity, migration restrictions, and project-specific repository outcomes.

Validation tools should reside under:

```text
TOOLS/
```

or another approved automation directory.

---

# Git Practices

General Git change discipline, branch hygiene, staged-scope review, and remote publication sequencing are governed by the pinned COG GitHub Development Workflow. EIB retains the repository-specific constraints and authority boundaries defined in this document, including project-specific migration and controlled-artifact governance expectations.

---

# AI Contributor Requirements

AI-assisted repository changes must follow these standards.

AI systems should:

1. Read the repository rules before making structural changes.
2. Inspect current repository state rather than assuming chat history is current.
3. Preserve established identifiers.
4. Avoid duplicate files and folders.
5. Update affected cross-references.
6. Update catalog and status documentation.
7. Never claim verification unless actual repository content was inspected.

---

# Repository Foundation Exit Criteria

The initial repository cleanup milestone is complete when:

- Only canonical top-level folder names remain.
- No malformed filenames remain.
- Duplicate files are resolved.
- Document locations are standardized.
- Catalog reflects actual repository content.
- Internal references have been reviewed.
- Repository clones successfully on Windows.
- Repository is usable through GitSync.
- VS Code opens the repository cleanly.
- Codex can read and modify the repository.
- Repository validation can be performed repeatably.

---

# Guiding Rule

When choosing between convenience and portability, choose portability.

When choosing between duplicate documentation and one authoritative source, choose one authoritative source.

When choosing between assumptions and verification, verify.

The repository should always leave the project easier to understand than it was before the change.