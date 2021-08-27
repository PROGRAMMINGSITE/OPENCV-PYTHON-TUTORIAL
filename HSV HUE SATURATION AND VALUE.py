#HUE correspons to the color components(base pigment),
# hence just by selecting a range of HUE you can salect any color.
#(0-360).

#.Saturation is the amount of color (depth of the pigment)-(dominance of HUE)(O-100%)
# Value is basically the brighness of the color.

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Tracking')

while True:
    frame =cv2.imread('th.png')

    key = cv2.imshow('frame', frame)
    if key ==27:
        break
cv2.destroyAllWindow()