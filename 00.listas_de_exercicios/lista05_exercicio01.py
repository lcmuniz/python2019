# Escreva um programa que receba um número natural n na entrada
# e imprima n!(fatorial) na saída.
# Exemplo:
# Digite o valor de n: 5
# 120
# Dica: lembre-se que o fatorial de 0 vale 1!

numero = int(input('Digite o valor de n: '))

fatorial = 1
i = 1

while i <= numero:
    fatorial = fatorial * i
    i = i + 1

print(fatorial)