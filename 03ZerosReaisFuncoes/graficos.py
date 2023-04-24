import numpy as np
import matplotlib.pyplot as plt
import exercicio1
import exercicio2

def f(x):
    return x**3 - 2*x**2 - 5*x + 6

x = np.linspace(-5, 5, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(y=0, color='black', linestyle='-')
plt.show()
    
exercicio1.tabelaSinais_import(f, -5, 5)

a = 1.006
b = 3.008

p, it = exercicio2.bisseccao(f, a, b)

print("Raiz aproximada:", p)
print("Número de iterações necessárias:", it)
