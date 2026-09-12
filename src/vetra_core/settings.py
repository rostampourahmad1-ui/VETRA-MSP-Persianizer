"""Versioned VETRA settings independent from the .MPP file."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass
class VetraSettings:
    schema_version: int = 1
    language: str = "fa-IR"
    calendar: str = "jalali"
    number_system: str = "persian"
    direction: str = "rtl"
    work_calendar: str = "administrative"
    date_format: str = "yyyy/MM/dd"
    msp_version_required: str = "Project 2024"

    def validate(self) -> None:
        if self.language not in {"fa-IR", "en-US"}:
            raise ValueError("Unsupported language")
        if self.calendar not in {"jalali", "gregorian"}:
            raise ValueError("Unsupported calendar")
        if self.number_system not in {"persian", "latin"}:
            raise ValueError("Unsupported number system")
        if self.direction not in {"rtl", "ltr"}:
            raise ValueError("Unsupported direction")

    def save(self, path: str | Path) -> None:
        self.validate()
        Path(path).write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "VetraSettings":
        settings = cls(**json.loads(Path(path).read_text(encoding="utf-8")))
        settings.validate()
        return settings
