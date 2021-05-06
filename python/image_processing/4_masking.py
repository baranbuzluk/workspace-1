# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:40:34 2021

@author: User
"""

import cv2
import numpy as np
# MASKING
#BEGIN
image = cv2.imread('messi5.jpg')
cv2.imshow('Orginal',image)
_shape = image.shape[:2]
cX,cY = image.shape[1]//2 , image.shape[0]//2
thickline = -1 # filled
white = (255,255,255)

def mask_rectangle():
    
    mask = np.zeros(_shape, dtype=np.uint8)
    started_point = (cX-75,cY-75)
    ended_point = (cX+75,cY+75)
    cv2.rectangle(mask,started_point,ended_point,white,thickline)
    cv2.imshow('Mask',mask)
    cv2.waitKey(0)
    
    masked = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('Masked',masked)
    cv2.waitKey(0)
    cv2.destroyWindow('Masked')
    cv2.destroyWindow('Mask')
    return


def mask_circle():
    center=(cX,cY)
    radius = 150
    mask = np.zeros(_shape, dtype=np.uint8)
    cv2.circle(mask,center,radius,white,thickline)
    cv2.imshow('Mask',mask)
    masked = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('Masked',masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

#END
    
mask_rectangle()
mask_circle()