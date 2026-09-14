---
title: Contributing Guide
document_id: GOV-013
version: 1.0
owner: BSJ
last_updated: 2026-09-13
lifecycle_status: Active
---

# Contributing to the Executive Intelligence Briefing (EIB)

Thank you for contributing to the Executive Intelligence Briefing (EIB) project.

EIB is more than a collection of documents. It is a governed knowledge system designed to transform information into reusable intelligence through thoughtful architecture, disciplined documentation, and continuous improvement.

Whether you are correcting a typo, improving documentation, proposing an architectural enhancement, or introducing a new capability, every contribution should leave the repository stronger than it was before.

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.

---

# Governance Hierarchy

When guidance appears in multiple documents, precedence is determined in the following order:

1. CONSTITUTION.md
2. Architecture Decision Records (ADRs)
3. ARCHITECTURE.md
4. GOVERNANCE.md
5. CONTRIBUTING.md
6. Templates and Examples

When uncertainty exists, follow the highest applicable authority.

---

# Before You Contribute

Before making changes, follow the pinned COG
[GitHub Development Workflow](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/development/GITHUB_WORKFLOW.md)
and the EIB-specific requirements in
[REPOSITORY_WORKFLOW.md](REPOSITORY_WORKFLOW.md). As an EIB contributor, also
ask yourself:

- Does this improve clarity?
- Does this reduce duplication?
- Does this preserve the reasoning behind previous decisions?
- Is this solution reusable?
- Is the change appropriately documented?
- Does this improve long-term maintainability?

If the answer to any question is **No**, consider refining the contribution before committing it.

---

# Repository Standards

EIB contributors should:

- Follow the documented architecture.
- Respect governance decisions.
- Read applicable ADRs before changing architectural behavior.
- Prefer evolving existing content before creating new content.

For reusable repository, documentation, naming, identity, and workflow
requirements, follow the pinned COG authorities identified by the
[COG Adoption Profile](DOCUMENTATION/COG_ADOPTION_PROFILE.md). EIB-specific
repository standards, extensions, exceptions, and migration constraints remain
governed by [REPOSITORY_STANDARDS.md](DOCUMENTATION/REPOSITORY_STANDARDS.md).

---

# Documentation Standards

Apply the pinned COG Documentation Standard for reusable documentation
identity, authority, lifecycle, references, review, and supersession guidance.
Use the EIB adoption profile and repository standards for EIB-specific
extensions and exceptions.

Where appropriate, include:

- Purpose
- Context
- Decision
- Benefits
- Trade-offs
- Related documents
- References to authoritative sources

Whenever significant decisions are made, preserve the reasoning behind those decisions—not just the outcome.

---

# Workflow and Pull Requests

Follow the EIB-specific workflow in [REPOSITORY_WORKFLOW.md](REPOSITORY_WORKFLOW.md)
and the pinned COG GitHub Development Workflow for commit, branch, push, and
verification mechanics. Keep pull requests focused, explain why the change is
needed, reference related issues or ADRs, and update documentation when behavior
changes.

---

# Definition of Done

Use the EIB-specific completion expectations below together with the pinned COG
Repository and Documentation Standards and the EIB workflow:

- Documentation is accurate.
- Related files have been updated.
- Internal links and governance references are verified.
- The repository is easier to understand than before.
- Long-term maintainability has improved.

---

# Code of Conduct

Contributors are expected to:

- Be respectful.
- Assume positive intent.
- Discuss ideas rather than individuals.
- Support evidence-based decisions.
- Value long-term maintainability over short-term convenience.
- Leave the repository better than they found it.

---

# Questions

When uncertainty exists:

1. Review the Constitution.
2. Review the Architecture documentation.
3. Review applicable ADRs.
4. Choose the solution that best supports long-term maintainability.
5. Document significant architectural decisions.

---

# Thank You

Every thoughtful contribution strengthens the Executive Intelligence Briefing project.

The goal is not merely to build documentation, but to build a governed body of knowledge that others can confidently understand, maintain, and improve for years to come.