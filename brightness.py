import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("images/test1.jpg")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
imgb = img+100
imgc = cv.add(img,100)
f,ax = plt.subplots(1,3)
ax[0].imshow(img,cmap="gray")
ax[0].set_title('Original')
ax[1].imshow(imgb,cmap="gray")
ax[1].set_title('img+100')
ax[2].imshow(imgc,cmap="gray")
ax[2].set_title('cv.add')
cv.imshow('img',img)
cv.waitKey(0)
cv.imshow('imgb',imgb)
cv.waitKey(0)
cv.imshow('imgc',imgc)
cv.waitKey(0)