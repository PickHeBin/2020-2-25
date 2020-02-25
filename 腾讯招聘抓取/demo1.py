#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-02-20

'''
Python 就业:
    薪资好  发展(AI)
    零基础而言 --> 开发工程师  爬虫工程师  自动化工程师
        java --> 结合 架构 全栈

1. 读书:  爬虫兼职多  毕业AI方向 -->  学员跟着老师学习 --> 3个月 重修 留级 兼职  300 - 800 一天  兼职老师带着做兼职  实战 毕业薪资高
2. 其他行业: 零基础  主导开发方向  岗位多 快速就业  15K左右  辅导 爬虫 自动化 未来发展
3. 编程基础: 全栈 架构  数据分析 数据挖掘  30K  自动化开发 ..

8K - 30K
Python学院院长 --> 腾讯内推名额  2个名额
支付500 低1500 学费优惠 剩下 分期
腾讯AI班级(单独5880) --> 主讲  腾讯专家 辅导 解答
弟子( 一对一解答 辅导 补课) 5个弟子名额


'''

import requests
import time

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'

for page in range(1, 10):
    # 请求参数
    params = {
        'timestamp': str(time.time()), # 时间戳
        'keyword': 'python',  # 岗位名称
        'pageIndex': page,  # 页数
        'pageSize': '10',  # 每个页面展示的数据有多少条
        'language': 'zh-cn',
        'area': 'cn'
    }

    response = requests.get(url, params=params).json()
    # 打印输入
    data = response['Data']['Posts']

    # [i for i in data]
    # posts = map(data)
    # 遍历
    for i in data:
        # 岗位名称
        RecruitPostName = i['RecruitPostName']
        # print(RecruitPostName)

        # 城市
        LocationName = i['LocationName']
        print(LocationName)

