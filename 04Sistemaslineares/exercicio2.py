def lu_factorization(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # Fatoração LU
    for k in range(n):
        L[k][k] = 1.0
        for j in range(k, n):
            s = sum(L[k][i] * U[i][j] for i in range(k))
            U[k][j] = A[k][j] - s
        for i in range(k+1, n):
            s = sum(L[i][j] * U[j][k] for j in range(k))
            L[i][k] = (A[i][k] - s) / U[k][k]

    return L, U


def lu_solve(A, b):
    L, U = lu_factorization(A)
    n = len(A)

    # Resolve Ly = b
    y = [0.0] * n
    for i in range(n):
        s = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - s

    # Resolve Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = (y[i] - s) / U[i][i]

    return x

A = [[-8, -1, 5],
     [-24, 1, -1],
     [-16, -2, 6]]

b = [-1, 1, 1]

x = lu_solve(A, b)
print(x)
