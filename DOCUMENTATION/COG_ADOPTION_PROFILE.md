---
title: COG Adoption Profile
document_id: GOV-015
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-09-10
---

# Executive Intelligence Briefing (EIB)

# COG Adoption Profile

## Purpose

This profile records EIB's selective adoption of reusable governance from the
Common Operations Guide (COG). It identifies the COG baseline used, the COG
authorities EIB adopts, and the EIB-specific authorities, extensions, and
exceptions that remain under EIB governance.

This profile is the authoritative EIB record of the approved COG adoption
decisions. It does not make EIB generically or completely conformant with COG.

---

## COG Repository and Baseline

COG repository:

```text
https://github.com/bjohnson70/COG
```

This initial EIB adoption is based only on COG commit:

```text
91fdba4b75df3132338968010bd666666e432abc
```

This commit is the authoritative COG Initial Baseline for this profile.

---

## Adoption Model

EIB uses a hybrid governance model:

- COG is authoritative for the reusable standards identified in this profile.
- EIB is authoritative for EIB requirements, project-specific governance,
  compatibility constraints, migration requirements, and domain-specific
  operating rules.
- EIB adopts COG outcomes using EIB's established repository structure where
  appropriate. Adoption does not require cosmetic restructuring to match COG.
- Existing EIB practices are evidence for possible COG refinement; they do not
  automatically become COG standards.

When EIB guidance overlaps an adopted COG authority, EIB should reference COG
for the reusable requirement and retain only EIB-specific implementation,
extension, or exception details locally.

---

## Adopted COG Authorities

EIB adopts the following COG baseline authorities at the commit identified
above:

