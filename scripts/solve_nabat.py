#!/usr/bin/env python3
"""
حل مرحله پنجم: ارزش نبات (nabat)
منطق ضرب‌المثل: «خر چه داند قیمت نقل و نبات»
روش: ارسال درخواست به api/price با هدر User-Agent برابر با khar و استخراج قیمت
"""

import requests
import json

def to_english_digits(s: str) -> str:
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    trans = str.maketrans(persian_digits, english_digits)
    return s.translate(trans)

def solve(cookies: dict):
    base_url = 'https://256.yektanet.tech/ramzolmasal/api'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'khar' # سرنخ robots.txt و ضرب‌المثل «خر چه داند قیمت نقل و نبات»
    }
    
    url = f'{base_url}/price?product_name=نبات'
    print(f'[*] دریافت قیمت نبات با User-Agent: khar...')
    r = requests.get(url, headers=headers, cookies=cookies)
    resp = r.json()
    print(f'[+] پاسخ سرور: {resp}')
    
    raw_price = resp['price']
    price_digits = to_english_digits(raw_price)
    flag = f'YEK{{{price_digits}}}'
    print(f'[+] پرچم تولید شد: {flag}')
    
    # انتخاب و ثبت
    requests.post(f'{base_url}/select', headers=headers, cookies=cookies, json={'id': 'nabat'})
    sub = requests.post(f'{base_url}/submit', headers=headers, cookies=cookies, json={'flag': flag}).json()
    print(f'[*] نتیجه ثبت پرچم: {sub}')

if __name__ == '__main__':
    cookies = {
        'ctf_device': 'c58274c5d2b8e26db7753999381fcabb',
        'ctf_session': 'b309c321eed958ae047cc0eb89edfea75fdfa4931b4a14f27d0b9bf88ff05a1b'
    }
    solve(cookies)
