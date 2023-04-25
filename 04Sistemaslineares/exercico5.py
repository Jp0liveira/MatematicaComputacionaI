import numpy as np

def newton_raphson_system(F, J, x0, epsilon=1e-6, max_iter=1000):
    xn = np.array(x0)
    print("Iteração\t\tXn\t\t\t\tF(Xn)")
    print("-------------------------------------------------------------------")
    for n in range(0, max_iter):
        Fxn = np.array(F(xn))
        Jxn = np.array(J(xn))
        print("%d\t\t\t%s\t\t%s" % (n, str(xn), str(Fxn)))
        if np.linalg.norm(Fxn) < epsilon:
            print('\nSolução encontrada:', xn)
            return xn
        delta_xn = np.linalg.solve(Jxn, -Fxn)
        xn = xn + delta_xn
    print('Número máximo de iterações excedido.')
    return None
def F(x):
    return [x[0]**2 + x[1]**2 + x[2]**2 - 25,
            x[0]*x[1] - 8,
            x[2]*x[0] - 6]

def J(x):
    return [[2*x[0], 2*x[1], 2*x[2]],
            [x[1], x[0], 0],
            [x[2], 0, x[0]]]

newton_raphson_system(F, J, [1, 2, 3])
