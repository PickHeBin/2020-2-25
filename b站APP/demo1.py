#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-02-22

import requests

url = 'https://api.bilibili.com/x/click-interface/web/heartbeat'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

data = {
    'aid': '90269539',
    'cid': '154157876',
    'mid': '424186080',
    'csrf': 'deb49c1c55cc37b3931aad8cce5e39f8',
    'played_time': '149',
    'realtime': '149',
    'start_ts': '1582350770',
    'type': '3',
    'dt': '2',
    'play_type': '0'
}

response = requests.post(url, headers=headers, data=data).text
print(response)
