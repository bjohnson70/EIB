---
Title: ADR-0001 – Public vs. Private Repository Strategy
Status: Accepted
Version: Foundation (v0.1)
Date: 2026-07-21
Author: EIB Project
---

# ADR-0001 – Public vs. Private Repository Strategy

## Status

Accepted

---

# Context

The Executive Intelligence Briefing (EIB) has two distinct objectives:

1. Capture and organize personal knowledge to support better decision-making.
2. Share reusable methods, templates, and guidance that can benefit others.

These objectives require different approaches to information management. Personal knowledge often contains confidential or sensitive information, while reusable knowledge should be openly shareable.

Attempting to maintain both objectives within a single repository increases complexity and creates unnecessary privacy risks.

---

# Decision

The EIB shall be maintained as two complementary repositories:

- **Public Repository**
- **Private Repository**

Each repository has a distinct purpose while reinforcing the other.

---

## Public Repository

### Purpose

Provide reusable knowledge that anyone can adopt.

### Contents

- Architecture
- Governance
- Templates
- Prompt Library
- Playbooks
- Setup Guides
- Documentation
- Examples
- Sample (fictional) data
- Architecture Decision Records (ADRs)

The Public Repository **must never contain personal, confidential, or restricted information.**

---

## Private Repository

### Purpose

Capture individualized knowledge and implementations.

### Contents

- Personal knowledge
- Family information
- Health records
- Retirement planning
- Financial planning
- Work projects
- Executive Intelligence Briefings
- Reports
- Personalized implementations of Public templates

The Private Repository **may contain confidential or sensitive information** and should be protected appropriately.

---

# Relationship

The Public Repository defines reusable structure.

The Private Repository applies that structure to real-world needs.

Whenever reusable improvements are discovered while working in the Private Repository, they should be evaluated for promotion into the Public Repository after all personal or confidential information has been removed.

This creates a continuous improvement cycle:

```text
Private Experience
        ↓
Generalize
        ↓
Remove Sensitive Information
        ↓
Improve Public Repository
        ↓
Future Users Benefit
```

---

# Benefits

This strategy provides:

- Strong protection of personal information.
- Reusable content for others.
- Clear separation of responsibilities.
- Easier long-term maintenance.
- Continuous improvement of public resources.
- Reduced duplication of effort.

---

# Trade-offs

Maintaining two repositories introduces additional work:

- Both repositories require maintenance.
- Reusable improvements must be intentionally promoted.
- Some information may exist in both repositories in different forms.

These trade-offs are acceptable because they preserve privacy while maximizing reuse.

---

# Alternatives Considered

## Single Repository

**Rejected**

Reason:

Combining public and private information creates unnecessary privacy risks and makes publication difficult.

---

## Branch-Based Separation

**Rejected**

Reason:

Git branches are not intended to serve as privacy boundaries and increase the risk of accidentally publishing confidential information.

---

## Manual Redaction Before Publication

**Rejected**

Reason:

Repeated manual redaction is error-prone, time-consuming, and difficult to sustain over time.

---

# Success Criteria

This decision is successful when:

- Personal information remains protected.
- Public knowledge continues to grow.
- Reusable templates become increasingly valuable.
- Private work regularly improves the Public Repository.
- Future contributors immediately understand the purpose of each repository.

---

# Related Documents

- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md
- MANIFESTO.md
- README.md

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.