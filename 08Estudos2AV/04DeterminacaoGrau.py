import pandas as pd
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


x = [1, 1.01, 1.02]
y = [1, 1.005, 1.01]
xp = 1.007
grau = 1
yp = interpNewton(x, y, xp, grau)
t = np.arange(1.0, 1.02, 0.01)
yt = []
for i in t:
    yt.append(interpNewton(x, y, i, grau))
plt.plot(t, yt, 'b-')
plt.plot(x, y, 'ro')
plt.plot(xp, yp, 'g*')
plt.grid()
plt.show()