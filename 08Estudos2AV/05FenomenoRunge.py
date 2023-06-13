import numpy as np
import matplotlib.pyplot as plt


def interpNewton(x, y, xi, grau):
    n = len(x)
    fdd = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    # fdd_table = pd.DataFrame(fdd)
    # print(fdd_table)
    xterm = 1
    yint = fdd[0][0]
    for order in range(1, grau + 1):
        xterm = xterm * (xi - x[order - 1])
        yint = yint + fdd[0][order] * xterm

    return yint


def runge(x):
    return 1 / (1 + 25 * x ** 2)


def cheby_nodes(x0, x1, n):
    return (x1 - x0) * (np.cos((2 * np.arange(1, n + 1) - 1) / (2 * n) * np.pi) + 1) / 2 + x0


x0 = -1
x1 = 1
x = np.linspace(x0, x1, 500)
t1 = np.linspace(x0, x1, 11)
t2 = cheby_nodes(x0, x1, 11)

plt.plot(x, runge(x), 'y-')
plt.plot(t1, runge(t1), 'bo', label='Igual')
plt.plot(t2, runge(t2), 'ro', label='Cheby')
yt2 = []
for i in x:
    # yt2.append(interpNewton(t1,runge(t1),i,10))
    yt2.append(interpNewton(t2, runge(t2), i, 10))
plt.plot(x, yt2, 'g-')
plt.legend()
plt.show()