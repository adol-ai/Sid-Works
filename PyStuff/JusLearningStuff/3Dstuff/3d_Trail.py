import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

'''
x = np.random.randint(100, size = 100)
y = np.random.randint(100, size = 100)
z = np.random.randint(100, size = 100)

ax.scatter(x,y,z)
plt.show()'''

X = np.arange(-5, 8, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z, cmap=cm.coolwarm, antialiased=False)
plt.show()
