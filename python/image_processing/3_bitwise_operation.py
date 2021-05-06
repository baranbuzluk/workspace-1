# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:29:35 2021

@author: User
"""

import cv2
import numpy as np

# BITWISE OPERATION
#BEGIN
_shape=(300,300)
rectangle = np.zeros(shape=_shape, dtype=np.uint8)
started_point = (25,25)
ended_point = (275,275)
white = (255,255,255)
thickline=-1  # filled
cv2.rectangle(rectangle,started_point,ended_point,white,thickline)
cv2.imshow('Rectangle',rectangle)
cv2.waitKey(0)
circle = np.zeros(shape=_shape, dtype=np.uint8)
centerXY= (circle.shape[1] // 2 ,circle.shape[0] // 2)
radius = 150
cv2.circle(circle,centerXY,radius,white,thickline)
cv2.imshow('Circle',circle)
cv2.waitKey(0)


 ## BITWISE OPERATIONS
bitwiseAnd=cv2.bitwise_and(rectangle,circle)
cv2.imshow('bitwiseAnd',bitwiseAnd)
cv2.waitKey(0)

bitwiseOr=cv2.bitwise_or(rectangle,circle)
cv2.imshow('bitwiseOr',bitwiseOr)
cv2.waitKey(0)

bitwiseXor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow('bitwiseXor',bitwiseXor)
cv2.waitKey(0)

bitwiseNot=cv2.bitwise_not(rectangle,circle)
cv2.imshow('bitwiseNot',bitwiseNot)
cv2.waitKey(0)

cv2.destroyAllWindows()

#END
    
