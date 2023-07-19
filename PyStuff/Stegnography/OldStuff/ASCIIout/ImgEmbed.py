import time
import base64
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

msg="Hey hiiytdytfuy ytdyuyfu fyrdytfuyf rydyd u ytdytf ytdgh qwert Yoooo"

def encode(msg,pic):
    global img_ar
    s=msg.encode('ascii')
    s_encode=base64.b64encode(s)
    print("~~~~~~~~~~~~~~~~~~~~~> ",s_encode)
    s_hex=base64.decodebytes(s_encode)
    s_bin="".join("{:08b}".format(x) for x in s_hex)
    print(len(s_bin))
    print(s_bin)
    msg_l=[*s_bin]
    img=Image.open(pic).convert('RGB')
    img_ar=np.array(img)
    a=-1
    stop=0
    index1=-1
    for i in img_ar:
        index2=-1
        if stop==1:
            break
        index1+=1
        for j in i:
            index3=-1
            index2+=1
            if stop==1:
                break
            for k in j:
                index3+=1
                #time.sleep(1)
                k=bin(k)[2:].zfill(8)
                byte=[*k]
                if a==len(msg_l):
                    stop=1
                    break
                else:
                    byte[-1]=msg_l[a]
                msg_byte="".join(x for x in byte)
                img_ar[index1][index2][index3]=int("0b"+msg_byte,2)
                a+=1
    embed=Image.fromarray(img_ar)
    embed.save("E.png")
    #print(img_ar,"\n\n\n\n\n\n\n\n\n\n")

def decode(pic):
    img=Image.open(pic).convert('RGB')
    img_ar=np.array(img)
    #print(img_ar)
    a=-1
    stop=0
    index1=-1
    msg_bin=""
    for i in img_ar:
        if stop==1:
            break
        for j in i:
            if stop==1:
                break
            for k in j:
                k=bin(k)[2:].zfill(8)
                byte=[*k]
                if a==544:
                    stop=1
                    break
                else:
                    msg_bin+=byte[-1]
                a+=1
    print(byte)
    print("\n\n======================~~~~~~~~~~~~~~~~~~~~~~~~~===========================")
    print(msg_bin)
    print("\n\n")
    d_msg=bin(int(msg_bin,2)).encode('utf-8')
    d_s=base64.encodebytes(d_msg)
    #s=d_s.encode('ascii')
    print(d_s)
    #print(img_ar)

encode(msg,"org.png")
decode("E.png")
