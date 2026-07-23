---
title: Repository Structure
document_id: DEV-001
version: 2.0
status: Approved
owner: BSJ
author: BSJ & ChatGPT
last_updated: 2026-07-23
depends_on:
  - DOCUMENT_CATALOG.md
  - Architecture/ARCHITECTURE.md
---

# Repository Structure

## Purpose

This document defines the approved organizational structure of the Executive Intelligence Briefing (EIB) repository.

Rather than serving as a simple directory listing, this document establishes the architectural rules governing where documents belong, how new capabilities are introduced, and how the repository scales while remaining understandable and maintainable.

---

# Design Goals

The repository is organized to achieve the following objectives:

- Separate governance from implementation.
- Group related knowledge together.
- Minimize duplication.
- Support future automation.
- Enable AI agents to reason about repository contents.
- Make information easy to discover.
- Scale without requiring structural redesign.

Every structural decision should support one or more of these goals.

---

# Repository Layout

```
/
├── README.md
├── MANIFESTO.md
├── CONSTITUTION.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── REVIEW_REGISTER.md
├── REPOSITORY_WORKFLOW.md
├── DOCUMENT_CATALOG.md
├── PRODUCT_REQUIREMENTS.md
├── EXECUTIVE_PRINCIPLES.md
├── REFERENCE_ARCHITECTURE.md
│
├── Architecture/
├── DATA/
├── DEVELOPMENT/
├── IMPLEMENTATION/
├── OPERATIONS/
└── ROADMAP/
```

The complete governed inventory is maintained in `DOCUMENT_CATALOG.md`.

---

# Directory Responsibilities

## Root

Contains repository-wide governance and executive documents.

No implementation-specific documents should reside at the repository root unless they intentionally serve the entire repository.

---

## Architecture/

Defines the logical architecture of the EIB platform.

Examples include:

- Product architecture
- Intelligence architecture
- Governance
- Report specification
- Scoring
- Personalization

Architecture answers:

> What is the system?

---

## DEVELOPMENT/

Defines standards used to build and maintain the repository.

Examples include:

- Repository structure
- Coding standards
- API specifications
- Versioning
- Plugin architecture

Development answers:

> How do we build it?

---

## IMPLEMENTATION/

Defines how the architecture is realized.

Examples include:

- Agents
- Prompt architecture
- Workflow orchestration
- Knowledge model
- Assembly engine
- Execution state
- Pipeline

Implementation answers:

> How does it work?

---

## DATA/

Defines how information is stored, retained, represented, and retrieved.

Examples include:

- Storage
- Embeddings
- Knowledge graph
- Historical intelligence
- Retention

Data answers:

> How is knowledge managed?

---

## OPERATIONS/

Defines how the platform is operated after deployment.

Examples include:

- Deployment
- Security
- Scheduling
- Backup
- Change management

Operations answers:

> How is the system run?

---

## ROADMAP/

Defines future work.

Examples include:

- MVP
- Release plans
- Feature backlog
- Technical debt
- Implementation planning

Roadmap answers:

> Where is the project going?

---

# Placement Rules

Every new governed document shall belong to exactly one primary directory.

Documents should not be duplicated across directories.

If multiple documents require the same information, they should reference the authoritative source rather than copying content.

---

# Naming Standards

Governed documents use:

- Uppercase filenames
- Underscores instead of spaces
- Markdown (`.md`) format
- Descriptive names

Examples:

```
PRODUCT_REQUIREMENTS.md
QUALITY_ASSURANCE_FRAMEWORK.md
INTELLIGENCE_PIPELINE_SPECIFICATION.md
```

---

# Repository Evolution

New capabilities should extend the existing structure whenever practical.

Creating new top-level directories should be considered an architectural change and should occur only when the existing organization can no longer accommodate future growth.

---

# Relationship to Other Documents

This document defines **where** information belongs.

`DOCUMENT_CATALOG.md` defines **what** exists.

`ARCHITECTURE.md` defines **how** the repository is organized logically.

Together, these documents form the governance foundation of the repository.

---

# Success Criteria

The repository structure succeeds when:

- Documents are easy to locate.
- Responsibilities are clearly separated.
- New contributors can quickly understand the organization.
- AI agents can reliably navigate the repository.
- Growth occurs without structural rework.
- The repository remains internally consistent over time.