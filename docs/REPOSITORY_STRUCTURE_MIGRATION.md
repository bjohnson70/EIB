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
```

Later development introduced lowercase directory structures such as:

```text
docs/
```

This resulted in inconsistent directory naming within the same repository.

The creation of COG provides an opportunity to resolve these inconsistencies
using a reusable standard rather than an EIB-specific convention.

---

## 4. Migration Principle

EIB will migrate toward COG standards deliberately rather than through a
single disruptive repository restructuring.

The migration SHALL follow these principles:

1. Do not create additional naming inconsistencies.
2. New functional directories SHOULD follow current COG standards.
3. Existing directories SHOULD be migrated in small, reviewable changes.
4. References to existing paths MUST be identified before a rename.
5. Links, scripts, configuration, workflows, and documentation MUST be
   updated when affected.
6. Repository functionality SHOULD be verified after each migration step.
7. Migration changes SHOULD be independently reversible when practical.
8. Content SHOULD NOT be reorganized solely for cosmetic reasons.
9. Functional restructuring and naming migration SHOULD be treated as
   separate decisions when practical.

---

## 5. Proposed Directory Mapping

The following mappings represent the current planned direction.

They are subject to validation before each migration occurs.

| Legacy Directory | Proposed Directory | Status |
|---|---|---|
| `AI/` | `ai/` | Planned |
| `ARCHITECTURE/` | `architecture/` | Planned |
| `CONFIG/` | `config/` | Planned |
| `CONNECTORS/` | `connectors/` | Planned |
| `DATA/` | `data/` | Planned |
| `DEVELOPMENT/` | `development/` | Planned |
| `DOCUMENTATION/` | `docs/` | Planned |
| `IMPLEMENTATION/` | `implementation/` | Planned |

Additional EIB directories SHALL be reviewed before migration.

A directory SHALL NOT be renamed simply because it is uppercase.

Its purpose, contents, dependencies, and relationship to the target repository
architecture SHOULD be understood first.

---

## 6. Documentation Directory

EIB will use:

```text
docs/
```

as the preferred location for general project documentation.

This follows the COG lowercase directory standard and common open-source
repository conventions.

The legacy:

```text
DOCUMENTATION/
```

directory SHOULD eventually be evaluated for migration into `docs/`.

Before migration:

- Inventory all files in `DOCUMENTATION/`
- Identify internal links referencing `DOCUMENTATION/`
- Identify links from root-level documents
- Identify external references where practical
- Determine whether any content is obsolete or duplicated
- Move content in controlled commits
- Verify links after migration

The existence of both `DOCUMENTATION/` and `docs/` SHOULD be considered a
temporary migration state rather than a permanent repository design.

---

## 7. Root-Level Files

This migration does not automatically require changes to established
root-level repository documents.

Conventional root documents may retain established names such as:

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
LICENSE
```

Other EIB-specific root documents SHOULD be evaluated separately based on
their function and discoverability.

Directory migration SHOULD NOT be used as justification for unrelated
root-document restructuring.

---

## 8. Case-Only Rename Risk

Directory names that differ only by capitalization require additional care.

For example:

```text
ARCHITECTURE/
```

to:

```text
architecture/
```

may behave differently depending on the operating system and local filesystem.

Windows and some macOS configurations may use case-insensitive filesystems,
while Linux commonly uses case-sensitive filesystems.

For case-only migrations, contributors SHOULD use a safe Git rename process,
which may require an intermediate name.

Example:

```text
ARCHITECTURE/
→ architecture-temp/
→ architecture/
```

The exact migration procedure SHOULD be documented before performing
case-only directory renames.

---

## 9. Migration Sequence

The recommended migration sequence is:

### Phase 1 — Standards

- Establish shared naming standards in COG
- Reference those standards from EIB
- Document the EIB migration plan

### Phase 2 — Inventory

- Inventory EIB directories
- Inventory files within each legacy directory
- Identify path references
- Identify scripts and configuration dependencies
- Identify documentation links
- Identify GitHub workflow dependencies

### Phase 3 — Low-Risk Migration

Begin with directories having:

