# ماتریس ردیابی نیازمندی‌ها

این ماتریس باید در طول توسعه تکمیل شود. شناسه‌ها پایدار هستند و تغییر دامنه باید با نسخه سند ثبت شود.

| شناسه | نیازمندی مبنا | ماژول هدف | تست پذیرش |
|---|---|---|---|
| REQ-UI | فارسی‌سازی Ribbon، Dialog و Fieldها | Localization، Persian UI | AT-06 |
| REQ-RTL | رابط راست‌به‌چپ واقعی | Persian UI | AT-06 |
| REQ-CAL | تبدیل Gregorian/Jalali و تاریخ ورودی | Jalali Calendar | AT-01، AT-02، AT-05 |
| REQ-HOL | تعطیلات رسمی و سفارشی ایران | Holidays، Work Calendar | AT-03، AT-04 |
| REQ-VIEW | Timescale، Gantt، Timeline و Viewهای فارسی | MSP Integration، Reporting | AT-06، AT-08 |
| REQ-MSP | حفظ موتور زمان‌بندی MSP | MSP Adapter | AT-07، AT-08، AT-09 |
| REQ-OUT | خروجی Excel، PDF و چاپ فارسی | Reporting | AT-10 |
| REQ-TPL | کتابخانه قالب‌های پروژه | Templates | AT-10 |
| REQ-OPS | نصب، حذف، Update، Diagnostics و Backup | Administration | AT-11، AT-12 |
| REQ-COMP | تشخیص نسخه و سازگاری MSP 2024 | Core، Administration | AT-09، AT-11 |

## قاعده تکمیل

هر ردیف باید به Issue یا Pull Request، مالک، نسخه هدف، وضعیت، شواهد آزمون و محدودیت شناخته‌شده متصل شود. نیازمندی فاقد تست قابل اجرا، آماده انتشار نیست.
