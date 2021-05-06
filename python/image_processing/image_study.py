# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:26:03 2021

@author: User
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show(image,title):
    plt.figure()
    plt.title(title)
    plt.imshow(image,cmap='gray')

image = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
show(image,'Orjinal')

blured_image = cv2.GaussianBlur(image,(3,3),cv2.BORDER_DEFAULT) 
show(blured_image,'blured_image')


mask = image-blured_image
show(mask,'mask')

image_plus_mask = mask+image
show(image_plus_mask,'image_plus_mask')

sayi=0
sayilar=dict()
sayi.count
while sayi!=-1:
    sayi=input()
    if sayilar[sayi]==None:
        sayilar[sayi]=0
    
    sayilar[sayi]+=1
    sayi=int(sayi)
print(sayilar)