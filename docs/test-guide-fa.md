# راهنمای نصب، راه‌اندازی و آزمایش VETRA MSP Persianizer

## وضعیت آمادگی

نسخه فعلی `0.3.0` برای **آزمایش هسته مستقل** آماده است. این نسخه تبدیل تاریخ میلادی/شمسی، تقویم کاری ایرانی، تعطیلات نسخه‌دار، ترجمه، تنظیمات، Project Wizard، گزارش فارسی، Fake MSP Adapter و Diagnostics را فراهم می‌کند.

اتصال واقعی به Microsoft Project 2024 هنوز در این ریپو به Adapter ویندوزی COM/VSTO متصل نشده است. بنابراین آزمایش کامل Ribbon، Dialog، Gantt، Timescale، ذخیره و بازخوانی واقعی `.MPP` و سازگاری MSP در این مرحله قابل اعلام نیست.

## بخش اول: نصب هسته روی Windows، Linux یا macOS

### گام ۱ — دریافت کد

```bash
git clone https://github.com/rostampourahmad1-ui/VETRA-MSP-Persianizer.git
cd VETRA-MSP-Persianizer
```

اگر Git در دسترس نیست، از صفحه GitHub گزینه **Code → Download ZIP** را انتخاب و فایل را استخراج کنید.

### گام ۲ — بررسی Python

Python نسخه 3.10 یا بالاتر لازم است.

```bash
python --version
# یا
python3 --version
```

### گام ۳ — ساخت محیط مجازی اختیاری

