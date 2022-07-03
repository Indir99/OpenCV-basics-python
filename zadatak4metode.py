import cv2 as cv

# Method 1
img = cv.imread('images/lena.jpg')
cv.imshow('Original', img)
cv.waitKey(0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image - Method 1', gray)
cv.waitKey(0)

# Method 2
img_gray = cv.imread('images/lena.jpg', 0)
cv.imshow('Grayscale Image - Method 2', img_gray)
cv.waitKey(0)

# Method 3
img = cv.imread('images/lena.jpg')

# Obtain the dimensions of the image array
# using the shape method
(row, col) = img.shape[0:2]

# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        img[i, j] = sum(img[i, j]) * 0.33

cv.imshow('Grayscale Image - Method 3', img)
cv.waitKey(0)
