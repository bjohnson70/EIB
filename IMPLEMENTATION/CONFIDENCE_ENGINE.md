---
title: Executive Confidence Engine
component_id: ENGINE-004
version: 1.1
lifecycle_status: Approved
owner: BSJ
last_updated: 2026-09-14
---

# Executive Confidence Engine

## Purpose

The Executive Confidence Engine evaluates how much EIB should trust an
information claim, correlation, or recommendation. Confidence measures the
strength of supporting evidence. It does not measure executive importance.

Confidence and Priority are separate outputs:

- Confidence asks: "How much should EIB trust this information?"
- Priority asks: "How important is this to this executive?"

Identical evidence must not receive a different Confidence score merely
because the recipient is a CISO, CFO, or another role. Role and profile may
affect available evidence and context, but must not directly alter the
canonical Confidence calculation.

## Objectives

The Confidence Engine shall:

- evaluate evidence reliability;
- make uncertainty visible;
- prevent unsupported certainty;
- preserve source traceability; and
- produce a repeatable, explainable result without requiring Python.

## Processing Pipeline

```text
Collect Evidence
    -> Evaluate Source Authority
    -> Evaluate Corroboration
    -> Evaluate Freshness
    -> Evaluate Completeness
    -> Evaluate Consistency
    -> Calculate Weighted Confidence
    -> Apply Post-Calculation Constraints
    -> Assign Evidence State and Explanation
```

Validation is a process and control. It is not a sixth weighted factor.

## Canonical Inputs

Each assessment should contain, where applicable:

- the claim or conclusion being assessed;
- the evidence supporting it;
- source name, source type, provenance, and source classification;
- original and retrieval timestamps;
- source independence relationships;
- corroborating and contradicting evidence;
- completeness and known gaps;
- the applicable freshness domain class;
- validation results; and
- the evaluation timestamp.

The input may be a normalized `BriefingItem` or a later Intelligence Object.
The required BriefingItem fields are `id`, `source`, `category`, `title`,
`summary`, `timestamp`, `priority`, and `confidence`. Confidence is an output
of this engine; a supplied value must not be treated as evidence merely
because it is present.

## Canonical Factors and Weights

Exactly five factors are used in the canonical calculation:

| Factor | Weight |
|---|---:|
| Source Authority | 30% |
| Corroboration | 25% |
| Freshness | 15% |
| Completeness | 15% |
| Consistency | 15% |
| **Total** | **100%** |

Priority, urgency, impact, executive role, and personal interest are not
Confidence factors. They may be used by later prioritization or
personalization stages.

Each factor is assigned a value from `0.00` through `1.00` using the rubrics
below. The canonical calculation is:

```text
Confidence =
    (Source Authority * 0.30)
  + (Corroboration   * 0.25)
  + (Freshness       * 0.15)
  + (Completeness    * 0.15)
  + (Consistency     * 0.15)
```

Calculate using the unrounded factor values, then apply constraints, then
round the numeric result to two decimal places for presentation. Do not round
individual weighted terms before the final result.

## Factor Rubrics

### Source Authority

Source Authority measures provenance, not whether the claim is true.

| Value | Meaning |
|---:|---|
| 1.00 | Authoritative or primary: official system of record, issuing government authority, or direct organizational record |
| 0.90 | Verified or highly trusted: verified API, established authoritative provider, or authenticated enterprise source |
| 0.75 | Credible or established: reputable news organization, recognized industry source, or established professional publication |
| 0.50 | Supplemental or unverified: secondary reporting, community information, or limited provenance |
| 0.25 | Unknown or weak: social post, anonymous claim, unknown provenance, or unverifiable source |

Source Authority alone must never establish truth.

### Corroboration

Corroboration measures independent support, not agreement. Use the highest
applicable value:

| Value | Meaning |
|---:|---|
| 1.00 | Confirmed by two or more independent credible or authoritative sources |
| 0.90 | Confirmed by one additional independent credible or authoritative source |
| 0.70 | Single authoritative or primary source; independent corroboration unavailable |
| 0.50 | Single credible source; independent corroboration unavailable |
| 0.25 | Single supplemental, weak, or unknown source |
| 0.00 | Material credible contradiction exists and remains unresolved |

