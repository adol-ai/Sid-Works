from tkinter import filedialog
import random
import tqdm
import glob
import time
import os

t1 = time.time()
print("Select the Directory Yo!")
imgDir = filedialog.askdirectory()
dirStuff = imgDir
if "\\" in imgDir:
    imgDir = imgDir + '\\'
else:
    imgDir = imgDir + '/'
print("---->", imgDir)
x = [glob.glob(imgDir+y) for y in ['*.jpg', '*.png', '*.tiff', '*.bmp', '*.jpeg']]
x = sum(x , [])
random.shuffle(x)

a=1
for i in tqdm.tqdm(x, desc = "ReNamin' the Images Yo!", colour = 'red'):
    os.rename(i, imgDir+str(a)+str(os.path.basename(dirStuff))+'.png')
    a+=1
t2 = time.time()
print("\nCompleteExecTime: ", (t2-t1))