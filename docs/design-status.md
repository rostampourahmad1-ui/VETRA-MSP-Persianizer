# وضعیت طراحی و پیاده‌سازی

## تصمیم اجرایی فعلی

هسته دامنه با Python استاندارد و بدون وابستگی خارجی پیاده‌سازی شده است. این انتخاب برای سرویس‌های تبدیل تاریخ، تقویم کاری، ترجمه و قراردادهای Integration انجام شده است؛ زیرا این اجزا باید مستقل از Microsoft Project و رابط کاربری باشند و در محیط‌های تست و ابزارهای تشخیصی نیز قابل اجرا بمانند.

اتصال واقعی به Microsoft Project 2024 در یک Adapter ویندوزی جداگانه پیاده خواهد شد. این Adapter مجاز به اجرای زمان‌بندی مستقل نیست و فقط از Object Model یا Extensionهای تأییدشده MSP استفاده می‌کند.

## وضعیت اجزا

| جزء | وضعیت | توضیح |
|---|---|---|
| Gregorian/Jalali | پیاده‌سازی اولیه | تبدیل رفت‌وبرگشت و Parser تاریخ |
| تقویم کاری ایرانی | پیاده‌سازی اولیه | اداری، کارگاه، تعطیلی سفارشی |
| ترجمه و اعداد | پیاده‌سازی اولیه | واژه‌نامه داده‌محور و RTL |
| قرارداد MSP Adapter | تعریف شده | بدون دسترسی مستقیم به COM در محیط Linux |
| Date Picker | طراحی قرارداد | نیازمند لایه UI ویندوزی |
| Ribbon/Dialog/Views | طراحی معماری | نیازمند بررسی Extension واقعی MSP |
| MPP compatibility | معیار آزمون تعریف شده | اجرای نهایی روی Windows/MSP لازم است |
| Installer/Update | در نقشه‌راه | پس از تثبیت Adapter |

در فاز بعدی، `FakeMspAdapter` برای توسعه و تست بدون Project اضافه شده است. `HolidayCatalog` داده تعطیلات را نسخه‌دار و قابل بارگذاری می‌کند. `DiagnosticsReport` فقط اطلاعات محیط و نسخه‌ها را گزارش می‌دهد و داده پروژه را جمع‌آوری نمی‌کند.

## ریسک‌های باز

دسترسی واقعی به Ribbon، Dialogهای داخلی، Timescale، Gantt و Date Picker ممکن است بین روش‌های VBA، COM، VSTO و Office Add-in متفاوت باشد. قبل از ادعای فارسی‌سازی کامل، باید روی محیط واقعی Microsoft Project 2024 نمونه فنی اجرا شود.

## گام بعدی

گام بعدی ایجاد Adapter ویندوزی با قراردادهای خواندن Task، Resource، Calendar، View و Save/Reload MPP است. این کار به Windows و نصب MSP 2024 نیاز دارد و در محیط Linux فعلی فقط می‌توان قرارداد و Fake Adapter آن را توسعه داد.

## منابع

[1]: https://learn.microsoft.com/en-us/office/vba/api/overview/project "Microsoft Project VBA reference"
[2]: https://learn.microsoft.com/en-us/office/vba/api/project.application "Project Application object reference"
