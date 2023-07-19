import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img1 = Image.open("Images/1.jpg").convert("RGB")
img1_ar = np.array(img1)

img2 = Image.open("Images/2.jpg").convert("RGB")
img2_ar = np.array(img2)

img3 = Image.open("Images/3.jpg").convert("RGB")
img3_ar = np.array(img3)

img4 = Image.open("Images/4.jpg").convert("RGB")
img4_ar = np.array(img4)

img5 = Image.open("Images/5.jpg").convert("RGB")
img5_ar = np.array(img5)

img6 = Image.open("Images/6.jpg").convert("RGB")
img6_ar = np.array(img6)

img7 = Image.open("Images/7.jpg").convert("RGB")
img7_ar = np.array(img7)

img8 = Image.open("Images/8.jpg").convert("RGB")
img8_ar = np.array(img8)

img9 = Image.open("Images/9.jpg").convert("RGB")
img9_ar = np.array(img9)

completeGrid = np.zeros((3,3), dtype = np.ndarray)
print(completeGrid)

completeGrid[0,0]=img1_ar
completeGrid[0,1]=img2_ar
completeGrid[0,2]=img3_ar
completeGrid[1,0]=img4_ar
completeGrid[1,1]=img5_ar
completeGrid[1,2]=img6_ar
completeGrid[2,0]=img7_ar
completeGrid[2,1]=img8_ar
completeGrid[2,2]=img9_ar

patchedGrid = np.vstack((np.hstack(completeGrid[0]), np.hstack(completeGrid[1]), np.hstack(completeGrid[2])))
print(patchedGrid.shape)

finalImg = Image.fromarray(patchedGrid)
finalImg.save("PatchedImg.png")

plt.imshow(patchedGrid)
plt.show()

