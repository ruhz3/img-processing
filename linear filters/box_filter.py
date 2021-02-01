import numpy as np
import cv2

FILTER_SIZE = 3


def box_filter(img, i, j):
    height, width = img.shape
    sum = 0
    for r in range(-int(FILTER_SIZE/2), int(FILTER_SIZE/2) + 1):
        for c in range(-int(FILTER_SIZE/2), int(FILTER_SIZE/2) + 1):
            if (i + r >= 0 and i + r < height) and (j + c >= 0 and j + c < width) :
                sum += img[i + r][j + c]
    return int(sum / (FILTER_SIZE * FILTER_SIZE))


input_img = cv2.imread('sample.jpg', 0)

height, width = input_img.shape
output_img = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        output_img[i][j] = box_filter(input_img, i, j)

cv2.imshow('input', input_img)
cv2.imshow('output', output_img)
cv2.waitKey()

