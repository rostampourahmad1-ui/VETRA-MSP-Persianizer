"""Versioned holiday data boundary for official and project holidays."""
from __future__ import annotations

from dataclasses import asdict
from datetime import date
import json
from pathlib import Path

from .calendar import Holiday, IranianWorkCalendar


class HolidayCatalog:
    def __init__(self, version: str = "2026.1", holidays: list[Holiday] | None = None) -> None:
        self.version = version
        self.holidays = holidays or []

    def apply_to(self, calendar: IranianWorkCalendar) -> None:
        for holiday in self.holidays:
            calendar.add_holiday(holiday)

    def save(self, path: str | Path) -> None:
        payload = {"version": self.version, "holidays": [
            {"day": item.day.isoformat(), "title": item.title, "kind": item.kind}
            for item in self.holidays
        ]}
        Path(path).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "HolidayCatalog":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        holidays = [Holiday(date.fromisoformat(item["day"]), item["title"], item.get("kind", "official")) for item in payload["holidays"]]
        return cls(str(payload["version"]), holidays)
