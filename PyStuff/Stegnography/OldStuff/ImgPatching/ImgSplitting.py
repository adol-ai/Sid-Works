import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

GridSide = 1024

img = np.array(Image.open("PatchedImg.png"))
dim = img.shape
print(dim)

h_grids = int(dim[0]/GridSide)
v_grids = int(dim[1]/GridSide)
completeGrid = np.zeros((h_grids,v_grids), dtype = np.ndarray)
print(completeGrid)

v_l = list(range(0, dim[0], GridSide))
v_l.append(dim[0])
h_l = list(range(0, dim[1], GridSide))
h_l.append(dim[1])

print(v_l, h_l)

for i in range(3):
    for j in range(3):
        completeGrid[i][j] = img[v_l[i]:v_l[i+1],h_l[j]:h_l[j+1]]
        plt.imshow(img[v_l[i]:v_l[i+1],h_l[j]:h_l[j+1]])
        plt.show()

p = completeGrid[0][0]
print(p.shape)
plt.imshow(p)
plt.show()                         
