import numpy as np
import cv2

KERNEL_SIZE = 3


# 최대값 필터
def max_filter(img):
    height, width = img.shape
    result = np.zeros((height, width), np.uint8)
    kernel = []

    for x in range(width):
        for y in range(height):
            # to make result[y][x], make kernel
            for i in range(x - int(KERNEL_SIZE/2), x + int(KERNEL_SIZE/2) + 1):
                if i < 0 or i >= width:
                    continue
                for j in range(y - int(KERNEL_SIZE/2), y + int(KERNEL_SIZE/2) + 1):
                    if j < 0 or j >= height:
                        continue
                    kernel.append(img[j][i])
            kernel.sort()
            result[y][x] = kernel[len(kernel)-1]
            kernel.clear()

    return result


# 최소값 필터
def min_filter(img):
    height, width = img.shape
    result = np.zeros((height, width), np.uint8)
    kernel = []

    for x in range(width):
        for y in range(height):
            # to make result[y][x], make kernel
            for i in range(x - int(KERNEL_SIZE/2), x + int(KERNEL_SIZE/2) + 1):
                if i < 0 or i >= width:
                    continue
                for j in range(y - int(KERNEL_SIZE/2), y + int(KERNEL_SIZE/2) + 1):
                    if j < 0 or j >= height:
                        continue
                    kernel.append(img[j][i])
            kernel.sort()
            result[y][x] = kernel[0]
            kernel.clear()

    return result


input_img = cv2.imread('sample.jpg', 0)
max_img = max_filter(input_img)
min_img = min_filter(input_img)
result_img = cv2.hconcat([input_img, max_img, min_img])

cv2.imshow('max, min', result_img)
cv2.waitKey(0)