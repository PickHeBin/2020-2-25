#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-01-15


'''
零基础的?  0
入行Python:
    Python 爬虫  数据采集  数据清洗 .... 百度 谷歌...  月薪15K
    Python开发工程师  15K  知乎  豆瓣.... Python开发 后端开发
    自动化工程师  13K  自动化测试 自动化运维  自动化脚本

进阶:  5 - 10
    数据分析 --> 爬虫 开发
    AI -  机器学习 深度学习 机器视觉  年薪百万起步
    (建模 模型训练 数据集训练 /.... 算法  统计放分析)

方向?    VIP课程--->  2W余人  平均8K - 30K  从零基础开始

从事方向?

Python应用实战
跟着老师学习怎么学的? 全栈班级是5个月  AI 1.5个月
上课方式: 1  3 5 正课 2  4 6 解答课  20:30 - 22:30
线上直播授课  课后录播  随堂笔记源码  课后一对一辅导 补课  解答



'''
from random import random

from sprites import *

class Snow:
    def __init__(self,x,y,sw,sh):
        self.x = x
        self.y = y
        self.sw = sw
        self.sh = sh
        self.dx = 0
        self.dy = random.randint(-2,-1)

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def pos(self):
        return self.x,self.y

    def reborn(self):
        if self.y < -self.sh//2:
            self.y = random.randint(self.sw//2,2 * self.sw)

def draw(hg,snow):
    """hg：海龟，snow：雪花点"""
    hg.goto(snow.pos())
    hg.dot(abs(snow.dy)*3)      # 速度越快，雪花点越大

width,height = 480,360
screen = Screen()
screen.tracer(0,0)
screen.bgcolor('black')
screen.setup(width,height)
screen.title("帧动画_纯画笔下雪效果 Python Sprites Module")

tom = Sprite(visible=False)          # 新建不可见精灵对象
tom.color('white')                   # 颜色为白色

snows = []
for _ in range(300):
    x = random.randint(-width//2,width//2)
    y = random.randint(height//2,2 * height)
    snows.append(Snow(x,y,width,height))

clock = Clock()                       # 新建时钟对象，用来固定fps
while True:
    tom.clear()                       # 清除所有雪花
    [snow.update() for snow in snows] # 移动每片雪花
    [snow.reborn() for snow in snows] # 雪花到了最下面则移到最上面
    [draw(tom,snow) for snow in snows]# 重画每片雪花
    screen.update()                   # 更新显示
    clock.tick(60)

