import cv2 as cv
import numpy as np

img = cv.imread('j.png',1)
_, th1 = cv.adaptiveThreshold(img,55,455,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
_, th2 = cv.threshold(img,55,455,cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_, th4 = cv.threshold(img,127,200,cv.THRESH_TOZERO)
_, th5 = cv.threshold(img,127,200,cv.THRESH_TOZERO_INV)


cv.imshow('images',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('th5',th5)


cv.waitKey(0)
