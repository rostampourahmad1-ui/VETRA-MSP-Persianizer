"""Small standard-library CLI for local smoke testing and diagnostics."""
from __future__ import annotations

import argparse
from datetime import date
import sys

from .diagnostics import collect_report
from .fake_msp import FakeMspAdapter
from .jalali import gregorian_to_jalali, parse_jalali
from .msp_adapter import UnsupportedMspAdapter
from .project_wizard import ProjectWizardInput, build_plan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="vetra-core")
    sub = parser.add_subparsers(dest="command", required=True)
    diag = sub.add_parser("diagnostics")
    diag.add_argument("--fake", action="store_true")
    convert = sub.add_parser("convert-date")
    convert.add_argument("value")
    wizard = sub.add_parser("wizard")
    wizard.add_argument("name")
    wizard.add_argument("--template", default="construction")
    args = parser.parse_args(argv)

    if args.command == "diagnostics":
        adapter = FakeMspAdapter() if args.fake else UnsupportedMspAdapter()
        print(collect_report(adapter, "0.3.0", 1, "2026.1").to_json())
        return 0
    if args.command == "convert-date":
        print(parse_jalali(args.value).iso(persian_digits=True))
        return 0
    plan = build_plan(ProjectWizardInput(args.name, date.today(), template_key=args.template))
    print(f"پروژه: {plan.project.name}\nقالب: {plan.template.title}\nتعداد فعالیت: {len(plan.task_names())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
