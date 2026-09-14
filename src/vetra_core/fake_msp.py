"""Deterministic in-memory MSP adapter for contract and integration tests."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Sequence

from .msp_adapter import MspEnvironment, MspTaskSnapshot


@dataclass
class FakeMspAdapter:
    env: MspEnvironment = field(default_factory=lambda: MspEnvironment(
        product="Microsoft Project", version="2024", edition="Professional",
        office_version="2024", windows_version="Windows 11"))
    tasks: list[MspTaskSnapshot] = field(default_factory=list)
    opened_path: str | None = None
    saved_path: str | None = None
    project_start: date | None = None

    def environment(self) -> MspEnvironment:
        return self.env

    def list_tasks(self) -> Sequence[MspTaskSnapshot]:
        return tuple(self.tasks)

    def set_project_start(self, day: date) -> None:
        self.project_start = day

    def save_mpp(self, path: str) -> None:
        self.saved_path = str(Path(path))

    def open_mpp(self, path: str) -> None:
        self.opened_path = str(Path(path))
