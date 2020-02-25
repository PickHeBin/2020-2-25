#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-01-08

'''
Python爬虫假装浏览器


'''

import requests

proxie = {
    'http':'http://localhost:5555/random'
}


print(proxie)
url = 'https://www.baidu.com'

response = requests.get(url, proxies=proxie)
print(response)