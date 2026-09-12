## VETRA MSP Persianizer  
**فارسی‌ساز و بومی‌ساز Microsoft Project 2024**  
<div dir="rtl">هدف این پروژه **ساخت جایگزین MSP نیست**؛ بلکه ایجاد یک لایه بومی‌سازی روی Microsoft Project 2024 است که موتور زمان‌بندی خود MSP را حفظ کند و تجربه کاربری فارسی/شمسی را به آن اضافه کند.</div>  
Microsoft Project 2024 خودش امکاناتی مثل Gantt، Timeline، وابستگی‌ها، Milestone، Baseline، Critical Path، مدیریت منابع، Resource Leveling، سناریوهای What-if و گزارش‌ها را دارد؛ بنابراین پروژه VETRA Persianizer نباید این موتور را دوباره‌سازی کند، بلکه باید روی آن سوار شود.   
   
⸻  
   
## 1. چشم‌انداز معماری  
```
┌───────────────────────────────────────────────┐
│              VETRA MSP Persianizer            │
│                                               │
│  Persian UI │ Jalali Calendar │ RTL │ Reports │
│                                               │
├───────────────────────────────────────────────┤
│       VETRA Localization & Integration Layer │
├───────────────────────────────────────────────┤
│                                               │
│          Microsoft Project 2024               │
│                                               │
│ Scheduling Engine │ Gantt │ WBS │ Resources   │
│ Baseline │ CPM │ Cost │ EVM │ Timeline        │
│                                               │
└───────────────────────────────────────────────┘

```
**اصل کلیدی**  
<div dir="rtl">**موتور MSP دست‌نخورده باقی بماند.**</div>  
VETRA فقط:  
* فارسی‌سازی  
* شمسی‌سازی  
* RTL  
* بومی‌سازی  
* تقویم ایرانی  
* Date Picker  
* نمایش تاریخ شمسی  
* گزارش فارسی  
* قالب‌بندی ایرانی  
* UX فارسی  
<div dir="rtl">را به آن اضافه کند.</div>  
<div dir="rtl">این موضوع مهم است چون MSP در حالت استاندارد خودش محاسبات زمان‌بندی، وابستگی‌ها، Baseline و Critical Path را انجام می‌دهد. </div>  
   
⸻  
   
## 2. لایه فارسی‌سازی کامل  
## 2.1 فارسی‌سازی Ribbon  
<div dir="rtl">تمام بخش‌های مرتبط با Project:</div>  
* File  
* Task  
* Resource  
* Project  
* View  
* Report  
* Format  
<div dir="rtl">به فارسی تبدیل شوند.</div>  
<div dir="rtl">مثلاً:</div>  

| MSP          | VETRA          |
| ------------ | -------------- |
| Task         | فعالیت         |
| Summary Task | فعالیت خلاصه   |
| Milestone    | نقطه عطف       |
| Duration     | مدت            |
| Start        | شروع           |
| Finish       | پایان          |
| Predecessors | پیش‌نیازها      |
| Successors   | فعالیت‌های پسین |
| Resource     | منبع           |
| Cost         | هزینه          |
| Work         | کار            |
| Baseline     | خط مبنا        |
| Actual       | واقعی          |
| Variance     | انحراف         |
| Critical     | بحرانی         |
| Slack        | شناوری         |
  
   
⸻  
   
## 3. فارسی‌سازی تمام Dialogها  
<div dir="rtl">نه فقط Ribbon.</div>  
<div dir="rtl">تمام پنجره‌های:</div>  
* Task Information  
* Resource Information  
* Project Information  
* Change Working Time  
* Assign Resources  
* Resource Leveling  
* Set Baseline  
* Project Options  
* Advanced  
* Calendar  
* Schedule  
* Constraints  
* Dependencies  
* Reports  
<div dir="rtl">باید فارسی و RTL باشند.</div>  
   
⸻  
   
## 4. موتور تقویم شمسی  
<div dir="rtl">این بخش **قلب پروژه** است.</div>  
VETRA باید یک Calendar Engine مستقل داشته باشد:  
```
Gregorian
     ↕
Jalali
     ↕
Hijri

```
<div dir="rtl">ولی:</div>  
**تقویم اصلی پروژه = شمسی**  
   
