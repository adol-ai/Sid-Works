import sys
import time
import math
import base64
import piexif
import threading
import numpy as np
from PIL import Image
import multiprocessing
from colorama import Fore,Style

t1_ = time.time()
def steg(OutFile, SeedValue, BioTone, VoiceFile, Face1, Face2, Face3, Face4, Face5,  Palm=None,  Iris=None, Ear=None):
    b64 = {'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011', 'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111', 'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011', 'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111', 'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011', 'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111', 'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011', 'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111', 'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011', 'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111', 'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011', 's': '101100', 't': '101101', 'u': '101110', 'v': '101111', 'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011', '0': '110100', '1': '110101', '2': '110110', '3': '110111', '4': '111000', '5': '111001', '6': '111010', '7': '111011', '8': '111100', '9': '111101', '+': '111110', '/': '111111'}

    CompleteGrid = np.zeros((3,3), dtype=np.ndarray)
    Grids = {"BioTone":[VoiceFile, [1,1]], "Face1":[Face1, [0,0]], "Face2":[Face2, [0,1]], "Face3":[Face3, [0,2]], "Face4":[Face4, [1,0]], "Face5":[Face5, [1,2]], "Palm":[Palm, [2,0]], "Iris":[Iris, [2,1]], "Ear":[Ear, [2,2]]}
    Grids_ar = np.array(list(Grids.keys()))
    BioToneimg = Image.open(BioTone).convert('RGB')
    org_dim = np.array(BioToneimg).shape
    metaData = {}
    CheckList = []
    instance_data = threading.local()
    print("\n")
    def process(z):
        instance_data.z = z
        instance_data.t1 = time.time()
        if z not in CheckList:
            CheckList.append(z)
            print(Fore.YELLOW+Style.BRIGHT+"Grid: ", instance_data.z)
            print(Fore.BLUE+Style.BRIGHT+"FeedFile: ", Grids[instance_data.z][0])
            if instance_data.z=="BioTone":
                instance_data.byte_depth = 3
                instance_data.img = BioToneimg
            else:
                instance_data.byte_depth = 8
                np.random.seed(math.prod((int(SeedValue), list(Grids.keys()).index(instance_data.z))))
                instance_data.ar = np.random.randint(255,size=org_dim).astype(np.uint8)
                instance_data.img = Image.fromarray(instance_data.ar)
            instance_data.img_ar = np.array(instance_data.img)
            instance_data.dim = instance_data.img_ar.shape
            print(Fore.MAGENTA+Style.BRIGHT+"instance_data.byte_depth: ", instance_data.byte_depth, Fore.RESET)
            if Grids[instance_data.z][0] is not None:
                instance_data.f = open(Grids[instance_data.z][0], 'rb')
                instance_data.b64_str = instance_data.f.read()
                instance_data.obj_data = base64.urlsafe_b64encode(instance_data.b64_str)
                instance_data.obj_b64 = instance_data.obj_data.decode('ascii').replace("_","/").replace("-","+").replace('=','')
                instance_data.encode_ar = np.array(list(instance_data.obj_b64))
                print("Base64 Chars: ", len(instance_data.obj_b64))

                def b64_bin(x,d):
                    return d[x]
                instance_data.vfun = np.vectorize(b64_bin)
                instance_data.encode_bin = instance_data.vfun(instance_data.encode_ar, b64)
                print(instance_data.encode_bin)

                instance_data.s_bin="".join(instance_data.encode_bin)
                if len(instance_data.s_bin)%instance_data.byte_depth!=0:
                    instance_data.s_bin+="0"*(instance_data.byte_depth-(len(instance_data.s_bin)%instance_data.byte_depth))
                if instance_data.byte_depth<=0 or instance_data.byte_depth>8:
                    raise "Invalid Byte Depth Value"
                if len(instance_data.s_bin)>(math.prod([instance_data.dim[0],instance_data.dim[1],3,instance_data.byte_depth])):
                    print(Fore.RED, "DataBits ~",len(instance_data.s_bin), ">", "BitsAvailable ~", (math.prod([instance_data.dim[0],instance_data.dim[1],3,instance_data.byte_depth])), Fore.RESET)
                    raise "Insufficient Memory Spacing, Increase Byte Depth Value"
                instance_data.ch_bin=np.array(list(instance_data.s_bin)).reshape(int(len(instance_data.s_bin)/instance_data.byte_depth),instance_data.byte_depth)

                print(Fore.RED+"Available bits:  ",math.prod([instance_data.dim[0],instance_data.dim[1],3,instance_data.byte_depth]))
                print(Fore.RED+"Msg bits:  ",len(instance_data.s_bin))
                instance_data.px_ht = math.ceil((len(instance_data.s_bin)/3))
                instance_data.px_wd = 1
                if instance_data.px_ht>instance_data.dim[1]:
                    instance_data.px_wd = math.ceil(len(instance_data.s_bin)/instance_data.dim[0]/3/instance_data.byte_depth)
                    instance_data.px_ht = instance_data.dim[0]
                print(Fore.CYAN+Style.BRIGHT+"No of PixelsRows: ",instance_data.px_wd)
                print(Fore.CYAN+Style.BRIGHT+"No of PixelsColumns: ",instance_data.px_ht)

                instance_data.select_px = instance_data.img_ar[:instance_data.px_wd+1, :instance_data.px_ht+1]
                print(Fore.MAGENTA+Style.BRIGHT+"Select Pixel Count: ",len(instance_data.select_px))
                instance_data.flat_px = instance_data.select_px.flatten()
                print(instance_data.flat_px)
                zip_bin = np.array(list(zip(instance_data.flat_px,instance_data.ch_bin)), dtype=object)
                print(Fore.YELLOW+Style.BRIGHT+"Select Pixel Bits: ", len(instance_data.flat_px))

                def bin_embed(x):
                    instance_data.bin_val = bin(int(x[0]))
                    instance_data.bin_val = list(instance_data.bin_val)[2:]
                    instance_data.bin_val[-instance_data.byte_depth:] = x[1]
                    instance_data.bin_str = "".join(instance_data.bin_val)
                    return int(instance_data.bin_str,2)
                    
                instance_data.vfunc = np.vectorize(bin_embed, signature='(n)->()')
                instance_data.encoded_px = instance_data.vfunc(zip_bin)
                instance_data.encoded_px=np.append(instance_data.encoded_px, instance_data.flat_px[len(instance_data.encoded_px):])

                instance_data.reshaped_px = instance_data.encoded_px.reshape(instance_data.select_px.shape)
                instance_data.stuff_region = instance_data.reshaped_px.shape
                print(Fore.BLUE+Style.BRIGHT+"Embedded Region: ", instance_data.stuff_region)
                instance_data.img_ar[:instance_data.px_wd+1, :instance_data.px_ht+1]=instance_data.reshaped_px

                instance_data.endFile = Grids[instance_data.z][0].split("/")
                instance_data.embedFile = instance_data.endFile[len(instance_data.endFile)-1]
                metaData[str(Grids[instance_data.z][1])] = [instance_data.byte_depth, instance_data.stuff_region, instance_data.embedFile]
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", metaData)
                instance_data.t2 = time.time()
                print(Fore.RESET+"ExecTime",instance_data.t2-instance_data.t1,"\n\n")
            CompleteGrid[Grids[instance_data.z][1][0], Grids[instance_data.z][1][1]] = instance_data.img_ar
        
        if len(metaData)==len(sys.argv)-4:
            print("\n", metaData)
            Patched_img = np.vstack((np.hstack(CompleteGrid[0]), np.hstack(CompleteGrid[1]), np.hstack(CompleteGrid[2])))
            embed_img = Image.fromarray(Patched_img)
            embed_img.save(OutFile)
            exif_dict = piexif.load(OutFile)
            exif_dict["Exif"][piexif.ExifIFD.UserComment] = str(metaData).encode("utf-8")
            exif_bytes = piexif.dump(exif_dict)
            meta_img = Image.open(OutFile)
            meta_img.save(OutFile, exif=exif_bytes)
            t2_ = time.time()
            print(Fore.RED+"CompleteExecTime",t2_-t1_,"\n\n"+Fore.RESET)

    def formation(w):
        t = threading.Thread(target = process, args=(w,))
        t.start()
        
    instance_data.vfunct = np.vectorize(formation)
    instance_data.vfunct(Grids_ar)    
if __name__ == '__main__':
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(cores)
    pool.apply_async(steg, args = (*sys.argv[1:10],))
    pool.close()
    pool.join()