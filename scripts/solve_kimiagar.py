#!/usr/bin/env python3
"""
حل مرحله نهم: کیمیاگر (kimiagar)
منطق ضرب‌المثل: «زرگر که باشی، غربال دست میگیری»
سرنخ‌ها:
  - پرامپت: «زرگر که باشی، غربال دست میگیری. کارگاه این‌جاست: api/kimiagar»
  - سرنخ وضعیت (Charm): «محک خط را با شصت‌وچهار رنگ می‌نویسد، نه با شانزده.»
روش حل:
  ۱. اتصال به وب‌سوکت کارگاه کیمیاگر در wss://256.yektanet.tech/ramzolmasal/api/kimiagar
  ۲. سرور جریانی از حدود ۵۵۰ تا ۶۰۰ کلمه ارسال می‌کند که در کل شامل ۶۴ کلمه یکتا (شصت‌وچهار رنگ) است.
  ۳. برای غربال کردن طلا (زرگر): نماد شیمیایی طلا در جدول تناوبی Au است.
     کلماتی که هش SHA-256 آن‌ها در قالب Base64 با دو حرف Au شروع می‌شوند، کلمات طلایی هستند (دقیقاً ۱۶ کلمه).
  ۴. این ۱۶ کلمه به ترتیب الفبایی مرتب شده و بدون فاصله به هم متصل می‌شوند.
  ۵. پرچم به فرمت YEK{<joined_gold_words>} ثبت می‌شود.
"""

import asyncio
import websockets
import hashlib
import base64
import os
import requests

cookies = {
    'ctf_device': os.getenv('CTF_DEVICE', 'YOUR_CTF_DEVICE_COOKIE'),
    'ctf_session': os.getenv('CTF_SESSION', 'YOUR_CTF_SESSION_COOKIE')
}

async def solve():
    uri = "wss://256.yektanet.tech/ramzolmasal/api/kimiagar"
    headers = {
        "Cookie": f"ctf_device={cookies['ctf_device']}; ctf_session={cookies['ctf_session']}"
    }

    words = []
    print("در حال اتصال به کارگاه کیمیاگر...")
    async with websockets.connect(uri, additional_headers=headers) as ws:
        while True:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=2.5)
                words.append(msg.strip())
            except asyncio.TimeoutError:
                break

    unique_words = sorted(list(set(words)))
    print(f"تعداد کلمات دریافتی: {len(words)} | تعداد کلمات یکتا: {len(unique_words)}")

    gold_words = []
    for w in unique_words:
        digest = hashlib.sha256(w.encode('utf-8')).digest()
        b64 = base64.b64encode(digest).decode('ascii')
        if b64.startswith('Au'):
            gold_words.append(w)

    gold_words_sorted = sorted(gold_words)
    print(f"تعداد قطعات طلا (هش با پیشوند Au): {len(gold_words_sorted)}")

    flag = f"YEK{''.join(gold_words_sorted)}"
    print(f"پرچم نهایی کیمیاگر: {flag}")

    # انتخاب چالش و ثبت پرچم
    requests.post('https://256.yektanet.tech/ramzolmasal/api/select', json={'id': 'kimiagar'}, cookies=cookies)
    res = requests.post('https://256.yektanet.tech/ramzolmasal/api/submit', json={'flag': flag}, cookies=cookies)
    print("پاسخ سرور:", res.json())

if __name__ == '__main__':
    asyncio.run(solve())
