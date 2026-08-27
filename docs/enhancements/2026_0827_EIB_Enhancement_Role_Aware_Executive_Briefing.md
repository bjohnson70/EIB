# EIB Enhancement — Role-Aware Executive Briefing

**Date:** 2026-08-27  
**Status:** Approved Enhancement  
**Target:** EIB v8  
**Applies To:** Morning EIB, Executive Briefings, Role-Based Output

---

## Purpose

The EIB should adapt not only to the intelligence being presented, but also to the audience receiving it.

Different organizational roles require different levels of:

- Technical detail
- Operational detail
- Administrative context
- Strategic context
- Risk explanation
- Decision support
- Plain-language translation

A cybersecurity event may require substantial technical detail for a CISO while the same event may require only business impact, service risk, accountability, and decision information for a Chief Deputy Director.

The EIB therefore requires a formal audience model.

The operating principle is:

> **The same intelligence may be relevant to every executive, but it should not necessarily be explained to every executive the same way.**

---

# Requirement 1 — Audience-Aware Briefing

The EIB should identify the intended audience or role when generating a briefing.

Examples include:

- Chief Information Officer (CIO)
- Chief Information Security Officer (CISO)
- Chief Technology Officer (CTO)
- Deputy Director (DD)
- Chief Deputy Director (CDD)
- Director
- Executive Leadership
- Technical Leadership
- Administrative Leadership
- Program Leadership

The audience profile should influence:

- Language
- Technical depth
- Explanation
- Terminology
- Detail
- Risk framing
- Action framing
- Decision framing
- Length

---

# Requirement 2 — Role Is Not Sufficient by Itself

A job title alone does not completely determine the appropriate briefing style.

The EIB should consider at least three dimensions:

1. **Role**
2. **Role Orientation**
3. **Organizational Altitude**

The combination determines the default briefing profile.

---

# Requirement 3 — Role

Role describes the audience's organizational responsibility.

Examples:

| Role | Typical Responsibility |
|---|---|
| CISO | Cybersecurity, risk, compliance, privacy, resilience |
| CIO | Enterprise technology, business enablement, investment, operations |
| CTO | Technology architecture, platforms, engineering, modernization |
| DD | Business or program leadership |
| CDD | Department-wide executive leadership and coordination |
| Director | Enterprise mission, policy, accountability and external leadership |

Role helps determine:

> **What does this person need from the intelligence?**

---

# Requirement 4 — Role Orientation

The EIB should classify the audience's default orientation.

Suggested classifications:

## Technical

The role routinely requires technical understanding and technical decisions.

Examples may include:

- Security Architect
- Infrastructure Lead
- Engineering Lead
- Technical Operations Lead

---

## Technical / Executive

The role requires technical understanding but primarily uses that understanding to make executive, risk, investment, or organizational decisions.

Examples may include:

- CISO
- CIO
- CTO

---

## Business / Administrative

The role primarily manages:

- Programs
- People
- Budgets
- Policy
- Operations
- Service delivery
- Administration

Technical detail should normally be translated into business consequences.

Examples may include:

- Deputy Director
- Administrative leadership
- Program executives

---

## Executive / Administrative

The role primarily requires:

- Enterprise awareness
- Mission impact
- Risk
- Accountability
- Decisions
- Resources
- Public impact
- Executive coordination

Examples may include:

- Chief Deputy Director
- Director

Technical implementation detail should normally be minimized unless it materially affects an executive decision.

---

# Requirement 5 — Organizational Altitude

The EIB should recognize organizational altitude.

As organizational altitude increases:

> **Technical implementation detail should generally decrease.**

At the same time, emphasis should generally increase on:

- Mission impact
- Business impact
- Service impact
- Risk
- Financial impact
- Public impact
- Regulatory implications
- Accountability
- Ownership
- Decisions
- Resources
- Timing
- Dependencies
- Executive action

The general relationship is:

```text
HIGHER ORGANIZATIONAL ALTITUDE
            ↑
More:
Mission
Risk
Impact
Decision
Accountability
Cost
Timing
Plain Language
            |
            |
            |
Less:
Technical implementation
Configuration detail
Product internals
Technical jargon
Low-level remediation detail
            ↓
LOWER / TECHNICAL OPERATIONAL LEVEL