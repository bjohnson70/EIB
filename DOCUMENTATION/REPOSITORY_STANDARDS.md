---
title: Repository Standards
document_id: GOV-006
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-08-06
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

Repository structure should be predictable enough that a human contributor, ChatGPT, Codex, GitHub Copilot, or another AI system can locate and understand project content without relying on prior chat history.

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
document_id:
version:
status:
owner:
last_updated:
---
```

Additional metadata may be added where appropriate.

---

# Document Identifiers

Document identifiers must be:

- Unique
- Stable
- Human readable
- Never reused for unrelated documents

Examples include:

```text
ADR-0001
ARCH-001
ENGINE-001
MODEL-001
GOV-006
```

Moving or renaming a document does not change its identifier.

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

The catalog should record:

- Document identifier
- Document title
- Repository path
- Status
- Purpose or category

The catalog must be updated when governed documents are created, moved, renamed, deprecated, or removed.

---

# Repository Validation

Repository validation should eventually include automated checks for:

- Invalid filenames
- Duplicate case-sensitive paths
- Broken internal links
- Duplicate document identifiers
- Missing metadata
- Missing catalog entries
- Unsupported characters
- Orphaned documents

Validation tools should reside under:

```text
TOOLS/
```

or another approved automation directory.

---

# Git Practices

Changes should be:

- Focused
- Reviewable
- Reversible

Use meaningful commit messages.

Examples:

```text
docs(repo): establish repository standards
fix(repo): remove malformed filename
refactor(repo): consolidate architecture directories
docs(catalog): refresh document inventory
```

Do not combine unrelated repository changes into one commit when they can reasonably be separated.

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