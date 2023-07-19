import sys
import time
import math
import base64
import numpy as np
from PIL import Image
from colorama import Fore,Style

def steg(byte_depth, InputImageFile, InputAudioFile, OutImage):
    t1=time.time()
    b64={'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011', 'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111', 'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011', 'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111', 'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011', 'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111', 'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011', 'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111', 'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011', 'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111', 'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011', 's': '101100', 't': '101101', 'u': '101110', 'v': '101111', 'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011', '0': '110100', '1': '110101', '2': '110110', '3': '110111', '4': '111000', '5': '111001', '6': '111010', '7': '111011', '8': '111100', '9': '111101', '+': '111110', '/': '111111'}
    print(Fore.MAGENTA+Style.BRIGHT+"Byte_Depth: ", byte_depth, Fore.RESET)
    byte_depth = int(byte_depth)
    
    f = open(InputAudioFile, 'rb')
    b64_str = f.read()
    aud_data = base64.urlsafe_b64encode(b64_str)
    aud_b64 = aud_data.decode('ascii').replace("_","/").replace("-","+").replace('=','')
    encode_ar=np.array(list(aud_b64))

    def b64_bin(x,d):
        return d[x]
    vfun = np.vectorize(b64_bin)
    encode_bin = vfun(encode_ar, b64)
    print(encode_bin)

    s_bin="".join(encode_bin)
    if len(s_bin)%byte_depth!=0:
        s_bin+="0"*(byte_depth-(len(s_bin)%byte_depth))
    if byte_depth<=0 or byte_depth>8:
        raise "Invalid Byte Depth Value"
    if len(s_bin)>(math.prod([1024,1024,3,byte_depth])):
        raise "Insufficient Memory Spacing, Increase Byte Depth Value"
    ch_bin=np.array(list(s_bin)).reshape(int(len(s_bin)/byte_depth),byte_depth)

    print(Fore.RED+"Msg bits:  ",len(s_bin))
    px_ht = math.ceil((len(s_bin)/3))
    px_wd = 1
    if px_ht>1024:
        px_wd = math.ceil(len(s_bin)/1024/3/byte_depth)
        px_ht = 1024
    print(Fore.CYAN+Style.BRIGHT+"No of PixelsRows: ",px_ht)
    print(Fore.CYAN+Style.BRIGHT+"No of PixelsColumns: ",px_wd)


    img = Image.open(InputImageFile).convert('RGB')
    img_ar = np.array(img)

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
    print(Fore.RESET+"\n\nExecTime",t2-t1)
    embed_img=Image.fromarray(img_ar)
    embed_img.save(OutImage)

steg(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
