---
Title: ADR-0004 – Definition of Done
Status: Accepted
Version: Foundation (v0.1)
Date: 2026-07-21
Author: EIB Project
---

# ADR-0004 – Definition of Done

## Status

Accepted

---

# Context

Creating a document does not mean the work is complete.

Within the Executive Intelligence Briefing (EIB), every artifact should meet a common quality standard before it is considered finished.

A shared Definition of Done ensures consistency, improves maintainability, and reduces technical debt.

---

# Decision

A task, document, template, or intelligence product is considered **Done** when it satisfies the appropriate criteria below.

---

# General Definition of Done

The work is:

- Correct
- Complete for its intended purpose
- Understandable by someone other than the author
- Properly organized
- Version controlled
- Free of unnecessary duplication
- Appropriate for either the Public or Private Repository
- Reviewed for accuracy
- Ready for future maintenance

---

# Documentation Standard

Documentation is Done when:

- Purpose is clearly stated.
- Audience is identified.
- Terminology is consistent.
- Formatting follows repository standards.
- Related documents are referenced where appropriate.
- Major decisions include supporting reasoning.

---

# Template Standard

Templates are Done when:

- Personal information has been removed.
- Instructions are clear.
- Placeholders are obvious.
- Reuse requires minimal modification.
- They can serve as a starting point for future users.

---

# Intelligence Product Standard

Reports and briefings are Done when:

- Source knowledge is identifiable.
- Important assumptions are documented.
- Findings are prioritized.
- Recommendations are actionable.
- Date of generation is included.
- Limitations are acknowledged when appropriate.

---

# Architecture Standard

Architectural work is Done when:

- The decision is documented.
- Alternatives were considered.
- Trade-offs are explained.
- Related documents are updated.
- Future maintainers can understand the reasoning.

---

# Repository Standard

Repository work is Done when:

- Files are stored in the proper location.
- Naming conventions are followed.
- Duplicate documents are removed or consolidated.
- Appropriate commit messages are used.
- The repository remains easier to understand than before the change.

---

# Guiding Question

Before marking work complete, ask:

> **Does this leave behind a better starting point for the next person?**

If the answer is **No**, the work is not yet finished.

---

# Benefits

This standard:

- Improves consistency.
- Encourages reusable work.
- Reduces maintenance effort.
- Preserves reasoning.
- Makes onboarding easier.
- Improves long-term quality.

---

# Consequences

Positive:

- Higher quality documentation.
- Better knowledge preservation.
- More maintainable repositories.
- Clear expectations for contributors.

Trade-offs:

- Some work may take longer to complete.
- Requires discipline.
- Requires periodic review.

These trade-offs are acceptable because they improve the overall quality of the Executive Intelligence Briefing.

---

# Success Criteria

This decision is successful when:

- Contributors have a shared understanding of "Done."
- Documentation remains understandable over time.
- Reusable work is consistently produced.
- Future maintainers require less effort to understand previous work.

---

# Related Documents

- Architecture/GOVERNANCE.md
- Architecture/ARCHITECTURE.md
- ADR-0001 – Public vs. Private Repository Strategy
- ADR-0002 – Knowledge vs. Intelligence
- ADR-0003 – Document Lifecycle

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next person.