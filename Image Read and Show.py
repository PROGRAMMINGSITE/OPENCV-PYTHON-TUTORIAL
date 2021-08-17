import cv2
import numpy
img = cv2.imread('roadside.png',1)
img1 = cv2.imread('baboon.jpg',0)
img2 = cv2.imread('blox.jpg',-1)
img3 = cv2.imread('cards.png',0)
img4 = cv2.imread('chessboard.png',0)
print(img)
print(img1)
print(img2)
print(img3)
print(img4)
cv2.imshow('image',img)
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
cv2.imshow('image4',img4)
cv2.waitKey(50000)
#->1 Loads a color image.
#->0 Loads image in grayscale mode.
#->-1 loads image as such including alpha channel.
