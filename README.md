---
title: Executive Intelligence Briefing
document_id: ROOT-001
version: 2.0
status: Active
owner: BSJ
last_updated: 2026-08-07
---

# Executive Intelligence Briefing (EIB)

> Every solution should leave behind a better starting point for the next contributor.

---

# What Is EIB?

The **Executive Intelligence Briefing (EIB)** is an open architecture and reference framework for transforming fragmented information into concise, contextual, prioritized, and actionable intelligence.

EIB is designed to help users answer:

- What matters today?
- What changed?
- Why does it matter?
- What deserves attention?
- What should I consider doing next?

The daily Executive Intelligence Briefing is the first major product built on the platform.

The broader objective is an extensible **Executive Intelligence Platform**.

---

# Why EIB Exists

Modern leaders do not suffer from a lack of information.

They suffer from:

- Too much information
- Too little context
- Too little time
- Too many disconnected systems
- Too many decisions competing for attention

Traditional tools often provide:

```text
More data
More alerts
More dashboards
More feeds
```

EIB is designed to provide something different:

```text
Less noise
More context
Better prioritization
Better decisions
```

---

# Product North Star

> Give the user less to read, more to understand, and better context for the decision that follows.

---

# The Intelligence Model

EIB distinguishes between four related concepts:

```text
Knowledge
    │
    ▼
Reasoning
    │
    ▼
Intelligence
    │
    ▼
Action
```

**Knowledge** answers:

> What do we know?

**Reasoning** answers:

> Why does it matter?

**Intelligence** answers:

> What deserves attention now?

**Action** answers:

> What should happen next?

This model is defined in:

```text
ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
```

---

# Daily Briefing Experience

The standard daily EIB briefing is designed to be consumed in approximately:

```text
5–7 minutes
```

It should normally help the user understand:

- The day ahead
- Important calendar events
- Material changes
- Priority intelligence
- Emerging risks
- Opportunities
- Relevant metrics
- Recommendations
- What deserves monitoring next

The briefing should remain concise without becoming sterile.

The desired experience is:

> Data-rich, useful, professional, and still enjoyable to read.

---

# Calendar-First Context

The user's actual schedule is one of the strongest indicators of what matters today.

EIB therefore treats calendar context as an important input into prioritization.

Example:

```text
Vendor meeting today
        +
Material vendor development
        ↓
Higher briefing relevance
```

Calendar unavailability must never be silently represented as:

```text
No meetings scheduled
```

Source failure and empty results are different conditions.

---

# Intelligence Architecture

The conceptual intelligence flow is:

```text
Sources
   │
   ▼
Collection
   │
   ▼
Validation
   │
   ▼
Normalization
   │
   ▼
Enrichment
   │
   ▼
Correlation
   │
   ▼
Scoring
   │
   ▼
Prioritization
   │
   ▼
Recommendations
   │
   ▼
Personalization
   │
   ▼
Briefing Composition
   │
   ▼
Executive Intelligence
```

Detailed architecture is defined under:

```text
ARCHITECTURE/
```

---

# Core Product Capabilities

EIB is designed around modular capabilities including:

- Source connectors
- Normalization
- Correlation
- Priority scoring
- Confidence assessment
- Recommendation generation
- Personalization
- Briefing composition
- Historical intelligence
- Feedback and learning

The architecture separates these responsibilities so they can evolve independently.

---

# Strategic Locations

EIB supports configurable **Strategic Locations**.

A user may configure locations such as:

- Primary residence
- Office
- Secondary residence
- Rental property
- Travel destination
- Family location
- International business location

Strategic locations may influence:

- Weather
- Sunrise and sunset
- Travel context
- Time-zone awareness
- Local risk
- Geographic relevance

No specific location is hard-coded into the reusable platform.

---

# International Design

EIB is intended to support users and locations anywhere in the world.

The platform should not assume:

- United States geography
- Fahrenheit
- Miles
- U.S. dollars
- U.S. time zones
- English-only output
- U.S.-specific information sources

Localization should be driven by configuration and user profiles.

---

# Public and Private Repository Strategy

EIB separates reusable public architecture from private implementation data.

## Public Repository

The public repository may contain:

- Architecture
- Governance
- Documentation
- Models
- Templates
- Prompts
- Workflows
- Reference implementations
- Sample configuration

It should not contain private user information.

---

## Private Implementations

Private implementations may contain:

- Personal profiles
- Connected account data
- Private briefings
- Financial planning
- Health information
- Family information
- Work products
- Production configuration
- Personal operational history

The governing decision is:

```text
ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
```

---

# Repository Structure

The canonical repository structure is:

```text
EIB/
│
├── AI/
├── ARCHITECTURE/
├── CONFIG/
├── CONNECTORS/
├── DATA/
├── DEVELOPMENT/
├── DOCUMENTATION/
├── IMPLEMENTATION/
├── MODELS/
├── OPERATIONS/
├── PERSONALITY/
├── PROFILES/
├── PROMPTS/
├── ROADMAP/
├── TESTS/
├── TOOLS/
└── WORKFLOWS/
```

Repository-wide governing documents may remain at the root when appropriate.

Repository structure and naming are governed by:

```text
DOCUMENTATION/REPOSITORY_STANDARDS.md
```

---

# Where to Start

## Product or Executive Reader

Recommended sequence:

```text
README.md
VISION.md
EXECUTIVE_PRINCIPLES.md
PRODUCT_REQUIREMENTS.md
ARCHITECTURE/PRODUCT_ARCHITECTURE.md
ARCHITECTURE/REPORT_SPECIFICATION.md
```

