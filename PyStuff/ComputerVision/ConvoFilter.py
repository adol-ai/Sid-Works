import os
import cv2
import numpy as np

img=cv2.imread('27.png')

'''k1=np.array([[0,0,0],
             [0,1,0],
             [0,0,0]])'''

k1=np.ones((5,5), np.float32)/25

fil=cv2.filter2D(src=img, ddepth=-1, kernel=k1)

cv2.imshow("Pic",img)
cv2.imshow("img",fil)
