import numpy as np


def sistemaAumentado(x, y, dim):
    m = len(x)
    A = np.empty((dim, dim))
    b = np.empty((dim))
    soma = []
    for i in range(0, dim + 2):
        aux = 0
        for k in range(0, m):
            aux = aux + x[k] ** i
        soma.append(aux)

    for i in range(0, dim):
        for j in range(i, dim):
            A[i, j] = soma[i + j]
            if (i != j):
                A[j, i] = A[i, j]

    b = []
    for i in range(0, dim):
        aux = 0
        for k in range(0, m):
            aux = aux + y[k] * (x[k] ** (i))
        b.append(aux)

    return A, b


x = [-1.0, -0.75, -0.6, -0.5, -0.3, 0, 0.2, 0.4, 0.5, 0.7, 1]
y = [2.05, 1.153, 0.45, 0.4, 0.5, 0, 0.2, 0.6, 0.512, 1.2, 2.05]
A, b = sistemaAumentado(x, y, 3)
print("A = ", A)
print("b = ", b)
coef = np.linalg.solve(A, b)
print("coef = ", coef)