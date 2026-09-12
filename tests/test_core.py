import unittest
from datetime import date

from vetra_core.calendar import Holiday, IranianWorkCalendar
from vetra_core.jalali import JalaliDate, gregorian_to_jalali, jalali_to_gregorian, parse_jalali
from vetra_core.localization import Translator
from vetra_core.msp_adapter import UnsupportedMspAdapter


class CoreTests(unittest.TestCase):
    def test_known_nowruz_conversion_round_trip(self):
        self.assertEqual(gregorian_to_jalali(date(2026, 3, 21)), JalaliDate(1405, 1, 1))
        self.assertEqual(jalali_to_gregorian(1405, 1, 1), date(2026, 3, 21))

    def test_jalali_parser_accepts_persian_digits_and_separators(self):
        self.assertEqual(parse_jalali("۱۴۰۵/۰۶/۲۰"), JalaliDate(1405, 6, 20))
        self.assertEqual(parse_jalali("1405-06-20"), JalaliDate(1405, 6, 20))

    def test_calendar_has_iranian_workweek_and_custom_holiday(self):
        calendar = IranianWorkCalendar.administrative()
        friday = date(2026, 3, 20)
        saturday = date(2026, 3, 21)
        self.assertFalse(calendar.is_working_day(friday))
        self.assertTrue(calendar.is_working_day(saturday))
        calendar.add_holiday(Holiday(saturday, "تعطیلی پروژه", "project"))
        self.assertFalse(calendar.is_working_day(saturday))
        self.assertGreater(calendar.next_working_day(saturday), saturday)

    def test_translator_renders_persian_labels_and_digits(self):
        translator = Translator.default()
        self.assertEqual(translator.translate("Task Name"), "نام فعالیت")
        self.assertEqual(translator.duration(5, "days"), "۵ روز")
        self.assertEqual(translator.direction(), "rtl")

    def test_unsupported_adapter_fails_explicitly(self):
        with self.assertRaisesRegex(RuntimeError, "adapter"):
            UnsupportedMspAdapter().environment()


if __name__ == "__main__":
    unittest.main()
