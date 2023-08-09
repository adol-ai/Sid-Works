import time
import tqdm
import torch
from diffusers import DiffusionPipeline
from diffusers import StableDiffusionPipeline


#prompt = str(input("Prompt Here: "))
prompt = 'statue of greek man draped in persian blue silk with gold aztec symbols on it'
#pipe = StableDiffusionPipeline.from_pretrained("prompthero/openjourney-v4")
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe = pipe.to("cuda")

def disabled_safety_checker(images, clip_input):
    if len(images.shape)==4:
        num_images = images.shape[0]
        return images, [False]*num_images
    else:
        return images, False
pipe.safety_checker = disabled_safety_checker

t1 = time.time()
for i in tqdm.trange(10, colour="red"):
    img = pipe(prompt).images[0]
    img.save("L:\Sid-Works\PyStuff\TransferLearningStuff\StableDiffusion\Images\{}.png".format(time.time()))
t2 = time.time()

print("\nCompleteExecTime: ", (t2-t1))