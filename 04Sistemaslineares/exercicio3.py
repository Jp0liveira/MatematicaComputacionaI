def gauss_jacobi(A, b, x0, eps=1e-6, max_iter=1000):
    n = len(A)
    x = x0.copy()

    # Calcula a matriz D e a matriz R
    D = [[A[i][j] if i == j else 0 for j in range(n)] for i in range(n)]
    R = [[A[i][j] if i != j else 0 for j in range(n)] for i in range(n)]

    # Verifica o Critério das Linhas
    alpha = [sum(abs(A[i][j]) for j in range(n) if j != i) / abs(A[i][i]) for i in range(n)]
    if max(alpha) >= 1:
        raise Exception("O método de Gauss-Jacobi não converge.")

    # Realiza as iterações
    for it in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            s = sum(R[i][j] * x[j] for j in range(n))
            x_new[i] = (b[i] - s) / D[i][i]
        if all(abs(x[i] - x_new[i]) < eps for i in range(n)):
            return x_new
        x = x_new

    raise Exception("O número máximo de iterações foi atingido.")

A = [[-8, -1, 5],
     [-24, 1, -1],
     [-16, -2, 6]]
b = [-1, 1, 1]
x0 = [0, 0, 0]

try:
    x = gauss_jacobi(A, b, x0)
    print("Solução:", x)
except Exception as e:
    print(e)