Reports derived from the same originating evidence are one source for this
factor. Five reports repeating one wire-service story are not five independent
confirmations. Trace evidence toward its originating source where reasonably
possible.

### Freshness

Freshness is calculated relative to the applicable freshness class's Current
Window, represented by `W`. After selecting the appropriate authoritative
timestamp, calculate the age of the information at the evaluation time and
apply this table:

| Age | Freshness | Classification |
|---:|---:|---|
| `Age <= 1W` | `1.00` | Current |
| `Age > 1W through 2W` | `0.90` | Recent |
| `Age > 2W through 4W` | `0.75` | Aging |
| `Age > 4W through 8W` | `0.50` | Stale |
| `Age > 8W` | `0.25` | Very stale |
| Superseded, expired, or known no longer current | `0.00` | Superseded or expired |

The interval boundaries are inclusive at the upper endpoint and exclusive at
the lower endpoint after the first interval. For example, an item aged exactly
`2W` is Recent, while an item aged just over `2W` is Aging.

Use the timestamp representing when the underlying information became current
or was materially updated. Do not silently treat retrieval time as the time
the information became current. If available timestamps do not permit a
defensible age calculation, do not invent one. Report the limitation in the
Confidence explanation and apply the Completeness and `Indeterminate` rules
when appropriate.

### Completeness

Completeness measures whether the available evidence is sufficient for the
claim, not the volume of data collected.

| Value | Meaning |
|---:|---|
| 1.00 | Complete: all material information needed to support the claim is available |
| 0.90 | Substantially complete: minor details are missing but do not materially affect the conclusion |
| 0.75 | Adequate: enough information supports the conclusion, but meaningful context remains unavailable |
| 0.50 | Partial: significant information is missing and could change the conclusion |
| 0.25 | Fragmentary: only limited evidence or context is available |
| 0.00 | Insufficient: available information cannot reasonably support the claim |

Do not invent missing information.

### Consistency

Consistency measures agreement among available evidence. It must not be
resolved by simply counting sources.

| Value | Meaning |
|---:|---|
| 1.00 | Fully consistent: material evidence agrees and no meaningful contradictions exist |
| 0.90 | Substantially consistent: minor differences do not affect the conclusion |
| 0.75 | Generally consistent: discrepancies exist, but the principal conclusion remains supported |
| 0.50 | Mixed: meaningful discrepancies could affect interpretation |
| 0.25 | Materially inconsistent: substantial unresolved contradictions exist |
| 0.00 | Fundamentally contradictory: evidence cannot presently support a coherent conclusion |

Corroboration evaluates independence. Consistency evaluates agreement. Do not
conflate them.

## Post-Calculation Constraints

Apply these constraints after calculating the weighted score and before
rounding the final numeric result:

| Condition | Constraint |
|---|---|
| Unresolved material credible contradiction | Maximum final Confidence `0.74` |
| Material incompleteness that could change the conclusion | Maximum final Confidence `0.74` |
| Only weak or unknown provenance is available | Maximum final Confidence `0.49` |
| Insufficient evidence to support the claim | No numeric score; result is `Indeterminate` |

`Indeterminate` means EIB lacks sufficient evidence to make a defensible
confidence assessment. It does not mean the claim is false. Absence of
evidence is not low-confidence evidence.

When multiple constraints apply, use `Indeterminate` if applicable; otherwise
apply the lowest numeric ceiling.

## Evidence State

Evidence State is separate from Confidence and is not a factor:

| State | Meaning |
|---|---|
| `VERIFIED` | The material claim has sufficient authoritative or credible support and no unresolved material contradiction exists |
| `DEVELOPING` | Credible evidence exists, but facts remain incomplete, evolving, or subject to meaningful change |
| `UNVERIFIED` | A claim exists, but available evidence is insufficient to independently substantiate it |
| `INFERRED` | EIB derived the conclusion from available evidence; the conclusion was not directly stated by a source |

