import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("images/test1.jpg",cv.IMREAD_COLOR)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
fig,ax=plt.subplots()
ax.imshow(img)
ax.set_title("Image")
plt.show()
print(img.shape)
print(img.size)
print(img.dtype)