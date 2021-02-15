'''
Check the result by putting 'watermarked.png' to 'bit_pane_slicing.py'!

* modified existing source
https://theailearner.com/2019/01/25/bit-plane-slicing/
'''

import numpy as np
import cv2

# Read the image in greyscale
img = cv2.imread('sample.jpg', 0)
img = cv2.resize(img, (300, 300))
wm_img = cv2.imread('whale.png', 0)
wm_img = cv2.resize(wm_img, (300, 300))

# Make img to binary
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits

# Slice the pane by bit
eight_bit_img = (np.array([int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst], dtype=np.uint8) * 32).reshape(img.shape[0], img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst], dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst], dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst], dtype=np.uint8) * 2).reshape(img.shape[0], img.shape[1])

# Put watermark in 1_bit plane
one_bit_img = np.array(wm_img, dtype=np.uint8).reshape(img.shape[0], img.shape[1])


# Make watermarked image
result_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        result_img[i][j] += (eight_bit_img[i][j] + seven_bit_img[i][j] + six_bit_img[i][j]
                             + five_bit_img[i][j] + four_bit_img[i][j] + three_bit_img[i][j]
                             + two_bit_img[i][j] + one_bit_img[i][j]/128)
cv2.imwrite('watermarked.png', result_img)


# Display the images
cv2.imshow('watermarked', result_img)
cv2.waitKey(0)
