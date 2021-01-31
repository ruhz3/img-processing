import numpy as np
import cv2

BIT_NUM = 8

# Read the image in greyscale
input_img = cv2.imread('sample.jpg', 0)
height, width = input_img.shape

# Make histogram
histogram = np.zeros(2**BIT_NUM, np.float_)
for x in range(width):
	for y in range(height):
		histogram[input_img[y][x]] += 1

# Normalize histogram
for i in range(2**BIT_NUM):
	histogram[i] /= (width * height)

# Accumulate histogram
for i in range(1, 2**BIT_NUM):
	histogram[i] += histogram[i-1]

# Approximate output level
for i in range(1, 2**BIT_NUM):
	histogram[i] = round(histogram[i] * (2**BIT_NUM - 1))

# Equalize the image
output_img = np.zeros((height, width), np.uint8)
for x in range(width):
	for y in range(height):
		output_img[y][x] = histogram[input_img[y][x]]

# Display the images
cv2.imshow('input', input_img)
cv2.imshow('output', output_img)
cv2.waitKey(0)
