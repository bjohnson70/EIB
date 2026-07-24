---
title: AI Workspace
document_id: AI-000
version: 1.0
status: Approved
owner: BSJ
author: BSJ & ChatGPT
last_updated: 2026-07-24
---

# Executive Intelligence Briefing (EIB)
# AI Workspace

## Purpose

The AI directory serves as the operational workspace for AI-assisted development of the Executive Intelligence Briefing (EIB) repository.

Rather than storing project state inside a chat conversation, the repository itself becomes the persistent memory shared between ChatGPT, Codex, GitHub, GitSync, and future AI assistants.

This allows work to continue seamlessly across desktop, tablet, and mobile devices.

---

# Design Principles

The AI workspace shall be:

- Repository-first
- Human-readable
- AI-readable
- Version controlled
- Portable
- Platform independent

All files are ordinary Markdown documents that can be edited with any text editor.

---

# Workspace Contents

| File | Purpose |
|------|---------|
| `AI_RULES.md` | Defines the operating rules for AI contributors. |
| `REPOSITORY_STATUS.md` | Summarizes repository completion and health. |
| `NEXT_TASK.md` | Identifies the single highest-priority task. |
| `SESSION_NOTES.md` | Records the outcome of each work session. |
| `BACKLOG.md` | Tracks future work and enhancement ideas. |
| `DECISIONS.md` | Captures important architectural decisions not yet promoted to formal ADRs. |
| `PROMPTS/` | Reusable prompts for ChatGPT, Codex, and future AI tools. |

---

# Workflow

Typical workflow:

1. Open the repository.
2. Read `AI/NEXT_TASK.md`.
3. Review `AI/REPOSITORY_STATUS.md`.
4. Complete the assigned work.
5. Update affected documentation.
6. Update the AI workspace files.
7. Commit changes.
8. Synchronize using GitSync or Git.

---

# Guiding Principle

The repository—not the chat session—is the long-term memory of the project.

Any AI capable of reading the repository should be able to understand the project's current state and continue development with minimal additional context.

---

# Success Criteria

The AI Workspace succeeds when:

- Project status is always visible from the repository.
- AI tools can resume work without lengthy explanations.
- Human contributors can quickly understand current priorities.
- Repository knowledge survives across devices, AI models, and work sessions.