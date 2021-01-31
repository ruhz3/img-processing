import numpy as np
import cv2


def gaussian_filter(img, i, j):
    height, width = img.shape
    filter = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])
    sum = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (i+r>=0 and i+r<height) and (j+c>=0 and j+c<width) :
                sum += img[i + r][j + c] * filter[r+1][c+1]
    return int(sum / 16)


input_img = cv2.imread('sample.jpg', 0)

height, width = input_img.shape
output_img = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        output_img[i][j] = gaussian_filter(input_img, i, j)

cv2.imshow('input', input_img)
cv2.imshow('output', output_img)
cv2.waitKey()

