import os
import cv2
import glob
import matplotlib.pyplot as plt

os.chdir('HeatMap_CompleteStuff')
x = glob.glob("*.jpg")
a = 1
for i in x:
    img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
    imgOut = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    cv2.imwrite(i, imgOut)
    print("-"*a)
    a+=1
