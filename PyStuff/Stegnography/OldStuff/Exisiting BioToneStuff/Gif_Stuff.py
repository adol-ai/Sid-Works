import glob
import cv2
import numpy as np
from PIL import Image

l = glob.glob('GIF_frames/*.png')
print(l)

for i in l:
    try:
        img = cv2.imread(i)
        print(img.shape)
        dim = img.shape
        ratio = max(dim)//512
        print(np.shape(img))
        img_=cv2.resize(img, dsize=(dim[1]//ratio, dim[0]//ratio), interpolation=cv2.INTER_AREA)
        print(np.shape(img_))
        cv2.imwrite(i, img_)
        print("---->"+i)
    except:
        pass

frames = [Image.open(x) for x in l]
gif = frames[0]    
gif.save("InGif.gif", format="gif", append_images=frames, save_all=True, duration=200, loop=0)

