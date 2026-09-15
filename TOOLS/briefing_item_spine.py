from __future__ import annotations

import json
import os

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


VALID_PRIORITIES = {1, 2, 3, 4, 5}


@dataclass
class BriefingItem:
    id: str
    source: str
    category: str
    title: str
    summary: str
    timestamp: str
    priority: int
    confidence: float
    url: Optional[str] = None
    author: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    affected_systems: List[str] = field(default_factory=list)
    due_date: Optional[str] = None
    owner: Optional[str] = None
    action_required: bool = False
    action_item: Optional[str] = None
    related_items: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._validate_required_fields()
        self._normalize_values()

    def _validate_required_fields(self) -> None:
        required = {
            "id": self.id,
            "source": self.source,
            "category": self.category,
            "title": self.title,
            "summary": self.summary,
            "timestamp": self.timestamp,
            "priority": self.priority,
            "confidence": self.confidence,
        }
        for field_name, value in required.items():
            if value is None or value == "":
                raise ValueError(f"Required BriefingItem field '{field_name}' is missing.")

        if self.priority not in VALID_PRIORITIES:
            raise ValueError(f"priority must be one of {sorted(VALID_PRIORITIES)}")

        if not 0.0 <= float(self.confidence) <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")

        self._parse_timestamp(self.timestamp)

    def _normalize_values(self) -> None:
        self.id = str(self.id).strip()
        self.source = str(self.source).strip()
        self.category = str(self.category).strip()
        self.title = str(self.title).strip()
        self.summary = str(self.summary).strip()
        self.priority = int(self.priority)
        self.confidence = float(self.confidence)
        self.tags = [str(item).strip() for item in (self.tags or []) if str(item).strip()]
        self.affected_systems = [str(item).strip() for item in (self.affected_systems or []) if str(item).strip()]
        self.related_items = [str(item).strip() for item in (self.related_items or []) if str(item).strip()]

        timestamp = self._parse_timestamp(self.timestamp)
        self.timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ") if timestamp.tzinfo else timestamp.strftime("%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def _parse_timestamp(value: str) -> datetime:
        if not isinstance(value, str):
            raise ValueError("timestamp must be a string")
        text = value.strip()
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(text)
        except ValueError as exc:
            raise ValueError(f"Invalid timestamp: {value}") from exc
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["confidence"] = float(data["confidence"])
        data["priority"] = int(data["priority"])
        return data


def normalize_record(raw: Dict[str, Any]) -> BriefingItem:
    if not isinstance(raw, dict):
        raise ValueError("Fixture record must be a dictionary.")

    normalized = {
        "id": raw.get("id"),
        "source": raw.get("source"),
        "category": raw.get("category"),
        "title": raw.get("title"),
        "summary": raw.get("summary"),
        "timestamp": raw.get("timestamp"),
        "priority": raw.get("priority"),
        "confidence": raw.get("confidence"),
        "url": raw.get("url"),
        "author": raw.get("author"),
        "tags": raw.get("tags", []),
        "affected_systems": raw.get("affected_systems", []),
        "due_date": raw.get("due_date"),
        "owner": raw.get("owner"),
        "action_required": bool(raw.get("action_required", False)),
        "action_item": raw.get("action_item"),
        "related_items": raw.get("related_items", []),
    }
    return BriefingItem(**normalized)


def normalize_records(records: List[Dict[str, Any]]) -> List[BriefingItem]:
    if not isinstance(records, list):
        raise ValueError("Fixture input must be a list of record dictionaries.")
    items = [normalize_record(item) for item in records]
    return sorted(items, key=lambda item: (item.timestamp, item.id))


def main() -> int:
    fixture_path = os.path.join(os.path.dirname(__file__), "fixtures", "synthetic_briefing_items.json")
    if not os.path.exists(fixture_path):
        raise FileNotFoundError(f"Fixture not found: {fixture_path}")

    with open(fixture_path, "r", encoding="utf-8") as handle:
        records = json.load(handle)

    items = normalize_records(records)
    payload = [item.to_dict() for item in items]
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