Evidence State is not Priority, a sixth factor, or an executive-role modifier.
An inferred conclusion must remain traceable to its supporting evidence.

## Confidence Output Contract

The portable internal result shall contain:

```yaml
confidence: 0.82
confidence_level: Good
confidence_reason: >
  Recent authoritative source with one independent corroboration; some
  supporting context remains incomplete.
evidence_state: DEVELOPING
factor_scores:
  source_authority: 0.90
  corroboration: 0.90
  freshness: 0.90
  completeness: 0.75
  consistency: 0.75
supporting_sources:
  - source-id
constraints_applied: []
```

For an indeterminate result, use `confidence: Indeterminate`, identify the
insufficient evidence in `confidence_reason`, and retain the available
factor assessments. Numeric Confidence uses two decimal places.

Confidence levels are:

| Numeric range | Level |
|---:|---|
| 0.90-1.00 | High |
| 0.75-0.89 | Good |
| 0.50-0.74 | Moderate |
| 0.00-0.49 | Low |
| No defensible numeric score | Indeterminate |

Every result must include a concise evidence-based explanation. Presentation
layers may omit the numeric value for executive readability, but must preserve
the underlying structured result.

## Freshness Classes

The information type determines the class, not the executive's role. The
default Current windows are:

| Class | Typical information | Current window |
|---|---|---|
| `IMMEDIATE` | Breaking cyber event, emergency, outage, active incident, market-moving event | 1 hour or less |
| `DAILY` | News, markets, operational status, weather, active government developments | 24 hours or less |
| `PERIODIC` | Projects, organizational developments, recurring metrics, regulatory activity | 7 days or less |
| `REFERENCE` | Policies, standards, architecture, established reference information | 90 days or less, or until superseded |
| `DURABLE` | Historical facts and established decisions | No age penalty unless superseded |

The default Current Window values are:

| Class | `W` |
|---|---:|
| `IMMEDIATE` | 1 hour |
| `DAILY` | 24 hours |
| `PERIODIC` | 7 days |
| `REFERENCE` | 90 days, subject to supersession |
| `DURABLE` | No age-based decay |

`DURABLE` information receives Freshness `1.00` regardless of age unless it
has been superseded, expired, or is known no longer to be current.

For deterministic application, a DAILY item aged 18 hours has Freshness
`1.00`; a DAILY item aged 30 hours has Freshness `0.90`; and a DAILY item aged
3 days has Freshness `0.75`. A PERIODIC item aged 10 days has Freshness
`0.90`. A REFERENCE item aged 120 days has Freshness `0.90` unless it has been
superseded or expired. A DURABLE historical fact aged several years has
Freshness `1.00` unless it is no longer current.

A local Work EIB may override `W` for a freshness class or justified
organizational domain. For example, an authorized local configuration may set
IMMEDIATE `W` to 30 minutes. Local configuration changes `W` only; it does not
change the canonical decay values, intervals, or supersession rule. Internal
overrides must remain local and must not require confidential information in
the public repository.

## Role Portability

Role and profile may affect:

- authorized sources;
- available context;
- domain freshness configuration; and
- evidence requirements.

Role and profile must not directly alter the canonical weighted calculation.
The same evidence assessed under the same configuration must produce the same
Confidence for different recipients. Priority and personalization may vary.

## Public and Work EIB Boundary

The public EIB specification defines the methodology, rubrics, calculation,
output contract, default freshness classes, and portability rules.

A private Work EIB may add internal source classifications, evidence, context,
freshness overrides, and organizational extensions. Internal credentials,
PHI, PII, security findings, and organizational secrets must remain outside
the public repository. Public examples and tests must use synthetic or safe
data. Confidence explanations may cite internal evidence without exposing its
contents upstream.

## Relationship to Priority and Validation

Validation determines whether evidence is structurally and procedurally fit
for processing. It is not a confidence factor. Confidence evaluates evidence
strength. Priority later evaluates executive attention using confidence among
other factors. Neither Priority nor executive profile settings may be used as
a proxy for Confidence.

