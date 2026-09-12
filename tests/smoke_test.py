from datetime import date
from vetra_core.calendar import Holiday, IranianWorkCalendar
from vetra_core.jalali import JalaliDate, gregorian_to_jalali, jalali_to_gregorian, parse_jalali
from vetra_core.localization import Translator
from vetra_core.msp_adapter import UnsupportedMspAdapter

assert gregorian_to_jalali(date(2026, 3, 21)) == JalaliDate(1405, 1, 1)
assert jalali_to_gregorian(1405, 1, 1) == date(2026, 3, 21)
assert parse_jalali("۱۴۰۵/۰۶/۲۰") == JalaliDate(1405, 6, 20)
calendar = IranianWorkCalendar.administrative()
assert calendar.is_working_day(date(2026, 3, 20)) is False
saturday = date(2026, 3, 21)
assert calendar.is_working_day(saturday) is True
calendar.add_holiday(Holiday(saturday, "تعطیلی پروژه", "project"))
assert calendar.is_working_day(saturday) is False
assert calendar.next_working_day(saturday) > saturday
translator = Translator.default()
assert translator.translate("Task Name") == "نام فعالیت"
assert translator.duration(5, "days") == "۵ روز"
assert translator.direction() == "rtl"
try:
    UnsupportedMspAdapter().environment()
except RuntimeError as exc:
    assert "adapter" in str(exc).lower()
else:
    raise AssertionError("Unsupported adapter must fail explicitly")
print("SMOKE_TEST=passed")
