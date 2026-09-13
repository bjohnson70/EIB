---
title: Repository Document Catalog
document_id: GOV-005
version: 2.0
lifecycle_status: Active
owner: BSJ
last_updated: 2026-09-12
---

# Executive Intelligence Briefing (EIB)

# Repository Document Catalog

## Purpose

The Document Catalog is the authoritative inventory of governed documentation within the Executive Intelligence Briefing (EIB) repository.

It serves as the repository's Configuration Management Database (CMDB) for documentation.

Every governed document should appear here exactly once.

---

# Objectives

The Document Catalog exists to:

- Identify every governed document.
- Record document ownership.
- Record document identifiers.
- Record canonical locations.
- Support AI navigation.
- Prevent duplicate documentation.
- Support repository governance.
- Support traceability.

---

# Repository Status

Current Repository Phase:

```text
Repository Modernization
```

Canonical Architecture Directory:

```text
ARCHITECTURE/
```

Legacy Architecture Directory:

```text
Retired
```

---

# Active Controlled Artifact Registry

This is the authoritative registry of active controlled artifacts. Every row
identifies one artifact, its type-appropriate identity field, and its canonical
repository path. Lifecycle and review-state normalization remains a later
reconciliation step.

| Identity | Identity field | Canonical artifact |
|----------|---------------|--------------------|
| ADR-0001 | document_id | ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md |
| ADR-0002 | document_id | ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md |
| ADR-0003 | document_id | ARCHITECTURE/ADR-0003-Document-Lifecycle.md |
| ADR-0004 | document_id | ARCHITECTURE/ADR-0004-Definition-of-Done.md |
| ADR-0005 | document_id | ARCHITECTURE/ADR-0005-Versioning-Strategy.md |
| AI-001 | document_id | AI/AI_RULES.md |
| AI-PROMPT-001 | document_id | AI/PROMPTS/CONTINUE_BUILDING.md |
| ARCH-001 | document_id | ARCHITECTURE/DESIGN_PHILOSOPHY.md |
| ARCH-002 | document_id | ARCHITECTURE/SYSTEM_ARCHITECTURE.md |
| ARCH-003 | document_id | ARCHITECTURE/EDITORIAL_GUIDELINES.md |
| ARCH-004 | document_id | ARCHITECTURE/QUALITY_STANDARDS.md |
| ARCH-005 | document_id | ARCHITECTURE/PRODUCT_VISION.md |
| ARCH-006 | document_id | ARCHITECTURE/INTELLIGENCE_ENGINE.md |
| ARCH-007 | document_id | ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md |
| DEV-001 | document_id | DEVELOPMENT/REPOSITORY_STRUCTURE.md |
| DEV-002 | document_id | DEVELOPMENT/ENGINEERING_STANDARDS.md |
| DEV-003 | document_id | DEVELOPMENT/GITHUB_ACCESS_AND_VERIFICATION.md |
| DEV-004 | document_id | docs/REPOSITORY_STRUCTURE_MIGRATION.md |
| DEV-DEVICE-001 | document_id | DEVELOPMENT/DEVICE_AWARE_WORKFLOW.md |
| ENGINE-001 | component_id | IMPLEMENTATION/PRIORITY_ENGINE.md |
| ENGINE-002 | component_id | IMPLEMENTATION/CORRELATION_ENGINE.md |
| ENGINE-003 | component_id | IMPLEMENTATION/RECOMMENDATION_ENGINE.md |
| ENGINE-004 | component_id | IMPLEMENTATION/CONFIDENCE_ENGINE.md |
| GOV-002 | document_id | ARCHITECTURE/GOVERNANCE.md |
| GOV-003 | document_id | REPOSITORY_CHARTER.md |
| GOV-005 | document_id | DOCUMENT_CATALOG.md |
| GOV-006 | document_id | DOCUMENTATION/REPOSITORY_STANDARDS.md |
| GOV-007 | document_id | DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md |
| GOV-008 | document_id | DOCUMENTATION/REPOSITORY_INVENTORY.md |
| GOV-009 | document_id | REPOSITORY_WORKFLOW.md |
| GOV-010 | document_id | REVIEW_REGISTER.md |
| GOV-013 | document_id | CONTRIBUTING.md |
| GOV-016 | document_id | CONSTITUTION.md |
| GOV-015 | document_id | DOCUMENTATION/COG_ADOPTION_PROFILE.md |
| IA-0001 | document_id | IMPLEMENTATION/IMPLEMENTATION_ARCHITECTURE.md |
| IA-0002 | document_id | IMPLEMENTATION/AGENT_ARCHITECTURE.md |
| IA-0003 | document_id | IMPLEMENTATION/WORKFLOW_ORCHESTRATION.md |
| IA-0004 | document_id | IMPLEMENTATION/INTELLIGENCE_PIPELINE_SPECIFICATION.md |
| IA-0005 | document_id | IMPLEMENTATION/INTELLIGENCE_OBJECT_MODEL.md |
| IA-0006 | document_id | IMPLEMENTATION/BRIEFING_ASSEMBLY_ENGINE.md |
| IA-0007 | document_id | IMPLEMENTATION/KNOWLEDGE_MODEL.md |
| IA-0008 | document_id | IMPLEMENTATION/CONFIGURATION_AND_PROFILE_MODEL.md |
| IA-0009 | document_id | IMPLEMENTATION/EXECUTION_STATE_MODEL.md |
| IA-0010 | document_id | IMPLEMENTATION/OBSERVABILITY_AND_TELEMETRY.md |
| IA-0011 | document_id | IMPLEMENTATION/QUALITY_ASSURANCE_FRAMEWORK.md |
| IA-0012 | document_id | IMPLEMENTATION/TESTING_STRATEGY.md |
| IA-0013 | document_id | IMPLEMENTATION/SOURCE_CONNECTOR_FRAMEWORK.md |
| IA-0014 | document_id | IMPLEMENTATION/DOMAIN_AGENT_SPECIFICATIONS.md |
| IA-0017 | document_id | DEVELOPMENT/CODING_STANDARDS.md |
| IA-0018 | document_id | DEVELOPMENT/API_SPECIFICATION.md |
| IA-0019 | document_id | DEVELOPMENT/PLUGIN_ARCHITECTURE.md |
| IA-0020 | document_id | DEVELOPMENT/VERSIONING_STRATEGY.md |
| IA-0021 | document_id | DATA/STORAGE_ARCHITECTURE.md |
| IA-0022 | document_id | DATA/KNOWLEDGE_GRAPH.md |
| IA-0023 | document_id | DATA/EMBEDDING_STRATEGY.md |
| IA-0024 | document_id | DATA/HISTORICAL_INTELLIGENCE.md |
| IA-0025 | document_id | DATA/RETENTION_POLICY.md |
| IA-0032 | document_id | ROADMAP/MVP_DEFINITION.md |
| IA-0036 | document_id | REFERENCE_ARCHITECTURE.md |
| IMP-014 | document_id | IMPLEMENTATION/PROMPT_ARCHITECTURE.md |
| MODEL-001 | model_id | MODELS/briefing_item.md |
| MODEL-002 | model_id | MODELS/action_item.md |
| MODEL-003 | model_id | MODELS/DOMAIN/email_summary.md |
| MODEL-004 | model_id | MODELS/DOMAIN/calendar_event.md |
| MODEL-005 | model_id | MODELS/DOMAIN/security_alert.md |
| MODEL-006 | model_id | MODELS/DOMAIN/risk.md |
| MODEL-008 | model_id | MODELS/DOMAIN/executive_decision.md |
| MODEL-SCHEMA-001 | document_id | MODELS/SCHEMA/model_schema.md |
| OPS-001 | document_id | OPERATIONS/DEPLOYMENT_ARCHITECTURE.md |
| OPS-002 | document_id | OPERATIONS/SECURITY_MODEL.md |
| OPS-003 | document_id | OPERATIONS/BACKUP_AND_RECOVERY.md |
| OPS-004 | document_id | OPERATIONS/CHANGE_MANAGEMENT.md |
| OPS-005 | document_id | OPERATIONS/SCHEDULING.md |
| PA-0007 | document_id | EXECUTIVE_PRINCIPLES.md |
| PA-003 | document_id | ARCHITECTURE/PRODUCT_ARCHITECTURE.md |
| PA-004 | document_id | ARCHITECTURE/REPORT_SPECIFICATION.md |
| PA-005 | document_id | ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md |
| PA-006 | document_id | ARCHITECTURE/DATA_SOURCE_STRATEGY.md |
| PA-007 | document_id | ARCHITECTURE/SCORING_MODEL.md |
| PA-008 | document_id | ARCHITECTURE/PERSONALIZATION_MODEL.md |
| PM-001 | document_id | ROADMAP.md |
| PRD-0001 | document_id | PRODUCT_REQUIREMENTS.md |
| PROFILE-001 | schema_id | PROFILES/profile_schema.md |
| PROMPT-001 | document_id | PROMPTS/SYSTEM/executive_briefing.md |
| PROMPT-002 | document_id | PROMPTS/WORKFLOWS/run_eib.md |
| PROFILE-002 | document_id | PERSONALITY/executive_balanced.md |
| REQ-001 | document_id | docs/enhancements/2026_0808_EIB_Enhancement_Weather_and_Briefing_Scope.md |
| REQ-002 | document_id | docs/enhancements/2026_0817_EIB_Enhancement_Continuous_Awareness_and_Breaking_Updates.md |
| REQ-003 | document_id | docs/enhancements/2026_0827_EIB_Enhancement_Role_Aware_Executive_Briefing.md |
| REQ-004 | document_id | docs/requirements/EIB_v8_Requirements_Traceability_Checklist.md |
| REQ-005 | document_id | DOCUMENTATION/TRACEABILITY_MATRIX.md |
| ROOT-002 | document_id | VISION.md |
| ROOT-003 | document_id | MANIFESTO.md |
| ROADMAP-002 | document_id | ROADMAP/IMPLEMENTATION_PLAN.md |
| ROADMAP-003 | document_id | ROADMAP/RELEASE_PLAN.md |

