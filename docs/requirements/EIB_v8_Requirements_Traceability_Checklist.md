# EIB v8 — Requirements Traceability Checklist

**Created:** 2026-08-21  
**Last Updated:** 2026-08-27  
**Status:** Active Requirements Control  
**Target:** EIB v8  
**Purpose:** Requirements traceability and implementation verification

---

## Purpose

This document provides the implementation and acceptance checklist for requirements that must be incorporated into EIB v8.

It prevents approved enhancements from being lost between:

1. Operational experience
2. Design discussions
3. Enhancement documentation
4. Prompt development
5. Automation development
6. Testing
7. Production use

This checklist does not replace the underlying enhancement documents.

It verifies whether EIB v8 actually implements them.

---

# Authoritative Enhancement Sources

## Morning Briefing

`docs/enhancements/2026_0808_EIB_Enhancement_Weather_and_Briefing_Scope.md`

## Continuous Awareness

`docs/enhancements/2026_0817_EIB_Enhancement_Continuous_Awareness_and_Breaking_Updates.md`

These documents define the requirements and rationale.

This checklist verifies implementation.

---

# A — Morning EIB

## A1 — Mission

- [ ] Answers: **What do I need to know this morning?**
- [ ] Operates as a broad personal executive briefing first.
- [ ] Professional decision support remains an important secondary function.
- [ ] Professional relevance is an analytical lens rather than the sole story-selection criterion.

## A2 — Information Funnel

Before final story selection, consider:

- [ ] Calendar / My Day
- [ ] Current location
- [ ] Weather
- [ ] Local / regional news
- [ ] California news
- [ ] United States news
- [ ] International / geopolitical news
- [ ] Economy
- [ ] Financial markets
- [ ] Technology
- [ ] Artificial intelligence
- [ ] Cybersecurity
- [ ] California government
- [ ] California state workforce
- [ ] Executive implications
- [ ] Personal implications
- [ ] Decisions
- [ ] Risks
- [ ] Opportunities
- [ ] Watch items

---

# B — Location and Weather

## B1 — Location

- [ ] Determine current or expected location when available.
- [ ] Travel context can override normal home location.
- [ ] Weather uses appropriate current location.
- [ ] Local news uses appropriate current location.
- [ ] Breaking-event monitoring considers current location.

## B2 — Weather

Morning weather includes:

- [ ] Current conditions
- [ ] Current temperature
- [ ] Daily high
- [ ] Daily low
- [ ] Sunrise
- [ ] Sunset
- [ ] Significant advisories
- [ ] Significant risks
- [ ] Useful short-term outlook
- [ ] Hourly outlook

## B3 — Weather Visualization

- [ ] Visual hourly weather graph displayed when supported.
- [ ] Graph appears in or adjacent to Weather.
- [ ] Temperature progression is easy to understand.
- [ ] Significant precipitation emphasized when appropriate.
- [ ] Significant hazards emphasized when appropriate.
- [ ] Text/table fallback exists when graphical rendering is unavailable.

---

# C — News Coverage

Morning EIB deliberately considers:

## C1 — Local / Regional

- [ ] Breaking local news
- [ ] Public safety
- [ ] Transportation
- [ ] Utilities
- [ ] Weather
- [ ] Wildfires
- [ ] Air quality
- [ ] Regional government
- [ ] Major regional economic developments
- [ ] Events likely to affect the user's day

## C2 — California

- [ ] Major California news
- [ ] State government
- [ ] Legislature
- [ ] Governor / executive actions
- [ ] Economy
- [ ] Emergencies
- [ ] Major regulatory developments
- [ ] State workforce when relevant

## C3 — National

- [ ] Federal government
- [ ] Economy
- [ ] Major court decisions
- [ ] National emergencies
- [ ] Significant political developments
- [ ] Infrastructure disruptions
- [ ] Public safety
- [ ] Major societal developments

