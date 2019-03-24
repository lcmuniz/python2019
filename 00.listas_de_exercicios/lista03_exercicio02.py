# Receba um número inteiro na entrada e imprima Divisível por 3
# se o número for divisível por 3. Caso contrário, imprima o mesmo
# número que foi dado na entrada.

numero = int(input('Digite um número: '))

if numero % 3 == 0:
    print('Divísivel por 3')
else:
    print(numero)