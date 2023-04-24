def gauss_elimination(A, b):
    n = len(A)

    # Fase de eliminação
    for i in range(n):
        # Pivô
        pivot = A[i][i]
        if pivot == 0:
            return "Não é possível dividir por zero. O sistema não possui solução única."
        for j in range(i + 1, n):
            ratio = A[j][i] / pivot
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]

    # Verifica se o sistema possui solução única
    for i in range(n):
        if A[i][i] == 0 and b[i] != 0:
            return "O sistema não possui solução única."

    # Fase de substituição
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] = b[j] - A[j][i] * x[i]

    return x

A = [[-8, -1, 5],
     [-24, 1, -1],
     [-16, -2, 6]]

b = [-1, 1, 1]

x = gauss_elimination(A, b)

print(x)
