# CONTOURS IS A PYTHNON LIST OF ALL THE CONTOURS IN THE IMAGE.
# EACH INDIVIDUA; CONTOUR IS A NUMPY ARRAY OF(X,Y)COORDINATE
# OF BOUNDARY POINTS OF THE OBJECT.
import cv2
import numpy as np

img = cv2.imread('one.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
print('number of contours = '+ str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours, -1,(0, 255, 0),1)
cv2.imshow('images',img)
#cv2.imshow('image gray',imgray)
cv2.waitKey(0)
