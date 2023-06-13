import numpy as np
import matplotlib.pyplot as plt

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


x = [-1.0, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1.0]
y = [36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246]
ly = np.log(y)
A, b = sistemaAumentado(x, ly, 2)
print("A = ", A)
print("b = ", b)
coef = np.linalg.solve(A, b)
print("coef = ", coef)

def p(coef,x):
  y = np.exp(coef[0])*np.exp(coef[1]*x)
  return y

plt.plot(x,y,'ro')
data=np.linspace(min(x),max(x),100)
plt.plot(data,p(coef,data),'b-')
plt.grid()
plt.show()