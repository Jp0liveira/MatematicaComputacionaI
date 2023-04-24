import numpy as np
def tabelaSinais_import(f, a=-10, b=10, num_pontos=1000):
    x_vals = []
    sinal_f_vals = []
    dx = (b - a) / (num_pontos - 1)

    for i in range(num_pontos):
        x = a + i * dx
        x_vals.append(x)
        sinal_f = 1 if f(x) >= 0 else -1
        sinal_f_vals.append(sinal_f)

    mudancas_sinais = []
    for i in range(1, num_pontos):
        if sinal_f_vals[i] != sinal_f_vals[i-1]:
            mudancas_sinais.append(i)

    print("Tabela de Sinais de f(x)")
    print("--------------------------")
    print("|\tx\t|\tsinal de f(x)|")
    print("--------------------------")

    for i in mudancas_sinais:
        print(" |\t{:.3f}\t|\t{:2.0f}\t\t|".format(x_vals[i], sinal_f_vals[i]))

    print("--------------------------")

# Exemplo de uso
def f(x):
    return x ** 3 - 2 * x ** 2 - 5 * x + 6 * np.log(x)
