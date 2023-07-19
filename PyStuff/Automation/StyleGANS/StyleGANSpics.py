import io
import os
import time
import requests
import threading
from PIL import Image
from colorama import Fore,Style

a=0
img=["https://thispersondoesnotexist.com/image"]
imgSet=img*1000

t1=time.time()
def saving(img_):
    try:
        global a
        t1_=time.time()
        r=requests.get(img_).content
        os.chdir("K:\\Python Files\\Automation\\StyleGANS\\Dataset")
        f=io.BytesIO(r)
        imgf=Image.open(f)
        imgf.save(str(a)+'.jpg')
        t2_=time.time()
        if a%2==0:
            print(Fore.MAGENTA+Style.BRIGHT+str(a)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs')
        else:
            print(Fore.CYAN+Style.BRIGHT+'\t\t'+str(a)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs')
        a+=1
    except:
        print(Fore.RED+Style.BRIGHT+"~~~|",i)
        pass

for i in imgSet:
    ThreadObj=threading.Thread(target=saving,args=(i,))
    ThreadObj.start()
    ThreadObj.join(timeout=60)
              
t2=time.time()
print("\n\n\nExecTime:", t2-t1)
