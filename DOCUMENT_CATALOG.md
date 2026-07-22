---
title: Document Catalog
document_id: GOV-005
version: 1.2
status: Accepted
review_id: AR-0011
review_status: Accepted
governance_framework: 1.2
repository_release: Governance Framework v1.2
owner: Bryan Johnson
role: Product Owner
steward: ChatGPT
steward_role: Chief Architect
last_reviewed: 2026-07-22
next_review: TBD
---

# Document Catalog

## Purpose

The Document Catalog is the authoritative inventory of all governed documents within the Executive Intelligence Briefing (EIB) repository.

It serves as the repository's configuration management database (CMDB) for governance documentation by tracking ownership, review history, versions, status, and relationships between documents.

---

# Governance Lifecycle

Every governed document progresses through the following lifecycle:

- Draft
- Under Review
- Accepted
- Superseded
- Archived

---

# Governed Documents

| GOV ID | Review ID | Document | Location | Version | Status | Last Review |
|---------|-----------|----------|----------|---------|---------|-------------|
| GOV-001 | AR-0006 | Repository Architecture | Architecture/ARCHITECTURE.md | 1.x | Accepted | 2026-07-22 |
| GOV-002 | AR-0007 | Repository Governance | Architecture/GOVERNANCE.md | 1.0 | Accepted | 2026-07-22 |
| GOV-003 | AR-0010 | Architecture Review Register | REVIEW_REGISTER.md | 1.2 | Accepted | 2026-07-22 |
| GOV-004 | AR-0008 | Repository Workflow | REPOSITORY_WORKFLOW.md | 1.0 | Accepted | 2026-07-22 |
| GOV-005 | AR-0011 | Document Catalog | DOCUMENT_CATALOG.md | 1.2 | Accepted | 2026-07-22 |

---

# Core Repository Documents

| Document | Governance Status | Purpose |
|----------|-------------------|---------|
| README.md | Reviewed | Repository introduction |
| MANIFESTO.md | Reviewed | Repository vision |
| CONSTITUTION.md | Reviewed | Governing principles |
| ROADMAP.md | Reviewed | Repository roadmap |
| CONTRIBUTING.md | Reviewed | Contributor guidance |
| STATUS.md | Pending AR-0014 | Executive dashboard |

---

# Architecture Documents

| Document | Purpose |
|----------|---------|
| Architecture/ARCHITECTURE.md | Repository architecture |
| Architecture/GOVERNANCE.md | Governance framework |
| Architecture/ADR/ADR-0001.md | ADR Framework *(planned)* |

---

# Governance Documents

| Document | Purpose |
|----------|---------|
| REVIEW_REGISTER.md | Architecture Review audit trail |
| REPOSITORY_WORKFLOW.md | Repository operating procedures |
| DOCUMENT_CATALOG.md | Governance inventory |

---

# Planned Repository Artifacts

| Document | Purpose |
|----------|---------|
| CHANGELOG.md | Repository history |
| RELEASE_NOTES.md | Release summaries |
| STYLE_GUIDE.md | Documentation standards |
| GLOSSARY.md | Repository terminology |
| Architecture/ADR Index | ADR inventory |

---

# Governance Standards

Every governed document shall:

- Have a unique GOV identifier.
- Have a unique Architecture Review identifier.
- Follow the governance metadata standard.
- Identify the Product Owner.
- Identify the Chief Architect.
- Be verified after every GitHub commit.
- Be listed in this catalog.

---

# Governance Metadata Standard

Every governed document should include the following metadata:

```yaml
document_id:
title:
version:
status:

review_id:
review_status:

governance_framework:
repository_release:

owner:
role:

steward:
steward_role:

last_reviewed:
next_review:
```

---

# Repository Statistics

Governed Documents

**5**

Architecture Documents

**2**

Governance Documents

**3**

Architecture Reviews

**10**

Governance Framework

**Version 1.2**

Repository Maturity

**Governed Foundation**

---

# Repository Relationships

```text
CONSTITUTION
        │
        ▼
Architecture/GOVERNANCE
        │
        ▼
REPOSITORY_WORKFLOW
        │
        ▼
REVIEW_REGISTER
        │
        ▼
DOCUMENT_CATALOG
        │
        ▼
STATUS
```

---

# Related Documents

- CONSTITUTION.md
- Architecture/ARCHITECTURE.md
- Architecture/GOVERNANCE.md
- REPOSITORY_WORKFLOW.md
- REVIEW_REGISTER.md
- STATUS.md