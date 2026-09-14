"""Windows Microsoft Project COM adapter boundary.

This module is intentionally conservative: it does not implement a scheduling
engine and refuses to run when pywin32/Windows/MSP are unavailable.
"""
from __future__ import annotations

from datetime import date
from typing import Sequence

from .msp_adapter import MspEnvironment, MspTaskSnapshot


class WindowsMspComAdapter:
    """Minimal COM lifecycle adapter to be completed on a Windows test host."""

    def __init__(self, visible: bool = False) -> None:
        if __import__("sys").platform != "win32":
            raise RuntimeError("WindowsMspComAdapter requires Windows and Microsoft Project 2024")
        try:
            import win32com.client  # type: ignore
        except ImportError as exc:
            raise RuntimeError("Install pywin32 on the Windows test host before using COM adapter") from exc
        self._client = win32com.client
        self._app = self._client.Dispatch("MSProject.Application")
        self._app.Visible = visible

    def environment(self) -> MspEnvironment:
        version = str(getattr(self._app, "Version", "unknown"))
        return MspEnvironment("Microsoft Project", version, "Unknown")

    def list_tasks(self) -> Sequence[MspTaskSnapshot]:
        project = getattr(self._app, "ActiveProject", None)
        if project is None:
            return ()
        result = []
        for task in project.Tasks:
            if task is None:
                continue
            result.append(MspTaskSnapshot(
                uid=str(task.UniqueID), name=str(task.Name), start=None, finish=None,
                duration_days=None, predecessors=str(task.Predecessors or ""),
                percent_complete=float(task.PercentComplete or 0),
            ))
        return tuple(result)

    def set_project_start(self, day: date) -> None:
        project = self._app.ActiveProject
        project.ProjectStart = day.strftime("%m/%d/%Y")

    def save_mpp(self, path: str) -> None:
        self._app.ActiveProject.SaveAs(path)

    def open_mpp(self, path: str) -> None:
        self._app.FileOpen(path)
