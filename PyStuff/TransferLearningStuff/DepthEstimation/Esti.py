from transformers import DPTImageProcessor, DPTForDepthEstimation
from colorama import Fore, Style
from PIL import Image
import numpy as np
import torch
import tqdm
import glob
import time

t1 = time.time()
x = glob.glob("Images/*.jpg")
pbar = tqdm.tqdm(total=len(x), colour="red")
for i in x:
    if "Depth." not in i:
        t1_ = time.time()
        img  = Image.open(i)
        processor = DPTImageProcessor.from_pretrained("Intel/dpt-large")
        model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

        inputs = processor(images=img, return_tensors="pt")
        with torch.no_grad():
            output = model(**inputs)
            predicted_depth = output.predicted_depth

        prediction = torch.nn.functional.interpolate(
            predicted_depth.unsqueeze(1),
            size = img.size[::-1],
            mode = "bicubic",
            align_corners = False
        )

        output = prediction.squeeze().cpu().numpy()
        out_img = (output * 255 / np.max(output)).astype("uint8")
        depth = Image.fromarray(out_img)

        z = i.split(".")
        z = 'Depth.'.join(z)
        depth.save(z)
        t2_ = time.time()
        pbar.update(1)
print("\n" + Fore.WHITE + Style.BRIGHT + z + " ExecTime:" + str(t2_-t1_) + Fore.RESET)
t2 = time.time()

pbar.close()
print("\nCompleteExecTime: ", (t2-t1))cd 