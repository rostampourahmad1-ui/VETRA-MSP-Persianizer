"""Deterministic Persian reports over MSP snapshots; no scheduling is performed."""
from __future__ import annotations

import csv
import io
import json
from datetime import date
from typing import Sequence

from .jalali import gregorian_to_jalali
from .localization import Translator
from .msp_adapter import MspTaskSnapshot


class PersianReport:
    def __init__(self, tasks: Sequence[MspTaskSnapshot], translator: Translator | None = None) -> None:
        self.tasks = tuple(tasks)
        self.translator = translator or Translator.default()

    def rows(self) -> list[dict[str, str]]:
        result = []
        for task in self.tasks:
            result.append({
                "شناسه": task.uid,
                "نام فعالیت": task.name,
                "شروع": _format_date(task.start, self.translator),
                "پایان": _format_date(task.finish, self.translator),
                "مدت": self.translator.duration(task.duration_days, "days") if task.duration_days is not None else "",
                "پیش‌نیازها": task.predecessors,
                "درصد تکمیل": self.translator.number(task.percent_complete),
            })
        return result

    def to_json(self) -> str:
        return json.dumps(self.rows(), ensure_ascii=False, indent=2)

    def to_csv(self) -> str:
        output = io.StringIO(newline="")
        rows = self.rows()
        writer = csv.DictWriter(output, fieldnames=list(rows[0]) if rows else ["شناسه", "نام فعالیت"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return output.getvalue()


def _format_date(value: date | None, translator: Translator) -> str:
    if value is None:
        return ""
    return gregorian_to_jalali(value).iso(persian_digits=translator.use_persian_digits)
