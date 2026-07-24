---
title: Run EIB Workflow Prompt
prompt_id: WF-001
version: 1.0
status: Production
owner: BSJ
last_updated: 2026-07-24
system_prompt: SYS-001
---

# Run Executive Intelligence Briefing

## Objective

Execute the complete Executive Intelligence Briefing workflow using the configured application settings, executive profile, enabled connectors, and system prompt.

Produce a concise, actionable, executive-quality briefing.

---

# Phase 1 – Initialization

1. Load application configuration.
2. Load the active executive profile.
3. Determine enabled data sources.
4. Initialize execution context.
5. Record workflow start time.

If any required configuration is unavailable, report the issue and continue where possible.

---

# Phase 2 – Data Collection

Collect information from every enabled source.

Potential sources include:

- Gmail
- Google Calendar
- GitHub
- Web News
- RSS
- Local Documents
- Future Connectors

For each source:

- Collect new information.
- Record collection success or failure.
- Ignore duplicate records.
- Continue if a non-critical source fails.

---

# Phase 3 – Normalization

Convert all collected information into a common internal structure.

Each record should contain, where available:

- Source
- Timestamp
- Topic
- Priority
- Summary
- URL or citation
- Confidence

---

# Phase 4 – Analysis

Analyze the collected information.

Identify:

- Risks
- Opportunities
- Deadlines
- Emerging trends
- Calendar conflicts
- Follow-up items
- Executive decisions

Merge related information into unified summaries.

---

# Phase 5 – Prioritization

Rank items by executive importance.

Priority order:

1. Immediate action required
2. Executive decision needed
3. High business risk
4. Regulatory impact
5. Security concerns
6. Operational issues
7. Strategic opportunities
8. General awareness

Do not prioritize based solely on recency.

---

# Phase 6 – Executive Summary

Prepare a one-page executive summary that answers:

- What changed?
- What matters?
- What requires attention?
- What decisions are pending?

The summary should be readable in approximately one minute.

---

# Phase 7 – Detailed Briefing

Generate the remaining briefing sections:

- Calendar
- Important Communications
- Cybersecurity
- Artificial Intelligence
- Technology
- Leadership
- Projects
- Action Items

Omit sections without meaningful updates.

---

# Phase 8 – Validation

Before publishing verify:

- No duplicated information.
- Citations included where applicable.
- Confidence levels assigned.
- Action items are supported.
- Risks properly prioritized.
- Writing is concise.
- Grammar is correct.

---

# Phase 9 – Publish

Produce the final Executive Intelligence Briefing.

Append:

- Execution timestamp
- Data sources used
- Connector failures
- Overall confidence assessment

---

# Error Handling

If a connector fails:

- Record the failure.
- Continue execution.
- Note the missing information in the final report.

If information conflicts:

- Explain the discrepancy.
- Prefer primary sources.
- Reduce confidence appropriately.

Never fabricate missing information.

---

# Completion Criteria

The workflow is complete when:

- All enabled connectors have been processed.
- Executive priorities have been ranked.
- The report has been validated.
- Action items have been identified.
- Output is suitable for executive consumption.

The final result should enable an executive to understand the most important developments of the day in less than ten minutes while providing sufficient detail for follow-up when needed.