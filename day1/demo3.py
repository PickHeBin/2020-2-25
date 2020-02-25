#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo3.py
# Author: MuNian
# Date  : 2020-01-07


# 伊人在河边在火山分享了视频，快来围观！传送门戳我>>https://share.huoshan.com/hotsoon/s/fcKU6CYz700/ 复制此链接，打开【火山小视频】，直接观看视频~

'''
https://share.huoshan.com/pages/item/index.html?item_id=6776467704787389709&tag=10437&timestamp=1578407453&watermark=2&media_type=4&share_ht_uid=0&did=70132909477&iid=94892124490&utm_medium=huoshan_android&tt_from=copy_link&app=live_stream&utm_source=copy_link&schema_url=sslocal%3A%2F%2Fitem%3Fid%3D6776467704787389709
https://share.huoshan.com/pages/item/index.html?item_id=6779013731134360839&tag=0&timestamp=1578407191&watermark=2&media_type=4&share_ht_uid=0&did=70132909477&iid=94892124490&utm_medium=huoshan_android&tt_from=copy_link&app=live_stream&utm_source=copy_link&schema_url=sslocal%3A%2F%2Fitem%3Fid%3D6779013731134360839
'''

import requests

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# post请求参数
data = {
    'i': '你好', # 需要翻译的内容
    'doctype': 'json',
}


response = requests.post(url, data=data).json()
print(response)





