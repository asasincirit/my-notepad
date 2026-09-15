[app]

# نام برنامه
title = Notepad++

# نام پکیج اندروید
package.name = mynotepad

# دامنه یکتا برای برنامه
package.domain = org.joharchi

# پوشه‌ای که main.py داخل آن قرار دارد
source.dir = .

# فایل‌هایی که همراه برنامه وارد APK شوند
source.include_exts = py,txt,png,jpg,jpeg,kv

# نسخه برنامه
version = 1.0

# کتابخانه‌های مورد نیاز
requirements = python3,kivy

# حالت نمایش
orientation = portrait

# تمام صفحه نبودن
fullscreen = 0


# ----------------------------------------
# تنظیمات اندروید
# ----------------------------------------

# حداقل نسخه Android
android.minapi = 23

# نسخه هدف Android
android.api = 35

# معماری‌های قابل پشتیبانی
android.archs = arm64-v8a

# مجوزهای مورد نیاز
android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO

android.accept_sdk_license = True
# ----------------------------------------
# ظاهر برنامه
# ----------------------------------------

# آیکون برنامه
# اگر آیکون داری، این خط را از حالت کامنت خارج کن:
icon.filename = %(source.dir)s/icon.png


# ----------------------------------------
# تنظیمات Buildozer
# ----------------------------------------

[buildozer]

# لاگ ساخت
log_level = 2

# هشدارها
warn_on_root = 1
