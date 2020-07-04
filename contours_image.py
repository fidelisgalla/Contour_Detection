# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 07:57:36 2020

@author: fidelis.limbong
"""

import cv2
from matplotlib import pyplot as plt
import imutils

img = cv2.imread('shape.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray,50,150)


imgcnt = edge.copy()

cnt = cv2.findContours(imgcnt,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = imutils.grab_contours(cnt)
cnt = sorted(cnt,key=cv2.contourArea,reverse = True)


screencnt = None
for c in cnt:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.01*peri,True)
    #if there are four DP 
    if len(approx) == 5:
        screencnt = approx
        break

import numpy as np
blank = np.zeros(img.shape).astype(img.dtype)
cv2.drawContours(blank,cnt,-1,(255,0,0),1)

cv2.imshow('frame',blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
