import cv2 as cv
import numpy as np

img = cv.imread('j.png',1)
_, th1 = cv.threshold(img,55,455,cv.THRESH_BINARY)
_, th2 = cv.threshold(img,55,455,cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_, TH4 = cv.threshold(img,127,200,cv.THRESH_TOZERO)
_, TH5 = cv.threshold(img,127,200,cv.THRESH_TOZERO_INV)


cv.imshow('images',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('TH4',TH4)
cv.imshow('TH5',TH5)


cv.waitKey(0)
