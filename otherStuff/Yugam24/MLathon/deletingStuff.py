from tkinter import filedialog
import tqdm
import glob
import time
import os

print("Select the imgAnno Directory Yo!")
inDir = filedialog.askdirectory()
if "\\" in inDir:
    inDir = inDir + '\\'
else:
    inDir = inDir + '/'
print("---->", inDir)
imgStuff = [glob.glob(inDir+y) for y in ['*.jpg', '*.png']]
imgStuff = set([y[:-4] for y in sum(imgStuff , [])])
xmlStuff = glob.glob(inDir+'*.xml')
xmlStuff = set([y[:-4] for y in xmlStuff])

diffStuff = (xmlStuff - imgStuff) | (imgStuff - xmlStuff)

t1 = time.time()
for i in tqdm.tqdm(diffStuff, desc = "Deletin' Stuff Yo!", colour = 'red'):
    try:
        os.remove(i+'.xml')
    except:
        try:
            os.remove(i+'.png')
        except:
            os.remove(i+'.jpg')

t2 = time.time()
print("\nCompleteExecTime: ", (t2-t1))