import numpy as np
import matplotlib.pyplot as plt
def lagrange_interpolation(x, y, xi):
    # Verifica se o número de pontos é igual
    if len(x) != len(y):
        raise ValueError("Os tamanhos de x e y devem ser iguais.")

    n = len(x) - 1  # Grau do polinômio interpolador
    pn_xi = 0  # Valor interpolado para xi

    # Calcula o polinômio interpolador
    for i in range(n+1):
        term = y[i]
        for j in range(n+1):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        pn_xi += term

    return pn_xi

# Pontos da tabela
x = [-1, 0, 2]
y = [4, 1, -1]

# Valor a ser interpolado
xi = 1.5

# Interpolação de Lagrange
result = lagrange_interpolation(x, y, xi)

t  = np.arange(-1.0,2.0,0.1)
yt = []
for i in t:
  yt.append(lagrange_interpolation(x, y, i))

plt.plot(t,yt,'b-')
plt.plot(x,y,'ro')
plt.plot(xi,result,'g*')
plt.show()

# Imprime o valor interpolado
print("Valor interpolado:", result)








