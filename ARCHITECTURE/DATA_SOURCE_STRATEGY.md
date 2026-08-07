---
title: Data Source Strategy
document_id: PA-006
version: 3.0
status: Approved
owner: BSJ
last_updated: 2026-08-07
depends_on:
  - ARCHITECTURE/PRODUCT_ARCHITECTURE.md
  - ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
  - ARCHITECTURE/SCORING_MODEL.md
  - DOCUMENTATION/REPOSITORY_STANDARDS.md
---

# Executive Intelligence Briefing (EIB)

# Data Source Strategy

## Purpose

This document defines the strategy for acquiring, governing, evaluating, and maintaining the information sources that feed the Executive Intelligence Briefing (EIB).

Its purpose is to ensure that executive intelligence remains timely, trustworthy, relevant, traceable, and scalable while avoiding unnecessary dependence on any single vendor, API, connector, or technology.

---

# Philosophy

Information is the raw material of intelligence.

The value of EIB depends on the quality, diversity, reliability, and timeliness of the sources from which it learns.

The architecture therefore favors:

- Authoritative sources over speculative sources.
- Corroboration over single-source dependence.
- Traceability over opaque aggregation.
- Configuration over hard-coded integrations.
- Resilience over brittle dependencies.
- Relevance over indiscriminate collection.

---

# Strategic Objectives

The data source strategy shall:

- Maximize useful source diversity.
- Minimize vendor lock-in.
- Prefer authoritative sources.
- Support automated collection.
- Preserve source provenance.
- Enable historical analysis where appropriate.
- Continuously evaluate source quality.
- Respect privacy, security, legal, and licensing constraints.
- Support both public and private EIB implementations.
- Prevent collection volume from overwhelming executive relevance.

---

# Source Categories

## Internal Enterprise Sources

Examples include:

- Email
- Calendar
- Corporate announcements
- Service-management systems
- Security platforms
- Project-management systems
- Operational dashboards
- Business metrics
- Collaboration platforms
- Enterprise repositories

These sources may contain sensitive or restricted information and must follow applicable access controls.

---

## External Authoritative Sources

Examples include:

- Government publications
- Regulatory agencies
- Industry associations
- Vendor advisories
- Standards bodies
- Threat-intelligence providers
- Financial-market sources
- Research organizations

These sources are especially valuable when primary-source authority matters.

---

## Public Information Sources

Examples include:

- RSS feeds
- Public APIs
- Official websites
- Legislative portals
- Open datasets
- Public repositories
- News organizations

Public availability does not automatically imply high reliability.

Public sources must still be evaluated for quality and provenance.

---

## User-Contributed Sources

Examples include:

- Uploaded documents
- Reports
- Meeting notes
- Strategic plans
- Policies
- Presentations
- Personal observations
- User-maintained Markdown files

User-contributed information should retain sufficient provenance to distinguish user statements from independently verified facts.

---

## Connected Personal Sources

Private EIB implementations may connect to sources such as:

- Personal email
- Personal calendars
- File repositories
- Health or wellness data
- Financial planning data
- Property records
- Travel information

These sources require explicit access controls and must never be promoted into public repositories without appropriate generalization and removal of sensitive information.

---

# Source Quality Attributes

Each source should be evaluated across multiple dimensions.

| Attribute | Description |
|---|---|
| Authority | Is the source recognized as authoritative for the subject? |
| Accuracy | Has the source historically provided reliable information? |
| Timeliness | How quickly is relevant information updated? |
| Completeness | Does the source contain sufficient context? |
| Availability | Is the source consistently accessible? |
| Stability | Does its format or interface remain reasonably stable? |
| Traceability | Can intelligence be traced back to the originating source? |
| Independence | Is the source independent of other corroborating sources? |
| Security | Can the source be accessed and stored safely? |
| Executive Value | Does the source materially improve decision-making? |

No single attribute should determine source quality by itself.

---

# Source Classification

Sources may be classified as:

```text
Trusted
Preferred
Standard
Supplemental
Experimental
Deprecated
```

