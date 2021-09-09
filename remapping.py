from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
def update_map(ind, map_x, map_y):
    if ind == 0:
        for i in range(map_x.shape[0]):
            for j in range(map_x.shape[1]):
                if j > map_x.shape[1]*0.25 and j < map_x.shape[1]*0.75 and i > map_x.shape[0]*0.25 and i < map_x.shape[0]*0.75:
                    map_x[i,j] = 2 * (j-map_x.shape[1]*0.25) + 0.5
                    map_y[i,j] = 2 * (i-map_y.shape[0]*0.25) + 0.5
                else:
                    map_x[i,j] = 0
                    map_y[i,j] = 0
    elif ind == 1:
        for i in range(map_x.shape[0]):
            map_x[i,:] = [x for x in range(map_x.shape[1])]
        for j in range(map_y.shape[1]):
            map_y[:,j] = [map_y.shape[0]-y for y in range(map_y.shape[0])]

src = cv.imread('bts.png',cv.IMREAD_COLOR)
if src is None:
    print('Could not open or find the image: ')
    exit(0)
map_x = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)
map_y = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)
window_name = 'Remap demo'
cv.namedWindow(window_name)
ind = 0
while True:
    update_map(ind, map_x, map_y)
    ind = (ind + 1) % 4
    dst = cv.remap(src, map_x, map_y, cv.INTER_LINEAR)
    cv.imshow(window_name, dst)
    c = cv.waitKey(1000)
    if c == 27:
        break