import numpy as np
import matplotlib.pyplot as plt
def divided_differences(x, y):
    # Verifica se o número de pontos é igual
    if len(x) != len(y):
        raise ValueError("Os tamanhos de x e y devem ser iguais.")

    n = len(x) - 1  # Grau do polinômio interpolador
    f = [[0.0] * (n+1) for _ in range(n+1)]  # Tabela de diferenças divididas

    for i in range(n+1):
        f[i][0] = y[i]  # Preenche a primeira coluna com os valores de y

    for j in range(1, n+1):
        for i in range(n+1-j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])

    return f

def newton_interpolation(x, y, xi):
    # Verifica se o número de pontos é igual
    if len(x) != len(y):
        raise ValueError("Os tamanhos de x e y devem ser iguais.")

    n = len(x) - 1  # Grau do polinômio interpolador
    f = divided_differences(x, y)  # Tabela de diferenças divididas
    pn_xi = f[0][0]  # Valor interpolado para xi

    for i in range(1, n+1):
        term = f[0][i]  # Termo do polinômio de Newton
        for j in range(i):
            term *= (xi - x[j])
        pn_xi += term

    return pn_xi

# Pontos da tabela
x = [-1, 0, 2]
y = [4, 1, -1]

# Valor de xi para interpolação
xi = 1.5

# Interpolação usando o método de Newton
result = newton_interpolation(x, y, xi)

t  = np.arange(-1.0,2.0,0.1)
yt = []
for i in t:
  yt.append(newton_interpolation(x, y, i))

plt.plot(t,yt,'b-')
plt.plot(x,y,'ro')
plt.plot(xi,result,'g*')
plt.show()

# Imprime o valor interpolado
print("Valor interpolado para xi =", xi, ":", result)