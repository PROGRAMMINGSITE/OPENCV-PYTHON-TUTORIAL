import numpy as np
import cv2

def nothing(x):
    print(x)
#create a black image a window

cv2.namedWindow('images')

cv2.createTrackbar('cp','images',10, 400,nothing)

switch = 'color/gray'
cv2.createTrackbar(switch, 'images', 0,1,nothing)
while(1):
    img = cv2.imread('S.jpeg')
    pos = cv2.getTrackbarPos('CP','images')
    font = cv2.FONT_HERSNEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,4,(0,0,255))

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    s =cv2.getTrackbarPos(switch,'images')
    if s == 0:
        img[:] = 0
    else:
        pos = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.imshow('images',img)
cv2.destroyAllWidow()

