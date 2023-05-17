#Implementar dois algoritmos de interpolação, sendo um deles pela forma de Newton.
def newton_interpolation(x, y, xi):
    """
    x  : lista de valores de x
    y  : lista de valores de y
    xi : ponto a ser interpolado
    """
    n = len(x)
    fdd = [[None for _ in range(n)] for _ in range(n)]
    y = x[:]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    ans = fdd[0][0]
    xterm = 1
    for j in range(1, n):
        xterm *= (xi - x[j - 1])
        ans += (fdd[0][j] * xterm)

    return ans

def linear_interpolation(x, y, xi):
    """
    x  : lista de valores de x
    y  : lista de valores de y
    xi : ponto a ser interpolado
    """
    if xi in x:
        return y[x.index(xi)]
    else:
        for i in range(len(x) - 1):
            if x[i] < xi < x[i+1]:
                m = (y[i+1] - y[i]) / (x[i+1] - x[i])
                return y[i] + m * (xi - x[i])

#Escolha 2 funções polinomiais de graus entre 10 e 20 e obtenha o polinômio interpolador dessas
# 3 funções para 5, 8 e 10 pontos na tabela.
import numpy as np

# Definição das funções
def f(x):
    return x**10

def g(x):
    return x**20

# Pontos de interpolação
x_5 = np.linspace(0, 1, 5)
x_8 = np.linspace(0, 1, 8)
x_10 = np.linspace(0, 1, 10)

# Calculando os valores de y para cada função e conjunto de pontos
y_f_5 = f(x_5)
y_f_8 = f(x_8)
y_f_10 = f(x_10)

y_g_5 = g(x_5)
y_g_8 = g(x_8)
y_g_10 = g(x_10)

# Interpolando
y_inter_f_5 = newton_interpolation(x_5, y_f_5, x_5)
y_inter_f_8 = newton_interpolation(x_8, y_f_8, x_8)
y_inter_f_10 = newton_interpolation(x_10, y_f_10, x_10)
print(y_inter_f_5)
print(y_inter_f_8)
print(y_inter_f_10)

y_inter_g_5 = newton_interpolation(x_5, y_g_5, x_5)
y_inter_g_8 = newton_interpolation(x_8, y_g_8, x_8)
y_inter_g_10 = newton_interpolation(x_10, y_g_10, x_10)
print(y_inter_g_5)
print(y_inter_g_8)
print(y_inter_g_10)


#Para 10 pontos igualmente espaçados use a função Spline quadrática e
# compare com a interpolação de 10 pontos acima.
from scipy.interpolate import interp1d

# Definição dos pontos
x_points = np.linspace(0, 1, 10)

# Calculando os valores de y para cada função
y_f_points = f(x_points)
y_g_points = g(x_points)

# Definição das funções de interpolação spline quadrática
spline_quad_f = interp1d(x_points, y_f_points, kind='quadratic')
spline_quad_g = interp1d(x_points, y_g_points, kind='quadratic')

# Agora, você pode usar estas funções para calcular os valores interpolados:
y_inter_spline_f = spline_quad_f(x_points)
y_inter_spline_g = spline_quad_g(x_points)


import matplotlib.pyplot as plt

# Plot f(x)
plt.figure(figsize=(12, 6))
plt.plot(x_points, y_f_points, 'o', label='Original data', markersize=10)
plt.plot(x_points, y_inter_f_10, 'r', label='Newton interpolation')
plt.plot(x_points, y_inter_spline_f, 'b', label='Quadratic spline')
plt.legend()
plt.title('Interpolation comparison for f(x) = x^10')
plt.show()

# Plot g(x)
plt.figure(figsize=(12, 6))
plt.plot(x_points, y_g_points, 'o', label='Original data', markersize=10)
plt.plot(x_points, y_inter_g_10, 'r', label='Newton interpolation')
plt.plot(x_points, y_inter_spline_g, 'b', label='Quadratic spline')
plt.legend()
plt.title('Interpolation comparison for g(x) = x^20')
plt.show()


#Escolha 20 pontos aleatórios dentro do intervalo tabelado, mas diferente dos
#valores na tabela, e compare o valor da interpolação com o valor da função original.
# Gerando 20 pontos aleatórios

x_random = np.sort(np.random.uniform(0, 1, 20))

# Calculando os valores das funções originais
y_f_random = f(x_random)
y_g_random = g(x_random)

# Calculando os valores interpolados
y_inter_f_newton_random = newton_interpolation(x_points, y_f_points, x_random)
y_inter_g_newton_random = newton_interpolation(x_points, y_g_points, x_random)

y_inter_f_spline_random = spline_quad_f(x_random)
y_inter_g_spline_random = spline_quad_g(x_random)

# Comparando os valores
for i in range(20):
    print(f'x = {x_random[i]}')
    print(f'Original f(x) = {y_f_random[i]}, Newton interpolation = {y_inter_f_newton_random[i]}, Quadratic spline = {y_inter_f_spline_random[i]}')
    print(f'Original g(x) = {y_g_random[i]}, Newton interpolation = {y_inter_g_newton_random[i]}, Quadratic spline = {y_inter_g_spline_random[i]}')
    print('---')


# Plot f(x)
plt.figure(figsize=(12, 6))
plt.plot(x_random, y_f_random, 'o', label='Original data', markersize=10)
plt.plot(x_random, y_inter_f_newton_random, 'r', label='Newton interpolation')
plt.plot(x_random, y_inter_f_spline_random, 'b', label='Quadratic spline')
plt.legend()
plt.title('Interpolation comparison for f(x) = x^10 with random points')
plt.show()

# Plot g(x)
plt.figure(figsize=(12, 6))
plt.plot(x_random, y_g_random, 'o', label='Original data', markersize=10)
plt.plot(x_random, y_inter_g_newton_random, 'r', label='Newton interpolation')
plt.plot(x_random, y_inter_g_spline_random, 'b', label='Quadratic spline')
plt.legend()
plt.title('Interpolation comparison for g(x) = x^20 with random points')
plt.show()