## C4 — International

- [ ] National security
- [ ] Armed conflicts
- [ ] Major geopolitical changes
- [ ] Diplomacy
- [ ] International economy
- [ ] Energy
- [ ] Global trade
- [ ] Major disasters
- [ ] Significant U.S. implications
- [ ] Significant California implications

---

# D — Technology, AI and Cybersecurity

Morning EIB deliberately considers:

- [ ] Major technology developments
- [ ] Artificial intelligence
- [ ] AI governance
- [ ] Major technology outages
- [ ] Cloud-service disruptions
- [ ] Developer-platform disruptions
- [ ] Significant cybersecurity incidents
- [ ] Significant vulnerabilities
- [ ] Active exploitation
- [ ] Ransomware
- [ ] Critical-infrastructure threats
- [ ] Significant federal cybersecurity guidance

Technical filtering:

- [ ] Routine vulnerabilities do not overwhelm EIB.
- [ ] Specialist technical reporting remains separate when appropriate.
- [ ] Executive-impacting technical events are elevated appropriately.
- [ ] Known human cyber dispositions are considered before presenting previously evaluated issues.

---

# E — Freshness and Aging

- [ ] New information receives appropriate priority.
- [ ] Persistent active risk retains appropriate awareness.
- [ ] Stale information drops out.
- [ ] Repetitive summaries are avoided.
- [ ] Previously reported stories remain only when materially relevant.
- [ ] New facts can re-elevate a story.
- [ ] Material status changes can re-elevate a story when relevant.
- [ ] Resolution is reported only when useful.

Operating principle:

> **New information earns attention. Persistent risk retains appropriate awareness. Stale repetition drops out.**

---

# F — Executive Presentation

## F1 — Relevance

- [ ] Important stories receive concise relevance analysis.
- [ ] Professional implications identified when genuine.
- [ ] Personal implications identified when useful.
- [ ] Professional connections are not artificially manufactured.

## F2 — Classification

Stories may result in:

- [ ] Action Required
- [ ] Executive / Personal Awareness
- [ ] Continue Monitoring
- [ ] No Action Required
- [ ] EIB does not manufacture an action.

## F3 — Read Time

- [ ] Approximately 5–7 minutes.
- [ ] Breadth achieved through prioritization.
- [ ] Summaries remain concise.
- [ ] Repetition minimized.
- [ ] Important categories are not eliminated simply to reduce length.

---

# G — Continuous Awareness

## G1 — Monitoring

- [ ] Begins after Morning EIB.
- [ ] Target interval approximately every two hours.
- [ ] Continues through active day.
- [ ] Compares against Morning EIB and previous Breaking Updates.
- [ ] Does not regenerate complete EIB every two hours.

## G2 — Purpose

Every cycle asks:

> **Has something happened that may reasonably require the user to take action or make a decision now?**

- [ ] Monitoring searches broadly.
- [ ] Notification remains narrowly filtered.
- [ ] Discovery of important news does not itself require notification.

## G3 — Silence

When nothing qualifies:

- [ ] No Breaking Update.
- [ ] No ChatGPT notification.
- [ ] No email.
- [ ] No "nothing happened" alert.

> **Silence is successful system behavior.**

---

# H — Breaking Update Right-Now Action Gate

Before interrupting the user:

- [ ] Is this materially relevant to the user?
- [ ] Could it reasonably cause action or a decision **RIGHT NOW**?
- [ ] Is it genuinely new or materially changed?
- [ ] Has a prior human disposition already closed or excluded it?
- [ ] Would waiting until the Morning EIB materially reduce response value?

If the Right-Now Action test fails:

> **Morning EIB is the default destination.**

Possible immediate interests include:

- [ ] Health
- [ ] Safety
- [ ] Family
- [ ] Current location
- [ ] Travel
- [ ] Financial exposure
- [ ] Network availability
- [ ] Cybersecurity
- [ ] Technology operations
- [ ] Business operations
- [ ] DDS responsibilities
- [ ] Emergency response
- [ ] Critical infrastructure

