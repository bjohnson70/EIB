# EIB Repository Structure Migration Plan

## 1. Purpose

This document defines the planned migration of the Executive Intelligence Briefing (EIB) repository from legacy directory conventions to shared repository standards established by the Common Operation Guide (COG).

The migration is intended to improve consistency, portability, contributor usability, navigation, maintainability, and reuse of shared standards.

This document defines a migration plan only. It does not authorize or perform directory renaming by itself.

---

## 2. Governing Standard

EIB follows reusable development and repository standards maintained in COG.

The governing naming standard is `COG/standards/NAMING_STANDARD.md`.

Functional repository directories SHOULD use lowercase names by default.

> Define the convention once in COG. Reference it everywhere else.

EIB SHOULD reference COG standards rather than independently maintaining competing cross-project conventions.

---

## 3. Background

EIB predates the mature COG cross-project standards repository.

Legacy functional directories include `AI/`, `ARCHITECTURE/`, `CONFIG/`, `CONNECTORS/`, `DATA/`, `DEVELOPMENT/`, `DOCUMENTATION/`, and `IMPLEMENTATION/`.

Later development introduced lowercase structures such as `docs/`.

COG provides the common standard for resolving these inconsistencies.

---

## 4. Migration Principles

EIB will migrate incrementally rather than through a single disruptive restructuring.

1. Do not create additional naming inconsistencies.
2. New functional directories SHOULD follow COG standards.
3. Existing directories SHOULD be migrated in small, reviewable changes.
4. References to existing paths MUST be identified before renaming.
5. Links, scripts, configuration, workflows, and documentation MUST be updated when affected.
6. Repository functionality SHOULD be verified after each migration.
7. Changes SHOULD be independently reversible when practical.
8. Content SHOULD NOT be reorganized solely for cosmetic reasons.
9. Functional restructuring and naming migration SHOULD be separate decisions when practical.

---

## 5. Proposed Directory Mapping

| Legacy | Proposed | Status |
|---|---|---|
| `AI/` | `ai/` | Planned |
| `ARCHITECTURE/` | `architecture/` | Planned |
| `CONFIG/` | `config/` | Planned |
| `CONNECTORS/` | `connectors/` | Planned |
| `DATA/` | `data/` | Planned |
| `DEVELOPMENT/` | `development/` | Planned |
| `DOCUMENTATION/` | `docs/` | Planned |
| `IMPLEMENTATION/` | `implementation/` | Planned |

Additional directories SHALL be reviewed before migration.

A directory SHALL NOT be renamed simply because it is uppercase. Its purpose, contents, dependencies, and relationship to the target architecture SHOULD be understood first.

---

## 6. Documentation Directory

EIB will use `docs/` as the preferred location for general project documentation.

The legacy `DOCUMENTATION/` directory SHOULD eventually be evaluated for migration into `docs/`.

Before migration:

- Inventory its files.
- Identify internal and external path references.
- Identify links from root documents.
- Determine whether content is obsolete or duplicated.
- Move content through controlled commits.
- Verify links afterward.

The simultaneous existence of `DOCUMENTATION/` and `docs/` is a temporary migration state.

