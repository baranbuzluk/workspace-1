# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:18:36 2021

@author: User
"""

import numpy as np
import cv2

#GORUNTU ISLEME
#BEGIN
image = cv2.imread('messi5.jpg')
print(image.shape[0])
def transiation(): 
    cv2.imshow('Original',image)
    
    matris = np.float32([[1,0,10],[0,1,20]])
    shifted = cv2.warpAffine(image,matris,(image.shape[1],image.shape[0]))
    cv2.imshow('Shifted Down and Right',shifted)
    
    matris = np.float32([[1,0,-50],[0,1,-90]])
    shifted = cv2.warpAffine(image,matris,(image.shape[1],image.shape[0]))
    #cv2.imshow('Shifted Up and Left',shifted)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

def rotate():
    cv2.imshow('Original',image)
    (height,width) = image.shape[:2]
    center = (width//2, height//2)
    angle = 180
    rate = 1.0
    matrix = cv2.getRotationMatrix2D(center,angle,rate)
    rotated_image = cv2.warpAffine(image,matrix,(height,width))
    cv2.imshow('Rotated image 45 angle',rotated_image)
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 

def resize():
    cv2.imshow('Original',image)
    r = 150.0 / image.shape[1]
    y = int( image.shape[0]* r)
    dim = (150, y)
    resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    cv2.imshow('Resized Width',resized)
    
    r = 150.0 / image.shape[0 ]
    x = int( image.shape[1]* r)
    dim = (150, x)
    resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    cv2.imshow('Resized Height',resized)
    #BGR
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def crop():
    cv2.imshow('Original',image)
    
    cropped = image[200:250,100:350] # Y,X
    cv2.imshow('cropped',cropped)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def flip(): # simetri alma
    cv2.imshow('Original',image)
    
    flipped = cv2.flip(image,1) 
    cv2.imshow('Flipped Horizontally',flipped)
    
    flipped = cv2.flip(image,0)
    #cv2.imshow('Flipped Vertically',flipped)
    
    flipped = cv2.flip(image,-1)
    #cv2.imshow('Flipped Horizontally & Vertically',flipped)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

#END

#transiation()
#rotate()
#resize()
#crop()
flip()