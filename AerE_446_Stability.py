import matplotlib.pyplot as plt

lam1 = 1/8
lam2 = 1/2

dx = []
x0_lam1 = -0.5
x0_lam2 = 0.25

x1_lam1 = x0_lam1; x2_lam1 = x0_lam1; x3_lam1 = x0_lam1
x1_lam2 = x0_lam2; x2_lam2 = x0_lam2; x3_lam2 = x0_lam2

iter = 0
g1x1 = []; g2x1 = []; g3x1 = []
g1x2 = []; g2x2 = []; g3x2 = []
while iter <= 15:
    dx.append(iter)
    iter += 1;

    g1_x1 = 4*lam1*x1_lam1*(1 - x1_lam1); g1x1.append(g1_x1)
    g2_x1 = x2_lam1/(4*lam1*(1 - x2_lam1)); g2x1.append(g2_x1)
    g3_x1 = -(4*lam1*x3_lam1**2)/(1 - 4*lam1); g3x1.append(g3_x1)

    g1_x2 = 4 * lam2 * x1_lam2 * (1 - x1_lam2); g1x2.append(g1_x2)
    g2_x2 = x2_lam2 / (4 * lam2 * (1 - x2_lam2)); g2x2.append(g2_x2)
    g3_x2 = -(4 * lam2 * x3_lam2 ** 2) / (1 - 4 * lam2); g3x2.append(g3_x2)

    x1_lam1 = g1_x1
    x2_lam1 = g2_x1
    x3_lam1 = g3_x1

    x1_lam2 = g1_x2
    x2_lam2 = g2_x2
    x3_lam2 = g3_x2


plt.figure(1)
plt.scatter(dx, g1x1, label='Method 1')
plt.scatter(dx, g2x1, label='Method 2')
plt.scatter(dx, g3x1, label='Method 3')

plt.figure(2)
plt.scatter(dx, g1x2, label='Method 1')
plt.scatter(dx, g2x2, label='Method 2')
plt.scatter(dx, g3x2, label='Method 3')


plt.figure(1)
plt.xlim([0,15])
plt.ylim([-1.5,0.5])
plt.xlabel('n')
plt.ylabel('X^n')
plt.legend()
plt.grid(True)
plt.title('Stability Analysis for \u03BB = 1/8')

plt.figure(2)
plt.xlim([0,15])
plt.ylim([-0.2,0.7])
plt.xlabel('n')
plt.ylabel('X^n')
plt.legend()
plt.grid(True)
plt.title('Stability Analysis for \u03BB = 1/2')
plt.show()

