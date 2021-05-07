# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:48:51 2021

@author: User
"""

# GRAYSCALE HISTOGRAM
#BEGIN
from matplotlib import pyplot as plt
import cv2

image = cv2.imread('messi5.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Orginal',image)

channels = [0]
mask=None
scale=[256]
pixels= [0,256]
hist = cv2.calcHist([image],channels,mask,scale,pixels ) 

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim(pixels)
plt.show()

           

cv2.waitKey(0)
cv2.destroyAllWindows()

#END 