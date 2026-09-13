#!/usr/bin/env python3
"""
حل مرحله دهم (فینال): دیوار به دیوار (pelak)
منطق ضرب‌المثل: «مرغ همسایه غازه!»
سرنخ‌ها:
  - پرامپت: «اینجا خونته. هرچی تو خونه‌ی خودت هست، به چشمت نمیاد.»
  - وضعیت (Charm): «همیشه شماره تلفنشو می‌چسبونه به شماره موبایلش و میشه رمزش.»
روش حل:
  ۱. خانه خودمان در دامنه https://256.yektanet.tech (پلاک ۲۵۶) قرار دارد.
  ۲. همسایه دیوار به دیوار ما پلاک ۲۵۴ در دامنه https://254.yektanet.tech است که تنها با ارسال هدر Referer از پلاک ۲۵۶ پاسخ می‌دهد.
  ۳. در پلاک ۲۵۴ تصویر ghaz.jpg قرار دارد که در انتهای آن یک فایل فشرده Zip مخفی شامل تصویر morgh.jpg پیوست شده است (مرغ داخل غاز همسایه!).
  ۴. کد پستی پلاک همسایه برابر با 3767481923 است.
  ۵. با جستجوی این کد پستی در گوگل، شرکت «غاز ایران» (مدیریت امیر طاهری در نسیم شهر) در سامانه جویشگر پیدا می‌شود:
     - تلفن: 02156573210 (بدون صفر و پیش شماره: 2156573210)
     - همراه: 09198584667 (بدون صفر: 9198584667)
  ۶. اتصال شماره تلفن به همراه: 21565732109198584667 رمز بازگشایی فایل زیپ است!
  ۷. با باز شدن فایل زیپ، تصویر morgh.jpg استخراج می‌شود که در بنر پایین آن نوشته شده:
     «رمز زیپ: 6ebd1e974a22»
  ۸. پرچم نهایی حاصل ترکیب رمز فایل زیپ و کد استخراج‌شده داخل تصویر مرغ است:
     YEK{21565732109198584667:6ebd1e974a22}
"""

import requests

cookies = {
    'ctf_device': 'c58274c5d2b8e26db7753999381fcabb',
    'ctf_session': 'b309c321eed958ae047cc0eb89edfea75fdfa4931b4a14f27d0b9bf88ff05a1b'
}

zip_password = "21565732109198584667"
secret_token = "6ebd1e974a22"

flag = f"YEK{{{zip_password}:{secret_token}}}"
print(f"Submitting final flag: {flag}")

# Select challenge
requests.post('https://256.yektanet.tech/ramzolmasal/api/select', json={'id': 'pelak'}, cookies=cookies)

# Submit flag
res = requests.post('https://256.yektanet.tech/ramzolmasal/api/submit', json={'flag': flag}, cookies=cookies)
print("Response:", res.json())
