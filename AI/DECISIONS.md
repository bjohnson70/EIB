---
title: Architectural Decisions
document_id: AI-004
version: 1.0
status: Approved
owner: BSJ
author: BSJ & ChatGPT
last_updated: 2026-07-24
depends_on:
  - AI/README.md
  - AI/AI_RULES.md
---

# Architectural Decisions

## Purpose

This document records significant architectural and design decisions made during the development of the Executive Intelligence Briefing (EIB).

Unlike formal Architecture Decision Records (ADRs), this document is intended to be a lightweight chronological log that captures *why* important decisions were made. It provides context for future contributors and AI systems, helping them understand the reasoning behind the repository's evolution.

---

# Decision Log

---

## 2026-07-24

### Decision

Create an `AI/` workspace within the repository.

### Reason

Project continuity should not depend on an individual chat conversation or a specific AI model.

By storing operational context in the repository itself, any future AI or human contributor can resume work with minimal additional explanation.

### Outcome

Created the AI collaboration subsystem consisting of:

- README.md
- AI_RULES.md
- NEXT_TASK.md
- REPOSITORY_STATUS.md
- SESSION_NOTES.md
- BACKLOG.md
- DECISIONS.md
- PROMPTS/

---

## 2026-07-24

### Decision

Use ordinary Markdown for all AI coordination documents.

### Reason

Markdown is portable, version controlled, easy to review, and supported by GitHub, GitSync, Codex, Obsidian, Visual Studio Code, and standard text editors.

Avoiding proprietary formats ensures long-term accessibility.

### Outcome

All AI workspace documents are maintained as plain Markdown.

---

## 2026-07-24

### Decision

Adopt a repository-first workflow.

### Reason

The GitHub repository is the authoritative source of truth.

Chat conversations provide temporary assistance but are not considered persistent project memory.

### Outcome

AI systems should read the repository before making changes and update repository documentation before concluding a work session.

---

# Guidelines

Add a new entry when:

- Repository structure changes.
- Major architectural decisions are made.
- Development workflow changes.
- Governance policies are modified.
- Significant technology choices are adopted.

Entries should explain:

1. What decision was made.
2. Why it was made.
3. Expected impact.
4. Result, if known.

---

# Relationship to ADRs

This document is intentionally lightweight.

If a decision becomes significant enough to warrant detailed analysis, it may later be promoted to a formal Architecture Decision Record (ADR).

Until then, this document serves as the project's historical memory.