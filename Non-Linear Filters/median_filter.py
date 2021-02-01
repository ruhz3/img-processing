import numpy as np
import cv2


KERNEL_SIZE = 3


# 중간값 필터
def med_filter(img):
    height, width = img.shape
    result = np.zeros((height, width), np.uint8)
    kernel = []

    for x in range(width):
        for y in range(height):
            # to make result[y][x], make kernel and sort
            for i in range(x - int(KERNEL_SIZE/2), x + int(KERNEL_SIZE/2) + 1):
                if i < 0 or i >= width:
                    continue
                for j in range(y - int(KERNEL_SIZE/2), y + int(KERNEL_SIZE/2) + 1):
                    if j < 0 or j >= height:
                        continue
                    kernel.append(img[j][i])
            kernel.sort()
            result[y][x] = kernel[int(len(kernel)/2)]
            kernel.clear()

    return result


input_img = cv2.imread('sample.jpg', 0)
med_img = med_filter(input_img)
result_img = cv2.hconcat([input_img, med_img])

cv2.imshow('median', result_img)
cv2.waitKey(0)