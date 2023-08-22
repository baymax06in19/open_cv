import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
def img_brighten(image,shift):
    h=image.shape[0]
    w=image.shape[1]
    result=np.zeros(image.shape,image.dtype)
    for i in range(0,h):
        for j in range(0,w):
            no_overflow = True if image[i,j] + shift <255 else False
            result[i,j] = min(image[i,j]+shift,255) if no_overflow else 255

    return result
    
img = cv.imread("images/test1.jpg",cv.IMREAD_GRAYSCALE)
imgb = img_brighten(img,205)
f,ax = plt.subplots(1,2)
ax[0].imshow(img,cmap='gray')
ax[0].set_title('Original')
ax[1].imshow(imgb,cmap='gray')
ax[1].set_title('image_brighten')
plt.show()
