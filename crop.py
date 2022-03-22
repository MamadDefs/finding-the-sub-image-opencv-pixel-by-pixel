import cv2 as cv

original=cv.imread("original.jpg")
cv.imwrite("crop.jpg",original[100:300,200:300])
