"""MSP integration contracts.

This module intentionally contains no scheduling logic. A Windows COM/VSTO
adapter will implement these protocols against Microsoft Project 2024.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol, Sequence


@dataclass(frozen=True)
class MspEnvironment:
    product: str
    version: str
    edition: str
    office_version: str | None = None
    windows_version: str | None = None


@dataclass(frozen=True)
class MspTaskSnapshot:
    uid: str
    name: str
    start: date | None
    finish: date | None
    duration_days: float | None
    predecessors: str = ""
    percent_complete: float = 0.0


class MspAdapter(Protocol):
    """Read/write boundary; all scheduling calculations stay in MSP."""

    def environment(self) -> MspEnvironment: ...

    def list_tasks(self) -> Sequence[MspTaskSnapshot]: ...

    def set_project_start(self, day: date) -> None: ...

    def save_mpp(self, path: str) -> None: ...

    def open_mpp(self, path: str) -> None: ...


class UnsupportedMspAdapter:
    """Safe placeholder until Windows/MSP integration is available."""

    def __init__(self, reason: str = "Microsoft Project adapter is not available on this platform") -> None:
        self.reason = reason

    def _fail(self) -> None:
        raise RuntimeError(self.reason)

    def environment(self) -> MspEnvironment:
        self._fail()

    def list_tasks(self) -> Sequence[MspTaskSnapshot]:
        self._fail()

    def set_project_start(self, day: date) -> None:
        self._fail()

    def save_mpp(self, path: str) -> None:
        self._fail()

    def open_mpp(self, path: str) -> None:
        self._fail()
