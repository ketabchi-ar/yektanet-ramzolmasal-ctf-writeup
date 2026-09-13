#!/usr/bin/env python3
"""
حل مرحله دوم: کلاغ (kalagh)
الگوریتم: محاسبه Proof-of-Work هش FNV-1a (32-bit unsigned) تا مرحله ۴۰
"""

import requests
import json
import sys

def fnv1a(s: str) -> int:
    h = 2166136261
    for b in s.encode('ascii'):
        h = ((h ^ b) * 16777619) & 0xFFFFFFFF
    return h

def mine_nonce(payam: str) -> tuple[str, int]:
    prefix = (payam + ':').encode('ascii')
    h_init = 2166136261
    for b in prefix:
        h_init = ((h_init ^ b) * 16777619) & 0xFFFFFFFF
    
    nonce = 0
    while True:
        h = h_init
        s_nonce = str(nonce).encode('ascii')
        for b in s_nonce:
            h = ((h ^ b) * 16777619) & 0xFFFFFFFF
        if h < 2048:
            return str(nonce), h
        nonce += 1

def solve(cookies: dict):
    base_url = 'https://256.yektanet.tech/ramzolmasal/api'
    headers = {'Content-Type': 'application/json'}
    
    # 1. دریافت کلاغ اول
    r = requests.get(f'{base_url}/kalagh', headers=headers, cookies=cookies)
    curr = r.json()
    print(f'[*] کلاغ اول: شماره {curr.get("shomare")}')
    
    crow_40_payam = None
    while True:
        shomare = curr.get('shomare')
        payam = curr.get('payam')
        
        if shomare == 40:
            crow_40_payam = payam
            print(f'[+] پیام کلاغ چهلم پیدا شد: {payam}')
        
        nonce, q = mine_nonce(payam)
        resp = requests.post(
            f'{base_url}/kalagh',
            headers=headers,
            cookies=cookies,
            json={'shomare': shomare, 'nonce': nonce}
        )
        curr = resp.json()
        if 'error' in curr:
            print(f'[*] پایان زنجیره: {curr["error"]}')
            break

    flag = f'YEK{{{crow_40_payam}}}'
    print(f'[+] پرچم نهایی مرحله کلاغ: {flag}')
    
    # ثبت پرچم
    requests.post(f'{base_url}/select', headers=headers, cookies=cookies, json={'id': 'kalagh'})
    sub = requests.post(f'{base_url}/submit', headers=headers, cookies=cookies, json={'flag': flag}).json()
    print(f'[*] نتیجه ثبت پرچم: {sub}')

if __name__ == '__main__':
    # کوکی‌های سشن را جایگزین کنید
    cookies = {
        'ctf_device': 'c58274c5d2b8e26db7753999381fcabb',
        'ctf_session': 'b309c321eed958ae047cc0eb89edfea75fdfa4931b4a14f27d0b9bf88ff05a1b'
    }
    solve(cookies)
