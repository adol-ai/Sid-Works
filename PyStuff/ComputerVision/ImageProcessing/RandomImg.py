import pprint
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

data = np.random.randint((255,255,255), size=(254,254,3), dtype=np.uint8)

img = Image.fromarray(data)
img.save("RandomImage.png")
print(len(data))
plt.imshow(data)
plt.show()