Operating principle:

> **Important does not equal Breaking.**

> **Breaking means immediate awareness may reasonably change what the user does now.**

---

# I — Alert-Fatigue Protection

The following alone do not trigger Breaking Updates:

- [ ] Major media attention
- [ ] Historical significance
- [ ] Political significance
- [ ] International significance
- [ ] Large numbers of people affected
- [ ] Routine vulnerability disclosure
- [ ] CVSS severity alone
- [ ] CISA KEV inclusion alone
- [ ] Active exploitation alone
- [ ] Routine market movement
- [ ] Government announcement alone
- [ ] Corporate announcement alone
- [ ] Material-but-nonactionable incident lifecycle change

Important but nonurgent information waits for the Morning EIB.

When uncertain:

> **Hold for morning.**

---

# J — Operational Examples

Acceptance behavior must reproduce these decisions.

## J1 — Remote Major Wildfire

Example: major Texas wildfire without current-location, family, travel, work, infrastructure, or immediate safety impact.

Expected:

- [ ] Event recognized as important.
- [ ] Breaking Update suppressed.
- [ ] Event considered for Morning EIB.

## J2 — Major Geopolitical / Economic Announcement

Example: expanded U.S. sanctions on Iran without immediate financial, travel, operational, or governmental action requirement.

Expected:

- [ ] Event recognized.
- [ ] Breaking Update suppressed.
- [ ] Event considered for Morning EIB.

## J3 — Relevant Technology Outage

Example: significant GitHub outage during active GitHub/EIB work.

Expected:

- [ ] Official status checked.
- [ ] Operational relevance identified.
- [ ] Right-Now Action Gate passes when outage affects current activity.
- [ ] Breaking Update generated when appropriate.

---

# K — Cybersecurity Applicability

## K1 — Initial Evaluation

For newly relevant cybersecurity issues:

- [ ] Determine whether affected technology is known or plausibly present.
- [ ] Absence from approved-software inventory alone does not establish N/A.
- [ ] Human SecOps evaluation is requested when required.
- [ ] Evidence source is retained.

## K2 — Human Disposition

Recognized states include:

- [ ] Applicable
- [ ] Potentially Applicable
- [ ] Investigating
- [ ] Not Applicable / N/A
- [ ] Closed
- [ ] Reopened

Once authorized SecOps determines N/A or Closed:

- [ ] Determination is retained.
- [ ] Determination is honored by Breaking monitoring.
- [ ] Routine new reporting about the same issue does not reopen it.
- [ ] Repeated Breaking Updates are suppressed.

## K3 — Reopening

A closed/N/A issue may be reopened only when materially new evidence plausibly changes applicability.

Examples:

- [ ] Newly discovered deployment
- [ ] Newly affected product
- [ ] New supply-chain dependency
- [ ] New third-party exposure
- [ ] New evidence of compromise
- [ ] Material expansion of affected versions
- [ ] Human SecOps reopens issue

## K4 — Zimbra Acceptance Case

Given:

> DDS has provided a human-validated N/A determination for Zimbra.

When:

> Additional reporting states Zimbra exploitation has expanded.

Expected:

- [ ] Prior DDS disposition retrieved.
- [ ] N/A determination honored.
- [ ] No Breaking Update generated.
- [ ] Issue remains closed unless new evidence plausibly changes DDS applicability.

---

# L — Breaking Categories

Continuous Awareness may monitor:

- [ ] Local / regional emergencies
- [ ] California emergencies
- [ ] Major U.S. developments
- [ ] Major international developments
- [ ] Cybersecurity incidents
- [ ] Active exploitation
- [ ] Technology outages
- [ ] Cloud outages
- [ ] AI-platform outages
- [ ] Developer-platform outages
- [ ] Financial-market disruptions
- [ ] Economic shocks
- [ ] Critical infrastructure
- [ ] Natural disasters
- [ ] Severe weather
- [ ] Wildfires
- [ ] Air-quality emergencies
- [ ] Transportation disruptions
- [ ] Public-safety events

