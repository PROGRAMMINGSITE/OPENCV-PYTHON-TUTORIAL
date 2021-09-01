# histogram is a tool to underdtand about image
# it's gives the overall idea about thr intensity distribution
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = np.zeros((200,200), np.uint8)
cv.rectangle(img, (0, 100), (200, 200), (255), -1)
cv.rectangle(img, (0, 50), (100, 100), (127), -1)

cv.imshow("img", img)


plt.hist(img.ravel(), 256, [0, 256])


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()