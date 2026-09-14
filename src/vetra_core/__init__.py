"""VETRA MSP Persianizer core domain services."""

from .calendar import Holiday, IranianWorkCalendar, WorkInterval
from .compatibility import CompatibilityReport, compare_task_snapshots
from .diagnostics import DiagnosticsReport, collect_report
from .holidays import HolidayCatalog
from .jalali import JalaliDate, gregorian_to_jalali, jalali_to_gregorian, parse_jalali
from .localization import Translator
from .project_wizard import ProjectWizardInput, apply_plan, build_plan
from .reporting import PersianReport
from .settings import VetraSettings

__all__ = [
    "DiagnosticsReport",
    "CompatibilityReport",
    "Holiday",
    "HolidayCatalog",
    "IranianWorkCalendar",
    "JalaliDate",
    "PersianReport",
    "ProjectWizardInput",
    "Translator",
    "VetraSettings",
    "WorkInterval",
    "collect_report",
    "compare_task_snapshots",
    "apply_plan",
    "build_plan",
    "gregorian_to_jalali",
    "jalali_to_gregorian",
    "parse_jalali",
]

__version__ = "0.3.0"
