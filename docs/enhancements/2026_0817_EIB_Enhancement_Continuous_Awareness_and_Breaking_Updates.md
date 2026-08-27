# EIB Enhancement — Continuous Awareness and Breaking Updates

**Date:** 2026-08-17  
**Last Updated:** 2026-08-27  
**Status:** Approved Enhancement  
**Target:** EIB v8  
**Applies To:** EIB Continuous Awareness / Breaking Updates

---

## Purpose

This document codifies the approved requirements for extending the EIB beyond the once-daily morning briefing.

The morning EIB establishes the intelligence baseline for the day.

Significant events may occur after that briefing. The EIB therefore requires a lightweight Continuous Awareness capability that periodically checks for developments that may require immediate user awareness, action, or decision-making.

The operating model is:

> **Morning EIB = comprehensive daily intelligence baseline.**

> **EIB Breaking Update = exception-based notification of something that may require action or a decision right now.**

The objective is:

> **Awareness without alert fatigue.**

---

# Requirement 1 — Continuous Awareness

After the morning EIB is generated, the system should periodically check for significant new developments throughout the active day.

The target interval is approximately:

> **Every two hours**

The purpose is not to regenerate the complete EIB every two hours.

Each monitoring cycle should instead ask:

> **Has something happened since the morning EIB or most recent Breaking Update that may reasonably require the user to take action or make a decision now?**

If no qualifying development exists:

> **Do not notify.**

Silence is the correct and preferred result when nothing meets the Breaking Update threshold.

---

# Requirement 2 — Right-Now Action Gate

A Breaking Update is an interruption.

Therefore, the primary qualification test is:

> **Could this reasonably cause me to take action or make a decision right now?**

If the answer is **No**, the event should normally wait for the next morning EIB.

Examples of possible immediate actions include:

- Change travel plans
- Protect personal or family safety
- Change financial activity
- Investigate a cybersecurity exposure
- Direct SecOps or IT staff to investigate
- Apply emergency mitigation
- Avoid or stop using an affected technology service
- Change an operational process
- Respond to an active outage
- Prepare for severe weather
- Respond to an emergency
- Take another action that loses meaningful value if delayed until tomorrow

An event does not need to guarantee action.

There must, however, be a reasonable possibility that immediate awareness could change what the user does now.

---

# Requirement 3 — Important Is Not Breaking

The EIB must distinguish between:

## Important

Significant information that belongs in the intelligence picture but can reasonably wait until the next morning briefing.

## Breaking

A significant development where immediate awareness may reasonably change an action, decision, or response.

The following characteristics alone do **not** make an event Breaking:

- Large scale
- High severity
- Major news coverage
- Political importance
- Historical importance
- International importance
- Large numbers of people affected
- Significant economic implications
- A newly disclosed vulnerability
- Active exploitation somewhere in the world
- A government announcement
- A major corporate announcement

The question remains:

> **Does this create a plausible reason for the user to do something now?**

If not:

> **Hold for the morning EIB.**

---

# Requirement 4 — Default to Morning EIB

The Morning EIB is the normal destination for important intelligence.

Breaking Updates are the exception.

When deciding between the two:

> **Morning EIB is the default.**

> **Breaking Update requires additional justification.**

When uncertain whether an event warrants interruption:

> **Hold it for the morning EIB.**

The system should not generate a Breaking Update merely because it found an important new story during a monitoring cycle.

---

# Requirement 5 — Operational Lessons

Operational use during August 2026 demonstrated that the original Breaking threshold remained too permissive.

Several examples established the need for a stricter action-oriented gate.

## Example — Major Texas Wildfire

A major wildfire affecting tens of thousands of acres in Texas is important U.S. news.

However, absent:

- Current-location impact
- Family impact
- Travel impact
- Business impact
- Infrastructure dependency
- Immediate personal safety implications
- Another direct reason for action

the event does not require interruption.

**Disposition: Morning EIB**

---

## Example — Expanded U.S. Sanctions on Iran

Expansion of U.S. sanctions against Iran may be geopolitically and economically significant.

However, absent an immediate:

- Financial decision
- Market exposure
- Travel issue
- Government responsibility
- Business impact
- Operational consequence

the announcement does not require immediate interruption.

**Disposition: Morning EIB**

---

## Example — Zimbra Active Exploitation

Active exploitation of a serious vulnerability may initially justify evaluation.

However, DDS subsequently provided a human-validated determination that Zimbra is not applicable to the organization.

Once that determination exists, additional reporting about exploitation of the same Zimbra issue does not justify repeatedly interrupting the user.

**Disposition: Suppress from Breaking Updates unless materially new intelligence plausibly reopens DDS applicability.**

---

## Example — GitHub Outage

A GitHub outage occurring during active use may immediately explain:

- Failed repository operations
- CI/CD failures
- GitHub Actions failures
- Development workflow problems
- Copilot disruption
- EIB development or automation failures

Immediate awareness can change what the user does.

**Disposition: Breaking Update when operational impact is significant and relevant.**

---

# Requirement 6 — Candidate Breaking Categories

Continuous Awareness should monitor:

