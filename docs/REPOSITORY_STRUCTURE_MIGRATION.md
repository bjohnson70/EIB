# EIB Repository Structure Migration Plan

## 1. Purpose

This document defines the planned migration of the Executive Intelligence Briefing (EIB) repository from legacy directory conventions to the shared repository standards established by the Common Operation Guide (COG).

The migration is intended to improve consistency, portability, contributor usability, navigation, maintainability, and reuse of shared standards.

This document defines a migration plan only. It does not authorize or perform directory renaming by itself.

---

## 2. Governing Standard

EIB follows reusable development and repository standards maintained in COG.

The governing naming standard is:

`COG/standards/NAMING_STANDARD.md`

Functional repository directories SHOULD use lowercase names by default.

> Define the convention once in COG. Reference it everywhere else.

EIB SHOULD reference COG standards rather than independently maintaining competing cross-project conventions.

---

## 3. Background

EIB predates the mature COG cross-project standards repository. Many EIB functional directories therefore use uppercase names, including:

```text
AI/
ARCHITECTURE/
CONFIG/
CONNECTORS/
DATA/
DEVELOPMENT/
DOCUMENTATION/
IMPLEMENTATION/