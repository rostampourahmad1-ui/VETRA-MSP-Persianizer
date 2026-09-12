"""Pure-Python Gregorian/Jalali conversion used by the VETRA domain layer.

The implementation is dependency-free so it can be reused by an MSP adapter,
installer diagnostics, and offline test tools.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
import re


@dataclass(frozen=True, order=True)
class JalaliDate:
    year: int
    month: int
    day: int

    def __post_init__(self) -> None:
        if self.year < 1:
            raise ValueError("Jalali year must be positive")
        if not 1 <= self.month <= 12:
            raise ValueError("Jalali month must be between 1 and 12")
        max_day = 31 if self.month <= 6 else 30 if self.month <= 11 else 30
        if self.month == 12 and self.day > (30 if is_jalali_leap(self.year) else 29):
            raise ValueError("Invalid day for Jalali month")
        if not 1 <= self.day <= max_day:
            raise ValueError("Invalid Jalali day")

    def iso(self, persian_digits: bool = False) -> str:
        value = f"{self.year:04d}/{self.month:02d}/{self.day:02d}"
        return to_persian_digits(value) if persian_digits else value


_DIGIT_MAP = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
_REVERSE_DIGIT_MAP = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")


def to_persian_digits(value: str) -> str:
    return value.translate(_DIGIT_MAP)


def to_latin_digits(value: str) -> str:
    return value.translate(_REVERSE_DIGIT_MAP)


def is_jalali_leap(year: int) -> bool:
    # Leap calculation through the same conversion boundary avoids a second
    # approximation and matches the 33-year/astronomical cycle used here.
    start = jalali_to_gregorian(year, 1, 1)
    next_start = jalali_to_gregorian(year + 1, 1, 1)
    return (next_start - start).days == 366


def jalali_to_gregorian(year: int, month: int, day: int) -> date:
    if not 1 <= month <= 12 or day < 1:
        raise ValueError("Invalid Jalali date")
    jy = year - 979
    days = 365 * jy + (jy // 33) * 8 + ((jy % 33) + 3) // 4 + 78 + day
    days += (month - 1) * 31 if month <= 7 else (month - 7) * 30 + 186
    gy = 1600 + 400 * (days // 146097)
    days %= 146097
    if days > 36524:
        gy += 100 * ((days - 1) // 36524)
        days = (days - 1) % 36524
        if days >= 365:
            days += 1
    gy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        gy += (days - 1) // 365
        days = (days - 1) % 365
    gd = days + 1
    leap = (gy % 4 == 0 and gy % 100 != 0) or gy % 400 == 0
    month_lengths = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    gm = 1
    for length in month_lengths:
        if gd <= length:
            break
        gd -= length
        gm += 1
    return date(gy, gm, gd)


def gregorian_to_jalali(value: date) -> JalaliDate:
    gy = value.year - 1600
    jy = 979
    month_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if value.month > 2 else gy
    days = (365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100
            + (gy2 + 399) // 400 - 80 + value.day + month_days[value.month - 1])
    jy += 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm = 1 + days // 31
        jd = 1 + days % 31
    else:
        jm = 7 + (days - 186) // 30
        jd = 1 + (days - 186) % 30
    return JalaliDate(jy, jm, jd)


def parse_jalali(text: str) -> JalaliDate:
    normalized = to_latin_digits(text.strip())
    match = re.fullmatch(r"(\d{4})\s*[/\-.]\s*(\d{1,2})\s*[/\-.]\s*(\d{1,2})", normalized)
    if not match:
        raise ValueError(f"Unsupported Jalali date: {text!r}")
    return JalaliDate(*(int(part) for part in match.groups()))


def _g_days_from_civil(year: int, month: int, day: int) -> int:
    year -= 1 if month <= 2 else 0
    era = (year if year >= 0 else year - 399) // 400
    yoe = year - era * 400
    doy = (153 * (month + (-3 if month > 2 else 9)) + 2) // 5 + day - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe


def _civil_from_days(days: int) -> date:
    era = (days if days >= 0 else days - 146096) // 146097
    doe = days - era * 146097
    yoe = (doe - doe // 1460 + doe // 36524 - doe // 146096) // 365
    year = yoe + era * 400
    doy = doe - (365 * yoe + yoe // 4 - yoe // 100)
    mp = (5 * doy + 2) // 153
    day = doy - (153 * mp + 2) // 5 + 1
    month = mp + (3 if mp < 10 else -9)
    year += 1 if month <= 2 else 0
    return date(year, month, day)
