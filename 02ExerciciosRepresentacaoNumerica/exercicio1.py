def calcular_S(n, x):
    soma = sum(x for x in range(1, n+1))
    S = 10000 - soma
    return S

# Para n=100000 e x=0.1
S1 = calcular_S(100000, 0.1)
print("S1 =", S1)

# Para n=80000 e x=0.125
S2 = calcular_S(80000, 0.125)
print("S2 =", S2)

#Para calcular o erro absoluto e relativo,
#precisamos de um valor exato para S.

def calcular_S_exato(n, x):
    S_exato = 10000 - (n*(n+1)*x)/2
    return S_exato

# Para n=100000 e x=0.1
S1_exato = calcular_S_exato(100000, 0.1)
print("S1 exato =", S1_exato)

# Para n=80000 e x=0.125
S2_exato = calcular_S_exato(80000, 0.125)
print("S2 exato =", S2_exato)


# Erro absoluto para S1
erro_absoluto_S1 = abs(S1 - S1_exato)
print("Erro absoluto para S1 =", erro_absoluto_S1)

# Erro relativo para S1
erro_relativo_S1 = erro_absoluto_S1 / S1_exato
print("Erro relativo para S1 =", erro_relativo_S1)

# Erro absoluto para S2
erro_absoluto_S2 = abs(S2 - S2_exato)
print("Erro absoluto para S2 =", erro_absoluto_S2)

# Erro relativo para S2
erro_relativo_S2 = erro_absoluto_S2 / S2_exato
print("Erro relativo para S2 =", erro_relativo_S2)