| COG authority | EIB adoption |
| --- | --- |
| [COG Repository Standard](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/standards/REPOSITORY_STANDARD.md) | EIB adopts its repository discoverability, canonical-source, organization-outcome, hygiene, and change-discipline requirements. |
| [COG Documentation Standard](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/standards/DOCUMENTATION_STANDARD.md) | EIB adopts its controlled-document, metadata, identity, catalog, reference, lifecycle, and supersession outcomes. |
| [COG Naming Standard](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/standards/NAMING_STANDARD.md) | EIB adopts its naming defaults for new artifacts, subject to documented project-specific compatibility and migration requirements. |
| [COG Decision Record Standard](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/standards/DECISION_RECORD_STANDARD.md) | EIB adopts the ADR threshold, decision-status, stable-identity, and durable-content practices while retaining its established ADR location and project decision context. |
| [GitHub Development Workflow](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/development/GITHUB_WORKFLOW.md) | EIB adopts the reusable GitHub workflow outcomes. EIB-specific procedures remain governed by EIB. |
| [Shared vs Project-Specific Governance](https://github.com/bjohnson70/COG/blob/91fdba4b75df3132338968010bd666666e432abc/governance/SHARED_VS_PROJECT_SPECIFIC.md) | EIB adopts its authority-boundary criteria when determining whether a practice belongs in COG or EIB. |

---

## EIB-Specific Extensions

EIB retains the following extensions because they serve EIB's operating and
modernization needs:

- The lifecycle defined by
  [ADR-0003](../ARCHITECTURE/ADR-0003-Document-Lifecycle.md) adds `Review`,
  `Approved`, `Revised`, `Deprecated`, and `Archived or Removed` to COG's
  baseline lifecycle. These states map to COG as follows:

| EIB lifecycle state | COG baseline mapping |
| --- | --- |
| Draft | Draft |
| Review | Draft |
| Approved | Draft until it is the current authority; Active thereafter |
| Active | Active |
| Revised | Active; Git and document version identify the revision |
| Deprecated | Superseded or Retired, according to whether a replacement exists |
| Archived or Removed | Retired; historical traceability is retained in Git or an appropriate archive |

- EIB uses its established uppercase functional directories while its approved
  incremental migration plan remains in effect.
- EIB uses project-specific document identifiers and metadata conventions
  compatible with the adopted COG documentation outcomes.

---

## EIB-Specific Exceptions

- [DOCUMENTATION/](.) remains EIB's authoritative governance-document location
  pending an explicitly approved migration. The existence of `docs/` does not
  establish a competing authoritative location.
- No directory is to be moved, renamed, consolidated, or deleted solely to
  match COG naming or layout preferences.
- The known duplicate `DEV-001` identifier is not resolved by this profile.
  Its eventual resolution must determine the stronger historical and
  authoritative claim through Git history, catalog history, document metadata,
  and repository references.
- [REPOSITORY_STANDARDS.md](REPOSITORY_STANDARDS.md) remains in place during
  this adoption step. It may later be narrowed to retain EIB-specific
  requirements while referencing adopted COG authorities for shared rules.

---

## Non-Applicable COG Authorities

None of the COG authorities assessed for this Initial Baseline adoption is
designated non-applicable at this time. EIB's adoption is selective: only the
authorities listed above are adopted through this profile.

Future COG standards or guidance are not adopted unless EIB deliberately
reviews and records their applicability in this profile or another approved EIB
controlled document.

---

## EIB Authorities That Remain Project-Specific

EIB remains the sole authority for its:

- Product requirements, architecture, intelligence model, data model, and
  implementation choices.
- Public/private repository strategy, security and privacy boundaries, and
  domain-specific operational procedures.
- Platform compatibility constraints, repository migration sequencing, and
  implementation validation appropriate to EIB.
- EIB roadmap, product backlog, AI collaboration operations, prompts,
  connectors, configuration, profiles, and operational documentation.

---

## Approved Adoption Decisions

1. **Hybrid governance:** COG is authoritative for reusable repository,
   documentation, naming, decision-record, and workflow standards. EIB retains
   authority for EIB-specific requirements, exceptions, compatibility
   constraints, migration requirements, and domain-specific operating rules.
2. **Control by authority and function:** A document is controlled because of
   what it does, not its directory. Location alone does not determine whether
   it requires an ID, metadata, catalog entry, version, status, or lifecycle
   governance.
3. **`DOCUMENTATION/` remains authoritative pending migration:** `docs/` does
   not become authoritative merely because it is an intended future structure.
   Neither directory is moved, renamed, consolidated, or deleted by this
   decision.
4. **Retain and map the EIB extended lifecycle:** EIB retains richer lifecycle
   states where useful and maps them to the COG baseline rather than removing
   them for conformity.
5. **Resolve `DEV-001` by document history:** Neither document is renumbered by
   this decision. The stronger historical and authoritative claim retains the
   identifier after the required evidence review.
6. **Formal, selective COG adoption:** EIB adopts COG authorities individually.
   This profile distinguishes adopted authorities, EIB extensions, EIB
   exceptions, non-applicability, and EIB-only authority.

---

## COG Baseline Review Rule

The COG baseline commit recorded in this profile does not automatically change
when COG changes. A future COG revision requires deliberate EIB review before
it affects EIB governance.

Any EIB adoption of a future COG baseline must identify the reviewed COG commit,
the applicable authorities, any exceptions or extensions, and any required EIB
implementation changes.

---

## Change Control

Changes under this profile should:

1. Identify the applicable COG authority and the relevant pinned or approved
   COG baseline.
2. Preserve EIB's canonical project-specific authority where COG does not
   govern the subject.
3. Document a justified EIB exception, extension, or non-applicability when
   needed.
4. Avoid duplicate authoritative requirements by referencing COG for shared
   rules.
5. Update this profile and [DOCUMENT_CATALOG.md](../DOCUMENT_CATALOG.md) when
   the formal EIB adoption record changes.

## Related Documents

- [DOCUMENT_CATALOG.md](../DOCUMENT_CATALOG.md)
- [REPOSITORY_STANDARDS.md](REPOSITORY_STANDARDS.md)
- [REPOSITORY_MIGRATION_PLAN.md](REPOSITORY_MIGRATION_PLAN.md)
- [ADR-0003](../ARCHITECTURE/ADR-0003-Document-Lifecycle.md)
- [ADR-0005](../ARCHITECTURE/ADR-0005-Versioning-Strategy.md)
- [REPOSITORY_WORKFLOW.md](../REPOSITORY_WORKFLOW.md)
