import cv2 as cv
import numpy as np

IMAGE_PATH = "images/lums.png"

img = cv.imread(IMAGE_PATH)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (3, 3), 0)

sobel = cv.Canny(img, 100, 100)

cv.imshow("sobel", sobel)
cv.waitKey(0)
