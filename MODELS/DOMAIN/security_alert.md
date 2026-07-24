---
title: Security Alert Data Model
model_id: MODEL-005
version: 1.0
status: Approved
owner: BSJ
last_updated: 2026-07-24
---

# SecurityAlert

## Purpose

The `SecurityAlert` model represents a cybersecurity event, vulnerability, threat advisory, incident, or emerging risk that may require executive awareness or action.

Rather than preserving technical details alone, the model translates security information into business impact and executive decision support.

Each SecurityAlert should remain traceable to its originating source while enabling consistent prioritization across the Executive Intelligence Briefing (EIB).

---

# Required Fields

| Field | Type | Description |
|--------|------|-------------|
| id | UUID/String | Unique EIB identifier |
| source | String | Originating connector or security source |
| title | String | Alert title |
| summary | Markdown | Executive summary |
| severity | Enum | Technical severity |
| priority | Integer | Executive priority (1–5) |
| confidence | Decimal | Confidence score |
| detected_timestamp | DateTime | Time the alert was identified |

---

# Optional Fields

| Field | Type | Description |
|--------|------|-------------|
| affected_systems | List[String] | Systems, applications, or services impacted |
| affected_business_units | List[String] | Organizational impact |
| cve | List[String] | Associated CVE identifiers |
| vendor | String | Vendor issuing the advisory |
| threat_actor | String | Threat actor if known |
| attack_vector | String | Initial attack vector |
| mitigation | Markdown | Recommended mitigation |
| executive_impact | Markdown | Business implications |
| action_required | Boolean | Indicates follow-up is recommended |
| source_reference | String | Original alert identifier |
| related_items | List[String] | Related EIB object IDs |
| source_items | List[String] | Supporting BriefingItem IDs |
| url | String | Source reference |

---

# Severity Levels

Technical severity uses:

| Severity | Meaning |
|----------|---------|
| Critical | Immediate exploitation or severe business impact |
| High | Significant security concern |
| Medium | Moderate security concern |
| Low | Limited security concern |
| Informational | Awareness only |

Severity represents technical impact.

Executive priority represents business impact.

These values should not automatically be identical.

---

# Executive Intelligence

Each SecurityAlert should answer:

- What happened?
- Why does it matter?
- Who or what is affected?
- What is the business risk?
- What action is recommended?
- Is executive awareness required?

---

# Business Impact

Possible business impacts include:

- Service disruption
- Regulatory exposure
- Privacy impact
- Financial loss
- Reputation damage
- Operational degradation
- Third-party dependency risk

Business impact should be described in executive language rather than technical terminology.

---

# Relationships

SecurityAlert may reference:

- BriefingItem
- ActionItem
- Risk
- ExecutiveDecision
- ProjectUpdate

---

# Lifecycle

1. Collected
2. Normalized
3. Correlated
4. Prioritized
5. Validated
6. Published
7. Archived

---

# Validation Rules

A valid SecurityAlert must:

- Include a title
- Include severity
- Include detected timestamp
- Include an executive summary
- Have a priority between 1 and 5
- Have confidence between 0.00 and 1.00
- Preserve source traceability

---

# Example

```yaml
id: security-alert-001
source: CISA
title: Critical Vulnerability in Internet-Facing VPN Appliance
summary: >
  A critical vulnerability affecting internet-facing VPN appliances
  is being actively exploited. Organizations should apply vendor
  patches immediately.
severity: Critical
priority: 1
confidence: 0.99
detected_timestamp: 2026-07-24T07:15:00-07:00
affected_systems:
  - Remote Access VPN
vendor: Example Vendor
mitigation: >
  Apply the latest security update and review authentication logs
  for indicators of compromise.
action_required: true
```

---

# Future Enhancements

Future releases may include:

- CVSS scoring
- EPSS probability
- MITRE ATT&CK mappings
- KEV catalog integration
- Threat intelligence correlation
- Asset criticality scoring
- Automated remediation recommendations
- Historical trend analysis

---

# Success Criteria

A SecurityAlert is successful when an executive can determine in less than one minute:

- What the threat is
- The potential business impact
- Whether immediate action is required
- The recommended next steps
- The confidence in the information

The SecurityAlert model translates technical cybersecurity events into actionable executive intelligence while preserving the traceability required for informed decision-making.