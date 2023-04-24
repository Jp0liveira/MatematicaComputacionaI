import math
def exp_taylor(x, n, toler=1e-10):
    # Se x for negativo, invertemos o sinal e calculamos 1/𝑒^𝑥
    if x < 0:
        return 1 / exp_taylor(-x, n, toler)

    # Inicializa a soma como zero
    soma = 0

    # Calcula a série de Taylor
    for i in range(n):
        termo = x ** i / math.factorial(i)
        if termo < toler:
            break
        soma += termo

    # Retorna o valor aproximado da exponencial
    return soma

print(exp_taylor(1, 10))

def exp_taylor_overflow(x, n, toler=1e-10):
    res = 0
    k = 0
    t = 1
    while abs(t) > toler:
        res += t
        k += 1
        # calcula o fatorial utilizando o algoritmo da divisão dupla
        fact = 1
        if k > 1:
            for i in range(2, k+1, 2):
                fact *= i * (i-1)
            if k % 2 == 1:
                fact *= k
        t = (x**k) / fact
        if k >= n:
            break
    return res

print(exp_taylor_overflow(1, 10))