## Historical / Decontrolled Identity Registry

These identities remain permanently non-reusable. Recording an identity here
does not make its associated artifact active or controlled.

| Identity | Disposition | Former/current artifact | Reuse |
|----------|-------------|-------------------------|-------|
| AI-000 | Historical / Decontrolled | AI/README.md | No |
| AI-002 | Historical / Decontrolled | AI/NEXT_TASK.md | No |
| AI-003 | Historical / Decontrolled | AI/REPOSITORY_STATUS.md | No |
| AI-004 | Historical / Decontrolled | AI/DECISIONS.md | No |
| AI-005 | Historical / Decontrolled | AI/SESSION_NOTES.md | No |
| AI-006 | Historical / Decontrolled | AI/BACKLOG.md | No |
| ARCH-008 | Historical / Decontrolled | ARCHITECTURE/README.md | No |
| IA-0016 | Historical / Superseded / Permanently Non-Reusable | REPOSITORY_STRUCTURE.md; successor DEV-001 at DEVELOPMENT/REPOSITORY_STRUCTURE.md | No |
| GOV-001 | Historical / Decontrolled | DOCUMENTATION/DECISION_LOG.md | No |
| GOV-011 | Historical / Decontrolled | CHANGELOG.md | No |
| GOV-012 | Historical / Decontrolled | DECISIONS.md | No |
| GOV-014 | Historical / Decontrolled | DOCUMENTATION/REPOSITORY_SCORECARD.md | No |
| MODELS-README-001 | Historical / Decontrolled | MODELS/README.md | No |
| ROOT-001 | Historical / Decontrolled | README.md | No |
| ROADMAP-004 | Historical / Decontrolled | ROADMAP/FEATURE_BACKLOG.md | No |
| ROADMAP-005 | Historical / Decontrolled | ROADMAP/TECHNICAL_DEBT.md | No |
| TESTS-001 | Historical / Decontrolled | TESTS/README.md | No |
| TOOLS-001 | Historical / Decontrolled | TOOLS/README.md | No |

