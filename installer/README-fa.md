# ساخت و استفاده از setup.exe

## نکته مهم

در محیط توسعه Linux این پروژه، کامپایلر Windows Installer موجود نیست؛ بنابراین فایل باینری `setup.exe` در این ریپو ذخیره نمی‌شود. فایل `VETRA-MSP-Persianizer.nsi` و اسکریپت‌های PowerShell، ورودی کامل و قابل بازتولید برای ساخت Installer روی Windows هستند.

## ساخت setup.exe روی Windows

۱. Windows 10/11 را آماده کنید.
۲. [NSIS](https://nsis.sourceforge.io/Download) را نصب کنید.
۳. ریپو را دریافت کنید:

```powershell
git clone https://github.com/rostampourahmad1-ui/VETRA-MSP-Persianizer.git
cd VETRA-MSP-Persianizer
```

۴. Microsoft Project 2024 را روی ماشین Build نصب کنید یا حداقل روی ماشین مقصد موجود باشد.
۵. فایل `installer/VETRA-MSP-Persianizer.nsi` را با NSIS اجرا کنید.
۶. روش خط فرمان:

```powershell
makensis installer\VETRA-MSP-Persianizer.nsi
```

خروجی در مسیر `installer\VETRA-MSP-Persianizer-Setup.exe` یا مسیر کاری تعریف‌شده توسط NSIS ایجاد می‌شود.

## نصب کاملاً خودکار

PowerShell را با **Run as Administrator** اجرا کنید و Installer را اجرا کنید:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\installer\Install-Vetra.ps1
```

Installer این موارد را انجام می‌دهد:

- تشخیص Windows؛
- تشخیص Microsoft Project 2024 از Registry؛
- تشخیص Python؛
- نصب Python 3.11 از طریق winget در صورت نبودن Python؛
- نصب یا به‌روزرسانی `pywin32`؛
- کپی هسته، مستندات و تنظیمات در Program Files؛
- ایجاد پشتیبان در `%ProgramData%\VETRA\Backups`؛
- ایجاد فایل `vetra-env.ps1`؛
- عدم تغییر یا حذف فایل‌های MPP.

برای نصب آزمایشی بدون تغییر:

```powershell
.\installer\Install-Vetra.ps1 -WhatIf
```

برای ردکردن نصب Python یا pywin32:

```powershell
.\installer\Install-Vetra.ps1 -SkipPythonInstall -SkipPywin32
```

## حذف و بازگردانی

```powershell
.\installer\Uninstall-Vetra.ps1
```

Uninstaller ابتدا از نصب فعلی پشتیبان می‌گیرد، اجزای VETRA را حذف می‌کند و به فایل‌های Microsoft Project و `.MPP` دست نمی‌زند.

## آزمون پس از نصب

```powershell
. 'C:\Program Files\VETRA\MSP Persianizer\vetra-env.ps1'
python -m vetra_core.cli diagnostics
python -m vetra_core.cli diagnostics --fake
python -m unittest discover -s 'C:\Program Files\VETRA\MSP Persianizer\tests' -p 'test_*.py' -v
```

## محدودیت فعلی

این Installer هسته Python و اسکلت COM را نصب می‌کند. هنوز Add-in کامل Ribbon/Dialog و فارسی‌سازی واقعی همه Viewهای MSP در آن فعال نشده است. قبل از انتشار سازمانی، امضای دیجیتال Installer، تست روی Windows پاک، تست Upgrade/Rollback و تأیید MPP Compatibility الزامی است.
