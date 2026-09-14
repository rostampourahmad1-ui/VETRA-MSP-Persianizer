# طراحی Integration ویندوزی Microsoft Project 2024

## وضعیت

`WindowsMspComAdapter` اسکلت اولیه اتصال COM است و فقط روی Windows دارای Microsoft Project اجرا می‌شود. این Adapter هنوز محصول نصب‌شونده نهایی یا فارسی‌سازی Ribbon/Dialog نیست؛ هدف فعلی آن اثبات Lifecycle، خواندن Snapshot، تنظیم Project Start و Save/Open فایل MPP است.

## پیش‌نیازهای محیط آزمایش

Windows سازگار، Microsoft Project 2024، Python 3.10 یا بالاتر، مجوز MSP، دسترسی COM و بسته `pywin32` لازم است. نصب pywin32 فقط روی ماشین Windows آزمایش انجام می‌شود:

```powershell
python -m pip install pywin32
```

کد این ریپو عمداً روی Linux، بدون اجرای COM، قابل تست باقی می‌ماند.

## اجرای نمونه روی Windows

```powershell
$env:PYTHONPATH = "src"
python -c "from vetra_core.windows_msp_adapter import WindowsMspComAdapter; a=WindowsMspComAdapter(visible=True); print(a.environment())"
```

در صورت بازبودن پروژه، Snapshot فعالیت‌ها را با `list_tasks()` دریافت کنید. در اولین آزمایش فقط خواندن انجام دهید و از نوشتن روی فایل اصلی خودداری کنید.

## ترتیب آزمایش Adapter

۱. از فایل MPP نسخه پشتیبان تهیه کنید.
۲. MSP را بدون VETRA باز کنید و مقادیر مرجع را ثبت کنید.
۳. Adapter را با `visible=True` اجرا کنید.
۴. نسخه محیط و تعداد Taskها را ثبت کنید.
۵. یک کپی آزمایشی MPP را باز کنید.
۶. Project Start را فقط روی کپی تغییر دهید.
۷. فایل را با نام جدید ذخیره کنید.
۸. فایل ذخیره‌شده را در MSP استاندارد باز کنید.
۹. Snapshot قبل و بعد را با `compare_task_snapshots` مقایسه کنید.
۱۰. هر اختلاف را بررسی و در `docs/acceptance-tests.md` ثبت کنید.

## سیاست ایمنی

Adapter نباید موتور زمان‌بندی مستقل داشته باشد. مقداردهی تاریخ به MSP سپرده می‌شود. هیچ عملیات Delete، Overwrite یا تغییر فایل اصلی در تست خودکار مجاز نیست. هر عملیات نوشتن باید روی مسیر خروجی جدید انجام شود.

## محدودیت‌های فعلی

خواندن کامل Start و Finish، Resource، Calendar، Baseline، View و Report به نگاشت دقیق Object Model MSP و آزمایش روی نسخه واقعی نیاز دارد. نسخه فعلی فقط اسکلت این مرز را فراهم می‌کند و ادعای فارسی‌سازی کامل MSP ندارد.
