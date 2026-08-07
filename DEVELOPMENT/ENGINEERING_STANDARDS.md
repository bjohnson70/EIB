---
title: Engineering Standards
document_id: DEV-001
version: 1.0
status: Active
owner: BSJ
last_updated: 2026-08-07
---

# Executive Intelligence Briefing (EIB)

# Engineering Standards

## Purpose

This document defines the engineering standards for executable software, automation, validation tools, and AI-assisted development within the Executive Intelligence Briefing (EIB) repository.

Its purpose is to ensure that code remains understandable, testable, maintainable, portable, and safe for both human and AI contributors.

---

# Core Principles

Engineering work should favor:

- Clarity over cleverness.
- Small changes over large uncontrolled changes.
- Reuse over duplication.
- Verification over assumption.
- Portability over environment-specific behavior.
- Explicit behavior over hidden behavior.
- Simple designs before complex frameworks.
- Automated validation where practical.

---

# Repository as Source of Truth

The repository is the authoritative development source.

Before making changes, contributors should inspect:

- Existing architecture.
- Existing implementation specifications.
- Existing code.
- Repository standards.
- Applicable ADRs.
- Current Git status.

Historical chat context may provide useful background but should not override current repository content.

---

# Language Standards

Python is the preferred language for repository validation and automation utilities unless another language is clearly better suited to the task.

Python code should target a currently supported Python 3 release.

---

# Python Style

Python code should generally follow:

- PEP 8 conventions.
- Descriptive variable names.
- Small functions with clear responsibilities.
- Type hints where they improve clarity.
- Docstrings for public functions and modules.
- Standard library dependencies when practical.

Avoid unnecessary dependencies.

---

# File Naming

Python source files should use lowercase snake_case.

Examples:

```text
repository_health.py
validate_metadata.py
validate_links.py
```