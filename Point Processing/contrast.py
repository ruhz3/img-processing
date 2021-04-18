import numpy as np
import cv2
import math

WIDTH = 300
HEIGHT = 200
PATCH_SIZE = 5


# 이미지 불러오기
img = cv2.imread('sample.JPG', 1)
img = cv2.resize(img, dsize=(WIDTH, HEIGHT))

# 1 : original
original = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        original[y][x] = img[y][x].copy()

# 2 : darken
darken = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            if img[y][x][i] - 128 > 0:
                darken[y][x][i] = img[y][x][i] - 128
            else:
                darken[y][x][i] = 0

# 3 : lower contrast
lower_contrast = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            lower_contrast[y][x][i] = int(img[y][x][i]/2)

# 4 : non-linear lower contrast
nl_lower_contrast = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            nl_lower_contrast[y][x][i] = int(math.pow(img[y][x][i]/255, 1/3)*255)

# 5 : invert
invert = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            invert[y][x][i] = 255 - img[y][x][i]

# 6 : lighten
lighten = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            if img[y][x][i] + 128 < 255:
                lighten[y][x][i] = img[y][x][i] + 128
            else:
                lighten[y][x][i] = 255

# 7 : raise contrast
raise_contrast = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            if img[y][x][i] * 2 < 255:
                raise_contrast[y][x][i] = int(img[y][x][i]*2)
            else:
                raise_contrast[y][x][i] = 255

# 8 : non-linear lower contrast
nl_raise_contrast = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)
for x in range(WIDTH):
    for y in range(HEIGHT):
        for i in range(3):
            nl_raise_contrast[y][x][i] = int(math.pow(img[y][x][i]/255, 2)*255)

row1 = cv2.hconcat([original, darken, lower_contrast, nl_lower_contrast])
row2 = cv2.hconcat([invert, lighten, raise_contrast, nl_raise_contrast])
result = cv2.vconcat([row1, row2])
cv2.imshow('result', result)
cv2.waitKey()