- Few dependencies
- Primarily documentation content
- Minimal automation dependencies
- Easily verifiable references

Each directory migration SHOULD use a separate commit where practical.

### Phase 4 — Functional Migration

Migrate directories involved in:

- Configuration
- Connectors
- Data processing
- Automation
- Application logic
- Workflows

These migrations require additional dependency testing.

### Phase 5 — Verification

After migration:

- Verify repository links
- Verify documentation navigation
- Verify configuration references
- Verify scripts
- Verify automated workflows
- Verify development tooling
- Verify public clone usability

### Phase 6 — Cleanup

After successful verification:

- Remove obsolete migration artifacts
- Update repository maps and catalogs
- Update contributor documentation
- Record completed migration decisions
- Mark this migration plan complete

---

## 10. Public and Private Architecture

EIB is intended to support an open-source implementation model.

The public EIB repository SHOULD remain organization-agnostic.

Public repository content may include:

- Framework architecture
- Collectors
- Connectors
- Public intelligence sources
- Generic configuration examples
- Data schemas
- Processing logic
- Risk-assessment logic
- Briefing templates
- Documentation
- Sample data that contains no sensitive organizational information

Organization-specific information SHOULD remain outside the public
organization-agnostic layer.

Examples include:

- Internal asset inventories
- Internal application inventories
- Internal system names
- Organization-specific exposure information
- Internal security findings
- Internal vulnerability dispositions
- Internal owners
- Internal ticket numbers
- Internal contact information
- Non-public evidence
- Organization-specific executive commentary

This separation allows an organization to adopt EIB while maintaining its own
private operational context.

---

## 11. Applicability and Human Validation

Public intelligence can identify potential organizational risk.

Public intelligence alone cannot definitively establish whether a technology
exists within a specific adopter's environment.

Automated inventory checks may assist with prioritization and research, but
an organization SHOULD establish its own process for validating applicability.

For cybersecurity vulnerability intelligence, EIB SHOULD support a
human-in-the-loop disposition model.

A generic public intelligence record may identify:

- Vulnerability
- Vendor
- Product
- Severity
- Exploitation status
- CISA Known Exploited Vulnerability status
- Patch availability
- Mitigation availability
- Public risk priority

The adopting organization's private process may then determine:

- Whether the technology exists
- Whether the vulnerable configuration exists
- Whether the asset is exposed
- What evidence supports the determination
- Who performed the validation
- What remediation is required
- Whether the issue is closed

This preserves EIB's organization-agnostic architecture while supporting
real-world operational vulnerability management.

---

## 12. CISA RSS Collector Dependency

The planned CISA RSS intelligence collector SHALL follow the repository
structure established through this migration.

The collector SHOULD NOT introduce new legacy uppercase directory structures.

Before implementation begins:

1. Confirm the appropriate EIB directory architecture.
2. Determine whether the collector belongs within an existing functional
   component or a new standards-compliant directory.
3. Define public configuration for CISA feeds.
4. Define normalized public intelligence records.
5. Preserve organization-specific applicability outside the public collector.
6. Document collector behavior and configuration.
7. Ensure the design can support additional RSS or Atom sources in the future.

The initial implementation may use CISA as the first public intelligence
source, but the underlying collector SHOULD be designed as a reusable RSS/Atom
capability rather than hard-coded exclusively to CISA.

---

## 13. Migration Tracking

Directory migrations SHOULD be tracked as discrete repository changes.

For each migrated directory, record:

- Original path
- New path
- Date migrated
- Commit
- References updated
- Verification performed
- Known remaining issues

This document MAY be updated as migration progresses.

Detailed implementation records may be maintained elsewhere if the migration
becomes sufficiently complex to warrant a dedicated tracker.

---

## 14. Decision Status

**Status:** Approved migration direction

**Implementation:** Incremental

**Governing Standard:** COG Naming Standard

**Primary Objective:** Bring EIB repository structure into alignment with
shared COG standards without introducing unnecessary disruption.

---

## 15. Guiding Principle

> COG defines how projects are built. EIB defines what the Executive
> Intelligence Briefing does.

Repository structure should reinforce that separation.