from colorama import Fore, Style
from tkinter import filedialog
from ultralytics import YOLO
import pandas as pd
import numpy as np
import random
import torch
import tqdm
import glob
import os

workinDir = os.getcwd()
if "\\" in workinDir:
    workinDir = workinDir + '\\'
else:
    workinDir = workinDir + '/'
print(Fore.YELLOW+Style.BRIGHT+"\n\nSelect in-imgDir Yo !"+Fore.RESET)
imgDir = filedialog.askdirectory()
print("---->", imgDir)
os.chdir(imgDir)

print(Fore.BLUE+Style.BRIGHT+"\n\nSelect the Trained Weight File Yo!"+Fore.RESET)
inWeight = filedialog.askopenfilename(filetypes=[("pt Weight File", "*.pt")])

numStuff = {'crane': 0, 'crow': 1, 'egret': 2, 'kingfisher': 3, 'myna': 4, 'peacock': 5, 'pitta': 6, 'rosefinch': 7, 'tailorbird': 8, 'wagtail': 9}
clsStuff = {0: 'Crane', 1: 'Crow', 2: 'Egret', 3: 'Kingfisher', 4: 'Myna', 5: 'Peacock', 6: 'Pitta', 7: 'Rosefinch', 8: 'Tailorbird', 9: 'Wagtail'}
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
modelStuff = YOLO(inWeight).to(device)

imgStuff = glob.glob("*.jpg")

outVal = []
for inImg in tqdm.tqdm(imgStuff, desc = "Flowin' through images Yo!", colour = "red"):
    outStuff = modelStuff(inImg, save_conf=True)
    outNum = outStuff[0].boxes.cls.to("cpu")
    if len(outNum)==0:
        outNum = random.choice(list(clsStuff.keys()))
    else:
        outNum = int(outNum[0])
    outCls = clsStuff[outNum]
    imgName = inImg.split('.')[0]
    rowVal = [imgName, outCls, outNum]
    outVal.append(rowVal)

df = pd.DataFrame(outVal, columns = ['ID', 'Target_name', 'Target_num'])
df.to_csv(workinDir+'outCSV.csv', index = False)