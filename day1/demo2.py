#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo2.py
# Author: MuNian
# Date  : 2020-01-07

import requests

url = 'https://v.6.cn/coop/mobile/index.php?act=recommend&padapi=minivideo-getlist.php&page=1'

headers = {
    # 模拟浏览器 浏览器类型
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'
}

response = requests.get(url, headers=headers, verify=False).json()
print(response)

