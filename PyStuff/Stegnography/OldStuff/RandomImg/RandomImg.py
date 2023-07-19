import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

np.random.seed(42)
ar = np.random.randint(255,size=(1024,1024,3)).astype(np.uint8)

print(ar)

img = Image.fromarray(ar)
print(img)
plt.imshow(ar)
plt.show()

img.save("RandImg.png")
