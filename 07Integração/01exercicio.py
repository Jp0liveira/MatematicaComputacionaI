import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Função polinomial: f(x) = 2x^3 - 5x^2 + 3x - 1
def polynomial_function(x):
    return 2 * x**3 - 5 * x**2 + 3 * x - 1

# Função exponencial: g(x) = 3e^x
def exponential_function(x):
    return 3 * math.exp(x)

# Função senoidal: h(x) = 2sin(x)
def sine_function(x):
    return 2 * math.sin(x)

# Função para calcular a integral numérica usando a regra dos trapézios
def numerical_integration_trapezios(f, a, b, n):
    h = (b - a) / n  # Tamanho do intervalo
    integral_sum = f(a) + f(b)  # Soma das extremidades do intervalo

    for i in range(1, n):
        x = a + i * h
        integral_sum += 2 * f(x)  # Soma dos pontos internos multiplicados por 2

    integral = (h / 2) * integral_sum
    return integral


# Função para calcular a integral numérica usando a regra 1/3 de Simpson
def numerical_integration_simpson(f, a, b, n):
    h = (b - a) / n  # Tamanho do intervalo
    integral_sum = f(a) + f(b)  # Soma das extremidades do intervalo

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            integral_sum += 2 * f(x)  # Soma dos pontos pares multiplicados por 2
        else:
            integral_sum += 4 * f(x)  # Soma dos pontos ímpares multiplicados por 4

    integral = (h / 3) * integral_sum
    return integral


# Intervalo de integração
a = 0
b = 1

# Número de pontos para trapezios
n = 5

# Número de pontos para simpson
p = 6


# Calculando a integral numérica das três funções por trapezios
polynomial_integral_trapezios = numerical_integration_trapezios(polynomial_function, a, b, n)
exponential_integral_trapezios = numerical_integration_trapezios(exponential_function, a, b, n)
sine_integral_trapezios = numerical_integration_trapezios(sine_function, a, b, n)

# Imprimindo os resultados
print("\nIntegral da função polinomial: ", polynomial_integral_trapezios)
print("Integral da função exponencial: ", exponential_integral_trapezios)
print("Integral da função senoidal: ", sine_integral_trapezios)

# Calculando a integral numérica das três funções por simpsom
polynomial_integral_simpson = numerical_integration_simpson(polynomial_function, a, b, p)
exponential_integral_simpson = numerical_integration_simpson(exponential_function, a, b, p)
sine_integral_simpson = numerical_integration_simpson(sine_function, a, b, p)

# Imprimindo os resultados
print("\nIntegral da função polinomial: ", polynomial_integral_simpson)
print("Integral da função exponencial: ", exponential_integral_simpson)
print("Integral da função senoidal: ", sine_integral_simpson)

# Pontos fornecidos
x_points = [0, 0.2, 0.4, 0.6, 0.8]
y_points = [2.3, 3.1, 2.7, 1.8, 1.2]

# Grau do polinômio para ajuste
degree = 3

# Ajuste de curva polinomial
coefficients = np.polyfit(x_points, y_points, degree)

# Função polinomial ajustada
def fitted_function(x):
    return np.polyval(coefficients, x)

# Intervalo para o gráfico
x_range = np.linspace(0, 1, 100)
y_range = fitted_function(x_range)

# Cálculo da integral aproximada usando a curva ajustada
def approximate_integral(a, b):
    integral, error = quad(fitted_function, a, b)
    return integral

# Exemplo de cálculo da integral aproximada em qualquer ponto
integral_approximation = approximate_integral(0.1, 0.9)

# Plot do gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x_points, y_points, color='red', label='Pontos Originais')
plt.plot(x_range, y_range, color='blue', label='Curva Ajustada')
plt.fill_between(x_range, y_range, color='lightblue', alpha=0.5, label='Área Sob a Curva')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste de Curva e Integral Aproximada')
plt.legend()
plt.grid(True)
plt.show()

# Imprimindo o resultado da integral aproximada
print("Integral aproximada: ", integral_approximation)