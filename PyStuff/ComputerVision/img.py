import os
import cv2


os.chdir("F:\\Python Files\\Computer Vision\\DataSet")

for i in os.walk(os.getcwd()):
    print(i)
    img=i[2][7]

img_cv=cv2.imread(img,0)

cv2.imshow('pic',img_cv)
