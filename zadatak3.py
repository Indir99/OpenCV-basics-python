import cv2 as cv
import numpy as np


img = cv.imread('images/lena.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

# Labplacian filter
lap = cv. Laplacian(gray, cv.CV_64F)
lap = np.uint8(np. absolute(lap))
cv.imshow('Laplacian', lap)
cv.waitKey(0)

# Sobel filter
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobelx', sobelx)
cv.waitKey(0)
cv.imshow('Sobely', sobely)
cv.waitKey(0)
cv.imshow('Combined Sobel', combined_sobel)
cv.waitKey(0)

canny = cv.Canny(gray, 150, 175)
cv.imshow(' Canny ', canny)
cv.waitKey(0)
