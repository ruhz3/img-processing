import numpy as np
import scipy.stats as st
import cv2

# Rule of thumb for Gaussian: set filter (half - KERNEL_LEN) to about (3 * SIG)
KERNEL_LEN = 5
SIG = 2


def gaussian_kernel(kernlen, nsig):
    """Returns a 2D Gaussian kernel array."""
    interval = (2*nsig+1.)/(kernlen)
    x = np.linspace(-nsig-interval/2., nsig+interval/2., kernlen+1)
    kern1d = np.diff(st.norm.cdf(x))
    kernel_raw = np.sqrt(np.outer(kern1d, kern1d))
    kernel = kernel_raw/kernel_raw.sum()
    return kernel


def gaussian_filter(img, kernel, i, j):
    height, width = img.shape
    sum = 0
    for r in range(-int(KERNEL_LEN/2), int(KERNEL_LEN/2) + 1):
        for c in range(-int(KERNEL_LEN/2), int(KERNEL_LEN/2) + 1):
            if (i + r >= 0 and i + r < height) and (j + c >= 0 and j + c < width) :
                sum += img[i + r][j + c] * kernel[r + 1][c + 1]

    return int(sum)


input_img = cv2.imread('sample.jpg', 0)

height, width = input_img.shape
output_img = np.zeros((height, width), np.uint8)
kernel = gaussian_kernel(KERNEL_LEN, SIG)

for i in range(height):
    for j in range(width):
        output_img[i][j] = gaussian_filter(input_img, kernel, i, j)

cv2.imshow('input', input_img)
cv2.imshow('output', output_img)
cv2.waitKey()

