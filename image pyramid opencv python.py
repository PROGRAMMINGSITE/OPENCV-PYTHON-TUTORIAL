#import cv2
#import numpy as np
#img = cv2.imread('one.png')
#layer = img.copy()
#gp = [layer]

#for i in range(6):
#    layer=cv2.pyrDown(layer)
#    gp.append(layer)
#    cv2.imshow(str(i),layer)
#cv2.imshow('images',img)
#cv2.waitKey(0)


# A LEVEL IN LAPLACIAN PYRAMID IS FORMEF BY THE DIFFERENCE BETWEEN THAT LEVEL
# IN GAUSSIAN PYRAMID AND EXPANDED VERSION OF ITS LEVEL IN GAUSSIAN PYRAMID
import cv2
import numpy as np
img = cv2.imread('one.png')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow('upper level gaussuian pyramid',layer)
lp = [layer]

for i in range(5 , 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract({gp[i-1],gaussian_extended})
    cv2.imshow(str(i),laplacian)
    #print(i)
cv2.imshow('images',img)
cv2.waitKey(0)
