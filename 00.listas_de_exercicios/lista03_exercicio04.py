# Receba um número inteiro na entrada e imprima Divisível por 3 e
# por 5 na saída se o número for divisível por 3 e por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print('Divísivel por 3 e por 5')
else:
    print(numero)