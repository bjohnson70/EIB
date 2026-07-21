---
Title: ADR-0003 – Document Lifecycle
Status: Accepted
Version: Foundation (v0.1)
Date: 2026-07-21
Author: EIB Project
---

# ADR-0003 – Document Lifecycle

## Status

Accepted

---

# Context

Knowledge rarely begins in its final form.

Ideas become notes. Notes become drafts. Drafts become templates. Templates become personalized implementations. Valuable implementations become reusable guidance.

Without a defined lifecycle, documents become difficult to maintain, duplicate effort increases, and outdated information is mistaken for authoritative guidance.

EIB requires a consistent lifecycle for all significant documents.

---

# Decision

The EIB adopts the following document lifecycle:

```text
Idea
   ↓
Draft
   ↓
Template
   ↓
Personalized
   ↓
Published
   ↓
Maintained
   ↓
Archived (if necessary)
```

Not every document must pass through every stage, but every significant document should have a clearly understood status.

---

## Lifecycle Stages

### Idea

A concept, observation, or problem statement.

Purpose:

Capture information before it is forgotten.

---

### Draft

An incomplete working document.

Drafts are expected to evolve and may contain unresolved questions.

---

### Template

A generalized, reusable document.

Templates should not contain personal or confidential information.

Templates normally belong in the Public Repository.

---

### Personalized

A template customized for an individual, organization, or project.

Personalized documents normally belong in the Private Repository.

---

### Published

A document approved for operational use or public distribution.

Publication does not imply the document is permanent.

---

### Maintained

A published document that is periodically reviewed and improved.

Maintenance includes corrections, enhancements, and updates.

---

### Archived

Documents no longer actively maintained but retained for historical reference.

Archived documents should be clearly marked.

---

# Promotion Process

Whenever a Personalized document contains reusable knowledge:

```text
Personalized Document
        ↓
Identify Reusable Content
        ↓
Remove Sensitive Information
        ↓
Generalize
        ↓
Create or Improve Template
        ↓
Publish to Public Repository
```

---

# Benefits

The lifecycle:

- Makes document maturity obvious.
- Encourages reusable templates.
- Prevents duplication.
- Supports continuous improvement.
- Preserves institutional knowledge.

---

# Consequences

Positive:

- Better organization.
- Improved reuse.
- Easier maintenance.
- Clear document status.
- Simpler onboarding for future contributors.

Trade-offs:

- Requires occasional review.
- Some documents may move through stages more than once.

These trade-offs are acceptable because they improve long-term maintainability.

---

# Success Criteria

This decision is successful when:

- Document status is clear.
- Reusable knowledge is promoted to the Public Repository.
- Outdated information is archived instead of deleted.
- Contributors understand how documents evolve over time.

---

# Related Documents

- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md
- ADR-0001 – Public vs. Private Repository Strategy
- ADR-0002 – Knowledge vs. Intelligence

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.