## Reserved Identity Registry

| Identity | Disposition | Artifact | Reuse |
|----------|-------------|----------|-------|
| MODEL-007 | Reserved / Never Assigned | None | No |

## Stale Catalog Errors

| Value | Treatment | Reason |
|-------|-----------|--------|
| ARCH-009 | Stale catalog error; not an identity | Never validly assigned; REFERENCE_ARCHITECTURE.md is IA-0036 |

The active registry is authoritative for current controlled-artifact
registration. The older organizational tables below are navigation material and
must not be interpreted as a second identity or disposition registry.

---

# Root Documents

| Document | ID | Status |
|----------|----|--------|
| README.md | Historical ROOT-001 | Historical / Decontrolled |
| VISION.md | ROOT-002 | Active |
| MANIFESTO.md | ROOT-003 | Active |
| CONSTITUTION.md | GOV-016 | Active |
| PRODUCT_REQUIREMENTS.md | PRD-0001 | Active |
| ROADMAP.md | PM-001 | Active |
| REPOSITORY_CHARTER.md | GOV-003 | Pending Review |
| REPOSITORY_WORKFLOW.md | GOV-009 | Active |
| REVIEW_REGISTER.md | GOV-010 | Active |
| DOCUMENT_CATALOG.md | GOV-005 | Active |
| CHANGELOG.md | Historical GOV-011 | Historical / Decontrolled |
| DECISIONS.md | Historical GOV-012 | Historical / Decontrolled |
| CONTRIBUTING.md | GOV-013 | Pending Review |
| EXECUTIVE_PRINCIPLES.md | PA-0007 | Active |
| REFERENCE_ARCHITECTURE.md | IA-0036 | Pending Review |

