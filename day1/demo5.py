#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo5.py
# Author: MuNian
# Date  : 2020-01-07

import requests


session = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

data = {
    'email': '13129597923',
    'password':'munian123'

}

# 代入data参数请求网页
session.post('http://www.renren.com/SysHome.do', data=data)

response = session.get('http://www.renren.com/410043129/profile')


print(response.text)


