import numpy as np
import matplotlib.pyplot as plt

y0 = 0
yn = 1

x0 = -2
xn = 2

x = np.linspace(x0,xn,61)
y = np.linspace(y0,yn,21)

X,Y = np.meshgrid(x,y)

plt.mesh([X,Y],[0])
plt.show()






