## Trusted

Highly authoritative and consistently reliable.

Examples may include:

- Official internal systems of record
- Primary government publications
- Verified enterprise platforms

---

## Preferred

High-quality sources that should normally be consulted when available.

---

## Standard

Reliable sources suitable for routine use.

---

## Supplemental

Useful for context or corroboration but should not normally serve as the sole basis for high-impact conclusions.

---

## Experimental

Sources undergoing evaluation.

Experimental sources should not silently become authoritative.

---

## Deprecated

Sources no longer recommended because of:

- Poor reliability
- Excessive maintenance
- Replacement by better sources
- Licensing concerns
- Security concerns
- Loss of executive value

---

# Source Reliability and Confidence

Source classification should contribute to, but not independently determine, intelligence confidence.

A trustworthy source can still contain:

- Stale information
- Partial information
- Ambiguous context
- Errors

Likewise, a supplemental source may provide useful corroboration.

Confidence should consider:

- Source reliability
- Freshness
- Agreement among sources
- Completeness
- Correlation quality

The Confidence Engine owns the final confidence calculation.

---

# Corroboration

Important intelligence should use independent corroboration when practical.

Examples:

```text
Calendar + Email
Security Advisory + Vulnerability Scanner
Government Publication + Regulatory Notice
GitHub Activity + Change Management
Weather Service + Travel Schedule
```

Multiple copies of the same originating report should not be treated as independent confirmation.

---

# Collection Principles

Collection should be:

- Automated where practical.
- Incremental where possible.
- Resilient to temporary failure.
- Observable.
- Rate-limit aware.
- Respectful of source terms and licensing.
- Limited to information that has a legitimate EIB purpose.

Collection should not become indiscriminate data accumulation.

The objective is **better intelligence**, not maximum data volume.

---

# Connector Separation

Source acquisition should be separated from intelligence-processing logic.

```text
External Source
      │
      ▼
Connector
      │
      ▼
Normalization
      │
      ▼
Intelligence Pipeline
```

Connectors should be responsible for:

- Authentication
- Retrieval
- Source-specific formatting
- Pagination
- Rate limits
- Basic metadata
- Error handling

Connectors should not independently decide executive priority or final recommendations.

---

# Normalization

Different sources should be converted into common internal models before downstream intelligence processing.

Normalization supports:

- Correlation
- Prioritization
- Deduplication
- Confidence scoring
- Recommendation generation
- Briefing composition

Source-specific details should remain available as provenance metadata even after normalization.

---

# Source Provenance

Every intelligence item should retain enough provenance to answer:

> Where did this come from?

Where practical, provenance should include:

- Source name
- Connector
- Retrieval timestamp
- Original timestamp
- Source identifier
- Original location or reference
- Applicable source classification

Provenance is essential for explainability and trust.

---

# Duplicate Suppression

EIB should detect when the same underlying information appears through multiple sources.

Examples include:

- Calendar invitation plus confirmation email
- Security advisory repeated by several news sites
- Vendor bulletin reproduced by a secondary publication
- GitHub notification plus project-management update

Duplicate observations should normally be consolidated rather than presented as separate executive events.

---

# Freshness

Different sources have different useful lifetimes.

Examples:

```text
Weather                  Hours
Breaking security alert  Hours
Calendar event           Minutes to days
News                     Hours to days
Project status           Days
Policy                    Months to years
Historical knowledge      Years
```

Freshness requirements should therefore be configurable by source type and use case.

---

# Source Evaluation

Every significant source should be periodically reviewed.

Evaluation should consider:

- Reliability
- Executive value
- Accuracy
- Historical usefulness
- Collection cost
- Maintenance burden
- Security exposure
- Licensing restrictions
- Availability
- Performance
- Freshness
- Replacement alternatives

Sources that no longer justify their operational cost should be retired.

---

# Source Governance

Every production source should have documented:

- Name
- Owner or provider
- Source category
- Connector
- Authentication method
- Classification
- Collection frequency
- Data sensitivity
- Retention requirements
- Known limitations
- Failure behavior

