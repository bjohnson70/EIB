---
Title: ADR-0005 – Versioning Strategy
Status: Accepted
Version: Foundation (v0.1)
Date: 2026-07-21
Author: EIB Project
---

# ADR-0005 – Versioning Strategy

## Status

Accepted

---

# Context

The Executive Intelligence Briefing (EIB) is expected to evolve over many years. Users and contributors need a simple, consistent way to understand the maturity of the project and the purpose of each release.

A versioning strategy provides a roadmap for growth while maintaining compatibility and documenting progress.

---

# Decision

EIB will use milestone-based semantic versioning.

Each version will include both:

- A semantic version number.
- A descriptive milestone name.

This approach communicates not only the sequence of releases but also the purpose of each stage.

---

# Initial Release Roadmap

| Version | Milestone | Primary Objective |
|----------|-----------|-------------------|
| v0.1 | Foundation | Architecture and Governance |
| v0.2 | Structure | Repository Organization and Templates |
| v0.3 | Knowledge | Knowledge Capture Framework |
| v0.4 | Intelligence | Executive Intelligence Engine |
| v0.5 | Automation | Automated Briefings and Workflows |
| v1.0 | Public Launch | Stable Public Framework |

---

# Version Definitions

## Major Version

A major version represents a significant milestone or a change that affects the project's overall architecture or public compatibility.

Example:

v1.0 → v2.0

---

## Minor Version

A minor version introduces new capabilities while remaining consistent with the project's architecture.

Example:

v0.3 → v0.4

---

## Patch Version

Patch versions are reserved for corrections, refinements, and documentation improvements that do not significantly change functionality.

Example:

v1.0.0 → v1.0.1

---

# Release Requirements

Each release should include:

- Updated CHANGELOG.md
- Updated ROADMAP.md
- Completed milestones
- Known limitations
- Appropriate Git tag

---

# Benefits

This strategy:

- Makes project maturity obvious.
- Aligns development with milestones.
- Simplifies communication.
- Supports future automation.
- Encourages disciplined releases.

---

# Consequences

Positive:

- Clear project history.
- Predictable release cadence.
- Easier contributor onboarding.
- Better planning.

Trade-offs:

- Milestones require periodic review.
- Version numbers must remain synchronized with documentation.

These trade-offs are acceptable because they improve long-term maintainability.

---

# Success Criteria

This decision is successful when:

- Users understand the maturity of each release.
- Releases have clear objectives.
- Documentation reflects the current version.
- Version history accurately represents project evolution.

---

# Related Documents

- ROADMAP.md
- CHANGELOG.md
- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.