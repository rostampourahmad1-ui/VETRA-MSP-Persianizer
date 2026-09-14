"""Privacy-conscious health report for support and installation checks."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

from .msp_adapter import MspAdapter


@dataclass(frozen=True)
class DiagnosticsReport:
    vetra_version: str
    adapter_available: bool
    product: str | None
    msp_version: str | None
    edition: str | None
    office_version: str | None
    windows_version: str | None
    settings_schema: int
    calendar_catalog_version: str

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)


def collect_report(adapter: MspAdapter, vetra_version: str, settings_schema: int, calendar_catalog_version: str) -> DiagnosticsReport:
    try:
        env = adapter.environment()
    except RuntimeError:
        return DiagnosticsReport(vetra_version, False, None, None, None, None, None, settings_schema, calendar_catalog_version)
    return DiagnosticsReport(vetra_version, True, env.product, env.version, env.edition, env.office_version, env.windows_version, settings_schema, calendar_catalog_version)


def write_report(report: DiagnosticsReport, path: str | Path) -> None:
    Path(path).write_text(report.to_json() + "\n", encoding="utf-8")
