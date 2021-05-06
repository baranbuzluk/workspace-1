# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:07:29 2021

@author: User
"""
import numpy as np
import cv2
#SMOOTING, BLURRING
#BEGIN
image = cv2.imread('messi5.jpg')
cv2.imshow('Original',image)
def blur():
    blurred = np.hstack([
        cv2.blur(image,(3,3)),
        cv2.blur(image,(5,5)),
        cv2.blur(image,(27,27))
        ])
    cv2.imshow('Averaged',blurred)
    cv2.waitKey(0)
    return

def gaussian_blur():
    blurred = np.hstack([
            cv2.GaussianBlur(image,(3,3),0),
            cv2.GaussianBlur(image,(5,5),0),
            cv2.GaussianBlur(image,(27,27),0)
            ])
    cv2.imshow('Gaussian',blurred)
    cv2.waitKey(0)
    return


def median_blur():
    blurred = np.hstack([
            cv2.medianBlur(image,3),
            cv2.medianBlur(image,5),
            cv2.medianBlur(image,7)
            ])
    cv2.imshow('Median',blurred)
    cv2.waitKey(0)
    return

def bilateral_filter():
    blurred = np.hstack([
            cv2.bilateralFilter(image,5,21,21),
            cv2.bilateralFilter(image,7,31,31),
            cv2.bilateralFilter(image,9,41,41)
            ])
    cv2.imshow('bilateral_filter',blurred)
    cv2.waitKey(0)
    return
#END
    

#blur()
#gaussian_blur()
#median_blur()
bilateral_filter()

cv2.destroyAllWindows()
