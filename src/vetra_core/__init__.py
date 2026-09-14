"""VETRA MSP Persianizer core domain services."""

from .calendar import Holiday, IranianWorkCalendar, WorkInterval
from .diagnostics import DiagnosticsReport, collect_report
from .holidays import HolidayCatalog
from .jalali import JalaliDate, gregorian_to_jalali, jalali_to_gregorian, parse_jalali
from .localization import Translator
from .settings import VetraSettings

__all__ = [
    "DiagnosticsReport",
    "Holiday",
    "HolidayCatalog",
    "IranianWorkCalendar",
    "JalaliDate",
    "Translator",
    "VetraSettings",
    "WorkInterval",
    "collect_report",
    "gregorian_to_jalali",
    "jalali_to_gregorian",
    "parse_jalali",
]

__version__ = "0.2.0"
