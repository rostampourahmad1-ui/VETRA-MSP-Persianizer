"""Data-driven Persian localization services."""
from __future__ import annotations

from dataclasses import dataclass


DEFAULT_TRANSLATIONS: dict[str, str] = {
    "Task": "فعالیت",
    "Summary Task": "فعالیت خلاصه",
    "Milestone": "نقطه عطف",
    "Duration": "مدت",
    "Start": "شروع",
    "Finish": "پایان",
    "Predecessors": "پیش‌نیازها",
    "Successors": "فعالیت‌های پسین",
    "Resource": "منبع",
    "Cost": "هزینه",
    "Work": "کار",
    "Baseline": "خط مبنا",
    "Actual": "واقعی",
    "Variance": "انحراف",
    "Critical": "بحرانی",
    "Slack": "شناوری",
    "% Complete": "درصد تکمیل",
    "Actual Cost": "هزینه واقعی",
    "Task Name": "نام فعالیت",
    "Project": "پروژه",
    "Resource Leveling": "ترازکردن منابع",
    "Status Date": "تاریخ وضعیت",
    "Calendar": "تقویم",
    "Report": "گزارش",
}

DEFAULT_UNITS = {"days": "روز", "day": "روز", "hours": "ساعت", "hour": "ساعت", "minutes": "دقیقه", "weeks": "هفته", "week": "هفته", "months": "ماه", "month": "ماه"}


@dataclass
class Translator:
    translations: dict[str, str]
    use_persian_digits: bool = True

    @classmethod
    def default(cls) -> "Translator":
        return cls(dict(DEFAULT_TRANSLATIONS))

    def translate(self, value: str) -> str:
        return self.translations.get(value, value)

    def number(self, value: int | float | str) -> str:
        text = str(value)
        return text.translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")) if self.use_persian_digits else text

    def duration(self, value: int | float, unit: str = "days") -> str:
        rendered = f"{self.number(value)} {DEFAULT_UNITS.get(unit, unit)}"
        return rendered

    def direction(self) -> str:
        return "rtl"


@dataclass(frozen=True)
class FieldMapping:
    msp_name: str
    persian_name: str
    data_type: str


DEFAULT_FIELD_MAPPINGS = tuple(
    FieldMapping(source, target, "text") for source, target in DEFAULT_TRANSLATIONS.items()
)
