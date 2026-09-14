import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class InstallerAssetTests(unittest.TestCase):
    def test_required_installer_assets_exist(self):
        for relative in (
            "installer/Install-Vetra.ps1",
            "installer/Uninstall-Vetra.ps1",
            "installer/VETRA-MSP-Persianizer.nsi",
            "installer/README-fa.md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_installer_checks_msp_and_preserves_mpp(self):
        script = (ROOT / "installer/Install-Vetra.ps1").read_text(encoding="utf-8")
        self.assertIn("Microsoft Project 2024", script)
        self.assertIn("Backups", script)
        self.assertIn("Existing MPP files were not modified", script)

    def test_uninstaller_does_not_delete_mpp_files(self):
        script = (ROOT / "installer/Uninstall-Vetra.ps1").read_text(encoding="utf-8")
        self.assertIn(".MPP files were not deleted", script)
        self.assertNotIn("*.mpp", script.lower())

    def test_nsis_declares_admin_and_powershell(self):
        script = (ROOT / "installer/VETRA-MSP-Persianizer.nsi").read_text(encoding="utf-8")
        self.assertIn("RequestExecutionLevel admin", script)
        self.assertIn("WindowsPowerShell", script)
        self.assertIn("WriteUninstaller", script)


if __name__ == "__main__":
    unittest.main()
