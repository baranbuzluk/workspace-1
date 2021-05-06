# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:44:53 2021

@author: User
"""

import cv2
import numpy as np

# C0LOR SPACES
#BEGIN
image = cv2.imread('messi5.jpg')
cv2.imshow('Orginal',image)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow('lab',lab)
cv2.waitKey(0)
cv2.destroyAllWindows()
#END