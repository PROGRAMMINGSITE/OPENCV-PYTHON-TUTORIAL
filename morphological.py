#morphological transformations are some simple
# operation based on the image shapes
# are normally performaed on binary images
#A kernel tells you how to change the value of any given pixel by combinig it with different
#amounts of the neighboring pixels

import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread('th.png',cv2.IMREAD_GRAYSCALE)
mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask, kernel)

titles = ['CERTIFICATE OF FBISE','mask']
images = [img,mask]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
