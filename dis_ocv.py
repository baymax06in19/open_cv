import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("images/test1.jpg",cv.IMREAD_COLOR)
cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()