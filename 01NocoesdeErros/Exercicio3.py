# Overflow
#Neste exemplo, a variável x é inicializada com o valor 1.0 e em seguida, é multiplicada por 2.0
# em um loop infinito.
#Conforme o loop é executado, o valor de x vai aumentando exponencialmente,
#até que ele ultrapassa o limite de representação em ponto flutuante, causando um erro de overflow.

#Overflow

# x = 1.0
# while True:
#     x *= 2.0
#     print(x)

# Arredondamento

# Neste exemplo, a variável x é inicializada com o valor 0.1 e em seguida,
# é somada a uma variável de acumulação S em um loop for. Como 0.1 não pode ser
# representado com exatidão em ponto flutuante, o resultado da soma pode ser afetado pelo arredondamento.
# No exemplo acima, o resultado do somatório pode ser
# ligeiramente diferente de 1.0, dependendo do arredondamento feito pelo Python.

x = 0.1
S = 0
for i in range(1, 10):
    S += x

print("O resultado do somatório é:", S)

