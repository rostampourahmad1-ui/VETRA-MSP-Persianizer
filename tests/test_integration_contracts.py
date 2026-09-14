import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from vetra_core.diagnostics import collect_report
from vetra_core.fake_msp import FakeMspAdapter
from vetra_core.holidays import HolidayCatalog
from vetra_core.calendar import Holiday, IranianWorkCalendar
from vetra_core.msp_adapter import MspTaskSnapshot, UnsupportedMspAdapter


class IntegrationContractTests(unittest.TestCase):
    def test_fake_adapter_preserves_boundary_operations(self):
        adapter = FakeMspAdapter(tasks=[MspTaskSnapshot("1", "فعالیت اول", date(2026, 3, 21), None, 5)])
        adapter.set_project_start(date(2026, 3, 21))
        adapter.open_mpp("sample.mpp")
        adapter.save_mpp("sample-out.mpp")
        self.assertEqual(len(adapter.list_tasks()), 1)
        self.assertEqual(adapter.opened_path, "sample.mpp")
        self.assertEqual(adapter.saved_path, "sample-out.mpp")

    def test_holiday_catalog_round_trip_and_application(self):
        catalog = HolidayCatalog("2026.1", [Holiday(date(2026, 3, 21), "نوروز")])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "holidays.json"
            catalog.save(path)
            restored = HolidayCatalog.load(path)
        calendar = IranianWorkCalendar.administrative()
        restored.apply_to(calendar)
        self.assertFalse(calendar.is_working_day(date(2026, 3, 21)))
        self.assertEqual(restored.version, "2026.1")

    def test_diagnostics_does_not_include_project_data(self):
        report = collect_report(FakeMspAdapter(), "0.2.0", 1, "2026.1")
        payload = json.loads(report.to_json())
        self.assertTrue(payload["adapter_available"])
        self.assertEqual(payload["msp_version"], "2024")
        self.assertNotIn("فعالیت اول", report.to_json())

    def test_diagnostics_reports_unavailable_adapter(self):
        report = collect_report(UnsupportedMspAdapter(), "0.2.0", 1, "2026.1")
        self.assertFalse(report.adapter_available)
        self.assertIsNone(report.msp_version)


if __name__ == "__main__":
    unittest.main()
