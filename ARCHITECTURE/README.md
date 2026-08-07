---
title: Architecture Overview
document_id: ARCH-008
version: 1.0
status: Active
owner: BSJ
last_updated: 2026-08-07
---

# Executive Intelligence Briefing (EIB)

# Architecture Overview

## Purpose

This document is the entry point for the EIB architecture library.

It explains how the architecture documents are organized, which documents should be read first, and how the major architecture decisions relate to one another.

If you are new to EIB architecture, begin here.

---

# Recommended Reading Order

## 1. Enterprise Architecture

Start with:

```text
ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md
```

This document defines:

- The overall architecture
- Major domains
- Logical system structure
- Architectural dependencies
- Platform-wide design principles

---

## 2. Architecture Governance

Then read:

```text
ARCHITECTURE/GOVERNANCE.md
```

This document defines:

- How architecture decisions are made
- Repository-owner authority
- Contributor responsibilities
- AI-assisted governance
- Review triggers
- Change-control expectations

---

## 3. Architecture Decision Records

Read the ADRs in numerical order.

### ADR-0001 — Public vs. Private Repository Strategy

```text
ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
```

Defines how reusable public architecture is separated from private implementations and sensitive information.

---

### ADR-0002 — Knowledge vs. Intelligence

```text
ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
```

Defines the conceptual progression:

```text
Knowledge
   ↓
Reasoning
   ↓
Intelligence
   ↓
Action
```

---

### ADR-0003 — Document Lifecycle

```text
ARCHITECTURE/ADR-0003-Document-Lifecycle.md
```

Defines how governed documents move from creation through retirement.

---

### ADR-0004 — Definition of Done

```text
ARCHITECTURE/ADR-0004-Definition-of-Done.md
```

Defines the quality and verification requirements that must be satisfied before repository work is considered complete.

---

### ADR-0005 — Versioning Strategy

```text
ARCHITECTURE/ADR-0005-Versioning-Strategy.md
```

Defines document versioning while establishing Git as the authoritative revision history.

---

# Product Architecture

After the foundational ADRs, review the product-level architecture.

## Product Architecture

```text
ARCHITECTURE/PRODUCT_ARCHITECTURE.md
```

Defines the major product capabilities and intended executive experience.

---

## Intelligence Architecture

```text
ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
```

Defines how raw information becomes executive intelligence.

---

## Report Specification

```text
ARCHITECTURE/REPORT_SPECIFICATION.md
```

Defines the standard daily briefing behavior, including:

- Calendar-first orientation
- 5–7 minute reading target
- Priority intelligence
- Recommendations
- Interpreted metrics
- Strategic-location context
- Professional but human presentation

---

## Personalization Model

```text
ARCHITECTURE/PERSONALIZATION_MODEL.md
```

Defines how the same underlying intelligence may be adapted to different users, responsibilities, locations, preferences, and presentation styles.

---

## Scoring Model

```text
ARCHITECTURE/SCORING_MODEL.md
```

Defines how EIB determines what deserves attention.

---

## Data Source Strategy

```text
ARCHITECTURE/DATA_SOURCE_STRATEGY.md
```

Defines how sources are acquired, classified, evaluated, governed, and traced.

---

# Existing Architecture Documents

The canonical `ARCHITECTURE/` directory currently includes or is expected to include:

```text
ARCHITECTURE/
│
├── README.md
├── ENTERPRISE_ARCHITECTURE.md
├── GOVERNANCE.md
│
├── ADR-0001-Public-vs-Private-Repositories.md
├── ADR-0002-Knowledge-vs-Intelligence.md
├── ADR-0003-Document-Lifecycle.md
├── ADR-0004-Definition-of-Done.md
├── ADR-0005-Versioning-Strategy.md
│
├── PRODUCT_ARCHITECTURE.md
├── INTELLIGENCE_ARCHITECTURE.md
├── REPORT_SPECIFICATION.md
├── PERSONALIZATION_MODEL.md
├── SCORING_MODEL.md
├── DATA_SOURCE_STRATEGY.md
│
├── DESIGN_PHILOSOPHY.md
├── EDITORIAL_GUIDELINES.md
├── INTELLIGENCE_ENGINE.md
├── PRODUCT_VISION.md
├── QUALITY_STANDARDS.md
└── SYSTEM_ARCHITECTURE.md
```

This list should evolve only through governed repository changes.

---

# Architecture vs. Implementation

Architecture defines:

```text
What the system must accomplish
and
How major concepts relate
```

Implementation defines:

```text
How those architectural decisions are technically realized
```

Implementation details belong primarily under:

```text
IMPLEMENTATION/
```

Architecture should not become dependent on unnecessary implementation detail.

---

# Architecture vs. Product Requirements

Product requirements define:

```text
What capabilities the product must provide
```

Architecture defines:

```text
How those capabilities fit together conceptually
```

The primary requirements document is:

```text
PRODUCT_REQUIREMENTS.md
```

---

# Architecture vs. Repository Governance

Repository structure and file-management standards are defined under:

```text
DOCUMENTATION/
```

Important documents include:

```text
DOCUMENTATION/REPOSITORY_STANDARDS.md
DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
DOCUMENTATION/REPOSITORY_INVENTORY.md
DOCUMENTATION/DOCUMENT_CATALOG.md
```

Architecture should reference these standards rather than duplicate them.

---

# Architectural Principles

Every significant architecture decision should generally improve one or more of the following:

- Clarity
- Modularity
- Explainability
- Reuse
- Portability
- Configurability
- Maintainability
- Traceability
- Intelligence quality
- Executive usability

---

# AI-Assisted Architecture

The architecture library is intentionally structured so both human contributors and AI systems can understand it.

AI assistants should:

1. Read this overview.
2. Read the Enterprise Architecture.
3. Review applicable ADRs.
4. Read relevant domain architecture.
5. Follow Repository Standards.
6. Inspect actual repository state before proposing structural changes.

AI systems must not rely solely on historical chat context when repository content is available.

---

# Canonical Directory Rule

The approved architecture directory is:

```text
ARCHITECTURE/
```

The legacy directory:

```text
Architecture/
```

is being retired through the Repository Foundation migration.

No new documents should be created under `Architecture/`.

---

# Repository Foundation Status

The Repository Foundation migration is consolidating architecture into the canonical uppercase directory.

Migration principles are:

```text
Inventory first.
Compare second.
Move third.
Verify always.
```

The migration is governed by:

```text
DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
```

---

# Related Documents

- README.md
- MANIFESTO.md
- CONSTITUTION.md
- PRODUCT_REQUIREMENTS.md
- ROADMAP.md
- ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md
- ARCHITECTURE/GOVERNANCE.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
- DOCUMENTATION/REPOSITORY_INVENTORY.md
- DOCUMENTATION/DOCUMENT_CATALOG.md

---

# Guiding Principle

> Architecture should leave the next contributor with a clearer starting point than the previous contributor had.

The architecture library succeeds when a new human or AI contributor can quickly understand what EIB is, why it is designed this way, and where new ideas belong.