# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:05:05 2021

@author: User
"""

import cv2
import numpy as np

# SPLIT AND MERGE RGB
#BEGIN
image = cv2.imread('messi5.jpg')
_shape = image.shape[:2]
cv2.imshow('Orginal',image)

B,G,R = cv2.split(image)

cv2.imshow('Red',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)
cv2.waitKey(0)

bgrList = [B,G,R]
merged = cv2.merge(bgrList)
cv2.imshow('Merged',merged)
cv2.waitKey(0)

zeros = np.zeros(_shape,dtype=np.uint8)
cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()
