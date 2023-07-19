import os
import cv2
import random
import pprint
import xml.etree.ElementTree as et


os.chdir("F:\\Python Files\\Computer Vision\\Yooooo")
img=cv2.imread("F:\Python Files\Computer Vision\Yooooo\GridPic_.png")

'''
random.seed=42
print(img.shape)
cv2.imshow("Pic", img)
cv2.waitKey(500)

datapoints=[]
for i in range(0,80):
    l=[random.randrange(0,800),random.randrange(0,600)+random.randrange(0,200),random.randrange(0,800),random.randrange(0,600)+random.randrange(0,200)]
    datapoints.append(l)
print(l)

#rec
for y in datapoints:
    min_point=(int(y[0]), int(y[1]))
    max_point=(int(y[2]), int(y[3]))
    cv2.rectangle(img,min_point,max_point,(0,0,0), thickness=1, lineType=cv2.LINE_8)

cv2.imwrite("MergedLayer.png",img)
cv2.imshow("LabelledPic", img)
cv2.waitKey(500)
'''

print(img.shape)
cv2.imshow("Pic", img)
cv2.waitKey(500)

datapoints=[]

#rec
px_val=100
div=int(800/px_val)
for x in range(0,div):
    min_point=(x*px_val, x*px_val)
    max_point=((x+1)*px_val, (x+1)*px_val)
    cv2.rectangle(img,min_point,max_point,(0,0,0), thickness=3, lineType=cv2.LINE_8)
    for y in range(0,div):
        min_point=(x*y*px_val, x*y*px_val)
        max_point=((x+1)*y*px_val, (x+1)*y*px_val)
        cv2.rectangle(img,min_point,max_point,(0,0,0), thickness=3, lineType=cv2.LINE_8)
        


cv2.imwrite("GridPic.png",img)
cv2.imshow("GridPic", img)
cv2.waitKey(500)
