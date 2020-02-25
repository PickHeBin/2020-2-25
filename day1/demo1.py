#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-01-07

'''
通用爬虫  百度  谷歌....搜索引擎
聚焦爬虫  精准的抓取数据

网络协议:
HTTP 超文本传输协议 发布 接受 HTML页面的方法  80
HTTPS HTTP + SSL(安全套接字) 443
Web安全传输协议 --> 传输层

HTTP的请求与响应:

模拟请求百度过程:
地址输入url --> 发送请求 --> 响应(response) --> 可以看到的界面Html  css  js

requests ==> Python第三方库
decode 解码
encode 编码
.text  字符格式
.content 字节内容
.json()  json格式
.request.headers 查看请求头部信息
'''

import requests

# 请求的地址
url = 'https://www.baidu.com/'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

response = requests.get(url, headers=headers).content.decode()
print(response)








