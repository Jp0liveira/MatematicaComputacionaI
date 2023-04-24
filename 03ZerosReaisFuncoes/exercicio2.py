import math

def bisseccao(f, a, b, eps=1e-6):
    i = 0
    print("Iteração\t a \t\t b \t\t p \t\t f(a) \t f(b) \t f(p) \t sinal")
    while abs(b - a) > eps:
        p = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fp = f(p)
        sinal = "-" if fa * fp < 0 else "+"
        print(f"{i}\t\t {a:.6f} \t {b:.6f} \t {p:.6f} \t {fa:.6f} \t {fb:.6f} \t {fp:.6f} \t {sinal}")
        if fa * fp < 0:
            b = p
        else:
            a = p
        i += 1
    p = (a + b) / 2
    return p, i

def numero_iteracoes(a, b, eps=1e-6):
    return int((math.log(b - a) - math.log(eps)) / math.log(2))

def f(x):
    return x ** 3 - 2 * x ** 2 - 5 * x + 6

a = 1.006
b = 3.008

i = numero_iteracoes(a, b)
print("Número de iterações:", i)

p, it = bisseccao(f, a, b)
print("Raiz aproximada:", p)
print("Número de iterações necessárias:", it)
