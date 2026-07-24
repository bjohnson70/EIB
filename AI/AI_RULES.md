---
title: AI Collaboration Rules
document_id: AI-001
version: 1.0
status: Approved
owner: BSJ
author: BSJ & ChatGPT
last_updated: 2026-07-24
depends_on:
  - AI/README.md
---

# AI Collaboration Rules

## Purpose

This document establishes the operating rules for all AI systems that contribute to the Executive Intelligence Briefing (EIB) repository.

Its purpose is to ensure that every AI session produces work that is accurate, consistent, traceable, and maintainable regardless of which AI model performs the work.

---

# Guiding Philosophy

The repository is the authoritative source of truth.

Chat conversations are temporary.

AI systems must learn the current state of the project by reading the repository—not by relying on conversational memory.

---

# Repository First

Before making changes an AI should review, at a minimum:

1. AI/NEXT_TASK.md
2. AI/REPOSITORY_STATUS.md
3. AI/DECISIONS.md
4. DOCUMENT_CATALOG.md
5. Any documents directly related to the requested work

Repository contents always take precedence over previous conversations.

---

# Standard Repository Output

When operating through ChatGPT, repository changes should always be presented in the following order:

1. Repository Path
2. Commit Message
3. Complete Document

This allows simple copy-and-paste updates into the repository.

When operating directly against a local repository (for example through Codex), files may be updated directly.

---

# Documentation Standards

Every governed document should include:

- title
- document_id
- version
- status
- owner
- author
- last_updated

Additional metadata should be included where appropriate.

---

# Writing Standards

Documentation should be:

- concise
- technically accurate
- executive friendly
- written in Markdown
- internally consistent
- free of unnecessary repetition

Documents should explain both **what** exists and **why** it exists.

---

# Repository Integrity

Before completing work an AI should:

- verify internal links
- update references if files move
- maintain consistent naming
- preserve document identifiers
- avoid duplicate documents

If uncertainty exists, the AI should clearly identify assumptions rather than presenting speculation as fact.

---

# Change Management

Each repository change should be:

- focused
- reviewable
- reversible

Large efforts should be divided into multiple commits whenever practical.

---

# Session Completion

At the conclusion of each work session the AI should:

1. Update SESSION_NOTES.md
2. Update REPOSITORY_STATUS.md
3. Update NEXT_TASK.md
4. Record significant architectural choices in DECISIONS.md
5. Recommend an appropriate commit message

---

# AI Independence

Any future AI system should be able to resume work by reading only the repository.

The repository should contain sufficient documentation that project continuity does not depend upon a specific AI model or an individual chat history.

---

# Long-Term Vision

The AI workspace is intended to become the operational memory of the Executive Intelligence Briefing project.

As the project evolves, additional AI tools may participate in development. These rules are designed to ensure that all contributors—human or AI—produce work that is consistent with the architecture, governance, and long-term vision of EIB.