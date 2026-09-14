"""Project templates and a deterministic Persian project wizard."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Mapping

from .calendar import IranianWorkCalendar
from .msp_adapter import MspAdapter


@dataclass(frozen=True)
class TaskTemplate:
    name: str
    duration_days: float | None = None
    milestone: bool = False
    children: tuple["TaskTemplate", ...] = ()


@dataclass(frozen=True)
class ProjectTemplate:
    key: str
    title: str
    description: str
    tasks: tuple[TaskTemplate, ...]


CONSTRUCTION_TEMPLATE = ProjectTemplate(
    key="construction",
    title="پروژه ساختمانی",
    description="قالب پایه پروژه‌های ساختمانی ایران",
    tasks=(
        TaskTemplate("مطالعات"), TaskTemplate("طراحی"), TaskTemplate("مجوز", milestone=True),
        TaskTemplate("تجهیز کارگاه"), TaskTemplate("تخریب"), TaskTemplate("گودبرداری"),
        TaskTemplate("پایدارسازی"), TaskTemplate("فونداسیون"), TaskTemplate("اسکلت"),
        TaskTemplate("سفت‌کاری"), TaskTemplate("نازک‌کاری"), TaskTemplate("تأسیسات"),
        TaskTemplate("تحویل", milestone=True),
    ),
)

GENERAL_TEMPLATE = ProjectTemplate(
    key="general", title="پروژه عمومی", description="قالب حداقلی برای شروع پروژه", tasks=(TaskTemplate("شروع"), TaskTemplate("تحویل", milestone=True))
)

TEMPLATES: Mapping[str, ProjectTemplate] = {item.key: item for item in (CONSTRUCTION_TEMPLATE, GENERAL_TEMPLATE)}


@dataclass(frozen=True)
class ProjectWizardInput:
    name: str
    start_date: date
    calendar: str = "administrative"
    template_key: str = "construction"
    language: str = "fa-IR"

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("Project name is required")
        if self.calendar not in {"administrative", "workshop"}:
            raise ValueError("Unsupported work calendar")
        if self.template_key not in TEMPLATES:
            raise ValueError("Unknown project template")
        if self.language not in {"fa-IR", "en-US"}:
            raise ValueError("Unsupported language")


@dataclass(frozen=True)
class WizardPlan:
    project: ProjectWizardInput
    template: ProjectTemplate
    work_calendar: IranianWorkCalendar

    def task_names(self) -> tuple[str, ...]:
        return tuple(task.name for task in self.template.tasks)


def build_plan(request: ProjectWizardInput) -> WizardPlan:
    request.validate()
    calendar = IranianWorkCalendar.workshop() if request.calendar == "workshop" else IranianWorkCalendar.administrative()
    return WizardPlan(request, TEMPLATES[request.template_key], calendar)


def apply_plan(plan: WizardPlan, adapter: MspAdapter) -> None:
    """Apply only project metadata supported by the adapter; MSP schedules tasks."""
    adapter.set_project_start(plan.project.start_date)
