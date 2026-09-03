# EIB Repository Structure Migration Plan

## 1. Purpose

This document defines the planned migration of the Executive Intelligence
Briefing (EIB) repository from its legacy directory naming conventions to the
shared repository naming standards established by the Common Operation Guide
(COG).

The migration is intended to improve:

- Consistency across EIB and related projects
- Compatibility with common Git and GitHub practices
- Cross-platform portability
- Contributor usability
- Repository navigation
- Long-term maintainability
- Reuse of shared standards across projects

This document defines a migration plan only.

It does not authorize or perform directory renaming by itself.

---

## 2. Governing Standard

EIB follows the reusable development and repository standards maintained in
the Common Operation Guide (COG).

The governing naming standard is:

`COG/standards/NAMING_STANDARD.md`

The COG standard establishes that functional repository directories SHOULD
use lowercase names by default.

The governing principle is:

> Define the convention once in COG. Reference it everywhere else.

EIB SHOULD reference COG standards rather than independently maintaining
competing cross-project naming conventions.

---

## 3. Background

EIB was created before the COG cross-project standards repository was fully
established.

As the project evolved, many EIB functional directories were created using
uppercase names.

Examples include:

```text
AI/
ARCHITECTURE/
CONFIG/
CONNECTORS/
DATA/
DEVELOPMENT/
DOCUMENTATION/
IMPLEMENTATION/