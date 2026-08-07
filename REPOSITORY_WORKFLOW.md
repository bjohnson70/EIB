---
title: Repository Workflow
document_id: GOV-009
version: 2.0
status: Active
owner: BSJ
last_updated: 2026-08-07
---

# Executive Intelligence Briefing (EIB)

# Repository Workflow

## Purpose

This document defines the standard workflow for developing, reviewing, validating, and maintaining the Executive Intelligence Briefing (EIB) repository.

The workflow is designed for both human contributors and AI-assisted development.

The objectives are:

- Maintain repository quality.
- Preserve architectural integrity.
- Support small, verifiable commits.
- Enable repeatable AI-assisted development.
- Keep Git history meaningful.

---

# Core Principles

Development should always favor:

- Small changes
- One logical objective per commit
- Verification before completion
- Documentation alongside implementation
- One authoritative copy of every concept

---

# Standard Development Workflow

```text
Identify Work
      │
      ▼
Review Existing Repository
      │
      ▼
Read Governing Documents
      │
      ▼
Implement Change
      │
      ▼
Update Documentation
      │
      ▼
Verify Repository
      │
      ▼
Commit
      │
      ▼
Push
```

---

# Step 1 — Identify Work

Every task should begin with a clearly defined objective.

Examples:

- Fix documentation
- Implement feature
- Update architecture
- Refactor repository
- Improve workflow
- Resolve duplicate content

Large objectives should be divided into smaller logical units.

---

# Step 2 — Review Existing Repository

Before changing anything:

- Search for existing documentation.
- Search for similar implementations.
- Identify dependencies.
- Avoid creating duplicate documents.

The repository is always the primary source of truth.

---

# Step 3 — Read Governing Documents

Depending on the change, review:

```text
CONSTITUTION.md

DOCUMENTATION/
    REPOSITORY_STANDARDS.md
    REPOSITORY_MIGRATION_PLAN.md
    DOCUMENT_CATALOG.md

ARCHITECTURE/
    README.md
    ENTERPRISE_ARCHITECTURE.md
    GOVERNANCE.md

Applicable ADRs
```

Implementation work should also review the relevant implementation specifications.

---

# Step 4 — Implement

Implement only the approved scope.

Prefer:

- Small commits
- Small pull requests
- Focused documents
- Incremental improvements

Avoid unrelated edits.

---

# Step 5 — Update Documentation

Implementation and documentation should evolve together.

Possible updates include:

- Architecture
- Product requirements
- Decision Log
- Repository Inventory
- Document Catalog
- Roadmap
- Changelog

---

# Step 6 — Verify

Before committing:

- Verify filenames.
- Verify links.
- Verify document identifiers.
- Verify metadata.
- Verify repository structure.
- Verify formatting.
- Verify references.
- Verify Git status.

Verification is part of the Definition of Done.

---

# Step 7 — Commit

Every commit should represent one logical change.

Good examples:

```text
docs(architecture): modernize report specification

docs(repo): update repository inventory

feat(engine): implement confidence scoring

refactor(repo): retire legacy architecture directory
```

Avoid combining unrelated work into one commit.

---

# Step 8 — Push

After verification:

```text
git add .
git commit -m "<message>"
git push
```

The repository should remain buildable and understandable after every push.

---

# AI-Assisted Workflow

AI contributors should:

1. Inspect repository state.
2. Read governing documents.
3. Reuse existing architecture.
4. Avoid duplicate content.
5. Preserve document identifiers.
6. Update related documents.
7. Verify changes.
8. Recommend follow-up work.

AI should never assume historical chat context is more authoritative than the repository itself.

---

# Repository Foundation Workflow

During Repository Foundation:

```text
Inventory
    ↓
Compare
    ↓
Preserve
    ↓
Standardize
    ↓
Verify
    ↓
Retire Legacy
```

Never delete a document before its replacement has been verified.

---

# Commit Philosophy

Commits should answer one question:

> What changed?

Examples:

```text
docs(product): update roadmap

docs(repo): modernize README

docs(architecture): migrate governance

refactor(repo): remove duplicate architecture directory
```

Good commit history tells the story of the repository.

---

# Branch Strategy

Current workflow:

```text
main
```

Future workflow may include:

```text
main
develop
feature/*
release/*
hotfix/*
```

The branching strategy should remain simple until project complexity requires expansion.

---

# Document Workflow

Governed documents generally follow:

```text
Draft
Review
Approved
Active
Deprecated
Archived
```

Git maintains historical versions.

Repository copies should represent the current authoritative version.

---

# Verification Checklist

Before every significant commit:

- [ ] Repository standards followed.
- [ ] Metadata updated.
- [ ] Links verified.
- [ ] Document identifiers preserved.
- [ ] Duplicate content avoided.
- [ ] Related documentation updated.
- [ ] Repository builds conceptually.
- [ ] Git status understood.
- [ ] Commit message reflects actual work.

---

# Codex Workflow

Codex-assisted development should follow this pattern:

```text
Repository
      ↓
Inspect
      ↓
Modify
      ↓
Verify
      ↓
Commit
      ↓
Push
      ↓
Review
```

Codex should always work against the current repository rather than recreated content from chat history.

---

# Success Criteria

The workflow succeeds when:

- Changes are easy to review.
- Git history is meaningful.
- Repository quality steadily improves.
- AI and humans follow the same governance model.
- New contributors can understand how work is performed.

---

# Related Documents

- README.md
- CONSTITUTION.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
- DOCUMENTATION/REPOSITORY_INVENTORY.md
- DOCUMENTATION/DOCUMENT_CATALOG.md
- DOCUMENTATION/DECISION_LOG.md
- ARCHITECTURE/GOVERNANCE.md
- ARCHITECTURE/ADR-0004-Definition-of-Done.md
- ARCHITECTURE/ADR-0005-Versioning-Strategy.md

---

# Guiding Principle

> Small, verified improvements made consistently are more valuable than large, unverified changes made occasionally.