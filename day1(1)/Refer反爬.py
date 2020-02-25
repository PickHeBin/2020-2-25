#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Refer反爬.py
# Author: MuNian
# Date  : 2020-01-14

import requests


url = 'https://i5.mmzztt.com/2019/09/14a06.jpg'

headers = {
    'Referer': 'https://www.mzitu.com/202948/3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'
}

img = requests.get(url, headers=headers).content
print(img)

