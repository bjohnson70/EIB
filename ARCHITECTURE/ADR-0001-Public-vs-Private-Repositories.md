---
title: ADR-0001 - Public vs. Private Repository Strategy
document_id: ADR-0001
version: 2.0
status: Accepted
owner: BSJ
last_updated: 2026-08-06
---

# ADR-0001 — Public vs. Private Repository Strategy

## Status

**Accepted**

---

# Purpose

Define the repository strategy that separates reusable public intellectual property from private implementation and personal information.

This Architecture Decision Record (ADR) establishes the governance model for all future EIB repositories and derivative projects.

---

# Context

The Executive Intelligence Briefing (EIB) project has two complementary goals:

1. Capture and organize personal knowledge to improve executive decision-making.
2. Share reusable architecture, documentation, prompts, templates, governance, and implementation guidance with the broader community.

These goals have different security, privacy, and governance requirements.

Combining reusable public content with personal or confidential information would:

- Increase the likelihood of accidental disclosure.
- Require continual manual redaction.
- Discourage open collaboration.
- Reduce long-term maintainability.
- Make publication significantly more difficult.

---

# Decision

The EIB ecosystem shall consist of separate repositories with clearly defined purposes.

## Public Repository

The Public Repository contains reusable intellectual property that anyone may study, adopt, or extend.

Examples include:

- Architecture
- Governance
- Design documents
- Templates
- Prompt libraries
- AI guidance
- Workflows
- Reference implementations
- Sample configurations
- Documentation

The Public Repository shall never contain:

- Personal information
- Financial information
- Health information
- Confidential work products
- Connected account data
- Credentials
- Organization-specific restricted information

---

## Private Repository

The Private Repository contains personalized implementations of the public framework.

Examples include:

- Executive Briefings
- Personal knowledge
- Retirement planning
- Health tracking
- Family information
- Connected services
- Production configuration
- Personal AI profiles
- Work products
- Operational history

The Private Repository may contain confidential information and shall be appropriately protected.

---

# Repository Relationship

The Public Repository defines the framework.

The Private Repository demonstrates the framework in use.

Whenever an improvement is discovered while working in the Private Repository, it should be:

1. Generalized.
2. Stripped of sensitive information.
3. Incorporated into the Public Repository.

This creates a continuous improvement cycle.

```text
Private Experience
        │
        ▼
Generalize
        │
        ▼
Remove Sensitive Information
        │
        ▼
Improve Public Repository
        │
        ▼
Future Users Benefit
```

---

# Benefits

This strategy provides:

- Protection of sensitive information.
- Reusable public intellectual property.
- Clear governance.
- Better collaboration.
- Cleaner repository management.
- Easier onboarding.
- Better AI compatibility.
- Long-term maintainability.

---

# Trade-offs

Maintaining multiple repositories requires:

- Synchronizing improvements.
- Additional governance.
- Promotion of reusable content.
- Occasional duplication of repository metadata.

These trade-offs are acceptable because they significantly improve security, maintainability, and collaboration.

---

# Alternatives Considered

## Single Repository

**Rejected**

Reason:

Public and private content have incompatible governance requirements.

---

## Branch Separation

**Rejected**

Reason:

Git branches are not a security boundary.

---

## Manual Redaction

**Rejected**

Reason:

Manual redaction is time-consuming, error-prone, and not sustainable.

---

# Success Criteria

This decision is considered successful when:

- Public repositories remain free of sensitive information.
- Private repositories continue evolving from the public architecture.
- Improvements routinely flow from private implementations into reusable public documentation.
- Repository responsibilities remain obvious to contributors.
- Repositories clone successfully across Windows, macOS, Linux, Android GitSync, VS Code, Codex, and GitHub.

---

# Repository Foundation Impact

This ADR