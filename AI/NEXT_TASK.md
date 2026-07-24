---
title: Next Task
document_id: AI-002
version: 1.0
status: Approved
owner: BSJ
author: BSJ & ChatGPT
last_updated: 2026-07-24
depends_on:
  - AI/README.md
  - AI/AI_RULES.md
---

# Next Task

## Purpose

This document identifies the **single highest-priority task** for the Executive Intelligence Briefing (EIB) repository.

It serves as the primary handoff mechanism between work sessions and allows any AI or human contributor to immediately determine what should be worked on next.

Only one task should be marked as Active.

---

# Current Status

**State:** Active

---

# Current Task

## Complete the AI Collaboration Workspace

Continue building the AI collaboration subsystem.

### Remaining Documents

- AI/REPOSITORY_STATUS.md
- AI/SESSION_NOTES.md
- AI/BACKLOG.md
- AI/DECISIONS.md
- AI/PROMPTS/CONTINUE_BUILDING.md

---

# Definition of Done

This task is complete when:

- All AI workspace documents exist.
- Cross-references between AI documents have been verified.
- The AI subsystem is documented in `DOCUMENT_CATALOG.md`.
- The repository can be resumed by a new AI using only the contents of the repository.

---

# Next Planned Milestone

After completion of the AI workspace:

## Roadmap

Create:

`ROADMAP/IMPLEMENTATION_PLAN.md`

followed by:

- ROADMAP/RELEASE_PLAN.md
- ROADMAP/FEATURE_BACKLOG.md
- ROADMAP/TECHNICAL_DEBT.md

---

# Rules

When the current task is completed:

1. Replace this task with the next highest-priority task.
2. Record the completed work in `AI/SESSION_NOTES.md`.
3. Update `AI/REPOSITORY_STATUS.md`.
4. Move future ideas to `AI/BACKLOG.md`.
5. Record significant architectural decisions in `AI/DECISIONS.md`.

This document should always answer one question:

> **"If I have time to work on EIB right now, what should I do first?"**