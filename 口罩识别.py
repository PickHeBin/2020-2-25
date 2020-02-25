#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 口罩识别.py
# Author: MuNian
# Date  : 2020-02-14


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import paddlehub as hub

test_img_path = ["./test_mask_detection.jpg"]
img = mpimg.imread(test_img_path[0])

# 展示待预测图片
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()

module = hub.Module(name="pyramidbox_lite_mobile_mask")

with open('test.txt', 'r') as f:
    test_img_path=[]
    for line in f:
        test_img_path.append(line.strip())
print(test_img_path)

input_dict = {"image": test_img_path}

# print(input_dict)

# execute predict and print the result
results = module.face_detection(data=input_dict)
# print(results)
for result in results:
    print(result)

# 预测结果展示
img = mpimg.imread("detection_result/test_mask_detection.jpg")
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()