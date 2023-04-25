def gauss_seidel(A, b, x0, eps=1e-6, max_iter=1000):
    n = len(A)
    x = x0.copy()
    alpha = [0] * n
    for i in range(n):
        alpha[i] = A[i][i] - sum(A[i][j] for j in range(n) if j != i)
        if abs(alpha[i]) >= abs(A[i][i]):
            raise ValueError("O método não é garantidamente convergente.")
    for it in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x_new[j] for j in range(i)) + sum(A[i][j] * x[j] for j in range(i+1, n))
            x_new[i] = (b[i] - s) / A[i][i]
        if all(abs(x[i] - x_new[i]) < eps for i in range(n)):
            return x_new
        x = x_new
    raise ValueError("O método não convergiu em {} iterações.".format(max_iter))

A = [[-8, -1, 5],
     [-24, 1, -1],
     [-16, -2, 6]]
b = [-1, 1, 1]
x0 = [0, 0, 0]

try:
    x = gauss_seidel(A, b, x0)
    print("Solução:", x)
except Exception as e:
    print(e)
