#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo2.py
# Author: MuNian
# Date  : 2020-01-14

'''
多线程: 多任务?
        一个人做多个事情?  一个手摸键盘  一个手鼠标   同步
        两个手  三  假的同步   异步




'''

import threading
import requests


def Video():
    # 伪造请求头
    headers = {
        # 浏览器类型
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'
    }

    for page in range(1, 5):
        # https://v.6.cn/coop/mobile/index.php?act=recommend&padapi=minivideo-getlist.php&page=2
        url = 'https://v.6.cn/coop/mobile/index.php?act=recommend&padapi=minivideo-getlist.php&page=' + str(page)

        # 模拟浏览器请求服务器
        #  返回的数据 json??
        response = requests.get(url, headers=headers, verify=False).json()
        # print(response)
        data = response['content']['list']
        for i in data:
            # 标题
            title = i['title']
            # 视频的播放链接(url)
            urls = i['playurl']
            # 请求视频地址 并且保存到本地
            VIdeo_response = requests.get(urls, headers=headers, verify=False)
            # a 文件追加  b 进制文件读写
            f = open('Video/{}.mp4'.format(title), 'ab')
            f.write(VIdeo_response.content)
            f.close()


# 创建线程
t = threading.Thread(target=Video)

# 运行线程
t.start()

