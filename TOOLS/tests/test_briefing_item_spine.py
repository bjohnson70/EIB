import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO

from TOOLS.briefing_item_spine import BriefingItem, main, normalize_record, normalize_records


class BriefingItemSpineTests(unittest.TestCase):
    def setUp(self):
        self.fixture = [
            {
                "id": "briefing-001",
                "source": "github",
                "category": "engineering",
                "title": "Review pull request backlog",
                "summary": "There are open PRs that need review before release.",
                "timestamp": "2026-09-13T08:00:00Z",
                "priority": 2,
                "confidence": 0.9,
                "url": "https://example.com/prs",
                "author": "alice@contoso.com",
                "tags": ["pull-request", "release"],
                "affected_systems": ["github"],
                "due_date": "2026-09-14",
                "owner": "eng-lead",
                "action_required": True,
                "action_item": "Review the top two pull requests.",
                "related_items": ["briefing-003"]
            },
            {
                "id": "briefing-002",
                "source": "gmail",
                "category": "operations",
                "title": "Leadership update from executive team",
                "summary": "The leadership team requested a review of follow-up actions.",
                "timestamp": "2026-09-13T07:30:00-04:00",
                "priority": 3,
                "confidence": 0.75,
                "author": "team-lead@example.com",
                "tags": ["executive", "follow-up"],
                "action_required": False,
                "owner": "ceo"
            },
            {
                "id": "briefing-003",
                "source": "security",
                "category": "security",
                "title": "Infrastructure patch window",
                "summary": "A maintenance window is scheduled for the platform.",
                "timestamp": "2026-09-13T09:15:00Z",
                "priority": 1,
                "confidence": 0.95,
                "affected_systems": ["platform"],
                "tags": ["maintenance", "security"],
                "action_required": True,
                "action_item": "Schedule the patch review and approval."
            },
            {
                "id": "briefing-004",
                "source": "calendar",
                "category": "operations",
                "title": "Board briefing prep",
                "summary": "Board materials need final review before the meeting.",
                "timestamp": "2026-09-13T12:00:00Z",
                "priority": 2,
                "confidence": 0.88,
                "due_date": "2026-09-13",
                "owner": "operations"
            }
        ]

    def test_fixture_loads_and_normalizes(self):
        items = normalize_records(self.fixture)
        self.assertEqual(len(items), 4)
        self.assertTrue(all(isinstance(item, BriefingItem) for item in items))
        self.assertEqual(
            [item.id for item in items],
            ["briefing-001", "briefing-003", "briefing-002", "briefing-004"],
        )

    def test_required_fields_are_validated(self):
        bad = dict(self.fixture[0])
        bad.pop("title")
        with self.assertRaises(ValueError):
            normalize_record(bad)

    def test_invalid_priority_is_rejected(self):
        bad = dict(self.fixture[0])
        bad["priority"] = 9
        with self.assertRaises(ValueError):
            normalize_record(bad)

    def test_invalid_confidence_is_rejected(self):
        bad = dict(self.fixture[0])
        bad["confidence"] = 1.5
        with self.assertRaises(ValueError):
            normalize_record(bad)

    def test_invalid_timestamp_is_rejected(self):
        bad = dict(self.fixture[0])
        bad["timestamp"] = "not-a-date"
        with self.assertRaises(ValueError):
            normalize_record(bad)

    def test_serialization_is_deterministic(self):
        item = normalize_record(self.fixture[0])
        data = item.to_dict()
        self.assertEqual(data["id"], "briefing-001")
        self.assertEqual(data["timestamp"], "2026-09-13T08:00:00Z")
        self.assertEqual(data["priority"], 2)
        self.assertEqual(data["confidence"], 0.9)

    def test_main_loads_fixture_and_emits_structured_output(self):
        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(), 0)

        records = json.loads(output.getvalue())
        self.assertEqual(len(records), 4)
        self.assertEqual(
            [record["id"] for record in records],
            ["briefing-001", "briefing-003", "briefing-002", "briefing-004"],
        )
        self.assertEqual(records[2]["timestamp"], "2026-09-13T11:30:00Z")


if __name__ == "__main__":
    unittest.main()
