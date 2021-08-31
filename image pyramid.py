#pyramid is a type of multi-scale signal representation in which
# a signal or an image is subject to repeated smoothing and subsampling.
#                            TYPE OF PYRAMID
#->GAUSSIAN PYRAMID
#->LAPLACIAN PYRAMID

import cv2
import numpy as np
img = cv2.imread('A.png')
a = cv2.pyrDown(img)
b = cv2.pyrDown(img)
c = cv2.pyrDown(img) 
cv2.imshow('image',img)
cv2.imshow('pydown 1 image',a)
cv2.imshow('pydown 2 image',b)
cv2.imshow('pydown 1 image',c)
cv2.waitKey()