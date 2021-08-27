import numpy as np
import cv2

def nothing(x):
    print(x)
#create a black image a window
img= np.zeros((300,512,3), np.uint8)
cv2.namedWindow('images')

cv2.createTrackbar('a','images',0, 255,nothing)
cv2.createTrackbar('b','images',0, 255,nothing)
cv2.createTrackbar('c','images',0, 255,nothing)
cv2.createTrackbar('d','images',0, 255,nothing)
switch = 'O: 0xFF\n 1: ON'
cv2.createTrackbar(switch, 'images', 0,1,nothing)
while(1):
    cv2.imshow('images',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    a =cv2.getTrackbarPos("a",'images')
    b =cv2.getTrackbarPos("b",'images')
    c =cv2.getTrackbarPos("c",'images')

    if switch == 0:
        img[:] = 0
    else:
        img[ : ] = [a,b,c]
cv2.destroyAllWidow()

