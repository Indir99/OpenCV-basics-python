import cv2 as cv
import numpy as np
import random


def sp_noise(image, prob):

    # Add salt and pepper noise to image
    # prob: Probability of the noise

    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


# Import image
img = cv.imread('images/lena.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

# Convert to grayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

# Noise
noise_img = sp_noise(gray, 0.05)
cv.imshow('Salt and Paper noise', noise_img)
cv.waitKey(0)

# Avergaing filter
average = cv.blur(noise_img, (3, 3))
cv.imshow('Average blur', average)
cv.waitKey(0)

# Gaussian
gaussian = cv.GaussianBlur(noise_img, (3, 3), 0)
cv.imshow('Gaussian blur', gaussian)
cv.waitKey(0)

# Median blur , good for salt and pepper noise
median = cv.medianBlur(noise_img, 3)
cv.imshow(' Median ', median)
cv.waitKey(0)

# Gaussian effect for bluring
gaussian = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Gaussian bluring', gaussian)
cv.waitKey(0)
cv.waitKey(0)
