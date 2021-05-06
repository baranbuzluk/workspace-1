# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:38:46 2021

@author: User
"""

import cv2
import numpy as np

# SEKIL CIZIMI
# BEGIN
_shape = (300, 300, 3)  # Y,X,Channel
canvas = np.zeros(shape=_shape, dtype=np.uint8)
thickline = 1
green = (0, 255, 0)  # BGR
red = (0, 0, 255)  # BGR
blue = (255, 0, 0)  # BGR
white = (255, 255, 255)


def drawLine():
    started_point = (0, 0)  # x,y
    ended_point = (300, 300)  # x,y
    cv2.line(canvas, started_point, ended_point, green, thickline)
    cv2.imshow('Canvas', canvas)
    cv2.waitKey(0)

    started_point = (300, 0)  # x,y
    ended_point = (0, 300)  # x,y
    cv2.line(canvas, started_point, ended_point, red, thickline)
    cv2.imshow('Canvas2', canvas)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    return


def drawRectangle():
    started_point = (10, 10)  # x,y
    ended_point = (60, 60)  # x,y
    cv2.rectangle(canvas, started_point, ended_point, green, thickline)
    cv2.imshow('Canvas', canvas)
    cv2.waitKey(0)

    started_point = (50, 200)  # x,y
    ended_point = (200, 225)  # x,y
    cv2.rectangle(canvas, started_point, ended_point, red, thickline)
    cv2.imshow('Canvas2', canvas)
    cv2.waitKey(0)

    started_point = (200, 50)  # x,y
    ended_point = (225, 125)  # x,y
    local_thickline = -1
    cv2.rectangle(canvas, started_point, ended_point, blue, local_thickline)
    cv2.imshow('Canvas2', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def drawCircle():
    (centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
    for radius in range(0, 175, 25):
        cv2.circle(canvas, (centerX, centerY), radius, white, thickline)
    cv2.imshow('Canvas', canvas)
    cv2.waitKey(0)


    local_thickline = -1
    for i in range(0, 25):
        radius = np.random.randint(low=5, high=200)
        color = np.random.randint(low=0, high=256, size=(3,)).tolist()
        points = np.random.randint(low=0, high=300, size=(2,))
        cv2.circle(canvas, tuple(points), radius, color, local_thickline)
    cv2.imshow('Canvas', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return
# END


# drawLine()
# drawRectangle()
# drawCircle()
