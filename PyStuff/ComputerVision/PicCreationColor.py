import os
import cv2
import random
import pprint
import xml.etree.ElementTree as et


os.chdir("F:\\Python Files\\Computer Vision\\Yooooo")
img=cv2.imread("F:\Python Files\Computer Vision\Yooooo\FinalLayer.png")


random.seed=42
print(img.shape)
cv2.imshow("Pic", img)
cv2.waitKey(500)

datapoints=[]
for i in range(0,200):
    l=[random.randrange(0,800),random.randrange(0,600)+random.randrange(0,200),random.randrange(0,800),random.randrange(0,600)+random.randrange(0,200)]
    datapoints.append(l)
print(l)

#rec
for y in datapoints:
    min_point=(int(y[0]), int(y[1]))
    max_point=(int(y[2]), int(y[3]))
    color = random.choices([(255,0,0), (0,255,0), (0,0,255), (0,255,255)])
    print(color)
    cv2.rectangle(img,min_point,max_point, color[0], thickness=1, lineType=cv2.LINE_8)

cv2.imwrite("ColorMergedLayer.png",img)
cv2.imshow("LabelledPic", img)
cv2.waitKey(500)


