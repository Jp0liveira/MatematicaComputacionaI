def newton_raphson(f, df, x0, epsilon=1e-6, max_iter=1000):
    xn = x0
    print("Iteração\t\tXn\t\t\tf(Xn)\t\t\tf'(Xn)")
    print("-------------------------------------------------------------------")
    for n in range(0, max_iter):
        fxn = f(xn)
        Dfxn = df(xn)
        print("%d\t\t\t%.8f\t\t%.8f\t\t%.8f" % (n, xn, fxn, Dfxn))
        if abs(fxn) < epsilon:
            print('\nRaiz encontrada: %f' % xn)
            return xn
        if Dfxn == 0:
            print('Derivada zero. Não é possível continuar.')
            return None
        xn = xn - fxn / Dfxn
    print('Número máximo de iterações excedido.')
    return None

def f(x):
    return x**3 - 2*x**2 - 5*x + 6

#encontar a derivada
def diff(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

#derivada da f(x)
def df(x):
    return diff(f, x)

newton_raphson(f, df, 3)
