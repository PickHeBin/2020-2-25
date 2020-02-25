#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 智能聊天机器人.py
# Author: MuNian
# Date  : 2020-02-15

import requests
import json
import os
from aip import AipSpeech


def communication(info):
    """图灵机器人接入"""
    key = '078bcdc31e7e4d4b9907dc51b966d7c1'     # 这里的yourkey需要去图灵机器人官网免费申请
    api = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    res = requests.get(api)
    dict_json = json.loads(res.text)
    if dict_json['code'] == 100000:     # 100000为图灵机器人api返回的参数
        return (dict_json["text"])
    elif dict_json['code'] == 200000:
        return (dict_json["text"] + dict_json['url'])


def Robot_Speech(data):
    """ 百度AI语音合成"""
    APP_ID = '17786055'
    API_KEY = '7kpX7SI4GTpzKWILZyCeZyik'
    SECRET_KEY = 'q7acskNrCuGcOYmsz7cq1qjY0wkorXRH '
    # 上面三个参数则需要去百度AI官网免费申请
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # 合成语音类型参数，详见百度AI
    result = client.synthesis(data, 'zh', 1, {
        'vol': 10, 'spd':4, 'per':'4'
    })
    # 识别正确返回语音二进制
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)


def main():
    while True:
        data = input('我：')
        if data == 'quit':
            print('牛皮哄哄：好了，我不和你聊了')
            break

        else:
            voice = communication(data)
            print('牛皮哄哄：'+voice)
        Robot_Speech(voice)
        os.system('auido.mp3')  #这里的语音则是使用系统默认的播放器播放


if __name__ == '__main__':
    main()