> **Category membership alone never satisfies the Breaking threshold.**

---

# M — Operational Status Monitoring

Explicit monitoring includes when relevant:

- [ ] GitHub
- [ ] GitHub Actions
- [ ] GitHub Copilot
- [ ] Microsoft
- [ ] Microsoft 365
- [ ] Microsoft Copilot
- [ ] Azure
- [ ] Major cloud platforms
- [ ] Major AI platforms
- [ ] Other platforms relevant to current activity

Minor degradation does not automatically require interruption.

---

# N — Source Quality

## N1 — Tier 1

Prefer:

- [ ] Vendor status pages
- [ ] Vendor security advisories
- [ ] Government alerts
- [ ] CISA
- [ ] National Weather Service
- [ ] Emergency-management agencies
- [ ] Official government announcements

## N2 — Tier 2

Use reputable reporting for:

- [ ] Corroboration
- [ ] Context
- [ ] Scope
- [ ] Consequences

## N3 — Tier 3

Supporting indicators may include:

- [ ] Downdetector
- [ ] Credible community reporting
- [ ] Other outage aggregators
- [ ] Supporting indicators are not authoritative root-cause sources.

---

# O — Deduplication and Lifecycle

- [ ] Already-reported events tracked.
- [ ] Identical information not re-alerted.
- [ ] A material change alone does not automatically trigger another alert.
- [ ] Changed status must itself pass the Right-Now Action Gate.
- [ ] Severity increase may trigger only when immediate relevance changes.
- [ ] Scope expansion may trigger only when immediate relevance changes.
- [ ] New security implications may trigger when actionable.
- [ ] Recovery may trigger when knowing now changes behavior.
- [ ] Resolution may trigger when knowing now changes behavior.

Possible states:

- [ ] Emerging
- [ ] Investigating
- [ ] Confirmed
- [ ] Identified
- [ ] Mitigating
- [ ] Recovering
- [ ] Monitoring
- [ ] Resolved

> **Not every lifecycle transition requires notification.**

---

# P — Breaking Update Presentation

A qualifying alert contains:

- [ ] What happened
- [ ] When
- [ ] Current status
- [ ] **Why it matters now**
- [ ] Immediate action when appropriate
- [ ] Authoritative sources
- [ ] Significantly shorter than Morning EIB

If no plausible immediate action or decision can be identified:

- [ ] Reconsider whether the event qualifies as Breaking.

Do not manufacture an action merely to justify an alert.

---

# Q — Alert Delivery

For every qualifying Breaking Update:

- [ ] Display in ChatGPT.
- [ ] Send to designated personal email.
- [ ] Send to designated work email.
- [ ] Mark IMPORTANT / High Priority when technically supported.

Recommended subject:

> **IMPORTANT — EIB Breaking Update — [Event]**

Email contains:

- [ ] What happened
- [ ] When
- [ ] Current status
- [ ] Why it matters now
- [ ] Immediate action when appropriate
- [ ] Sources

---

# R — Delivery Integrity

System distinguishes:

- [ ] Delivered
- [ ] Delivered and marked Important
- [ ] Delivery attempt failed
- [ ] Delivery capability unavailable
- [ ] Never claim delivery without successful execution.
- [ ] ChatGPT alert still displays if email delivery fails.
- [ ] Failure disclosed concisely.

---

# S — Following-Morning Continuity

- [ ] Important events suppressed from Breaking remain eligible for Morning EIB.
- [ ] Previous Breaking Updates considered.
- [ ] Entire prior alerts not automatically repeated.
- [ ] Continuing incidents receive useful status when appropriate.
- [ ] Resolved incidents included only when still relevant.
- [ ] No-longer-relevant incidents drop out.

