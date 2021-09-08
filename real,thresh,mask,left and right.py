import numpy as np
import cv2

# Load image, grayscale, Otsu's threshold, and extract ROI
image = cv2.imread('ahadrazaofficial.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
x,y,w,h = cv2.boundingRect(thresh)
ROI = image[y:y+h, x:x+w]

# Color segmentation on ROI
hsv = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 152])
upper = np.array([179, 255, 255])
mask = cv2.inRange(hsv, lower, upper)

# Crop left and right half of mask
x, y, w, h = 0, 0, ROI.shape[1]//2, ROI.shape[0]
left = mask[y:y+h, x:x+w]
right = mask[y:y+h, x+w:x+w+w]

# Count pixels
left_pixels = cv2.countNonZero(left)
right_pixels = cv2.countNonZero(right)

print('Left pixels:', left_pixels)
print('Right pixels:', right_pixels)

cv2.imshow('mask', mask)
cv2.imshow('thresh', thresh)
cv2.imshow('ROI', ROI)
cv2.imshow('left', left)
cv2.imshow('right', right)
cv2.waitKey()