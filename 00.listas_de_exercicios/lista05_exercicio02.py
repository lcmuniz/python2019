# Receba um número inteiro positivo na entrada e imprima os
# n primeiros números ímpares naturais.
# Para a saída, siga o formato do exemplo abaixo.
# Exemplo:
# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

n = int(input('Digite o valor de n: '))

i = 1

while i <= n * 2:
    if i % 2 == 1:
        print(i)
    i = i + 1

