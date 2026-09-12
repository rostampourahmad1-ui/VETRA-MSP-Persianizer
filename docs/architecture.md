# معماری VETRA MSP Persianizer

## نمای لایه‌ای

```text
VETRA Presentation Layer
  Persian UI | RTL | Dialogs | Date Picker | Reports | Export
              |
VETRA Localization & Integration Layer
  Translation | Field Mapping | MSP Adapter | View Formatting
              |
VETRA Domain Services
  Jalali Calendar | Holidays | Work Calendar | Date Parsing | Settings
              |
Microsoft Project 2024
  Scheduling | Dependencies | Resources | Baseline | CPM | EVM | MPP
```

## مرزهای طراحی

لایه MSP Adapter تنها نقطه تماس کنترل‌شده با Object Model و Extensionهای MSP است. سرویس تقویم شمسی نباید محاسبات Scheduling را تکرار کند. این سرویس تاریخ ورودی را اعتبارسنجی و بین Gregorian و Jalali تبدیل می‌کند و نتیجه را برای نمایش یا ورودی به Adapter می‌دهد.

Translation و Field Mapping باید داده‌محور باشند. متن‌های ترجمه‌شده نباید در کدهای View پراکنده شوند. هر کلید ترجمه باید شناسه پایدار، متن فارسی، متن انگلیسی، زمینه مصرف و وضعیت بازبینی داشته باشد.

تنظیمات کاربر باید نسخه‌دار و قابل مهاجرت باشند. فایل MPP نباید برای ذخیره تنظیمات VETRA دست‌کاری شود، مگر آنکه فیلد سفارشی و قرارداد سازگاری آن از قبل تعریف و آزموده شده باشد.

## اجزای پیشنهادی

| جزء | مسئولیت | نباید انجام دهد |
|---|---|---|
| Core | تنظیمات، تشخیص محیط، لاگ و چرخه عمر | زمان‌بندی پروژه |
| Localization | ترجمه، واژه‌نامه، واحد و اعداد | تغییر داده اصلی بدون قرارداد |
| Jalali Calendar | تبدیل تاریخ، تعطیلات، روز کاری و Date Picker | پیاده‌سازی موتور CPM |
| MSP Integration | اتصال به View، Task، Resource، Calendar و Report | پنهان‌کردن خطای سازگاری |
| Persian UI | RTL، Dialog، Menu، Tooltip و فرم‌ها | نگهداری منطق کسب‌وکار |
| Reporting | قالب گزارش، PDF، Excel و چاپ | تغییر نتیجه محاسبات MSP |
| Administration | نصب، Update، Diagnostics، License و Backup | حذف فایل MPP کاربر |

## قرارداد سازگاری MPP

برای هر نسخه محصول، یک مجموعه فایل مرجع شامل Task، Summary Task، Milestone، چهار نوع Dependency، Lead/Lag، Constraint، Resource، Calendar، Baseline، Actual و Custom Field نگهداری می‌شود. پیش و پس از استفاده از VETRA، فیلدهای کلیدی استخراج و مقایسه می‌شوند. اختلاف‌های مجاز باید صریحاً در قرارداد نسخه ثبت شوند.

## تصمیم‌های باز پیش از کدنویسی

۱. فناوری Add-in یا Automation بر اساس قابلیت واقعی MSP 2024 انتخاب شود.
۲. سطح دسترسی قابل اتکا به Ribbon، Dialog، Timeline، Timescale و چاپ با نمونه واقعی تعیین شود.
۳. روش توزیع ترجمه‌ها، فونت‌ها، تعطیلات و قالب‌ها مشخص شود.
۴. سیاست License و Update و مالکیت داده‌های Diagnostics تصویب شود.
۵. پشتیبانی رسمی نسخه‌های MSP و Windows اعلام شود.
