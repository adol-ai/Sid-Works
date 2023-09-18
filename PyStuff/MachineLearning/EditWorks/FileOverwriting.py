import os
import glob
import random

a = 1

os.chdir("CompleteStuff")
x = glob.glob("*.jpg")

random.shuffle(x)

for i in x:
    y = i.split('.jpg')[0]
    print('--->', y)
    os.rename(y+".jpg", str(a)+".jpg")
    os.rename(y+".txt", str(a)+".txt")
    print("-"*a)
    a+=1