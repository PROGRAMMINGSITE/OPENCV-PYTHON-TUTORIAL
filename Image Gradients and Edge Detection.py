# an image is a gradient directional change in the
# intensity change in the color in an image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('d.png')
lap = cv2.Laplacian(img,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
s

titles = ['images','Laplacian']
images = [img, lap]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()