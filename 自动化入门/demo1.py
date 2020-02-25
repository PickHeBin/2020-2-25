#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: MuNian
# Date  : 2020-02-19

'''
学习自动化为了什么?
办公自动化  脚本 辅助软件 按键精灵....  自动化程序
运维 测试??? --> 时代 淘汰率
成本 ---> 企业 自动化 测试运维   就业岗位 非常多 仅次于开发

网站  软件 ....  自动化测试 自动化运维

服务器崩了....  自动化运维 维护  市场平均薪资18K
学费优惠  直接可以进班  今天晚上 直接进班学习

目前  3W余人  毕业薪资 8K - 30K  兼职的大学生  全职
qq:975225531
一步步

学习5个月 为一期

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# 创建了一个变量(浏览器驱动的)
driver = webdriver.Chrome()

# 在空白网页自动输入 访问网址
driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('妹子图')

# 定位 百度一下的网页位置
ac = driver.find_element_by_id('su')
ActionChains(driver).move_to_element(ac).click().perform()





# 生成当前页面的快照并且保存
# driver.save_screenshot('baidu.png')
#
# # 定位到搜索框 并且进行搜索框的输入
# # 选择id选择器来进行定位
# driver.find_element_by_id('kw').send_keys('妹子图')
# # 输入回车键
# # driver.find_element_by_id('kw').send_keys(Keys.ENTER)
#
# # 点击百度一下
# driver.find_element_by_id('su').click()
#
# # 获取到网页源代码
# print(driver.page_source)
#
# # ctrl + a 全选
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')