```bash
python3 -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

هسته فعلی فقط از کتابخانه استاندارد Python استفاده می‌کند و برای اجرای تست‌ها نصب بسته اضافی لازم ندارد.

### گام ۴ — اجرای تست‌های خودکار

Linux/macOS:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=src python3 tests/smoke_test.py
```

Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -p "test_*.py" -v
python tests/smoke_test.py
```

نتیجه مورد انتظار:

```text
Ran 15 tests ... OK
SMOKE_TEST=passed
```

تعداد تست‌ها ممکن است با توسعه نسخه‌های بعدی افزایش یابد.

## بخش دوم: آزمایش CLI

### آزمایش تبدیل تاریخ شمسی

```bash
PYTHONPATH=src python3 -m vetra_core.cli convert-date ۱۴۰۵/۰۶/۲۰
```

خروجی مورد انتظار:

```text
۱۴۰۵/۰۶/۲۰
```

### آزمایش Diagnostics بدون MSP

```bash
PYTHONPATH=src python3 -m vetra_core.cli diagnostics
```

در این حالت `adapter_available` باید `false` باشد؛ این نتیجه طبیعی است چون Microsoft Project روی این محیط نصب نشده است.

### آزمایش Diagnostics شبیه‌سازی‌شده

```bash
PYTHONPATH=src python3 -m vetra_core.cli diagnostics --fake
```

در این حالت باید نسخه MSP شبیه‌سازی‌شده `2024` و Edition برابر `Professional` نمایش داده شود.

### آزمایش Project Wizard

```bash
PYTHONPATH=src python3 -m vetra_core.cli wizard "پروژه نمونه"
```

خروجی باید نام پروژه، عنوان قالب ساختمانی و تعداد فعالیت‌های قالب را نمایش دهد.

## بخش سوم: آزمایش گزارش فارسی

گزارش‌ساز فعلی از Snapshotهای Adapter استفاده می‌کند. برای آزمایش برنامه‌نویسی، تست‌های `tests/test_product_features.py` را اجرا کنید. خروجی گزارش شامل نام فعالیت، تاریخ شمسی، مدت فارسی و درصد تکمیل فارسی است.

در این نسخه خروجی‌های JSON و CSV فراهم شده‌اند. خروجی PDF، Excel واقعی، چاپ و Gantt تصویری تا اتصال به Adapter و لایه خروجی Windows در فاز بعدی تکمیل می‌شوند.

جزئیات نصب `pywin32`، اجرای Adapter COM و مقایسه Snapshot قبل و بعد در سند [Integration ویندوزی](windows-integration.md) آمده است.

## بخش چهارم: آماده‌سازی آزمایش یکپارچه با MSP 2024

نصب خودکار در `installer/` آماده است. برای ساخت باینری `setup.exe` روی Windows، راهنمای `installer/README-fa.md` را اجرا کنید. تولید باینری در محیط Linux این ریپو انجام نمی‌شود.

برای آزمایش واقعی باید یک رایانه Windows با مشخصات زیر آماده شود:

| مورد | الزام |
|---|---|
| سیستم‌عامل | Windows پشتیبانی‌شده توسط Microsoft Project 2024 |
| نرم‌افزار | Microsoft Project 2024، ترجیحاً Professional برای تست کامل‌تر |
| دسترسی | مجوز معتبر و دسترسی نصب/ثبت Add-in یا COM/VSTO |
| داده مرجع | یک فایل `.MPP` غیرحساس با Task، Summary Task، Milestone، Dependency، Resource، Calendar و Baseline |
| پشتیبان | کپی اصلی فایل MPP خارج از پوشه آزمایش |
| زبان و فونت | فونت فارسی تأییدشده و امکان نمایش RTL |

پیش از هر آزمایش، از فایل MPP کپی تهیه کنید. هرگز اولین آزمایش را روی فایل اصلی پروژه انجام ندهید.

## بخش پنجم: سناریوی آزمایش MSP

۱. Microsoft Project را بدون VETRA باز کنید و از فایل مرجع یک Baseline خروجی ثبت کنید.
۲. مقادیر Task Name، Start، Finish، Duration، Predecessors، Resource، Baseline و `% Complete` را ثبت کنید.
۳. نسخه آزمایشی Adapter ویندوزی را نصب یا فعال کنید.
۴. Diagnostics را اجرا کنید و نسخه MSP، Edition و وضعیت فعال‌سازی را ذخیره کنید.
۵. پروژه را با VETRA باز کنید.
۶. زبان فارسی، اعداد فارسی، RTL و تقویم شمسی را فعال کنید.
۷. تاریخ `۱۴۰۵/۰۶/۲۰` را در ورودی تاریخ وارد کنید و مقدار داخلی یا نمایش معادل را کنترل کنید.
۸. یک تعطیلی سفارشی با علت مشخص اضافه کنید.
۹. محاسبه پروژه را به Microsoft Project بسپارید و نتیجه Start/Finish را ثبت کنید.
۱۰. Gantt، Task Sheet، Timeline، Resource View، Baseline و Critical Path را بررسی کنید.
۱۱. فایل را با نام جدید ذخیره کنید.
۱۲. VETRA را غیرفعال کنید و فایل ذخیره‌شده را در MSP استاندارد باز کنید.
۱۳. داده‌های اصلی و نتایج زمان‌بندی را با مرحله دوم مقایسه کنید.
۱۴. نتیجه را در ماتریس پذیرش `docs/acceptance-tests.md` ثبت کنید.

## معیار قبولی آزمایش MSP

آزمایش فقط زمانی موفق است که فایل MPP در MSP استاندارد باز شود، داده‌های اصلی از بین نرود، محاسبات زمان‌بندی با اجرای مرجع یکسان بماند، تاریخ شمسی درست تبدیل شود، تعطیلی روی تقویم اعمال شود و هیچ نقص جدی در RTL، فونت یا نمایش Viewها وجود نداشته باشد.

هر تغییر ناخواسته در Scheduling، Dependency، Baseline، Resource یا MPP باید باعث توقف آزمایش و ثبت خطا شود.

## گزارش خطا

برای هر خطا این موارد را ثبت کنید:

- نسخه VETRA و commit؛
- نسخه دقیق MSP و Windows؛
- نام سناریوی پذیرش؛
- مراحل بازتولید؛
- نتیجه مورد انتظار؛
- نتیجه واقعی؛
- تصویر یا لاگ Diagnostics بدون اطلاعات حساس پروژه؛
- فایل MPP نمونه، فقط در صورت مجازبودن اشتراک‌گذاری.

## منابع

[1]: https://github.com/rostampourahmad1-ui/VETRA-MSP-Persianizer "VETRA MSP Persianizer repository"
[2]: https://learn.microsoft.com/en-us/office/vba/api/overview/project "Microsoft Project VBA reference"
