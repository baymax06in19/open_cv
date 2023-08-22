import matplotlib.pyplot as plt
import cv2 as cv
img = cv.imread("images/test1.jpg",cv.IMREAD_ANYCOLOR)
if img is None:
    print("image could not be read.")
    assert False    # essentially stop the program

#In the open cv color format is BGR
##img[:,:,0:2]=0  #For all the values in height,width,{0,1-which represent blue and green } assign the value 0 so the only value remain is red channel othe channels value 0 means black
##plt.imshow(img)
##cv.imshow('img',img)    #image can be seen totally red and black


img = cv.cvtColor(img,cv.COLOR_BGR2RGB) # change the color format channels
plt.imshow(img)
plt.title('image')
plt.xticks([]),plt.yticks([]) #values of the x and y axis removed
plt.show()

img[:,:,0:2]=0 #remove the RED and Green menas make them 0 which is black
plt.imshow(img)
plt.title('After Zeroing planes')
plt.xticks([]),plt.yticks([])
plt.show() # remain color is blue+black

#by using matplot lib plt.show() we can see the pixel values of the all the pixcel on the image