---
Title: Architecture Overview
Version: Foundation (v0.1)
Status: Active
Date: 2026-07-21
---

# EIB Architecture

Welcome to the architectural documentation for the **Executive Intelligence Briefing (EIB)**.

This directory contains the foundational decisions, standards, and governance that define how the project is designed and maintained.

If you're new to the project, this is the best place to begin.

---

# Recommended Reading Order

## 1. Architecture

Start here to understand the overall design.

- ARCHITECTURE.md

---

## 2. Governance

Learn how the project is managed.

- GOVERNANCE.md

---

## 3. Architecture Decision Records (ADRs)

Read the ADRs in numerical order to understand why major decisions were made.

### ADR-0001

Public vs. Private Repository Strategy

Defines the separation of reusable public assets from personalized private implementations.

---

### ADR-0002

Knowledge vs. Intelligence

Defines the transformation of information into actionable intelligence.

---

### ADR-0003

Document Lifecycle

Defines how ideas evolve into published and maintained documents.

---

### ADR-0004

Definition of Done

Defines the quality standards required before work is considered complete.

---

### ADR-0005

Versioning Strategy

Defines the project's release and version management approach.

---

# Guiding Principles

Every architectural decision should:

- Improve clarity.
- Reduce duplication.
- Preserve reasoning.
- Encourage reuse.
- Support long-term maintenance.

The guiding question is:

> **Does this leave behind a better starting point for the next person?**

---

# Directory Structure

```text
Architecture/
├── README.md
├── ARCHITECTURE.md
├── GOVERNANCE.md
├── ADR-0001-Public-vs-Private-Repositories.md
├── ADR-0002-Knowledge-vs-Intelligence.md
├── ADR-0003-Document-Lifecycle.md
├── ADR-0004-Definition-of-Done.md
└── ADR-0005-Versioning-Strategy.md
```

---

# Related Documents

From the repository root:

- README.md
- MANIFESTO.md
- ROADMAP.md
- CHANGELOG.md

---

# Purpose

The architecture is intended to evolve over time, but every change should be intentional, documented, and leave the project stronger than before.