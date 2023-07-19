import sys
import time
import math
import base64
import piexif
import cProfile
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
    orgDim = np.array(BioToneimg).shape
    metaData = {}
    CheckList = []
    print("\n")
    def formation(z):
        t1 = time.time()
        if z not in CheckList:
            print(Fore.YELLOW+Style.BRIGHT+"Grid: ", z)
            print(Fore.BLUE+Style.BRIGHT+"FeedFile: ", Grids[z][0])
            if z=="BioTone":
                byte_depth = 3
                img = BioToneimg
            else:
                byte_depth = 8
                np.random.seed(math.prod((int(SeedValue), list(Grids.keys()).index(z))))
                ar = np.random.randint(255,size=orgDim).astype(np.uint8)
                img = Image.fromarray(ar)
            img_ar = np.array(img)
            dim = img_ar.shape
            print(Fore.MAGENTA+Style.BRIGHT+"Byte_Depth: ", byte_depth, Fore.RESET)
            if Grids[z][0] is not None:
                f = open(Grids[z][0], 'rb')
                b64_str = f.read()
                obj_data = base64.urlsafe_b64encode(b64_str)
                obj_b64 = obj_data.decode('ascii').replace("_","/").replace("-","+").replace('=','')
                encode_ar = np.array(list(obj_b64))
                print("Base64 Chars: ", len(obj_b64))

                def b64_bin(x,d):
                    return d[x]
                vfun = np.vectorize(b64_bin)
                encode_bin = vfun(encode_ar, b64)
                print(encode_bin)

                s_bin="".join(encode_bin)
                if len(s_bin)%byte_depth!=0:
                    s_bin+="0"*(byte_depth-(len(s_bin)%byte_depth))
                if byte_depth<=0 or byte_depth>8:
                    raise Exception("Invalid Byte Depth Value")
                if len(s_bin)>(math.prod([dim[0],dim[1],3,byte_depth])):
                    print(Fore.RED, "DataBits ~",len(s_bin), ">", "BitsAvailable ~", (math.prod([dim[0],dim[1],3,byte_depth])), Fore.RESET)
                    raise Exception("Insufficient Memory Spacing, Increase Byte Depth Value")
                ch_bin=np.array(list(s_bin)).reshape(int(len(s_bin)/byte_depth),byte_depth)
                
                print(Fore.RED+"Available bits:  ",math.prod([dim[0],dim[1],3,byte_depth]))
                print(Fore.RED+"Msg bits:  ",len(s_bin))
                px_ht = math.ceil((len(s_bin)/3))
                px_wd = 1
                if px_ht>dim[1]:
                    px_wd = math.ceil(len(s_bin)/dim[0]/3/byte_depth)
                    px_ht = dim[0]
                print(Fore.CYAN+Style.BRIGHT+"No of PixelsRows: ",px_wd)
                print(Fore.CYAN+Style.BRIGHT+"No of PixelsColumns: ",px_ht)

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
                stuff_region = reshaped_px.shape
                print(Fore.BLUE+Style.BRIGHT+"Embedded Region: ", stuff_region)
                img_ar[:px_wd+1, :px_ht+1]=reshaped_px

                endFile = Grids[z][0].split("/")
                embedFile = endFile[len(endFile)-1]
                metaData[str(Grids[z][1])] = [byte_depth, stuff_region, embedFile]

                t2 = time.time()
                print(Fore.RESET+"ExecTime",t2-t1,"\n\n")
            CompleteGrid[Grids[z][1][0], Grids[z][1][1]] = img_ar
        CheckList.append(z)
        
    vfunct = np.vectorize(formation)
    vfunct(Grids_ar)
    print("\n", metaData)
    PatchedImg = np.vstack((np.hstack(CompleteGrid[0]), np.hstack(CompleteGrid[1]), np.hstack(CompleteGrid[2])))
    embed_img = Image.fromarray(PatchedImg)
    embed_img.save(OutFile)
    exif_dict = piexif.load(OutFile)
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = str(metaData).encode("utf-8")
    exif_bytes = piexif.dump(exif_dict)
    meta_img = Image.open(OutFile)
    meta_img.save(OutFile, exif=exif_bytes)

if __name__ == '__main__':
    cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(cores)
    profiler = cProfile.Profile()
    profiler.enable()
    pool.apply_async(steg, args = (*sys.argv[1:10],))
    profiler.disable()
    profiler.print_stats()
    pool.close()
    pool.join()
    t2_ = time.time()
    print(Fore.RED+"CompleteExecTime",t2_-t1_,"\n\n"+Fore.RESET)