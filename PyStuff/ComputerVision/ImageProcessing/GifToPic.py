import os
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence

gif = Image.open("CarlBradbury.gif")

print(gif.info["duration"])
a=0
os.chdir("F:\\Python Files\\ImageProcessing\\Frames")
for frame in ImageSequence.Iterator(gif):
    img = np.array(frame)
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(img_)
    cv2.imwrite(str(a)+".png",img_)
    a+=1
