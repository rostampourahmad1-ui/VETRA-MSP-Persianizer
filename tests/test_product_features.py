import json
import unittest
from datetime import date

from vetra_core.fake_msp import FakeMspAdapter
from vetra_core.msp_adapter import MspTaskSnapshot
from vetra_core.project_wizard import ProjectWizardInput, apply_plan, build_plan
from vetra_core.reporting import PersianReport


class ProductFeatureTests(unittest.TestCase):
    def test_construction_wizard_builds_expected_plan(self):
        plan = build_plan(ProjectWizardInput("پروژه نمونه", date(2026, 3, 21)))
        self.assertEqual(plan.template.key, "construction")
        self.assertIn("فونداسیون", plan.task_names())
        self.assertIn("تحویل", plan.task_names())

    def test_wizard_applies_only_project_start_to_adapter(self):
        adapter = FakeMspAdapter()
        plan = build_plan(ProjectWizardInput("پروژه نمونه", date(2026, 3, 21)))
        apply_plan(plan, adapter)
        self.assertEqual(adapter.project_start, date(2026, 3, 21))
        self.assertEqual(adapter.tasks, [])

    def test_persian_report_contains_jalali_dates_and_csv(self):
        tasks = [MspTaskSnapshot("1", "فونداسیون", date(2026, 3, 21), date(2026, 3, 25), 5, percent_complete=50)]
        report = PersianReport(tasks)
        payload = json.loads(report.to_json())
        self.assertEqual(payload[0]["شروع"], "۱۴۰۵/۰۱/۰۱")
        self.assertEqual(payload[0]["درصد تکمیل"], "۵۰")
        self.assertIn("نام فعالیت", report.to_csv())
        self.assertIn("فونداسیون", report.to_csv())

    def test_invalid_wizard_input_is_rejected(self):
        with self.assertRaises(ValueError):
            build_plan(ProjectWizardInput("", date(2026, 3, 21)))


if __name__ == "__main__":
    unittest.main()
