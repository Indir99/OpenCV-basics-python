import cv2 as cv
from cv2 import THRESH_BINARY_INV
import matplotlib .pyplot as plt

# Image read
#img = cv.imread('images/lena.jpg')
img = cv.imread('images/Napoleon.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title(' Grayscale histogram ')
plt.xlabel(' Bins ')
plt.ylabel(' Nummber of pixels ')
plt.plot(gray_hist)
plt.xlim([0, 256])

plt.show()

# Threshold
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow(' Thresholded ', thresh)

threshold, thresh_inv = cv.threshold(
    gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow(' Thresholded inverse ', thresh_inv)

adaptive_tresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow(' Adaptive thresholding ', adaptive_tresh)
cv.waitKey(0)
cv.waitKey(0)
