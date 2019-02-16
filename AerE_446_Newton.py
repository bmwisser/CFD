import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5,1.5,100)

plt.plot(x, np.exp(x), label='y = e^(x)')
plt.plot(x, 2-x, label='y = 2 - x')

plt.xlim([x[0],x[-1]])
plt.ylim([-1,6])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Solution of 2 - x = e^(x)')
plt.show()

iter_max = 1000
k = 0

x0 = 0.5

tol = 1e-8
iflag = 1

while (iflag == 1) and (k < iter_max):
    k += 1
    iflag = 0

    f = 2 - np.exp(x0)-x0
    fp = -np.exp(x0)-1

    xn = x0 - f/fp

    print(k-1, x0)

    error = abs(xn-x0)
    if error > tol:
        iflag = 1
        x0 = xn