---

# Architecture Documents

| Document | ID | Status |
|----------|----|--------|
| README.md | Historical ARCH-008 | Historical / Decontrolled |
| ENTERPRISE_ARCHITECTURE.md | ARCH-007 | Active |
| GOVERNANCE.md | GOV-002 | Active |
| ADR-0001-Public-vs-Private-Repositories.md | ADR-0001 | Active |
| ADR-0002-Knowledge-vs-Intelligence.md | ADR-0002 | Active |
| ADR-0003-Document-Lifecycle.md | ADR-0003 | Active |
| ADR-0004-Definition-of-Done.md | ADR-0004 | Active |
| ADR-0005-Versioning-Strategy.md | ADR-0005 | Active |
| PRODUCT_ARCHITECTURE.md | PA-003 | Active |
| REPORT_SPECIFICATION.md | PA-004 | Active |
| INTELLIGENCE_ARCHITECTURE.md | PA-005 | Active |
| DATA_SOURCE_STRATEGY.md | PA-006 | Active |
| SCORING_MODEL.md | PA-007 | Active |
| PERSONALIZATION_MODEL.md | PA-008 | Active |
| DESIGN_PHILOSOPHY.md | ARCH-001 | Pending Review |
| SYSTEM_ARCHITECTURE.md | ARCH-002 | Pending Review |
| EDITORIAL_GUIDELINES.md | ARCH-003 | Pending Review |
| QUALITY_STANDARDS.md | ARCH-004 | Pending Review |
| PRODUCT_VISION.md | ARCH-005 | Pending Review |
| INTELLIGENCE_ENGINE.md | ARCH-006 | Pending Review |

---

# Documentation

| Document | Status |
|----------|--------|
| REPOSITORY_STANDARDS.md | Active |
| REPOSITORY_MIGRATION_PLAN.md | Active |
| REPOSITORY_INVENTORY.md | Active |
| COG_ADOPTION_PROFILE.md (GOV-015) | Approved |
| DOCUMENT_CATALOG.md | Active |
| DECISION_LOG.md | Historical GOV-001 |
| REPOSITORY_STATUS.md | Pending Review |
| TRACEABILITY_MATRIX.md | Pending Review |
| CHANGELOG.md | Historical / Decontrolled |

---

# Development

| Directory | Status |
|-----------|--------|
| DEVELOPMENT | Planned Review |

---

# Implementation

| Directory | Status |
|-----------|--------|
| IMPLEMENTATION | Planned Review |

---

# Operations

| Directory | Status |
|-----------|--------|
| OPERATIONS | Planned Review |

---

# Data

| Directory | Status |
|-----------|--------|
| DATA | Planned Review |

---

# Models

| Directory | Status |
|-----------|--------|
| MODELS | Planned Review |

---

# Profiles

| Directory | Status |
|-----------|--------|
| PROFILES | Planned Review |

---

# Personality

| Directory | Status |
|-----------|--------|
| PERSONALITY | Planned Review |

---

# Prompts

| Directory | Status |
|-----------|--------|
| PROMPTS | Planned Review |

---

# Workflows

| Directory | Status |
|-----------|--------|
| WORKFLOWS | Planned Review |

---

# AI

| Directory | Status |
|-----------|--------|
| AI | Planned Review |

---

# Connectors

| Directory | Status |
|-----------|--------|
| CONNECTORS | Planned Review |

---

# Configuration

| Directory | Status |
|-----------|--------|
| CONFIG | Planned Review |

---

# Repository Rules

Every governed document shall:

- Have one canonical location.
- Have one document identifier.
- Have one authoritative version.
- Be referenced from this catalog.
- Follow Repository Standards.

---

# Future Automation

The Document Catalog should eventually be generated automatically from repository metadata.

Future validation should verify:

- Missing metadata.
- Duplicate identifiers.
- Broken references.
- Missing documents.
- Orphaned files.
- Incorrect directory placement.

---

# Success Criteria

The Document Catalog succeeds when:

- Every governed document is represented.
- No duplicate authoritative documents exist.
- AI contributors can locate documents without ambiguity.
- Repository structure is self-documenting.
- Repository governance is supported through a single authoritative inventory.

---

# Related Documents

- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
- DOCUMENTATION/REPOSITORY_INVENTORY.md
- REVIEW_REGISTER.md
- ARCHITECTURE/GOVERNANCE.md

---

# Guiding Principle

> If a document is important enough to govern the repository, it is important enough to appear in the Document Catalog.