⸻  
   
## 5. Date Picker شمسی  
<div dir="rtl">هر جا MSP از کاربر تاریخ می‌گیرد:</div>  
* Start  
* Finish  
* Deadline  
* Constraint  
* Actual Start  
* Actual Finish  
* Status Date  
* Baseline Date  
Date Picker شمسی نمایش داده شود.  
<div dir="rtl">مثلاً:</div>  
```
┌─────────────────────────────┐
│      شهریور ۱۴۰۵            │
├─────────────────────────────┤
│ ش  ی  د  س  چ  پ  ج         │
│  ۱  ۲  ۳  ۴  ۵  ۶  ۷        │
│  ۸  ۹ ۱۰ ۱۱ ۱۲ ۱۳ ۱۴        │
│ ...                          │
└─────────────────────────────┘

```
   
⸻  
   
## 6. نمایش تاریخ شمسی در تمام MSP  
<div dir="rtl">نباید فقط ستون Start و Finish شمسی شوند.</div>  
<div dir="rtl">تاریخ شمسی باید در:</div>  
* Task Sheet  
* Gantt  
* Timeline  
* Calendar  
* Network Diagram  
* Reports  
* Filters  
* Grouping  
* Status  
* Baseline  
* Resource Views  
* چاپ  
* Export  
<div dir="rtl">نمایش داده شود.</div>  
MSP به‌صورت داخلی قالب‌های تاریخ را در ستون‌ها، Calendar، Timeline، Gantt و Reports مدیریت می‌کند؛ VETRA باید یک لایه شمسی یکپارچه روی این نقاط ایجاد کند.   
   
⸻  
   
## 7. Timescale شمسی  
<div dir="rtl">یکی از مهم‌ترین قابلیت‌ها.</div>  
<div dir="rtl">مثلاً:</div>  
```
۱۴۰۵
│
شهریور
│
هفته ۲
│
شنبه ۱۴۰۵/۰۶/۱۴

```
<div dir="rtl">قابلیت انتخاب:</div>  
**سطح اول**  
<div dir="rtl">سال</div>  
**سطح دوم**  
<div dir="rtl">ماه</div>  
**سطح سوم**  
<div dir="rtl">هفته / روز</div>  
<div dir="rtl">و قالب‌های مختلف:</div>  
```
شهریور ۱۴۰۵
شهریور
۱۴۰۵/۰۶
۱۴۰۵/۰۶/۱۵
۱۵ شهریور
شنبه ۱۵ شهریور

```
   
⸻  
   
## 8. Gantt کاملاً شمسی  
<div dir="rtl">محور زمانی Gantt:</div>  
```
شهریور ۱۴۰۵
──────────────────────────────
شنبه ۱۴ | یکشنبه ۱۵ | دوشنبه ۱۶ ...

```
<div dir="rtl">و تمام محاسبات همچنان توسط MSP انجام شود.</div>  
   
⸻  
   
## 9. تقویم کاری ایرانی  
VETRA باید بتواند Calendarهای ایرانی ایجاد کند.  
<div dir="rtl">مثلاً:</div>  
**تقویم اداری**  
```
شنبه تا چهارشنبه
07:30 تا 16:30
پنجشنبه
07:30 تا 13:00
جمعه تعطیل

```
**تقویم کارگاه**  
```
شنبه تا پنجشنبه
07:00 تا 17:00
جمعه تعطیل

```
**تقویم دو شیفته**  
```
شیفت 1
07:00–17:00

شیفت 2
17:00–23:00

```
   
⸻  
   
## 10. تعطیلات رسمی ایران  
Database تعطیلات:  
* نوروز  
* تعطیلات رسمی  
* مناسبت‌های رسمی  
* تعطیلات مذهبی  
* تعطیلات اختصاصی پروژه  
<div dir="rtl">و امکان:</div>  
**Update Calendar**  
<div dir="rtl">برای سال جدید.</div>  
   
⸻  
   