- Current-location emergencies
- Severe weather
- Wildfires
- Air quality
- Transportation disruptions
- Public-safety emergencies
- Cybersecurity incidents
- Active exploitation
- Major technology outages
- Cloud-service disruptions
- AI-platform disruptions
- Developer-platform outages
- Financial-market disruptions
- Critical infrastructure incidents
- Major government actions
- Major California developments
- Major U.S. developments
- Major international developments

However:

> **Category membership never automatically qualifies an event as Breaking.**

Every candidate must pass the Right-Now Action Gate.

---

# Requirement 7 — Cybersecurity Breaking Threshold

Cybersecurity requires special handling because technical severity can easily create excessive alerts.

A cybersecurity issue may qualify for a Breaking Update when:

1. The issue is materially relevant to the user's environment, responsibilities, systems, or interests;

**AND**

2. There is a reasonable possibility that immediate action, investigation, mitigation, or decision-making is warranted.

Examples include:

- Confirmed exposure to actively exploited technology
- Credible evidence of compromise
- Emergency vendor mitigation
- Active attack against relevant infrastructure
- Critical vulnerability in technology known or reasonably suspected to be present
- Significant identity or authentication compromise
- Major supply-chain compromise affecting relevant technology
- Government emergency directive affecting relevant systems
- Significant cyber incident affecting current operations

Active exploitation alone is insufficient.

A CVSS score alone is insufficient.

CISA KEV inclusion alone is insufficient.

News coverage alone is insufficient.

The affected technology must have plausible relevance and immediate operational significance.

---

# Requirement 8 — Human Cyber Disposition Overrides Routine Alerting

The EIB Cyber Intelligence process maintains human-validated applicability determinations.

Possible determinations include:

- Applicable
- Potentially Applicable
- Investigating
- Not Applicable / N/A
- Closed
- Reopened

When an authorized human SecOps determination establishes:

> **Not Applicable / N/A**

or:

> **Closed**

the EIB must retain and honor that determination.

Subsequent reporting about the same vulnerability, product, or issue must **not** automatically generate another Breaking Update.

Re-alerting requires materially new intelligence that plausibly invalidates or reopens the prior determination.

Examples include:

- Newly identified affected product previously believed unrelated
- Newly discovered DDS deployment
- New supply-chain dependency
- New third-party exposure
- New evidence of compromise
- Material expansion of affected versions that changes applicability
- Human SecOps reopening the issue

Absent such evidence:

> **Honor the human disposition and suppress the alert.**

---

# Requirement 9 — Inventory Evidence Does Not Replace Human Disposition

Absence of software from an approved-software or application inventory is not sufficient by itself to establish non-applicability.

For a newly relevant cybersecurity issue, an initial human SecOps evaluation may still be required.

However, once SecOps provides the human determination, that determination becomes authoritative for EIB alerting unless materially new evidence warrants reopening it.

This creates the sequence:

> **New cyber issue → Evaluate applicability → Human disposition → Honor disposition → Reopen only with materially new evidence**

---

# Requirement 10 — Technology and Service Status Monitoring

The EIB should deliberately monitor operational technology sources rather than relying solely on general news reporting.

Initial platforms should include, when relevant:

- GitHub
- GitHub Actions
- GitHub Copilot
- Microsoft services
- Microsoft Copilot
- Microsoft 365
- Azure
- Major cloud platforms
- Major AI platforms
- Other services relevant to current activity

An outage qualifies for Breaking notification when it is sufficiently relevant and operationally significant that knowing about it now may change user behavior.

Minor degradation does not automatically qualify.

---

# Requirement 11 — Source Hierarchy

Breaking Updates should use the strongest available sources.

## Tier 1 — Authoritative

Examples:

- Official vendor status pages
- Government alerts
- CISA
- National Weather Service
- Emergency-management agencies
- Official government announcements
- Vendor security advisories

## Tier 2 — Reputable Independent Reporting

Use established reporting to:

- Confirm scope
- Add context
- Explain consequences
- Identify broader impact

## Tier 3 — Supporting Indicators

Examples:

- Downdetector
- Credible community reporting
- Other outage aggregators

Supporting indicators should not normally establish authoritative root cause or incident status.

---

# Requirement 12 — Corroboration

When practical, significant Breaking Updates should be corroborated.

For technology outages:

> **Official service status + independent outage/reporting evidence**

is preferred when available.

For cybersecurity:

> **Government/vendor advisory + reputable security reporting**

is preferred when available.

Do not delay a genuinely urgent warning merely to achieve unnecessary source perfection.

Clearly identify uncertainty.

---

# Requirement 13 — Deduplication

Do not repeatedly notify the user about the same event.

A previously reported event should generate another Breaking Update only when:

1. Something materially changes;

**AND**

2. That change itself may reasonably alter what the user should do now.

A material change without actionable consequence does not automatically justify another alert.

---

# Requirement 14 — Incident Lifecycle

Typical incident states may include:

1. Emerging
2. Investigating
3. Confirmed
4. Identified
5. Mitigating
6. Recovering
7. Monitoring
8. Resolved

The user does not require an alert for every lifecycle transition.

