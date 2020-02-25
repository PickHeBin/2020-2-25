#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day1.py
# Author: MuNian
# Date  : 2020-02-09

import requests
from lxml import etree
import re
from pandas import DataFrame
import pandas as pd

print("请输入要查询域名。（格式：qq.com）输入后按回车")
x = input()
# x="sina.com"
url = "http://whois.chinaz.com/" + x
r = requests.get(url)
r.encoding = 'utf-8'
root = etree.HTML(r.text)
# 获取wihos
cxym = root.xpath('//a[@class="col-gray03 fz18 pr5"]/text()')
zcs = root.xpath('//div[@class="block ball"]/span/text()')
print(zcs)
# lxyx=root.xpath('//li[@class="clearfix bor-b1s bg-list"]/div[@class="fr WhLeList-right block ball lh24"]/span/text()')
lxyx = root.xpath('//div[@class="fr WhLeList-right block ball lh24"]/span/text()')[0]
lxyx1 = '联系邮箱</div><div class="fr WhLeList-right block ball lh24"><span>(.*?)</span>'
lxdh1 = '联系电话</div><div class="fr WhLeList-right block ball lh24"><span>(.*?)</span>'
lxyx = re.findall(lxyx1, r.text)
lxdh = re.findall(lxdh1, r.text)
# lxdh=root.xpath('//div[@class="fr WhLeList-right block ball lh24"]/span/text()')[1]
# cjsj=root.xpath('//li[@class="clearfix bor-b1s bg-list"]/div[@class="fr WhLeList-right"]/span/text()')
# cjsj=root.xpath('//li[@class="clearfix bor-b1s bg-list"]/div[@class="fr WhLeList-right"]/span/text()')[0]
cjsj1 = '>创建时间</div><div class="fr WhLeList-right"><span>(.*?)</span>'
cjsj = re.findall(cjsj1, r.text)
gqsj1 = '过期时间</div><div class="fr WhLeList-right"><span>(.*?)</span>'
gqsj = re.findall(gqsj1, r.text)
gxsj1 = '更新时间</div><div class="fr WhLeList-right"><span>(.*?)</span>'
ymfwq1 = '域名服务器</div><div class="fr WhLeList-right"><span>(.*?)</span>'
dns1 = 'DNS</div><div class="fr WhLeList-right">(.*?)</div></li>'
gqsj = re.findall(gqsj1, r.text)
gxsj = re.findall(gxsj1, r.text)
ymfwq = re.findall(ymfwq1, r.text)
dns = re.findall(dns1, r.text)
# dns=dns.strip()
# 获取 IP
url2 = "http://ip.tool.chinaz.com/" + x
r1 = requests.get(url2)
r1.encoding = 'utf-8'
root1 = etree.HTML(r1.text)

ip = 'None'
szdz = 'None'
ipszd = 'None'
try:
    ip11 = root1.xpath('//p[@class="WhwtdWrap bor-b1s col-gray03"]/span/text()')
    ip = ip11[1]
    ip = ip.split(',')
    szdz = ip11[2]
    szdz = szdz.split(',')
    ipszd = ip11[3]
    ipszd = ipszd.split(',')
except Exception as e:
    pass

# 获取ICP备案信息
url2 = "http://www.jsons.cn/icpinfo/" + x
r2 = requests.get(url2)
r2.encoding = 'utf-8'
root2 = etree.HTML(r2.text)
print(url2, root1.text)

zbdw = root2.xpath('//li[@class="bg-gray clearfix"]/p/text()')[0].strip().split(',')
zbdwxz = root2.xpath('//ul[@class="bor-t1s IcpMainInfo"]/li/p/strong/text()')[0].strip().split(',')
baxkz = root2.xpath('//ul[@class="bor-t1s IcpMainInfo"]/li/p/font/text()')[0].strip().split(',')
wzmc = root2.xpath('//ul[@class="bor-t1s IcpMainInfo"]/li/p/text()')[3].strip().split(',')
wzfzr = root2.xpath('//ul[@class="bor-t1s IcpMainInfo"]/li/p/text()')[4].strip().split(',')
wzwz = root2.xpath('//ul[@class="bor-t1s IcpMainInfo"]/li/p/text()')[5].strip().split(',')
sqrq = root2.xpath('//ul[@class="bor-t1s IcpMainInfo"]/li/p/text()')[6].strip().split(',')
print(zbdw, zbdwxz, baxkz, wzmc, wzfzr, wzwz, sqrq)
# 合并数据
shuju = DataFrame(
    [cxym, zcs, lxyx, lxdh, cjsj, gqsj, gxsj, ymfwq, dns, ip, szdz, ipszd, zbdw, zbdwxz, baxkz, wzmc, wzfzr, wzwz,
     sqrq]).T
# shuju=DataFrame([cxym,zcs,lxyx,lxdh,cjsj,gqsj,gxsj,ymfwq,dns,ip11]).T
shuju.columns = ['域名', '注册商', '联系邮箱', '联系电话', '创建时间', '过期时间', '更新时间', '域名服务器', 'DNS', '解析IP', '数字地址', 'IP所在地', '主办单位',
                 '性质', '备案许可证', '网站名称', ' 负责人', '网站网址', '审核通过时间']
# 保存在本地
shuju.to_csv('shuju.csv')