## 11. تعطیلات سفارشی  
<div dir="rtl">مثلاً:</div>  
<div dir="rtl">تعطیلی کارگاه به علت بارندگی</div>  
<div dir="rtl">ثبت شود:</div>  
```
تاریخ: ۱۴۰۵/۰۸/۱۲
نوع: تعطیلی پروژه
علت: بارندگی
توضیح: عدم امکان بتن‌ریزی

```
<div dir="rtl">و Calendar MSP تحت تأثیر قرار بگیرد.</div>  
   
⸻  
   
## 12. تبدیل تاریخ هوشمند  
<div dir="rtl">کاربر بتواند بنویسد:</div>  
```
1405/06/20

```
<div dir="rtl">و VETRA آن را به تاریخ داخلی مناسب MSP تبدیل کند.</div>  
<div dir="rtl">همچنین:</div>  
```
۲۰ شهریور ۱۴۰۵

```
<div dir="rtl">یا حتی:</div>  
```
20/06/1405

```
   
⸻  
   
## 13. اعداد فارسی  
<div dir="rtl">تمام اعداد قابل نمایش:</div>  
```
۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹

```
<div dir="rtl">و امکان انتخاب:</div>  
* اعداد فارسی  
* اعداد انگلیسی  
   
⸻  
   
## 14. واحدهای فارسی  
<div dir="rtl">مثلاً:</div>  
```
5 days

```
<div dir="rtl">نمایش:</div>  
```
۵ روز

```
<div dir="rtl">یا:</div>  
```
12 hrs

```
<div dir="rtl">نمایش:</div>  
```
۱۲ ساعت

```
<div dir="rtl">و برای:</div>  
* روز  
* ساعت  
* دقیقه  
* هفته  
* ماه  
   
⸻  
   
## 15. RTL واقعی  
<div dir="rtl">صرفاً ترجمه فارسی کافی نیست.</div>  
<div dir="rtl">ساختار UI باید RTL باشد:</div>  
```
فعالیت ← تاریخ ← Gantt

```
<div dir="rtl">نه:</div>  
```
Gantt → Date → Task

```
<div dir="rtl">همچنین:</div>  
* پنجره‌ها  
* Dialogها  
* Grid  
* فرم‌ها  
* منوها  
* Tooltipها  
* Date Picker  
* Reports  
   
⸻  
   
## 16. نام‌گذاری فارسی فیلدها  
<div dir="rtl">تمام فیلدهای MSP باید Mapping فارسی داشته باشند.</div>  
<div dir="rtl">مثلاً:</div>  
```
Task Name
↓
نام فعالیت

Duration
↓
مدت

Start
↓
شروع

Finish
↓
پایان

% Complete
↓
درصد تکمیل

Actual Cost
↓
هزینه واقعی

```
   
⸻  
   
## 17. Gantt دو زبانه  
<div dir="rtl">کاربر بتواند انتخاب کند:</div>  
**فارسی**  
```
اجرای فونداسیون

```
<div dir="rtl">یا:</div>  
**انگلیسی**  
```
Foundation Construction

```
<div dir="rtl">بدون تغییر داده اصلی.</div>  
   
⸻  
   
## 18. Persian Task ID  
<div dir="rtl">امکان تعریف شناسه:</div>  
```
فعالیت-001
فعالیت-002
فعالیت-003

```
<div dir="rtl">یا:</div>  
```
۰۱
۰۲
۰۳

```
   
⸻  
   
## 19. WBS فارسی  
<div dir="rtl">مثلاً:</div>  
```
۰۱ پروژه
  ۰۱.۰۱ تجهیز کارگاه
  ۰۱.۰۲ تخریب
  ۰۱.۰۳ گودبرداری
  ۰۱.۰۴ پایدارسازی

```
   
⸻  
   
## 20. Milestone فارسی  
<div dir="rtl">نمایش:</div>  
```
◆ تحویل فونداسیون
◆ پایان اسکلت
◆ پایان سفت‌کاری
◆ پایان پروژه

```
   
⸻  
   
## 21. Dependency فارسی  
<div dir="rtl">در UI:</div>  
* پایان به شروع  
* شروع به شروع  
* پایان به پایان  
* شروع به پایان  
<div dir="rtl">ولی در موتور MSP همان:</div>  
```
FS / SS / FF / SF

```
<div dir="rtl">باقی بماند.</div>  
   
