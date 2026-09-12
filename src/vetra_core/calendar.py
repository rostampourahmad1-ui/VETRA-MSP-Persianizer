"""Iranian work-calendar domain services; MSP remains the scheduler."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from typing import Iterable

from .jalali import JalaliDate, gregorian_to_jalali


@dataclass(frozen=True)
class Holiday:
    day: date
    title: str
    kind: str = "official"


@dataclass(frozen=True)
class WorkInterval:
    start: time
    end: time

    def __post_init__(self) -> None:
        if self.start >= self.end:
            raise ValueError("Work interval start must be before end")

    @property
    def hours(self) -> float:
        delta = datetime.combine(date.min, self.end) - datetime.combine(date.min, self.start)
        return delta.total_seconds() / 3600


@dataclass
class IranianWorkCalendar:
    """A presentation/input calendar that can be projected into an MSP Calendar."""
    name: str = "تقویم اداری ایران"
    intervals_by_weekday: dict[int, tuple[WorkInterval, ...]] = field(default_factory=dict)
    holidays: dict[date, Holiday] = field(default_factory=dict)

    @classmethod
    def administrative(cls) -> "IranianWorkCalendar":
        # Python weekday: Monday=0 ... Sunday=6; Iranian workweek is Sat-Wed.
        regular = {weekday: (WorkInterval(time(7, 30), time(16, 30)),) for weekday in (5, 6, 0, 1, 2)}
        regular[3] = (WorkInterval(time(7, 30), time(13, 0)),)  # Thursday
        regular[4] = ()  # Friday
        return cls(intervals_by_weekday=regular)

    @classmethod
    def workshop(cls) -> "IranianWorkCalendar":
        regular = {weekday: (WorkInterval(time(7), time(17)),) for weekday in (5, 6, 0, 1, 2, 3)}
        regular[4] = ()
        return cls(name="تقویم کارگاه", intervals_by_weekday=regular)

    def add_holiday(self, holiday: Holiday) -> None:
        self.holidays[holiday.day] = holiday

    def is_working_day(self, day: date) -> bool:
        return bool(self.intervals_by_weekday.get(day.weekday(), ())) and day not in self.holidays

    def working_hours(self, day: date) -> float:
        if not self.is_working_day(day):
            return 0.0
        return sum(interval.hours for interval in self.intervals_by_weekday[day.weekday()])

    def next_working_day(self, day: date) -> date:
        candidate = day
        while not self.is_working_day(candidate):
            candidate += timedelta(days=1)
        return candidate

    def to_jalali(self, day: date, persian_digits: bool = False) -> str:
        return gregorian_to_jalali(day).iso(persian_digits=persian_digits)


def format_duration(days: float, unit: str = "روز", persian_digits: bool = True) -> str:
    value = f"{days:g} {unit}"
    if persian_digits:
        from .jalali import to_persian_digits
        value = to_persian_digits(value)
    return value