Recovery or resolution should generate another Breaking Update only when knowing the changed status now has practical value.

For example:

A service outage may warrant:

> **Service restored — normal operations may resume.**

However, routine incremental changes such as:

> 20% contained → 27% contained

do not warrant another Breaking Update unless that change materially affects the user's actions, safety, travel, or decisions.

---

# Requirement 15 — Current Location

Continuous Awareness should consider the user's current location when available.

This is particularly important for:

- Severe weather
- Wildfires
- Air quality
- Transportation
- Public safety
- Regional emergencies
- Travel disruptions

A geographically distant emergency normally belongs in the Morning EIB unless it creates a direct reason for immediate action.

Do not assume the normal home location when current travel/location information indicates otherwise.

---

# Requirement 16 — Personal and Operational Relevance

Breaking Update qualification should consider whether the event affects:

- User
- Family
- Current location
- Travel
- Finances
- Work responsibilities
- DDS operations
- Cybersecurity responsibilities
- Technology currently being used
- Critical services
- Immediate decision-making

The farther an event is from these interests, the stronger the justification required to interrupt the user.

---

# Requirement 17 — Breaking Update Format

Breaking Updates must be significantly shorter than the Morning EIB.

A standard alert should answer:

## What Happened?

Concise description.

## When?

Approximate start, discovery, or announcement time.

## Current Status

Examples:

- 🔴 Active / Escalating
- 🔴 Active Exploitation
- 🟠 Degraded / Mitigating
- 🟡 Monitoring / Recovering
- 🟢 Resolved

## Why It Matters Now

This section must explain why immediate awareness is justified.

## Action

When appropriate, state what the user may reasonably need to do now.

Do not manufacture an action.

If there is no plausible immediate action or decision:

> **Reconsider whether the event belongs in a Breaking Update at all.**

## Sources

Provide authoritative supporting sources.

---

# Requirement 18 — Alert Delivery

A qualifying EIB Breaking Update requires proactive delivery.

Approved model:

> **Breaking threshold met → EIB Breaking Update → ChatGPT notification → IMPORTANT email**

The user should not need to manually request another EIB to discover a truly urgent event.

---

# Requirement 19 — IMPORTANT Email

Every qualifying Breaking Update should generate an email to both designated delivery destinations:

- Personal email
- Work email

When supported, mark:

> **IMPORTANT / High Priority**

Recommended subject:

> **IMPORTANT — EIB Breaking Update — [Event]**

The email should contain:

- What happened
- When
- Current status
- Why it matters now
- Immediate action when appropriate
- Authoritative sources

---

# Requirement 20 — Delivery Integrity

Never claim that an email was sent unless delivery actually succeeded.

Possible states include:

- Delivered
- Delivered and Marked Important
- Delivery Attempt Failed
- Delivery Capability Unavailable

If email delivery fails, the ChatGPT alert may still display.

Disclose the delivery failure concisely.

---

# Requirement 21 — Silence Is a Successful Result

Continuous Awareness is not measured by the number of alerts produced.

A monitoring cycle that finds interesting developments but no Right-Now Action event should produce:

> **No alert.**

This is successful operation.

Do not send:

- Routine news summaries
- "Nothing happened" notices
- Low-value status changes
- Non-actionable geopolitical updates
- Remote emergencies without direct impact
- Cyber vulnerabilities already dispositioned N/A
- Routine vulnerability disclosures
- Repetitive incident lifecycle updates

Silence protects the value of the Breaking channel.

---

# Requirement 22 — Following-Morning Continuity

Important events suppressed from Breaking Updates because they failed the Right-Now Action Gate should still be considered for the next Morning EIB.

This includes:

- Important national news
- International developments
- Government actions
- Economic developments
- Remote disasters
- Significant but non-actionable cybersecurity intelligence
- Technology developments
- Material status changes

Suppression from Breaking does not mean the event is unimportant.

It means:

> **It can wait until morning.**

---

# Requirement 23 — Alert-Fatigue Protection

The purpose of Continuous Awareness is:

> **Awareness, not noise.**

The system should strongly favor fewer high-value alerts.

Before interrupting the user, ask:

1. **Is this materially relevant to me?**
2. **Could this reasonably cause me to take action or make a decision right now?**
3. **Has this already been dispositioned N/A or closed?**
4. **Is this genuinely new or materially changed?**
5. **Would delaying notification until the Morning EIB materially reduce my ability to respond?**

If these tests are not satisfied:

> **Do not interrupt.**

---

# Requirement 24 — Breaking Decision Gate

Use the following decision sequence:

```text
NEW EVENT
   ↓
Is it materially relevant to the user?
   ├── NO → Morning EIB or suppress
   ↓ YES
Could it reasonably require action or a decision RIGHT NOW?
   ├── NO → Morning EIB
   ↓ YES
Has it already been dispositioned N/A or closed?
   ├── YES → Suppress unless applicability materially reopens
   ↓ NO
Is this genuinely new or materially changed?
   ├── NO → Suppress duplicate
   ↓ YES
Would waiting until morning materially reduce response value?
   ├── NO → Morning EIB
   ↓ YES
BREAKING UPDATE