⸻  
   
## 22. Lead / Lag فارسی  
<div dir="rtl">مثلاً:</div>  
```
FS + 3 روز

```
<div dir="rtl">نمایش:</div>  
<div dir="rtl">**۳ روز تأخیر**</div>  
<div dir="rtl">یا:</div>  
```
FS - 2 روز

```
<div dir="rtl">نمایش:</div>  
<div dir="rtl">**۲ روز همپوشانی**</div>  
   
⸻  
   
## 23. Constraintهای فارسی  
<div dir="rtl">مثلاً:</div>  
* هرچه زودتر  
* هرچه دیرتر  
* شروع در تاریخ مشخص  
* پایان در تاریخ مشخص  
* شروع نشدن قبل از  
* پایان نشدن قبل از  
* شروع نشدن بعد از  
* پایان نشدن بعد از  
   
⸻  
   
## 24. Critical Path فارسی  
<div dir="rtl">نمایش:</div>  
<div dir="rtl">**مسیر بحرانی**</div>  
<div dir="rtl">و:</div>  
<div dir="rtl">**فعالیت بحرانی**</div>  
MSP 2024 قابلیت نمایش چند Critical Path را نیز دارد؛ این قابلیت باید بدون تغییر موتور زمان‌بندی، در UI فارسی ارائه شود.   
   
⸻  
   
## 25. Float / Slack فارسی  
<div dir="rtl">نمایش:</div>  
```
شناوری کل: ۵ روز
شناوری آزاد: ۲ روز

```
   
⸻  
   
## 26. Baseline فارسی  
<div dir="rtl">تمام قابلیت‌های Baseline حفظ شوند.</div>  
<div dir="rtl">مثلاً:</div>  
```
خط مبنای شماره ۱
خط مبنای شماره ۲
...
خط مبنای شماره ۱۱

```
MSP Desktop امکان ذخیره تا 11 Baseline را دارد.   
   
⸻  
   
## 27. Tracking Gantt فارسی  
<div dir="rtl">نمایش:</div>  
```
Baseline
──────────────

Current
──────────────

Actual
──────────────

```
<div dir="rtl">با برچسب فارسی:</div>  
<div dir="rtl">**برنامه مبنا / برنامه جاری / عملکرد واقعی**</div>  
   
⸻  
   
## 28. Status Date شمسی  
<div dir="rtl">مثلاً:</div>  
<div dir="rtl">**تاریخ وضعیت: ۱۴۰۵/۰۶/۲۱**</div>  
   
⸻  
   
## 29. گزارش‌های فارسی  
<div dir="rtl">تمام Reports MSP:</div>  
* Project Overview  
* Milestone  
* Cost  
* Resource  
* Progress  
* Variance  
* Earned Value  
<div dir="rtl">با عنوان و تاریخ شمسی.</div>  
Project خودش گزارش‌های گرافیکی و قابل سفارشی‌سازی دارد؛ VETRA باید قالب‌های فارسی آماده روی همان سیستم ایجاد کند.   
   
⸻  
   
## 30. خروجی Excel فارسی  
<div dir="rtl">خروجی:</div>  
* نام فعالیت فارسی  
* تاریخ شمسی  
* اعداد فارسی  
* RTL  
* سربرگ فارسی  
* قالب چاپ ایرانی  
   
⸻  
   
## 31. خروجی PDF فارسی  
<div dir="rtl">با:</div>  
* فونت فارسی  
* RTL  
* تاریخ شمسی  
* لوگو  
* عنوان پروژه  
* شماره صفحه  
* مشخصات تهیه‌کننده  
   
⸻  
   
## 32. چاپ حرفه‌ای  
<div dir="rtl">قابلیت:</div>  
**Print Gantt**  
<div dir="rtl">با تنظیم:</div>  
* A4  
* A3  
* Landscape  
* Portrait  
* محدوده تاریخ  
* مقیاس  
* Header  
* Footer  
   
⸻  
   
