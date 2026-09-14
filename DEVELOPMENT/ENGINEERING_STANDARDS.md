---
title: Engineering Standards
document_id: DEV-002
version: 1.0
lifecycle_status: Active
owner: BSJ
last_updated: 2026-09-13
---

# Executive Intelligence Briefing (EIB)

# Engineering Standards

## Purpose

This document defines the engineering standards for executable software, automation, validation tools, and AI-assisted development within the Executive Intelligence Briefing (EIB) repository.

Its purpose is to ensure that code remains understandable, testable, maintainable, portable, and safe for both human and AI contributors.

---

# Core Principles

Engineering work should follow the reusable repository, naming, workflow, and validation hygiene defined by the pinned COG authorities identified in the [COG Adoption Profile](../DOCUMENTATION/COG_ADOPTION_PROFILE.md), especially the COG Repository Standard and GitHub Development Workflow. EIB-specific engineering requirements remain in this document and in the EIB repository standards and workflow.

This document does not duplicate the reusable COG baseline. It governs EIB-specific engineering choices, implementation constraints, quality gates, and AI-assisted development obligations.

---

# Repository as Source of Truth

The repository is the authoritative development source for EIB.

Before making changes, contributors should inspect the current repository state and the relevant EIB architecture, governance, implementation, and documentation requirements. Generic repository inspection, focused-change discipline, and workflow hygiene are governed by the pinned COG standards; EIB-specific engineering, model, schema, security, validation, human approval boundaries, and AI-assisted development boundaries remain defined here.

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