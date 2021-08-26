from matplotlib import pyplot as plt
import cv2

img = cv2.imread('S.jpeg',-1)
cv2.imshow('image', img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([]),plt.yticks([])
plt.show( )

cv2.waitkey(100)
cv2.destroyAllWindow()
