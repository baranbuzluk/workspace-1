# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:58:13 2021

@author: User
"""

#COLOR HISTOGRAM
#BEGIN
from matplotlib import pyplot as plt
import cv2

image = cv2.imread('messi5.jpg')
cv2.imshow('Original',image)
channels = cv2.split(image)
colors = ('b','g','r')


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')


for (channel,color) in zip(channels,colors):
    hist = cv2.calcHist([channel], [0], None, [256] , [0,256])
    plt.plot(hist, color=color)
    plt.xlim([0,256])  

fig=plt.figure()

#PLOT A 2D COLOR HISTOGRAM FOR GREEN AND BLUE
ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1],channels[0]], [0,1] , None,
                    [32,32], [0,256,0,256])
p = ax.imshow(hist,interpolation='nearest')
ax.set_title('G and B')
plt.colorbar(p)

#PLOT A 2D COLOR HISTOGRAM FOR GREEN AND RED
ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1],channels[2]], [0,1] , None, 
                    [32,32], [0,256,0,256])
p = ax.imshow(hist,interpolation='nearest')
ax.set_title('G and B')
plt.colorbar(p)

#PLOT A 2D COLOR HISTOGRAM FOR BLUE AND RED
ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0],channels[2]], [0,1] , None, 
                    [32,32], [0,256,0,256])
p = ax.imshow(hist,interpolation='nearest')
ax.set_title('B and R')
plt.colorbar(p)

print("2D histogram shape:{}, with {} values".format(hist.shape,
      hist.flatten().shape[0]))
hist=cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])

print("3D histogram shape:{}, with {} values".format(hist.shape,
      hist.flatten().shape[0]))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#END