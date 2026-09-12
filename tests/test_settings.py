import tempfile
import unittest
from pathlib import Path

from vetra_core.settings import VetraSettings


class SettingsTests(unittest.TestCase):
    def test_settings_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "settings.json"
            expected = VetraSettings()
            expected.save(path)
            self.assertEqual(VetraSettings.load(path), expected)

    def test_invalid_language_is_rejected(self):
        with self.assertRaises(ValueError):
            VetraSettings(language="xx").validate()


if __name__ == "__main__":
    unittest.main()
