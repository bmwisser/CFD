import numpy as np
import matplotlib.pyplot as plt

count = 0

#Pick N to be odd
NN = [5,25]
for i in NN:
    count += 1
    N = i

    L = 1
    V = 1

    u = np.zeros(N)

    dy = (L-u[0])/(N-1)

    y = np.zeros(N)
    for i in range(0,N):
        y[i] = y[0] + (i)*dy

    u_actual = np.zeros(N)
    if count > 1:
        for i in range(0,N):
            u_actual[i] = (4 * (1 - y[i])*y[i])
        #plt.plot(u_actual, y, 'r', label='Actual Solution')

    tol = 1e-6
    iter = 0
    iter_max = 5000
    iflag = 1
    u_mid_old = u[int((N + 1) / 2)]  # ; print(u_mid_old)


    while iflag == 1 and iter < iter_max:

        iter += 1

        for i in range(1,N-1):

            u[i] = 0.5*((8*V/L**2)*dy**2 + u[i-1] + u[i+1])

        error = abs(u[int((N+1)/2)] - u_mid_old)

        if error < tol:
            iflag = 0
        else:
            u_mid_old = u[int((N + 1) / 2)]

    print(u)

    plt.plot(u,y,'-o', label='N = ' + str(N))

    if count > 1:
        plt.plot(u_actual, y, 'r', label='Actual Solution')

plt.xlim([0,1.3])
plt.ylim([0,1])
plt.xlabel('u(y)')
plt.ylabel('Height')
plt.legend()
plt.grid(True)
plt.title('Poiseuille flow solution for u(y)')
plt.show()