import cv2 as cv
import matplotlib .pyplot as plt

# Image read
#img = cv.imread('images/lena.jpg')
#img = cv.imread('images/MonaLisa-grayscale.jpg')
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
