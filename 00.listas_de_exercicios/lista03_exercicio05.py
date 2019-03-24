# Receba 3 números inteiros na entrada e imprima Crescente se
# eles forem dados em ordem crescente. Caso contrário, imprima
# Não está em ordem crescente.

p = int(input('Digite o primeiro número: '))
s = int(input('Digite o segundo número: '))
t = int(input('Digite o terceiro número: '))

if p < s < t:
    print('Crescente')
else:
    print('Não está em ordem crescente')