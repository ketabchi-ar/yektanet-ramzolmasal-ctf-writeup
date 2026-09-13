#!/usr/bin/env python3
"""
حل مرحله هفتم: خیار (khiar)
منطق ضرب‌المثل: «هر چه بگندد نمکش می‌زنند، وای به روزی که بگندد نمک»
سرنخ‌ها:
  - پرامپت: «شمارت داره می‌گنده. به ضرب‌المثل‌های فارسی فکر کن.»
  - وضعیت (Charm): «تو رو به بانمکیت می‌شناسن.»
روش حل:
  «بانمکیت» در سیستم به معنی شناسه کاربری (User ID) شماست که به عنوان نمک (Salt) در نظر گرفته می‌شود.
  برای نمک زدن به شماره موبایل، مقدار هش SHA-256 ترکیب شماره موبایل و شناسه کاربری محاسبه می‌شود:
  flag = YEK{sha256(phone + id)}
"""

import hashlib
import requests

phone = "09337373711"
user_id = "861e88c8"

salt_string = f"{phone}{user_id}"
flag_hash = hashlib.sha256(salt_string.encode('utf-8')).hexdigest()
flag = f"YEK{{{flag_hash}}}"

print(f"Phone: {phone}")
print(f"User ID (Salt): {user_id}")
print(f"Flag: {flag}")

cookies = {
    'ctf_device': 'c58274c5d2b8e26db7753999381fcabb',
    'ctf_session': 'b309c321eed958ae047cc0eb89edfea75fdfa4931b4a14f27d0b9bf88ff05a1b'
}

# Select challenge
requests.post('https://256.yektanet.tech/ramzolmasal/api/select', json={'id': 'khiar'}, cookies=cookies)

# Submit flag
res = requests.post('https://256.yektanet.tech/ramzolmasal/api/submit', json={'flag': flag}, cookies=cookies)
print("Submit response:", res.json())
