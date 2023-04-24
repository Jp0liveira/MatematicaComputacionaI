def secant_method(f, x0, x1, epsilon=1e-6, max_iter=1000):
    print(f'{"n":<5}{"x0":<15}{"x1":<15}{"f(x0)":<15}{"f(x1)":<15}{"x2":<15}{"f(x2)":<15}')
    print('-' * 90)
    for n in range(0, max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < epsilon:
            print(f'{n:<5}{x0:<15.8f}{x1:<15.8f}{fx0:<15.8f}{fx1:<15.8f}{x1:<15.8f}{fx1:<15.8f}')
            print(f'Raiz encontrada: {x1}')
            return x1
        if abs(fx0) < epsilon:
            print(f'{n:<5}{x0:<15.8f}{x1:<15.8f}{fx0:<15.8f}{fx1:<15.8f}{x0:<15.8f}{fx0:<15.8f}')
            print(f'Raiz encontrada: {x0}')
            return x0
        x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
        fx2 = f(x2)
        print(f'{n:<5}{x0:<15.8f}{x1:<15.8f}{fx0:<15.8f}{fx1:<15.8f}{x2:<15.8f}{fx2:<15.8f}')
        x0 = x1
        x1 = x2
    print('Número máximo de iterações excedido.')
    return None


def f(x):
    return x ** 3 - 2 * x ** 2 - 5 * x + 6


a = 1.006
b = 3.008

secant_method(f, a, b)
