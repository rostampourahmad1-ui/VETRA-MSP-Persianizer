import sys
import unittest
from datetime import date

from vetra_core.compatibility import compare_task_snapshots
from vetra_core.msp_adapter import MspTaskSnapshot
from vetra_core.windows_msp_adapter import WindowsMspComAdapter


def task(name: str, percent: float = 0) -> MspTaskSnapshot:
    return MspTaskSnapshot("1", name, date(2026, 3, 21), date(2026, 3, 25), 5, percent_complete=percent)


class CompatibilityTests(unittest.TestCase):
    def test_equal_snapshots_are_compatible(self):
        report = compare_task_snapshots([task("فونداسیون")], [task("فونداسیون")])
        self.assertTrue(report.compatible)
        self.assertEqual(report.differences, ())

    def test_changed_task_is_reported(self):
        report = compare_task_snapshots([task("فونداسیون")], [task("فونداسیون", 50)])
        self.assertFalse(report.compatible)
        self.assertEqual(report.differences[0].field, "percent_complete")

    def test_missing_and_added_tasks_are_reported(self):
        before = [task("اول")]
        after = [MspTaskSnapshot("2", "دوم", None, None, None)]
        report = compare_task_snapshots(before, after)
        self.assertEqual(report.missing_uids, ("1",))
        self.assertEqual(report.added_uids, ("2",))

    @unittest.skipIf(sys.platform == "win32", "This guard is for non-Windows development hosts")
    def test_windows_adapter_is_guarded_outside_windows(self):
        with self.assertRaisesRegex(RuntimeError, "Windows"):
            WindowsMspComAdapter()


if __name__ == "__main__":
    unittest.main()
