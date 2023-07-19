import sys
import time
import base64
import piexif
import numpy as np
from PIL import Image
from colorama import Fore, Style

t1_ = time.time()
def stegRev(InFile, DimSide):
    b64_rev={'000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D', '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H', '001000': 'I', '001001': 'J', '001010': 'K', '001011': 'L', '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P', '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T', '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X', '011000': 'Y', '011001': 'Z', '011010': 'a', '011011': 'b', '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f', '100000': 'g', '100001': 'h', '100010': 'i', '100011': 'j', '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n', '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r', '101100': 's', '101101': 't', '101110': 'u', '101111': 'v', '110000': 'w', '110001': 'x', '110010': 'y', '110011': 'z', '110100': '0', '110101': '1', '110110': '2', '110111': '3', '111000': '4', '111001': '5', '111010': '6', '111011': '7', '111100': '8', '111101': '9', '111110': '+', '111111': '/'}

    exif_dict = piexif.load(InFile)
    exif = exif_dict["Exif"].get(piexif.ExifIFD.UserComment)
    meta_stuff = eval(bytes(exif).decode("UTF-8"))
    meta_ar = np.array(list(meta_stuff.keys())) 
    print(Fore.YELLOW+Style.BRIGHT+str(meta_stuff))

    img = Image.open(InFile).convert('RGB')
    img_ar = np.array(img)
    dim = img_ar.shape

    GridSide = int(DimSide)
    h_grids = int(dim[0]/GridSide)
    v_grids = int(dim[1]/GridSide)
    completeGrid = np.zeros((h_grids,v_grids), dtype = np.ndarray)

    v_list = list(range(0, dim[0], GridSide))
    v_list.append(dim[0])
    h_list = list(range(0, dim[1], GridSide))
    h_list.append(dim[1])
    for i in range(3):
        for j in range(3):
            completeGrid[i,j] = img_ar[v_list[i]:v_list[i+1],h_list[j]:h_list[j+1]]
    CheckList = []
    print("\n")
    def process(z):
        if z not in CheckList:
            t1 = time.time()
            Grid_pos = eval(z)
            Grid_ar = completeGrid[Grid_pos[0], Grid_pos[1]]
            byte_depth = meta_stuff[z][0]
            select_px = Grid_ar[:meta_stuff[z][1][0], :meta_stuff[z][1][1]]
            print(Fore.YELLOW+Style.BRIGHT+"ExtractionFile: ", meta_stuff[z][2])
            print(Fore.BLUE+Style.BRIGHT+"Byte_Depth: ", byte_depth)

            def bin_extract(x):
                bin_val = bin(int(x))[2:].zfill(8)
                bin_val = list(bin_val)
                bin_str = "".join(bin_val[-byte_depth:])
                return bin_str
            
            vfunc = np.vectorize(bin_extract)
            decoded_px = vfunc(select_px)

            print(Fore.RED, decoded_px.flatten())
            decoded_bin=decoded_px.flatten().tolist()
            print(Fore.CYAN+Style.BRIGHT+"Extracted Bits: ", len(decoded_bin))
            s="".join(decoded_bin)
            decoded_ar = np.array(list(s))
            decoded_ar = decoded_ar.reshape(int(len(decoded_ar)/6),6)
            decoded_ar = np.array(list(map("".join, decoded_ar)))

            def bin_b64(x,d):
                return d[x]

            vfun = np.vectorize(bin_b64)
            encode_bin = vfun(decoded_ar, b64_rev)
            b64_str="".join(encode_bin).encode("ascii")
            print(Fore.MAGENTA+Style.BRIGHT+"Base64 Chars: ", len(b64_str))

            f = open("Extracted/"+meta_stuff[z][2], "wb")
            decoded_b64 = base64.b64decode(b64_str)
            f.write(decoded_b64)
            t2 = time.time()
            print(Fore.RESET+"ExecTime",t2-t1,"\n\n")
        CheckList.append(z)
    vfunct = np.vectorize(process)
    vfunct(meta_ar)
stegRev(sys.argv[1], sys.argv[2])
t2_ = time.time()
print(Fore.RED+"CompleteExecTime",t2_-t1_,"\n\n"+Fore.RESET)