---

## Architect

Recommended sequence:

```text
ARCHITECTURE/README.md
ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md
ARCHITECTURE/GOVERNANCE.md
ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
ARCHITECTURE/ADR-0003-Document-Lifecycle.md
ARCHITECTURE/ADR-0004-Definition-of-Done.md
ARCHITECTURE/ADR-0005-Versioning-Strategy.md
```

Then continue through the applicable product and implementation architecture.

---

## Developer

Recommended sequence:

```text
README.md
ARCHITECTURE/README.md
DOCUMENTATION/REPOSITORY_STANDARDS.md
DEVELOPMENT/REPOSITORY_STRUCTURE.md
DEVELOPMENT/CODING_STANDARDS.md
IMPLEMENTATION/IMPLEMENTATION_ARCHITECTURE.md
```

---

## AI Development Agent

AI systems should:

1. Inspect actual repository state.
2. Read Repository Standards.
3. Read applicable Architecture Decision Records.
4. Read the relevant architecture.
5. Preserve established document identifiers.
6. Avoid duplicate content.
7. Update affected cross-references.
8. Verify work before declaring completion.

Historical chat context should supplement the repository, not replace it.

---

# Repository Governance

The hierarchy of architectural authority is generally:

```text
CONSTITUTION.md
       ↓
Accepted ADRs
       ↓
DOCUMENTATION/REPOSITORY_STANDARDS.md
       ↓
ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md
       ↓
Domain Architecture
       ↓
Implementation Specifications
       ↓
Operational Guidance
```

Conflicting guidance should be resolved rather than allowed to persist indefinitely.

---

# Current Repository Foundation Work

The repository is undergoing a controlled Repository Foundation modernization.

Completed work includes:

- Canonical repository standards
- Repository migration plan
- Repository inventory
- Canonical `ARCHITECTURE/` directory
- Migration of ADR-0001 through ADR-0005
- Migration of legacy architecture documents
- Retirement of the duplicate `Architecture/` directory
- Modernized product architecture
- Modernized intelligence architecture
- Modernized personalization model
- Modernized scoring model
- Modernized briefing specification
- Strategic-location internationalization

Remaining work includes:

- Root-document modernization
- Document Catalog reconciliation
- Repository status reconciliation
- Duplicate governance-document review
- Internal-link validation
- Filename validation
- Clean Windows clone validation
- Codex-assisted development setup

---

# Core Principles

EIB follows several enduring principles.

## Intelligence Before Information

Do not show information merely because it exists.

Show it when it materially improves understanding.

---

## Executive Time Is Valuable

Every section should justify the user's attention.

---

## Same Truth, Different Relevance

Personalization may change relevance and presentation.

It must not change facts.

---

## Explain Before Recommending

The user should understand why an action is being suggested.

---

## Trust Through Transparency

Important intelligence should remain traceable to supporting evidence.

---

## Configuration Before Customization

Reusable capabilities should be configured rather than duplicated through user-specific code.

---

## Human Judgment Remains Central

EIB supports judgment.

It does not replace it.

---

## Professional Does Not Mean Sterile

Useful intelligence can remain human and enjoyable without sacrificing rigor.

---

# Metrics Philosophy

A metric should normally provide more than a number.

Preferred pattern:

```text
Current Value
Change
Interpretation
```

Example:

```text
Critical Vulnerabilities

24

-12%

Improving from the previous reporting period.
```

---

# Risk Direction

Where meaningful, risks should indicate movement:

```text
Increasing
Stable
Decreasing
```

Direction often provides more decision value than static severity alone.

---

# Confidence

EIB should communicate uncertainty explicitly.

Potential presentation states include:

```text
Verified
Developing
Estimated
```

A trustworthy briefing should never manufacture certainty to appear complete.

---

# Graceful Degradation

EIB should continue operating when non-critical sources fail.

Examples:

```text
Weather unavailable
→ Continue without weather.
```

```text
Calendar unavailable
→ Continue, but indicate schedule could not be verified.
```

```text
Low-confidence intelligence
→ Mark as developing or omit.
```

A partial but trustworthy briefing is better than a complete but misleading one.

---

# Development Philosophy

The repository should become easier to understand as it becomes more capable.

Contributors should prefer:

- Evolution over unnecessary replacement
- One authoritative copy
- Stable identifiers
- Focused commits
- Verifiable changes
- Portable repository paths
- Documentation that supports humans and AI

---

# Repository Status

EIB is currently in:

```text
Active Development
```

with the repository moving from its initial governance foundation toward a reusable, testable Executive Intelligence Platform.

The current focus is:

```text
Repository Foundation
+
Architecture Consolidation
+
AI-Assisted Development Enablement
```

---

# Related Documents

- VISION.md
- MANIFESTO.md
- CONSTITUTION.md
- PRODUCT_REQUIREMENTS.md
- EXECUTIVE_PRINCIPLES.md
- ROADMAP.md
- ARCHITECTURE/README.md
- ARCHITECTURE/ENTERPRISE_ARCHITECTURE.md
- ARCHITECTURE/PRODUCT_ARCHITECTURE.md
- ARCHITECTURE/REPORT_SPECIFICATION.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md
- DOCUMENTATION/REPOSITORY_MIGRATION_PLAN.md
- DOCUMENTATION/REPOSITORY_INVENTORY.md

---

# Guiding Principle

> Every solution should leave behind a better starting point for the next contributor.

EIB succeeds when information becomes easier to understand, intelligence becomes easier to trust, and the next decision requires less effort than it would have without the system.