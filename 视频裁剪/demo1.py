#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-02-24

'''
http://player.youku.com/embed/XMzc5MDI1MzQxNg==
http://player.youku.com/embed/XMzc4NzIyNDQ1Mg==
http://player.youku.com/embed/XMzc4NzIwMTEyNA==



'''


import flickrapi
#输入API的key和secret
flickr=flickrapi.FlickrAPI(api_key,api_secret,cache=True)
try:
  #爬取text为'New York'的照片,这里可以根据自己的需要设置其它的参数
 photos=flickr.walk(text='New York',extras='url_c')
except Exception as e:
  print('Error')
for photo in photos:
 #获得照片的url,设置大小为url_c(具体参数请参看FlickrAPI官方文档介绍)
 url=photo.get('url_c')
 print(str(url))