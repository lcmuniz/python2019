# Receba um número inteiro na entrada e imprima Divisível por 5 se
# o número for divisível por 5. Caso contrário, imprima o mesmo
# número que foi dado na entrada.

numero = int(input('Digite um número: '))

if numero % 5 == 0:
    print('Divísivel por 5')
else:
    print(numero)