This information should eventually be represented through configuration rather than informal documentation alone.

---

# Failure Handling

A failed source should not necessarily prevent an entire briefing from being produced.

Connectors should support graceful degradation.

Examples:

```text
Weather unavailable
→ Briefing continues without weather.

Calendar unavailable
→ Clearly indicate calendar data could not be verified.

Primary security source unavailable
→ Use corroborating sources where available and reduce confidence.
```

The briefing should distinguish **no relevant findings** from **source unavailable**.

---

# Source Security

Source access must follow least-privilege principles.

Requirements include:

- Credentials must not be stored in public repository content.
- Tokens and secrets must be protected.
- Connectors should request only necessary permissions.
- Sensitive information should remain within approved boundaries.
- Public and private repository separation defined in ADR-0001 must be maintained.

---

# Privacy

Private source collection should be purpose-limited.

EIB should not collect sensitive information merely because it is technically accessible.

Collection should support a defined intelligence or user need.

---

# International Support

Source architecture must not assume that users, locations, governments, currencies, time zones, or services are exclusively U.S.-based.

EIB should be able to support:

- International strategic locations
- Regional data sources
- Local weather providers
- Local regulatory authorities
- Multiple currencies
- Multiple time zones
- Country-specific information sources

Localization should occur through configuration rather than hard-coded assumptions.

---

# Configuration

Source behavior should increasingly be configuration-driven.

Potential configuration includes:

```text
source_id
connector
classification
enabled
priority
refresh_interval
freshness_threshold
retention
region
language
required_for_briefing
fallback_sources
```

This supports reusable public architecture while allowing private implementations to select their own sources.

---

# Observability

Source health should eventually be measurable.

Potential metrics include:

- Successful retrieval rate
- Failure rate
- Average latency
- Data freshness
- Duplicate rate
- Source contribution to briefing items
- Source contribution to accepted recommendations
- Maintenance cost

Sources that consume significant resources but produce little executive value should be candidates for retirement.

---

# Relationship to Intelligence Engines

Data sources feed the intelligence pipeline but should not control it.

```text
Sources
   ↓
Connectors
   ↓
Normalized Models
   ↓
Correlation
   ↓
Priority
   ↓
Confidence
   ↓
Recommendation
   ↓
Briefing
```

This separation protects EIB from becoming tied to any individual source or vendor.

---

# Repository Foundation Impact

During Repository Foundation migration:

- This document moves from `Architecture/` to canonical `ARCHITECTURE/`.
- Existing identifier `PA-006` is preserved pending broader identifier review.
- References are updated to canonical uppercase architecture paths.
- Future connector specifications should align with this strategy.

---

# Success Criteria

The Data Source Strategy succeeds when:

- Intelligence can be traced to its sources.
- Source failures degrade gracefully.
- Multiple sources can corroborate important events.
- No single vendor becomes an unnecessary architectural dependency.
- Sources can be added or removed primarily through configuration.
- Collection remains relevant rather than indiscriminate.
- Sensitive sources remain appropriately protected.
- EIB can support users and locations internationally.

---

# Related Documents

- ARCHITECTURE/PRODUCT_ARCHITECTURE.md
- ARCHITECTURE/INTELLIGENCE_ARCHITECTURE.md
- ARCHITECTURE/SCORING_MODEL.md
- ARCHITECTURE/ADR-0001-Public-vs-Private-Repositories.md
- ARCHITECTURE/ADR-0002-Knowledge-vs-Intelligence.md
- IMPLEMENTATION/SOURCE_CONNECTOR_FRAMEWORK.md
- IMPLEMENTATION/CONFIDENCE_ENGINE.md
- IMPLEMENTATION/CORRELATION_ENGINE.md
- DOCUMENTATION/REPOSITORY_STANDARDS.md

---

# Guiding Principle

> Better intelligence begins with better sources—but more sources do not automatically create better intelligence.

EIB should collect deliberately, corroborate intelligently, and always preserve enough provenance for the user to understand where an important conclusion came from.