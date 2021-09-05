import numpy as np
import cv2 as cv
img = cv.imread('circle.png')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 10,
                          param1=6, param2=6, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for (x, y ,r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 0, 0), 1)
    cv.circle(output, (x, y), 2, (0, 255, 255), 1)


cv.imshow('output',output)
cv.waitKey(0)
cv.destroyAllWindows()