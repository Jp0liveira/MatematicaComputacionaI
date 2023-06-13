def solve_linear_system(x, y):
    # Verifica se o número de pontos é igual
    if len(x) != len(y):
        raise ValueError("Os tamanhos de x e y devem ser iguais.")

    n = len(x) - 1  # Grau do polinômio interpolador
    A = []  # Coeficientes das variáveis do sistema linear
    b = []  # Valores do lado direito do sistema

    # Constrói a matriz A e o vetor b do sistema linear
    for i in range(n+1):
        row = []
        for j in range(n+1):
            row.append(x[i] ** j)
        A.append(row)
        b.append(y[i])

    # Resolve o sistema linear
    for i in range(n+1):
        # Pivotação parcial
        max_row = i
        for j in range(i+1, n+1):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Eliminação gaussiana
        for j in range(i+1, n+1):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]

    # Retrosubstituição
    coefficients = [0] * (n+1)
    for i in range(n, -1, -1):
        for j in range(i+1, n+1):
            b[i] -= A[i][j] * coefficients[j]
        coefficients[i] = b[i] / A[i][i]

    return coefficients

# Pontos da tabela
x = [-1, 0, 2]
y = [4, 1, -1]

# Resolução do sistema linear
coefficients = solve_linear_system(x, y)

# Coeficientes do polinômio interpolador
a, b, c = coefficients

# Imprime o polinômio interpolador
print("Polinômio interpolador: f(x) = {:.4} + {:.4}x + {:.4}x^2".format(a, b, c))


'''
Exemplo

    # Pontos da tabela
x = [-2, -1, 0, 1, 2, 3]
y = [5, 2, 1, 2, 7, 16]

# Resolução do sistema linear
coefficients = solve_linear_system(x, y)

# Coeficientes do polinômio interpolador
a, b, c, d, e, f = coefficients

# Imprime o polinômio interpolador
print("Polinômio interpolador: f(x) =", a, "* x^5 +", b, "* x^4 +", c, "* x^3 +", d, "* x^2 +", e, "* x +", f)

'''
