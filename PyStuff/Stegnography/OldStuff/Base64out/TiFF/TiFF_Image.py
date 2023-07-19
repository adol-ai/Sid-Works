import time
import math
import base64
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


img = Image.open("qwert.tiff").convert('RGB')
img_ar = np.array(img)

print(img_ar.shape)
