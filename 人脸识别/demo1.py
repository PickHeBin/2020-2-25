#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-02-18

'''
跟着暮念老学习:
    成为 老师亲传弟子 老师亲自学习 辅导 补课 解答
    实战 --->  5个同学  AI人工智能
    学费 支付500 低1500 学费优惠

萧萧 :2597099000
3W余人  8K - 30K 兼职  全职
直接进班学习
从零基础  到 开发 自动化  爬虫 算法  深度学习 AI(单独学习5880  跟着老师学 免费获取到这样学习名额 )

体温检测 AI识别 自动化驾驶 智慧城市  天眼  ....
AI医疗
AI 算法  OpenStack二开

付费学习 -> 不学不学
读书
就业问题
学习路线

22岁  8年
开发工作网页比较多
开发 OA ---> 主导开发  辅导 自动化 爬虫 -->  1- 3年 管理  全栈 架构

担心自己学不会?

初次接触 英语不好:  后期提升?  后端  逻辑能力?
练得少 从零基础开始  一行代码开始 -0-->
保障学员学会才毕业  重修(免费)
线上直播 + 课后录播
1 3 5正课 2 4 6解答课  20:30 -22:30
每天当中抽出零散一个小时 来学习就是ok的  课后 一对一补课  解答 辅导

7880 支付500 低1500 =  6380 / 分期12期 = 每个月才531 / 31 = 十几块钱
花呗 借呗 ....
工作 一个月531 承担不起  25岁
学生 1000 一个月
学费这一块有压力? 短期投资
长期?  大一  兼职 老师指导兼职
重修 留级  3个月 兼职开发 后端开发
大学 实战能力?  实习 6个月?   兼职 积累实战 --? 毕业 实习\
项目能力  大学Python基础 市场   独立开发能力  15K左右




'''

import cv2

# 摄像头视频采集
cap = cv2.VideoCapture(0)

#  创建一个窗口
cv2.namedWindow('python')

# 加载模型数据
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')

# 摄像头数据采集 - 数据流
while True:
    # 得到摄像头采集的视频数据的帧数
    ret, frame = cap.read()
    if not ret:
        cv2.waitKey(30)

    # 所得到的的每一组帧数 计算 -> 灰度图片转换 -> 计算强度得以降低
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 得到人脸位置
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, h+y), (255,0,0), 1)

    # 显示图像
    cv2.imshow('python', frame)
    # 等待用户检测人脸
    key = cv2.waitKey(20)

    if key & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