Conventional root documents may retain established names such as `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `LICENSE`.

---

## 7. Case-Only Rename Risk

Case-only renames require care because Windows and some macOS filesystems may be case-insensitive.

For example, migration from `ARCHITECTURE/` to `architecture/` may require an intermediate name such as `architecture-temp/`.

The exact procedure SHOULD be documented before case-only directory migrations.

---

## 8. Migration Sequence

### Phase 1 — Standards

- Establish shared standards in COG.
- Reference them from EIB.
- Maintain this migration plan.

### Phase 2 — Inventory

- Inventory directories and files.
- Identify path references.
- Identify scripts, configuration, documentation, and workflow dependencies.

### Phase 3 — Low-Risk Migration

Begin with directories having few dependencies and easily verifiable content.

Each migration SHOULD use a separate commit where practical.

### Phase 4 — Functional Migration

Migrate configuration, connectors, data processing, automation, application logic, and workflows with appropriate dependency testing.

### Phase 5 — Verification

Verify links, navigation, configuration, scripts, workflows, development tooling, and public clone usability.

### Phase 6 — Cleanup

Remove obsolete migration artifacts, update repository maps and contributor documentation, record decisions, and mark migration activities complete.

---

## 9. Public and Private Architecture

EIB is intended to support an open-source implementation model.

The public EIB repository SHOULD remain organization-agnostic.

Public content may include:

- Framework architecture
- Collectors and connectors
- Public intelligence sources
- Generic configuration
- Data schemas
- Processing and risk-assessment logic
- Briefing templates
- Documentation
- Non-sensitive sample data

Organization-specific information SHOULD remain outside the public layer.

Private information may include:

- Asset and application inventories
- Internal system names
- Exposure information
- Security findings
- Vulnerability dispositions
- Owners and ticket numbers
- Internal contacts
- Non-public evidence
- Internal remediation information
- Organization-specific executive commentary

This separation allows organizations to adopt EIB while retaining private operational context.

---

## 10. Applicability and Human Validation

Public intelligence identifies potential risk but cannot definitively establish whether a technology exists within a specific adopter's environment.

EIB SHOULD support a human-in-the-loop cybersecurity disposition model.

Public intelligence may identify vulnerability, vendor, product, severity, CVSS, exploitation status, CISA KEV status, patch availability, mitigation availability, and public risk priority.

An adopter's private process may determine:

- Whether the technology exists
- Whether a vulnerable configuration exists
- Whether an asset is exposed
- Supporting evidence
- Human validator
- Required remediation
- Closure status

Absence from an approved software inventory alone SHALL NOT automatically establish that a vulnerability is not applicable.

Applicability may require evaluation of approved and unapproved software, legacy systems, shadow IT, embedded components, third parties, cloud services, appliances, development dependencies, and other organizational evidence.

---

## 11. Cyber Intelligence Persistence Architecture

EIB must maintain durable records for both intelligence sources and disposition decisions.

These records must not depend solely on conversational memory, individual analyst knowledge, or previous briefing output.

> Public intelligence establishes risk. Private organizational evidence establishes applicability.

### 11.1 Cyber Intelligence Source Registry

EIB SHOULD maintain a structured Cyber Intelligence Source Registry.

A source record should support:

- Source name and organization
- URL
- Category
- Authority level
- Collection method
- Research purpose
- Update frequency
- Enabled status
- Validation requirements
- Notes

Possible categories include government, vendor, vulnerability research, threat intelligence, cybersecurity journalism, aggregation, podcast, email, RSS/Atom, API, and other analyst resources.

Inclusion in the registry does not imply equal evidentiary weight.

### 11.2 Source Authority Hierarchy

#### Tier 1 — Authoritative / Primary

Examples include CISA, the CISA Known Exploited Vulnerabilities Catalog, NIST National Vulnerability Database, Microsoft Security Response Center, Microsoft Security Update Guide, CERT/CC, and vendor security advisories.

Tier 1 sources SHOULD normally establish affected products, CVEs, severity, CVSS, exploitation status, patches, mitigations, and affected versions.

#### Tier 2 — Technical Research / Threat Intelligence

Examples include Microsoft Threat Intelligence, Palo Alto Networks threat research, Cisco Talos, Google Project Zero, Tenable Research, and SANS Internet Storm Center.

These sources provide technical analysis, exploitation context, threat-actor information, indicators, and operational insight.

#### Tier 3 — Cybersecurity Journalism / Discovery

Examples include KrebsOnSecurity, BleepingComputer, The Hacker News, and InfoSec Industry.

These sources support discovery and context.

Actionable findings SHOULD be validated against Tier 1 or appropriate Tier 2 sources whenever practical.

#### Tier 4 — Analyst Awareness

Examples include Cybersecurity Headlines, CyberWire Daily, Hacking Humans, Defense in Depth, Cybersecurity Today, SC Daily Cyber Threat Brief, Hacker News Recap, PAN-CAST, Threat Vector, email subscriptions, and messaging channels.

These sources support situational awareness and discovery but SHOULD NOT normally be the sole authoritative basis for vulnerability disposition.

### 11.3 Personal Resource Portfolio

An adopter may maintain a private Personal Resource Portfolio containing subscriptions, podcasts, websites, messaging channels, newsletters, vendor notifications, and professional communities.

Personal preferences are adopter-specific and SHOULD NOT be embedded in the public EIB repository.

Public EIB MAY provide a reusable schema or template for maintaining such information privately.

---

## 12. Cyber Intelligence Disposition & Evidence Register

EIB SHALL support a durable Cyber Intelligence Disposition & Evidence Register.

The register records organizational applicability decisions resulting from evaluation of public cybersecurity intelligence.

A record should support:

- CVE or intelligence identifier
- Vendor and product
- Intelligence source
- Date identified
- Severity
- Exploitation status
- CISA KEV status
- Organizational applicability
- Exposure status
- Inventory source
- Human validation requirement
- Human validator and validation date
- Evidence
- Internal owner
- Disposition
- Closure date
- Briefing suppression status
- Reopen criteria
- Internal notes

Example dispositions include `NEW`, `REVIEW_REQUIRED`, `APPLICABLE`, `NOT_APPLICABLE`, `MITIGATED`, `REMEDIATED`, `CLOSED`, and `MONITOR`.

---

## 13. Briefing Suppression

The disposition register SHOULD be consulted before previously evaluated intelligence is included in a new briefing.

A record with `Disposition: NOT_APPLICABLE`, `Status: CLOSED`, and `Briefing: SUPPRESS` should normally be excluded from subsequent routine briefings.

A closed item may return when materially new intelligence changes its applicability.

Examples include:

- Newly discovered affected technology
- Expanded affected-product scope
- New exploitation method
- Changed organizational configuration
- New inventory evidence
- Material vendor revision
- Evidence that the previous determination was incorrect

This prevents repeatedly presenting resolved intelligence to executive leadership while preserving the ability to reopen a determination.

---

## 14. Public and Private Persistence

The public EIB repository SHOULD contain:

- Source registry schema
- Generic public source definitions
- Authority classifications
- Collection configuration
- Disposition register schema
- Disposition workflow
- Suppression logic
- Generic examples
- Documentation

The public repository SHALL NOT contain adopter-specific organizational security evidence.

Private adopter storage may contain:

- Applicability decisions
- Technology inventory
- Exposure information
- Human validation results
- Evidence
- Validators
- System owners
- Tickets
- Remediation status
- Closure decisions
- Internal notes
- Personal resource preferences

Private storage technology is implementation-dependent and may include a private Git repository, protected database, SharePoint, security operations platform, vulnerability management platform, or another protected organizational data store.

Public EIB SHOULD NOT require a specific private storage technology.

---

## 15. Cyber Intelligence Processing Model

The EIB briefing pipeline should ultimately support the following sequence:

Public Intelligence Sources → Cyber Intelligence Source Registry → Collectors / Research → Normalize and Deduplicate → Authoritative Validation → Generic Risk Assessment → Private Disposition Register Check → Organizational Applicability → Human Validation When Required → Disposition → Briefing Suppression / Escalation → Executive Intelligence Briefing.

This architecture allows EIB to remain organization-agnostic while enabling adopters to preserve organizational knowledge and avoid repeatedly evaluating resolved intelligence.

---

## 16. CISA RSS Collector Dependency

The planned CISA RSS intelligence collector SHALL follow the repository structure established through this migration.

The collector SHOULD NOT introduce new legacy uppercase directories.

Before implementation:

1. Confirm the appropriate EIB directory architecture.
2. Determine the standards-compliant collector location.
3. Define public feed configuration.
4. Define normalized public intelligence records.
5. Preserve organizational applicability outside the public collector.
6. Document behavior and configuration.
7. Support additional RSS or Atom sources.
8. Consult the Cyber Intelligence Source Registry.
9. Support evaluation against a private Disposition & Evidence Register before briefing publication.

CISA may be the first configured source, but the collector SHOULD be a reusable RSS/Atom capability rather than hard-coded exclusively to CISA.

---

## 17. Migration Tracking

Directory migrations SHOULD be tracked as discrete changes.

For each migration record:

- Original path
- New path
- Date
- Commit
- References updated
- Verification performed
- Remaining issues

This document MAY be updated as migration progresses.

---

## 18. Decision Status

**Status:** Approved migration direction

**Implementation:** Incremental

**Governing Standard:** COG Naming Standard

**Primary Objective:** Align EIB repository structure with shared COG standards without unnecessary disruption.

EIB SHALL provide reusable public mechanisms for intelligence-source management and disposition processing while keeping adopter-specific evidence outside the public repository.

---

## 19. Guiding Principles

> COG defines how projects are built. EIB defines what the Executive Intelligence Briefing does.

> Public intelligence establishes risk. Private organizational evidence establishes applicability.

Persistent intelligence records should ensure that important organizational knowledge survives individual briefings, conversations, tools, and analysts.