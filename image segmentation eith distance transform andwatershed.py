import numpy as np
import cv2
import argparse
img = cv2.imread('cards1.png')

kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float32)

imgLaplacian = cv2.filter2D(img, cv2.CV_32F, kernel)
sharp = np.float32(img)
imgResult = sharp - imgLaplacian
# convert back to 8bits gray scale
imgResult = np.clip(imgResult, 0, 100)
imgResult = imgResult.astype('uint8')
imgLaplacian = np.clip(imgLaplacian, 0, 100)
imgLaplacian = np.uint8(imgLaplacian)
cv2.imshow('Laplace Filtered Image', imgLaplacian)
cv2.imshow('New Sharped Image', imgResult)
cv2.waitKey(0)