## 33. Persian Template Library  
<div dir="rtl">قالب‌های آماده:</div>  
* پروژه ساختمانی  
* پروژه عمرانی  
* پروژه EPC  
* پروژه معماری  
* پروژه تأسیسات  
* پروژه راهسازی  
<div dir="rtl">مثلاً:</div>  
```
پروژه ساختمانی
├── مطالعات
├── طراحی
├── مجوز
├── تجهیز کارگاه
├── تخریب
├── گودبرداری
├── پایدارسازی
├── فونداسیون
├── اسکلت
├── سفت‌کاری
├── نازک‌کاری
├── تأسیسات
└── تحویل

```
   
⸻  
   
## 34. Persian Project Wizard  
<div dir="rtl">هنگام ساخت پروژه جدید:</div>  
```
ایجاد پروژه جدید
        ↓
نام پروژه
        ↓
تقویم
        ↓
تاریخ شروع
        ↓
ساعت کاری
        ↓
تعطیلات
        ↓
واحدها
        ↓
زبان
        ↓
قالب پروژه
        ↓
ایجاد

```
   
⸻  
   
## 35. تنظیمات VETRA Persianizer  
<div dir="rtl">پنل مستقل:</div>  
```
تنظیمات VETRA
│
├── زبان
├── تقویم
├── تاریخ
├── اعداد
├── RTL
├── فونت
├── تعطیلات
├── ساعات کاری
├── واحدها
├── قالب گزارش
├── خروجی
└── سازگاری

```
   
⸻  
   
## 36. پشتیبانی از فایل MPP  
<div dir="rtl">هدف اصلی:</div>  
<div dir="rtl">**فایل .MPP همچنان فایل اصلی باشد.**</div>  
<div dir="rtl">یعنی:</div>  
```
MSP 2024
   ↕
VETRA Persianizer
   ↕
.MPP

```
<div dir="rtl">کاربر بتواند فایل را باز کند، ویرایش کند و مجدداً در MSP استاندارد باز کند.</div>  
   
⸻  
   
## 37. حفظ Compatibility  
<div dir="rtl">این یکی از **Critical Requirements** پروژه است.</div>  
<div dir="rtl">فایل ایجادشده توسط VETRA نباید به فایل اختصاصی غیرقابل استفاده تبدیل شود.</div>  
<div dir="rtl">باید:</div>  
**Open in Microsoft Project**  
<div dir="rtl">بدون از دست رفتن اطلاعات اصلی امکان‌پذیر باشد.</div>  
   
⸻  
   
## 38. تشخیص نسخه MSP  
<div dir="rtl">سیستم تشخیص دهد:</div>  
* Project Standard 2024  
* Project Professional 2024  
<div dir="rtl">و در صورت نیاز:</div>  
* نسخه Office  
* نسخه Windows  
* وضعیت Add-in  
<div dir="rtl">را بررسی کند.</div>  
   
⸻  
   
## 39. نصب و Uninstall حرفه‌ای  
<div dir="rtl">نصب:</div>  
```
VETRA MSP Persianizer
        ↓
Detect Microsoft Project
        ↓
Detect Version
        ↓
Install Components
        ↓
Enable Persianization

```
<div dir="rtl">و Uninstall:</div>  
```
Remove VETRA
↓
Restore MSP
↓
Keep .MPP files

```
   
⸻  
   
## 40. Update Engine  
<div dir="rtl">امکان:</div>  
**Check for Updates**  
<div dir="rtl">برای:</div>  
* تقویم سال جدید  
* تعطیلات  
* ترجمه‌ها  
* Bug Fix  
* Compatibility  
* قالب‌ها  
   
⸻  
   
## 41. معماری پیشنهادی فنی  
<div dir="rtl">برای طراحی، من این ساختار را پیشنهاد می‌کنم:</div>  
```
VETRA MSP Persianizer
│
├── 01. Core
│   ├── Configuration
│   ├── License
│   └── Update
│
├── 02. Localization Engine
│   ├── Persian UI
│   ├── RTL
│   ├── Translation
│   └── Persian Numbers
│
├── 03. Jalali Calendar Engine
│   ├── Gregorian ↔ Jalali
│   ├── Holidays
│   ├── Work Calendar
│   └── Date Picker
│
├── 04. MSP Integration
│   ├── Tasks
│   ├── Resources
│   ├── Calendar
│   ├── Views
│   ├── Reports
│   └── Ribbon
│
├── 05. Persian UI Layer
│   ├── Dialogs
│   ├── Forms
│   ├── Menus
│   └── Tooltips
│
├── 06. Persian Reporting
│   ├── Gantt
│   ├── Timeline
│   ├── Reports
│   ├── PDF
│   └── Excel
│
├── 07. Templates
│   ├── Construction
│   ├── EPC
│   ├── Infrastructure
│   └── General
│
└── 08. Administration
    ├── Settings
    ├── Updates
    ├── Diagnostics
    └── License

```
   
