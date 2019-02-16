import numpy as np
import sympy as sy
from sympy.functions import sin,cos
import matplotlib.pyplot as plt

x = sy.Symbol('x')
f = sin(x)

def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)

def Taylor(function,n,x0):
    i = 0
    s = 0
    while i<=n:
        s = s + (function.diff(x,i).subs(x,x0))*((x-x0)**i)/factorial(i)
        i +=1
    return s

x_max = 4*np.pi
x_min = -4*np.pi

x1 = np.linspace(x_min,x_max,500)
y1 = []
terms = [1,2,4,8,16]
terms2 = [2*i for i in terms]

plt.plot(x1,np.sin(x1),label='Sin(x)')

for j in terms2:
    func = Taylor(f,j,0)
    print('Taylor Expansion with '+str(int(j/2))+' terms',func)

    for k in x1:
        y1.append(func.subs(x,k))
    plt.plot(x1,y1,label=str(int(j/2))+' terms')
    y1 = []

plt.xlim([x_min,x_max])
plt.ylim([-4,4])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Taylor Series Approximation')
plt.show()

