#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-01-14

'''
https://www.baidu.com/   网址  url
统一资源定位符
http: 网络当中一个协议   超文本传输
hhtp + sll(安全套接字)


www.baidu.com ??? --域名?  解析出来可以得到服务器host(地址)

爬虫: 1. 遵守网络协议
     2. web安全机制
     3. 网络蜘蛛 --> 采集网页上面所有的数据  看不到(采集  数据挖掘) 看的到?

网络攻防: xss 网络漏洞?
            csrf 伪造攻击?


ssl

'''

# requests --> 请求?  请求服务器

import requests


url = 'https://www.baidu.com/'
response = requests.get(url).content.decode()
print(response)






