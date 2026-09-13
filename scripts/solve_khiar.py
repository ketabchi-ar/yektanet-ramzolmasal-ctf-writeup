#!/usr/bin/env python3
"""
حل مرحله هفتم: خیار (khiar)
منطق ضرب‌المثل: «هر چه بگندد نمکش می‌زنند، وای به روزی که بگندد نمک»
سرنخ‌ها:
  - پرامپت: «شمارت داره می‌گنده. به ضرب‌المثل‌های فارسی فکر کن.»
  - وضعیت (Charm): «تو رو به بانمکیت می‌شناسن.»
روش حل:
  «بانمکیت» در سیستم مسابقه اشاره به شناسه کاربری (User ID) منحصر‌به‌فرد شما دارد
  که در خروجی اندپوینت api/me برگردانده می‌شود و به عنوان نمک (Salt) در نظر گرفته می‌شود.
  برای نمک زدن به شماره موبایل، مقدار هش SHA-256 حاصل از ترکیب شماره موبایل ثبت‌نامی و شناسه کاربری محاسبه می‌شود:
  flag = YEK{sha256(phone + user_id)}
"""

import hashlib
import os
import requests

# شماره موبایل ثبت‌نامی کاربر در سامانه مسابقه (مانند 09123456789)
phone = os.getenv("CTF_PHONE", "09XXXXXXXXX")

# شناسه اختصاصی کاربر (User ID) که در پاسخ api/me قابل مشاهده است (یک رشته ۸ کاراکتری هگزادسیمال)
user_id = os.getenv("CTF_USER_ID", "YOUR_USER_ID")

salt_string = f"{phone}{user_id}"
flag_hash = hashlib.sha256(salt_string.encode('utf-8')).hexdigest()
flag = f"YEK{{{flag_hash}}}"

print(f"شماره موبایل: {phone}")
print(f"شناسه کاربری (نمک/Salt): {user_id}")
print(f"پرچم تولید شده: {flag}")

cookies = {
    'ctf_device': os.getenv('CTF_DEVICE', 'YOUR_CTF_DEVICE_COOKIE'),
    'ctf_session': os.getenv('CTF_SESSION', 'YOUR_CTF_SESSION_COOKIE')
}

if __name__ == '__main__':
    # انتخاب چالش خیار
    requests.post('https://256.yektanet.tech/ramzolmasal/api/select', json={'id': 'khiar'}, cookies=cookies)

    # ثبت پرچم
    res = requests.post('https://256.yektanet.tech/ramzolmasal/api/submit', json={'flag': flag}, cookies=cookies)
    print("پاسخ سرور:", res.json())
