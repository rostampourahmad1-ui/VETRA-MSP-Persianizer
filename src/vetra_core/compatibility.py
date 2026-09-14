"""Compatibility checks for before/after MPP snapshots."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Sequence

from .msp_adapter import MspTaskSnapshot


@dataclass(frozen=True)
class TaskDifference:
    uid: str
    field: str
    before: object
    after: object


@dataclass(frozen=True)
class CompatibilityReport:
    compatible: bool
    differences: tuple[TaskDifference, ...]
    missing_uids: tuple[str, ...]
    added_uids: tuple[str, ...]


def compare_task_snapshots(before: Sequence[MspTaskSnapshot], after: Sequence[MspTaskSnapshot]) -> CompatibilityReport:
    left = {task.uid: task for task in before}
    right = {task.uid: task for task in after}
    missing = tuple(sorted(set(left) - set(right)))
    added = tuple(sorted(set(right) - set(left)))
    differences: list[TaskDifference] = []
    fields = ("name", "start", "finish", "duration_days", "predecessors", "percent_complete")
    for uid in sorted(set(left) & set(right)):
        old, new = left[uid], right[uid]
        for field in fields:
            if getattr(old, field) != getattr(new, field):
                differences.append(TaskDifference(uid, field, getattr(old, field), getattr(new, field)))
    return CompatibilityReport(not missing and not added and not differences, tuple(differences), missing, added)
