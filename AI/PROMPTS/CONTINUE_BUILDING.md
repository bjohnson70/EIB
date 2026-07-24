---
title: Continue Building EIB
document_id: AI-PROMPT-001
version: 1.0
status: Approved
owner: BSJ
author: BSJ & ChatGPT
last_updated: 2026-07-24
depends_on:
  - AI/AI_RULES.md
  - AI/NEXT_TASK.md
  - AI/REPOSITORY_STATUS.md
---

# Continue Building the Executive Intelligence Briefing (EIB)

## Purpose

This prompt provides a standard operating procedure for any AI system continuing work on the Executive Intelligence Briefing (EIB) repository.

Its goal is to ensure that every work session begins with an understanding of the current repository state rather than relying on prior chat history.

---

# Startup Procedure

Before making any changes:

1. Read `AI/README.md`.
2. Read `AI/AI_RULES.md`.
3. Read `AI/NEXT_TASK.md`.
4. Read `AI/REPOSITORY_STATUS.md`.
5. Read `AI/DECISIONS.md`.
6. Read the documents directly related to the active task.
7. Review `DOCUMENT_CATALOG.md` if repository structure may be affected.

Do not assume previous chat conversations accurately reflect the current repository.

The repository is the authoritative source of truth.

---

# Execute the Active Task

Complete the work identified in `AI/NEXT_TASK.md`.

When performing work:

- Preserve the existing repository architecture.
- Follow established naming conventions.
- Maintain document metadata.
- Preserve document identifiers.
- Keep internal links accurate.
- Avoid creating duplicate documentation.

If uncertainty exists, document assumptions rather than presenting speculation as fact.

---

# Before Finishing

When the assigned work is complete:

1. Update any affected documents.
2. Update `DOCUMENT_CATALOG.md` if new documents were added.
3. Update `AI/REPOSITORY_STATUS.md`.
4. Record completed work in `AI/SESSION_NOTES.md`.
5. Record important architectural choices in `AI/DECISIONS.md`.
6. Update `AI/NEXT_TASK.md` with the next highest-priority task.
7. Recommend a concise Conventional Commit message.

---

# Guiding Principles

The repository should always be left in a better state than it was found.

Changes should be:

- Accurate
- Reviewable
- Well documented
- Consistent
- Traceable

Favor incremental improvements over large, difficult-to-review changes.

---

# Long-Term Objective

The Executive Intelligence Briefing repository should become self-describing.

Any future AI or human contributor should be able to clone the repository, read the AI workspace, and immediately understand:

- The project's purpose
- The current state
- The next priority
- The reasoning behind past decisions
- How to continue development

Project continuity should never depend on a specific AI model or an individual chat conversation.