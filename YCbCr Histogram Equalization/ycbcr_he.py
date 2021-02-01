import numpy as np
import cv2


BIT_NUM = 8


mat_go = np.array([[0.257, 0.504, 0.098],
                   [-0.148, -0.291, 0.439],
                   [0.439, -0.368, -0.071]])
mat_back = np.array([[1.164, 0.000, 1.596],
                     [1.164, -0.392, -0.813],
                     [1.164, 2.017, 0.000]])
bias = np.array([[16], [128], [128]])


def histogram_equalize(input):
    height, width = input.shape
    # Make histogram
    histogram = np.zeros(2 ** BIT_NUM, np.float_)
    for x in range(width):
        for y in range(height):
            histogram[input[y][x]] += 1

    # Normalize histogram
    for i in range(2 ** BIT_NUM):
        histogram[i] /= (width * height)

    # Accumulate histogram
    for i in range(1, 2 ** BIT_NUM):
        histogram[i] += histogram[i - 1]

    # Approximate output level
    for i in range(1, 2 ** BIT_NUM):
        histogram[i] = round(histogram[i] * 224) + 16

    # Equalize the image
    equalized_img = np.zeros((height, width), np.uint8)
    for x in range(width):
        for y in range(height):
            equalized_img[y][x] = histogram[input[y][x]]

    return equalized_img


# Read the image in greyscale
print("Process Start...")
input_img = cv2.imread('sample.jpg', 1)
B, G, R = cv2.split(input_img)
height, width = B.shape

print("Make RGB to YCbCr...")
Y = np.zeros((height, width), np.uint8)
Cb = np.zeros((height, width), np.uint8)
Cr = np.zeros((height, width), np.uint8)
for x in range(width):
    for y in range(height):
        rgb_in = np.array([[R[y][x]], [G[y][x]], [B[y][x]]])
        ycbcr_out = mat_go.dot(rgb_in) + bias
        Y[y][x] = int(ycbcr_out[0][0])
        Cb[y][x] = int(ycbcr_out[1][0])
        Cr[y][x] = int(ycbcr_out[2][0])

print("Histogram-equalize Y...")
new_Y = histogram_equalize(Y)

print("Get back to RGB...")
new_R = np.zeros((height, width), np.uint8)
new_G = np.zeros((height, width), np.uint8)
new_B = np.zeros((height, width), np.uint8)
for x in range(width):
    for y in range(height):
        new_R[y][x] = int(new_Y[y][x] * pow((R[y][x] / Y[y][x]), 0.15))
        new_G[y][x] = int(new_Y[y][x] * pow((G[y][x] / Y[y][x]), 0.5))
        new_B[y][x] = int(new_Y[y][x] * pow((B[y][x] / Y[y][x]), 0.6))
output_img = cv2.merge([new_B, new_G, new_R])

# Display the images
result_img = cv2.hconcat([input_img, output_img])
cv2.imshow('YCbCr Histogram Equalization', result_img)
cv2.waitKey(0)