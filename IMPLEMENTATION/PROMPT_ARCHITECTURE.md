---
title: Executive Intelligence Briefing Prompt Architecture
document_id: IA-0004
version: 1.0
status: Approved
owner: Bryan Johnson
author: Bryan Johnson & ChatGPT
last_updated: 2026-07-23
depends_on:
  - IMPLEMENTATION_ARCHITECTURE.md
  - AGENT_ARCHITECTURE.md
  - WORKFLOW_ORCHESTRATION.md
---

# Executive Intelligence Briefing Prompt Architecture

## Purpose

This document defines how prompts are designed, organized, versioned, and executed within the Executive Intelligence Briefing (EIB) platform.

Prompts are treated as software assets—not ad hoc instructions. They are modular, reusable, testable, and independently version controlled.

---

# Design Principles

Prompts shall be:

- Modular
- Single-purpose
- Deterministic
- Explainable
- Version controlled
- Independently testable
- Reusable

---

# Prompt Hierarchy

```
System Prompt

↓

Platform Prompt

↓

Agent Prompt

↓

Task Prompt

↓

Output Template
```

Each layer provides additional context without duplicating responsibilities.

---

# System Prompt

Defines global platform behavior.

Responsibilities include:

- Executive-first philosophy
- Writing standards
- Safety requirements
- Reasoning boundaries
- Global formatting conventions

The System Prompt is shared by every agent.

---

# Platform Prompt

Defines EIB-specific behavior.

Examples include:

- Report objectives
- Executive audience
- Coverage Assurance
- Report Specification
- Executive Principles
- Product terminology

Every agent inherits the Platform Prompt.

---

# Agent Prompt

Each agent owns its own operational prompt.

Examples:

- Cyber Intelligence Agent
- Weather Agent
- California Government Agent
- Editorial Agent
- Quality Assurance Agent

Each prompt contains only information relevant to that agent's responsibilities.

---

# Task Prompt

Task prompts provide execution-specific instructions.

Examples:

- Generate Executive Summary
- Evaluate cybersecurity events
- Produce weather commentary
- Create Action List
- Build Watch List

Task prompts are short-lived and context-specific.

---

# Output Templates

Output formatting shall be separated from reasoning.

Templates define:

- Headings
- Tables
- Lists
- Callouts
- Executive summaries
- Recommendation formatting

Changing presentation should not require modifying reasoning prompts.

---

# Prompt Composition

Each execution constructs prompts dynamically.

Example:

```
System Prompt
+
Platform Prompt
+
Cyber Agent Prompt
+
Today's Intelligence
+
Executive Context
+
Task Prompt
+
Output Template
```

This layered approach minimizes duplication and improves maintainability.

---

# Prompt Responsibilities

Each prompt should define:

- Objective
- Inputs
- Constraints
- Required outputs
- Success criteria
- Failure conditions

Prompts should avoid describing implementation details outside their scope.

---

# Prompt Versioning

Every prompt shall include metadata:

- Prompt ID
- Version
- Author
- Last Updated
- Status
- Related Documents

Changes to prompts should be traceable through version control.

---

# Prompt Testing

Each prompt should be validated for:

- Accuracy
- Completeness
- Consistency
- Hallucination resistance
- Executive readability
- Compliance with Report Specification

Prompt changes should be tested before production use.

---

# Prompt Reuse

Shared logic should exist in common prompts rather than being copied across multiple agents.

Benefits include:

- Easier maintenance
- Reduced inconsistency
- Faster enhancements
- Simpler testing

---

# Context Management

Each prompt should receive only the information required to complete its task.

Excessive context should be avoided to:

- Improve performance
- Reduce ambiguity
- Increase determinism
- Lower execution cost

---

# Prompt Security

Prompts shall never expose:

- Internal reasoning
- Hidden system instructions
- Sensitive executive information
- Authentication details
- Confidential implementation logic

---

# Prompt Quality Standards

Every production prompt should be:

✓ Clear

✓ Concise

✓ Unambiguous

✓ Testable

✓ Maintainable

✓ Explainable

✓ Versioned

---

# Future Enhancements

Future versions may support:

- Automatic prompt optimization
- A/B prompt testing
- Prompt performance metrics
- Domain-specific prompt libraries
- Prompt dependency analysis
- Prompt linting and validation

---

# Guiding Principle

Prompts are executable specifications that encode institutional knowledge. They should be engineered with the same rigor, discipline, testing, and version control applied to software source code.

---

# Related Documents

- IMPLEMENTATION_ARCHITECTURE.md
- AGENT_ARCHITECTURE.md
- WORKFLOW_ORCHESTRATION.md
- ../PRODUCT_REQUIREMENTS.md
- ../Architecture/REPORT_SPECIFICATION.md
- ../EXECUTIVE_PRINCIPLES.md