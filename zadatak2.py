import cv2 as cv

# Import image
img = cv.imread('images/lena.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

# Convert to grayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

# Avergaing filter
average = cv.blur(gray, (3, 3))
cv.imshow('Average blur', average)
cv.waitKey(0)

# Gaussian
gaussian = cv. GaussianBlur(gray, (3, 3), 0)
cv.imshow('Gaussian blur', gaussian)
cv.waitKey(0)

# Median blur , good for salt and pepper noise
median = cv. medianBlur(gray, 3)
cv.imshow(' Median ', median)
cv.waitKey(0)
