#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 黄金数据.py
# Author: MuNian
# Date  : 2020-02-22

import requests

url = 'http://web.juhe.cn:8080/finance/gold/shgold?key=c75c0190f87cf6a66e3f1fa7f2b4aa06'

response = requests.get(url).json()

data = response['result']

# result = map(lambda x:x, data)
for i in data:
    for n in range(1, 10):
        huanjin = i[str(n)]
        print(huanjin)
