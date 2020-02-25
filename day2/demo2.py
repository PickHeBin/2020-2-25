#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo2.py
# Author: MuNian
# Date  : 2020-01-08

'''

时间都去哪了?
课后高清录播
两天一节正课   2小时   两天 零散的两小时 一对一辅导 解答 补课

12K ?  有没有时间?
竞争力?  淘汰?


6880?    15k   20K?
学费分期 500预订一个名额  6380 分期12期   一个月才531块钱   花呗 借呗 /...


最后3个弟子名额?
兼职


提升能力?





'''

# pyquery: 通过前端属性 类选择  id选择 来获取数据

import requests
from pyquery import PyQuery as pq  # as 别名

count = 1

# 创建函数
def Meizitu(page): # 形参

    global count
    # 请求地址
    url = 'https://www.mzitu.com/207115/{}'.format(page)

    # 请求头
    headers = {
        # 每次都是从第一页到想要的页数
        'referer': 'https://www.mzitu.com/217520',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

    # 对妹子图网页发送请求 并且获取到响应的数据
    response = requests.get(url, headers=headers).text
    # 初始化数据
    doc = pq(response)
    # 根据类选择器来获取到对应的数据
    main_image = doc('.main-image p a img').items()
    for n in main_image:
        # 通过属性取到对应的图片链接
        img_urls = n.attr('src')
        images = requests.get(img_urls, headers=headers)
        # a--> 文件追加  b 进制文件读写
        # f = open('妹子图/{}.jpg'.format(count), 'ab')
        # f.write(images.content)
        # count += 1  # count = count + 1
        # f.close()
        with open('妹子图/{}.jpg'.format(count), 'ab') as f:
            f.write(images.content)
            count += 1



data = input('请输入你要抓取的页数:')
for i in range(1, int(data)):
    Meizitu(i) # 实参