> **Suppressed from Breaking does not mean unimportant. It means it can wait until morning.**

---

# T — Acceptance Testing

Before EIB v8 is complete, test:

## Scenario 1 — Normal Morning

Expected:

- [ ] Weather graph.
- [ ] Sunrise/sunset.
- [ ] Local through international news.
- [ ] 5–7 minute read.

## Scenario 2 — Traveling

Expected:

- [ ] Travel location drives weather.
- [ ] Travel location drives local awareness.
- [ ] Home location does not incorrectly dominate.

## Scenario 3 — Relevant Major Technology Outage

Expected:

- [ ] Official status detected.
- [ ] Relevance determined.
- [ ] Right-Now Action Gate evaluated.
- [ ] Breaking Update generated only when current action/decision may change.
- [ ] IMPORTANT email generated when alert qualifies.

## Scenario 4 — Remote Major Emergency

Expected:

- [ ] Event recognized.
- [ ] No Breaking Update absent direct impact.
- [ ] Event retained for Morning EIB when important.

## Scenario 5 — Important Geopolitical Development

Expected:

- [ ] Event recognized.
- [ ] No Breaking Update absent immediate actionable consequence.
- [ ] Morning EIB consideration retained.

## Scenario 6 — New Relevant Cyber Vulnerability

Expected:

- [ ] Applicability evaluated.
- [ ] Approved-software inventory treated as evidence, not sole proof.
- [ ] Human disposition obtained when required.
- [ ] Breaking alert only when plausible relevance and immediate action threshold both exist.

## Scenario 7 — Previously N/A Cyber Issue

Expected:

- [ ] Prior human disposition retrieved.
- [ ] N/A/Closed status honored.
- [ ] New reporting alone does not generate another alert.
- [ ] Reopen only with materially new applicability evidence.

## Scenario 8 — No Qualifying Change

Expected:

- [ ] Monitoring executes.
- [ ] No notification.
- [ ] No email.

## Scenario 9 — Repeated Incident Lifecycle Change

Expected:

- [ ] Duplicate suppressed.
- [ ] Status change evaluated against Right-Now Action Gate.
- [ ] No alert merely because incident moved from one lifecycle state to another.

## Scenario 10 — Meaningful Service Restoration

Expected:

- [ ] Restoration evaluated for immediate practical value.
- [ ] Resolution alert generated only when knowing now changes what the user should do.

## Scenario 11 — Email Failure

Expected:

- [ ] ChatGPT alert still displays.
- [ ] Failed delivery not represented as successful.
- [ ] User informed concisely.

---

# U — v8 Release Gate

EIB v8 is not fully implemented until:

- [ ] Morning enhancement incorporated.
- [ ] Continuous Awareness enhancement incorporated.
- [ ] Right-Now Action Gate incorporated.
- [ ] Human cyber disposition logic incorporated.
- [ ] N/A/closed suppression incorporated.
- [ ] Deduplication incorporated.
- [ ] Lifecycle action gate incorporated.
- [ ] Requirements reviewed.
- [ ] Acceptance scenarios tested.
- [ ] Material failures corrected.
- [ ] Master prompt reflects approved requirements.
- [ ] Automation reflects approved requirements.
- [ ] Notification implementation reflects approved requirements.
- [ ] Documentation reflects actual behavior.

---

# Final Acceptance Principle

EIB v8 must consistently answer:

> **Did the Morning EIB tell me what I needed to know?**

> **Did Breaking interrupt me only when something happened that may require me to do something now?**

> **Did important information that could wait get held for the Morning EIB instead?**

> **Did the system remain quiet when there was nothing worth interrupting me about?**

If all four are consistently true, EIB is operating as intended.

---

**Status:** Active  
**Next Step:** Use this checklist during EIB v8 implementation and validation.