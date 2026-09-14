---
title: Repository Workflow
document_id: GOV-009
version: 2.0
lifecycle_status: Active
owner: BSJ
last_updated: 2026-09-13
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

# Shared GitHub Workflow Authority

Reusable repository inspection, change, staging, commit, branch, push, and
verification workflow is governed by the pinned COG
[GitHub Development Workflow](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/development/GITHUB_WORKFLOW.md).
The EIB adoption and exception boundary is defined by the
[COG Adoption Profile](DOCUMENTATION/COG_ADOPTION_PROFILE.md).

EIB contributors must apply those authorities together with the EIB-specific
requirements below. This document does not reproduce the reusable COG workflow.

---

# EIB Step 1 — Read Governing Documents

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

# EIB Step 2 — Implement

Implement only the approved scope.

Prefer:

- Small commits
- Small pull requests
- Focused documents
- Incremental improvements

Avoid unrelated edits.

---

# EIB Step 3 — Update Documentation

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

# EIB Step 4 — Verify

EIB-specific verification includes filenames, links, document identities,
metadata, repository structure, references, and Git status. Verification is
part of the EIB Definition of Done.

Commit and push execution follows the pinned COG workflow; EIB work remains
subject to the approval and scope gates defined below.

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

Commit scope and message discipline follow the pinned COG GitHub Development
Workflow referenced above. EIB additionally requires that commit history remain
understandable and tell the story of repository change.

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
- DOCUMENT_CATALOG.md
- DOCUMENTATION/DECISION_LOG.md (historical/supporting decision log)
- ARCHITECTURE/GOVERNANCE.md
- ARCHITECTURE/ADR-0004-Definition-of-Done.md
- ARCHITECTURE/ADR-0005-Versioning-Strategy.md

---

# Guiding Principle

> Small, verified improvements made consistently are more valuable than large, unverified changes made occasionally.