## Acceptance Scenarios

The following synthetic scenarios are normative examples. Each calculation
uses the five canonical factors in the order defined above. Values shown are
factor values before the final rounding step.

### 1. Recent authoritative verified information

An official system of record reports a current, complete event. No credible
source conflicts with it.

```text
Source Authority = 1.00
Corroboration    = 1.00
Freshness        = 1.00
Completeness     = 1.00
Consistency      = 1.00

Confidence = (1.00 * .30) + (1.00 * .25) + (1.00 * .15)
           + (1.00 * .15) + (1.00 * .15)
           = 1.00
Constraints: none
Result: 1.00, High
Evidence State: VERIFIED
Reason: Current complete evidence from an authoritative source is fully corroborated and consistent.
```

### 2. Credible recent but developing information

A credible established source reports an evolving event. One independent
credible source corroborates it, but meaningful context remains unavailable.

```text
Source Authority = 0.75
Corroboration    = 0.90
Freshness        = 0.90
Completeness     = 0.75
Consistency      = 0.75

Confidence = (0.75 * .30) + (0.90 * .25) + (0.90 * .15)
           + (0.75 * .15) + (0.75 * .15)
           = 0.81
Constraints: none
Result: 0.81, Good
Evidence State: DEVELOPING
Reason: Recent credible reporting has independent support, but the event and its context are still developing.
```

### 3. Single weak or unknown unverified source

An anonymous social post makes a claim with no corroboration and limited
context.

```text
Source Authority = 0.25
Corroboration    = 0.25
Freshness        = 0.90
Completeness     = 0.25
Consistency      = 0.75

Confidence = (0.25 * .30) + (0.25 * .25) + (0.90 * .15)
           + (0.25 * .15) + (0.75 * .15)
           = 0.42
Constraints: weak/unknown provenance caps the result at 0.49; no additional cap is needed.
Result: 0.42, Low
Evidence State: UNVERIFIED
Reason: A fresh claim has weak provenance, no independent support, and fragmentary context.
```

### 4. Credible independent sources with unresolved material conflict

Two credible independent sources address the same event but materially
disagree about its status.

```text
Source Authority = 0.75
Corroboration    = 1.00
Freshness        = 0.90
Completeness     = 0.75
Consistency      = 0.25

Confidence = (0.75 * .30) + (1.00 * .25) + (0.90 * .15)
           + (0.75 * .15) + (0.25 * .15)
           = 0.76
Constraints: unresolved material credible contradiction caps the result at 0.74.
Result: 0.74, Moderate
Evidence State: DEVELOPING
Reason: Independent credible sources exist, but their unresolved material disagreement prevents high confidence.
```

### 5. Authoritative information stale for its domain

An official source provides complete, internally consistent information that
is 35 days old in a PERIODIC domain. The default PERIODIC Current Window is
7 days, so the age is greater than `4W` and no more than `8W`. No independent
corroboration is available.

```text
Source Authority = 1.00
Corroboration    = 0.70
Freshness        = 0.50
Completeness     = 1.00
Consistency      = 1.00

Confidence = (1.00 * .30) + (0.70 * .25) + (0.50 * .15)
           + (1.00 * .15) + (1.00 * .15)
           = 0.85
Constraints: none; stale freshness lowers, but does not erase, authoritative evidence.
Result: 0.85, Good
Evidence State: VERIFIED
Reason: The authoritative policy remains complete and internally consistent, but its age warrants confirmation before relying on it as current.
```

## Portability Requirements

A capable LLM or implementation without Python shall be able to apply this
document using authorized evidence and local profile/context. Implementations
must use the canonical factors, weights, rubrics, constraints, output fields,
and freshness classes. Bounded judgment is permitted only within a factor's
defined rubric and must be explained from evidence. Do not replace this
contract with an unbounded instruction to use judgment.

## Out of Scope

The Confidence Engine does not determine:

- executive priority;
- urgency or business impact;
- recommendations;
- personal interests;
- source acquisition or authentication; or
- organizational secrets and access credentials.