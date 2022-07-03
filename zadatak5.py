import cv2 as cv
# Image read
img = cv.imread('images/lena.jpg')
#img = cv.imread('images/Napoleon.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

# Gauss filter
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow(' Blured ', blur)

# canny edge detector
canny = cv.Canny(img, 125, 175)
cv.imshow(' Canny ', canny)

# dilatation
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow(' Dilatation ', dilated)

# erosion
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow(' Erosion ', eroded)

borders = canny - eroded
cv.imshow(' Borders ', borders)
cv.waitKey(0)
cv.waitKey(0)
