---
title: Executive Intelligence Briefing Repository Structure
document_id: IA-0016
version: 1.0
status: Approved
owner: Bryan Johnson
author: Bryan Johnson & ChatGPT
last_updated: 2026-07-23
depends_on:
  - CONSTITUTION.md
  - ARCHITECTURE/PRODUCT_ARCHITECTURE.md
  - IMPLEMENTATION/IMPLEMENTATION_ARCHITECTURE.md
---

# Executive Intelligence Briefing Repository Structure

## Purpose

This document defines the canonical organization of the Executive Intelligence Briefing (EIB) repository.

A consistent repository structure improves discoverability, maintainability, onboarding, automation, and long-term evolution. Every document, prompt, connector, workflow, test, and implementation artifact should have a clearly defined location.

---

# Design Philosophy

The repository is organized around **capabilities**, not technologies.

This allows the implementation language, framework, orchestration engine, or AI model to evolve without requiring significant reorganization.

The repository should be understandable by:

- Human developers
- AI coding agents
- Architects
- Contributors
- Future maintainers

---

# Repository Principles

The repository shall be:

- Predictable
- Self-documenting
- Modular
- Version controlled
- AI-friendly
- Easy to navigate
- Easy to extend

---

# High-Level Repository Layout

```text
/
├── README.md
├── MANIFESTO.md
├── CONSTITUTION.md
├── REFERENCE_ARCHITECTURE.md
├── PRODUCT_REQUIREMENTS.md
│
├── Architecture/
│
├── IMPLEMENTATION/
│
├── DEVELOPMENT/
│
├── DATA/
│
├── OPERATIONS/
│
├── ROADMAP/
│
├── prompts/
│
├── agents/
│
├── connectors/
│
├── workflows/
│
├── templates/
│
├── schemas/
│
├── configuration/
│
├── examples/
│
├── tests/
│
├── scripts/
│
├── docs/
│
└── archive/
```

---

# Directory Responsibilities

## Architecture/

Contains product architecture.

Examples:

- Vision
- Product Architecture
- Intelligence Architecture
- Scoring Model
- Report Specification

This directory answers:

**"What are we building?"**

---

## IMPLEMENTATION/

Contains implementation architecture.

Examples:

- Agent Architecture
- Workflow Orchestration
- Assembly Engine
- Knowledge Model
- Connector Framework

This directory answers:

**"How does it work?"**

---

## DEVELOPMENT/

Contains engineering standards.

Examples:

- Coding Standards
- Repository Structure
- API Specifications
- Plugin Architecture
- Versioning Strategy

This directory answers:

**"How do developers contribute?"**

---

## DATA/

Defines data architecture.

Examples:

- Storage
- Knowledge Graph
- Embeddings
- Retention
- Historical Intelligence

This directory answers:

**"How is information managed?"**

---

## OPERATIONS/

Defines runtime operations.

Examples:

- Deployment
- Scheduling
- Security
- Monitoring
- Backup
- Recovery

This directory answers:

**"How does the platform operate?"**

---

## ROADMAP/

Planning documentation.

Examples:

- MVP
- Release Plan
- Feature Backlog
- Technical Debt
- Implementation Plan

---

## prompts/

Version-controlled prompt assets.

Examples:

- System prompts
- Agent prompts
- Editorial prompts
- QA prompts

Prompts are treated as software assets.

---

## agents/

Agent definitions.

Each agent should contain:

- configuration
- prompt
- metadata
- tests

One directory per agent.

---

## connectors/

External integrations.

Examples:

- Weather
- News
- Cyber
- Calendar
- Email
- Financial Markets

Each connector should be independently testable.

---

## workflows/

Workflow definitions.

Examples:

- Morning Briefing
- Weekly Review
- Breaking News
- Executive Alert

---

## templates/

Reusable report templates.

Examples:

- Daily Briefing
- Weekly Briefing
- Executive Summary
- Watch List

---

## schemas/

Canonical schemas.

Examples:

- Intelligence Object
- Executive Score
- Recommendation
- Configuration

Schemas should remain backward compatible whenever practical.

---

## configuration/

Configuration profiles.

Examples:

- Executive Profiles
- Runtime Settings
- Feature Flags
- Connector Configuration

Configuration should never contain secrets.

---

## examples/

Reference examples.

Include:

- Sample reports
- Example intelligence
- Test datasets
- Demonstration workflows

---

## tests/

Automated validation.

Examples:

- Unit Tests
- Integration Tests
- Prompt Tests
- Quality Tests
- Regression Tests

Testing should mirror repository organization.

---

## scripts/

Automation utilities.

Examples:

- Build
- Validation
- Deployment
- Report generation
- Maintenance

Scripts should be deterministic and idempotent where practical.

---

## docs/

Supporting documentation not considered part of the formal architecture.

Examples:

- Tutorials
- FAQs
- User Guides
- Migration Guides

---

## archive/

Historical materials.

Examples:

- Deprecated specifications
- Superseded documents
- Legacy prompts
- Previous report formats

Archived content remains read-only.

---

# Naming Conventions

Repository names should be:

- Descriptive
- Consistent
- Lowercase where applicable
- Free of abbreviations unless widely understood

Examples:

```
agent_architecture.md

weather_connector.md

executive_summary_template.md
```

Avoid names such as:

```
new_doc.md

test2.md

temp.md

misc.md
```

---

# Directory Independence

Each top-level directory should represent a distinct architectural concern.

Cross-directory dependencies should be minimized and documented explicitly.

---

# Version Control

All repository content shall be managed through Git.

Every meaningful change should include:

- Clear commit message
- Traceable history
- Review where appropriate
- Updated document version when applicable

---

# Repository Growth

As the platform evolves:

- Add new directories only when a new architectural concern emerges.
- Prefer extending existing structures before creating parallel hierarchies.
- Avoid duplicate responsibilities across directories.

The repository should remain intuitive even as it grows.

---

# Success Criteria

The repository structure succeeds when:

- New contributors can quickly locate relevant content.
- AI coding agents can navigate the repository with minimal guidance.
- Architectural boundaries remain clear.
- Related artifacts are grouped logically.
- The repository scales without requiring major reorganization.

---

# Guiding Principle

A well-organized repository is an architectural asset.

Its structure should communicate the design of the platform as clearly as the documents it contains, enabling humans and AI systems alike to understand, extend, and maintain the Executive Intelligence Briefing with confidence.

---

# Related Documents

- README.md
- REFERENCE_ARCHITECTURE.md
- PRODUCT_REQUIREMENTS.md
- Architecture/PRODUCT_ARCHITECTURE.md
- IMPLEMENTATION/IMPLEMENTATION_ARCHITECTURE.md
- DEVELOPMENT/CODING_STANDARDS.md
- DEVELOPMENT/API_SPECIFICATION.md