# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 23:52:24 2021

@author: User
"""

from matplotlib import pyplot as plt
import cv2
import numpy as np
#COLOR EQUALIZE, HISTOGRAM AND MASK 
#BEGIN
image = cv2.imread('messi5.jpg')

def equalize():    
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original',image)
    
    equal = cv2.equalizeHist(image)
    cv2.imshow('Histogram Equalization',np.hstack([image,equal]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 
    
    
def histogram_mask():
    
    def plot_histogram(image,title,mask=None):
        channels = cv2.split(image)
        colors = ('b','g','r')
        plt.figure()
        plt.title(title)
        plt.xlabel('Bins')
        plt.ylabel('# of Pixels')
        
        for (channel,color) in zip(channels,colors):
            hist = cv2.calcHist([channel],[0],mask,[256],[0,256])
            plt.plot(hist,color=color)
            plt.xlim([0,256])
        return
    
    
    cv2.imshow('Orginal',image)
    plot_histogram(image,'Histogram for Original Image')
    mask = np.zeros(image.shape[:2],dtype='uint8')
    cv2.rectangle(mask,(15,15),(130,130),255,-1)
    cv2.imshow('Orginal',mask)
    
    masked = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('Applying the Mask',masked)
    
    plot_histogram(image,'Histogram for Masked Image',mask=mask)
    plt.show()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 
#END
    
#equalize()
#histogram_mask()