#%matplotlib inline
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import matplotlib
im = np.zeros((6,8),dtype=np.uint8)
im[2,3]=250
fig,ax=plt.subplots()
ax.imshow(im,cmap='gray',vmin=0,vmax=255)
ax.xaxis.tick_top()
plt.show()