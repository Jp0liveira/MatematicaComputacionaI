import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Conjunto de dados 1 - Modelo linear
np.random.seed(0)
X1 = np.linspace(-10, 10, 100)
Y1 = 3*X1 + 2 + np.random.normal(0, 1, size=X1.shape)

# Conjunto de dados 2 - Modelo polinomial
X2 = np.linspace(-10, 10, 100)
Y2 = 0.5*X2**2 + 2*X2 + 1 + np.random.normal(0, 1, size=X2.shape)

# Conjunto de dados 3 - Modelo não polinomial
X3 = np.linspace(0, 2*np.pi, 100)
Y3 = np.sin(X3) + np.random.normal(0, 0.1, size=X3.shape)

# Ajuste linear
def linear_func(x, a, b):
    return a*x + b

# Ajuste polinomial
def poly_func(x, a, b, c):
    return a*x**2 + b*x + c

# Ajuste não linear
def sin_func(x, a, b):
    return a * np.sin(b*x)

# Ajustando e plotando para o conjunto de dados 1
popt1, _ = curve_fit(linear_func, X1, Y1)
plt.scatter(X1, Y1, label='Dados originais')
plt.plot(X1, linear_func(X1, *popt1), 'r-', label='Ajuste linear: a=%5.3f, b=%5.3f' % tuple(popt1))
plt.legend()
plt.show()

# Ajustando e plotando para o conjunto de dados 2
popt2, _ = curve_fit(poly_func, X2, Y2)
plt.scatter(X2, Y2, label='Dados originais')
plt.plot(X2, poly_func(X2, *popt2), 'r-', label='Ajuste polinomial: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt2))
plt.legend()
plt.show()

# Ajustando e plotando para o conjunto de dados 3
popt3, _ = curve_fit(sin_func, X3, Y3, p0=[1, 1])
plt.scatter(X3, Y3, label='Dados originais')
plt.plot(X3, sin_func(X3, *popt3), 'r-', label='Ajuste não linear: a=%5.3f, b=%5.3f' % tuple(popt3))
plt.legend()
plt.show()
