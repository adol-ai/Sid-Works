import sys
import time
import math
import base64
import numpy as np
from PIL import Image
from colorama import Fore,Style

def steg(byte_depth, InputImageFile, InputFile, OutImage):
    t1=time.time()
    print(Fore.MAGENTA+Style.BRIGHT+"Byte_Depth: ", byte_depth, Fore.RESET)
    byte_depth = int(byte_depth)

    img = Image.open(InputImageFile).convert('RGB')
    img_ar = np.array(img)
    dim = img_ar.shape
    
    f = open(InputFile, 'rb')
    b64_str = f.read()
    aud_data = base64.urlsafe_b64encode(b64_str)
    aud_b64 = aud_data.decode('ascii').replace("_","/").replace("-","+").replace('=','')
    encode_ar=np.array(list(aud_b64))

    def b64_bin(x):
        return bin(ord(x))[2:]
    vfun = np.vectorize(b64_bin)
    encode_bin = vfun(encode_ar)
    print(encode_bin)

    s_bin="".join(encode_bin)
    if len(s_bin)%byte_depth!=0:
        s_bin+="0"*(byte_depth-(len(s_bin)%byte_depth))
    if byte_depth<=0 or byte_depth>8:
        raise "Invalid Byte Depth Value"
    '''if len(s_bin)>(math.prod([dim[0],dim[1],3,byte_depth])):
        print(Fore.RED, "DataBits ~",len(s_bin), ">", "BitsAvailable ~", (math.prod([dim[0],dim[1],3,byte_depth])))
        print(Fore.RESET)
        raise "Insufficient Memory Spacing, Increase Byte Depth Value"'''
    ch_bin=np.array(list(s_bin)).reshape(int(len(s_bin)/byte_depth),byte_depth)

    print(Fore.RED+"Available bits:  ",math.prod([dim[0],dim[1],3,byte_depth]))
    print(Fore.RED+"Msg bits:  ",len(s_bin))
    px_ht = math.ceil((len(s_bin)/3))
    px_wd = 1
    if px_ht>dim[1]:
        px_wd = math.ceil(len(s_bin)/dim[0]/3/byte_depth)
        px_ht = dim[0]
    print(Fore.CYAN+Style.BRIGHT+"No of PixelsRows: ",px_ht)
    print(Fore.CYAN+Style.BRIGHT+"No of PixelsColumns: ",px_wd)

    select_px = img_ar[:px_wd+1, :px_ht+1]
    print(Fore.MAGENTA+Style.BRIGHT+"Select Pixel Count: ",len(select_px))
    flat_px = select_px.flatten()
    print(flat_px)
    zip_bin = np.array(list(zip(flat_px,ch_bin)), dtype=object)
    print(Fore.YELLOW+Style.BRIGHT+"Select Pixel Bits: ", len(flat_px))

    def bin_embed(x):
        bin_val = bin(int(x[0]))
        bin_val = list(bin_val)[2:]
        bin_val[-byte_depth:] = x[1]
        bin_str = "".join(bin_val)
        return int(bin_str,2)
        
    vfunc = np.vectorize(bin_embed, signature='(n)->()')
    encoded_px = vfunc(zip_bin)
    encoded_px=np.append(encoded_px, flat_px[len(encoded_px):])

    reshaped_px = encoded_px.reshape(select_px.shape)
    print(Fore.BLUE+Style.BRIGHT+"Embedded Region: ", reshaped_px.shape)
    img_ar[:px_wd+1, :px_ht+1]=reshaped_px

    t2=time.time()
    print(Fore.RESET+"ExecTime",t2-t1,"\n\n")
    embed_img=Image.fromarray(img_ar)
    embed_img.save(OutImage)

steg(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