⸻  
   
## 42. Roadmap پیشنهادی توسعه  
## Phase 0 — Research & Architecture  
```
بررسی MSP 2024
↓
بررسی Object Model / API
↓
تشخیص نقاط قابل Extension
↓
طراحی Calendar Engine
↓
طراحی Localization Layer

```
   
⸻  
   
## Phase 1 — MVP  
<div dir="rtl">اول فقط این‌ها:</div>  
* نصب روی MSP 2024  
* فارسی‌سازی UI اصلی  
* RTL  
* تقویم شمسی  
* Date Picker شمسی  
* تاریخ شمسی Start/Finish  
* اعداد فارسی  
* Timescale شمسی  
* تعطیلات ایران  
* تقویم کاری ایرانی  
   
⸻  
   
## Phase 2 — MSP Persian Experience  
* Gantt فارسی  
* WBS فارسی  
* Timeline فارسی  
* Network Diagram  
* Critical Path  
* Baseline  
* Tracking Gantt  
* Resource Views  
* Dialogهای فارسی  
* Reports فارسی  
   
⸻  
   
## Phase 3 — Professional Persianization  
* قالب‌های آماده  
* گزارش‌ساز فارسی  
* Excel Export  
* PDF Export  
* Print Templates  
* Persian Project Wizard  
* تنظیمات پیشرفته  
* چند تقویم  
* چند نوع Calendar  
   
⸻  
   
## Phase 4 — Advanced  
* نصب‌کننده حرفه‌ای  
* Update System  
* License System  
* Diagnostics  
* Version Detection  
* Compatibility Layer  
* Backup / Restore  
* سازمانی کردن تنظیمات  
   
⸻  
   
# 43. چیزی که   
## نباید  
## در این پروژه وارد شود  
<div dir="rtl">برای اینکه پروژه از مسیر اصلی منحرف نشود، این‌ها متعلق به **VETRA Suite** هستند، نه VETRA MSP Persianizer:</div>  
❌ CRM ❌ حسابداری ❌ قراردادها ❌ صورت‌وضعیت ❌ مدیریت پیمانکار ❌ گزارش روزانه کارگاه ❌ مدیریت مصالح ❌ انبار ❌ BIM ❌ VETRA Vision ❌ AI Project Control ❌ مدیریت اسناد سازمانی ❌ Workflow سازمانی  
<div dir="rtl">این پروژه باید یک محصول بسیار متمرکز باشد:</div>  
**Microsoft Project 2024 + Persian + Jalali + RTL + Iranian Calendar + Persian Reports**  
   
⸻  
   
## 44. تعریف نهایی محصول  
<div dir="rtl">اگر بخواهم برای README / Roadmap / Architecture پروژه یک جمله رسمی بنویسم:</div>  
**VETRA MSP Persianizer یک لایه بومی‌سازی و فارسی‌سازی حرفه‌ای برای Microsoft Project 2024 است که بدون جایگزینی موتور زمان‌بندی Microsoft Project، محیط کاربری، تقویم، تاریخ‌ها، Timescale، Gantt، گزارش‌ها و خروجی‌های آن را به‌صورت کامل با زبان فارسی، رابط راست‌به‌چپ، تقویم هجری شمسی و استانداردهای کاری پروژه‌های ایران سازگار می‌کند.**  
و یک نکته معماری بسیار مهم: **VETRA Persianizer نباید Scheduling Engine خودش را بسازد.** موتور اصلی باید MSP باشد؛ چون MSP همین حالا قابلیت‌های پیچیده‌ای مثل زمان‌بندی وابسته، Resource Leveling، Baseline، Critical Path و مدیریت چند پروژه را دارد.   
