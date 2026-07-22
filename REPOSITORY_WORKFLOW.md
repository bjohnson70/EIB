---
title: Repository Workflow
document_id: GOV-004
version: 1.0
status: Accepted
repository_release: Foundation v1.1
owner: Bryan Johnson
role: Product Owner
steward: ChatGPT
steward_role: Chief Architect
last_reviewed: 2026-07-22
next_review: TBD
---

# Repository Workflow

## Purpose

This document defines the standard operating procedures used to maintain, evolve, and govern the Executive Intelligence Briefing (EIB) repository.

The goal is to ensure that every architectural change is intentional, reviewed, traceable, and verifiable.

GitHub is the authoritative source of truth for all repository content.

---

# Governance Model

## Product Owner

The Product Owner establishes the vision and priorities for the repository.

Responsibilities include:

- Define strategic direction
- Approve architectural changes
- Accept Architecture Reviews
- Prioritize repository work
- Make final governance decisions

Current Product Owner:

**Bryan Johnson**

---

## Chief Architect

The Chief Architect is responsible for maintaining architectural consistency throughout the repository.

Responsibilities include:

- Review repository documents
- Recommend improvements
- Maintain architectural integrity
- Reduce architectural debt
- Ensure consistency across documentation
- Verify completed work

Current Chief Architect:

**ChatGPT**

---

# Repository Principles

The repository operates according to the following principles.

1. GitHub is the single source of truth.
2. Architecture before implementation.
3. Governance before automation.
4. Evolution over replacement.
5. Documentation is part of the product.
6. Every significant change is reviewed.
7. Every committed change is verified.

---

# Existing Document Workflow

Every modification to an existing document follows the same workflow.

```text
Read document from GitHub
        ↓
Architecture Review
        ↓
Recommendations
        ↓
Product Owner Approval
        ↓
Generate Complete Replacement
        ↓
Product Owner Commits to GitHub
        ↓
Read Document from GitHub
        ↓
Verification
        ↓
Update Review Register
```

---

# New Document Workflow

When creating a new document:

```text
Verify document does not exist
        ↓
Determine repository path
        ↓
Generate complete document
        ↓
Recommend commit message
        ↓
Product Owner creates file
        ↓
Commit to GitHub
        ↓
Verify document
        ↓
Update Review Register
```

---

# Document Replacement Standard

Unless specifically requested otherwise:

- Entire documents are regenerated.
- Partial patches are avoided.
- GitHub becomes the authoritative version after commit.

This minimizes merge errors and simplifies repository maintenance.

---

# Verification Standard

Verification occurs after every repository update.

Verification confirms:

- Correct file path
- Successful commit
- Complete document
- Proper formatting
- Expected repository structure

Repository work is not considered complete until verification succeeds.

---

# Commit Message Convention

The repository follows conventional commit messages.

Examples:

```text
docs(governance): establish repository workflow
docs(architecture): modernize architecture document
feat(intelligence): add executive briefing generator
refactor(governance): simplify review process
fix(documentation): correct governance metadata
```

---

# Architecture Reviews

Every governed document receives an Architecture Review.

Reviews are recorded in:

```
REVIEW_REGISTER.md
```

Review identifiers are sequential.

Example:

```
AR-0008
```

---

# Repository Philosophy

The repository evolves continuously.

Rather than periodically rebuilding the repository, improvements are made incrementally through governed architectural reviews.

The objective is continuous improvement while preserving consistency and traceability.

---

# Success Criteria

The workflow is successful when:

- Every document is traceable.
- Every architectural decision is documented.
- Every significant change is reviewed.
- Every repository update is verified.
- GitHub remains the authoritative source.
- The repository becomes easier to understand over time.

---

# Related Documents

- CONSTITUTION.md
- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md
- REVIEW_REGISTER.md
- DOCUMENT_CATALOG.md
- STATUS.md