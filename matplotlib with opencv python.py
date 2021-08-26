import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('th.png',0)
__, th1= cv.threshold(img,50,255,cv.THRESH_BINARY)
__, th2= cv.threshold(img,50,255,cv.THRESH_BINARY)
__, th3= cv.threshold(img,50,255,cv.THRESH_BINARY)
__, th4= cv.threshold(img,50,255,cv.THRESH_BINARY)
__, th5= cv.threshold(img,50,255,cv.THRESH_BINARY)
__, th6= cv.threshold(img,50,255,cv.THRESH_BINARY)
__, th7= cv.threshold(img,50,255,cv.THRESH_BINARY)

tiltes = ['ORIGINAL IMAGE','BINARY','BINARY_INV','TRUNC']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2 , 3 , i+1), plt.imshow(images[i],'gray')
    plt.title(tiltes[i])
    plt.xticks([], plt.yticks([]))
    plt.show()
cv.imshow('images',img)
cv.waitKey()