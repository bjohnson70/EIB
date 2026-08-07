---
title: ADR-0005 - Versioning Strategy
document_id: ADR-0005
version: 1.0
status: Accepted
owner: BSJ
last_updated: 2026-08-06
---

# ADR-0005 — Versioning Strategy

## Status

**Accepted**

---

# Purpose

Define the versioning strategy for documentation, architecture, prompts, configuration, and other governed artifacts within the Executive Intelligence Briefing (EIB) repository.

This Architecture Decision Record establishes a consistent approach to version identification while relying on Git as the authoritative history of change.

---

# Context

As the EIB repository evolves, documents will be revised, reorganized, and expanded. Without a consistent versioning strategy, contributors may create duplicate files, inconsistent version numbers, or manually maintained backup copies.

Git already provides complete historical tracking. Document versioning should communicate the maturity of the document—not replace Git history.

---

# Decision

All governed documents shall include a version field in their metadata.

Example:

```yaml
version: 1.0
```

Version numbers communicate the maturity of the current document rather than the complete revision history.

Git remains the authoritative source for historical changes.

---

# Version Numbering

The following version format shall be used:

```text
Major.Minor
```

Examples:

```text
0.1
0.5
1.0
1.1
1.2
2.0
```

---

## Major Version

Increment the major version when:

- Significant architectural changes occur.
- Document purpose changes materially.
- Repository governance changes substantially.
- Backward compatibility is intentionally altered.

Examples:

```text
1.0 → 2.0
```

---

## Minor Version

Increment the minor version when:

- Content is clarified.
- References are updated.
- Examples are improved.
- Minor enhancements are made.
- Formatting is standardized.

Examples:

```text
1.0 → 1.1
```

---

# Git as the Source of History

Git provides:

- Complete revision history.
- Author information.
- Commit timestamps.
- Commit messages.
- Rollback capability.

Therefore, the repository shall not use filenames such as:

```text
Document_v2.md
Document_Final.md
Document_Final2.md
Document_NEW.md
Document_Backup.md
```

One authoritative document shall exist for each governed artifact.

---

# Repository Metadata

Governed Markdown documents should include:

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

This metadata communicates the current state of the document while Git maintains historical revisions.

---

# Versioning Principles

The EIB repository follows these principles:

- One authoritative copy.
- Stable document identifiers.
- Git is the historical record.
- Version numbers communicate document maturity.
- Duplicate documents are prohibited.
- Repository Standards govern document evolution.

---

# Benefits

This strategy:

- Simplifies repository maintenance.
- Eliminates duplicate document versions.
- Improves AI readability.
- Supports configuration management.
- Makes document maturity immediately visible.
- Reduces repository clutter.

---

# Repository Foundation Impact

The Repository Foundation Project standardizes version metadata across all governed documents.

Future contributors should update document versions whenever meaningful changes are made.

Git commit history provides the detailed record of what changed and why.

---

# Related Documents

- ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
- ARCHITECTURE/ADR-0003-Document-Lifecycle.md
- ARCHITECTURE/ADR-0004-Definition-of-Done.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md

---

# Guiding Principle

> Version numbers communicate the current state.

> Git preserves the journey.