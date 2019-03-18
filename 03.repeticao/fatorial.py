numero = int(input('Digite um número inteiro: '))

if numero < 0:
    print('Não existe fatorial de número negativo.')
    exit(0)

contador = numero
fatorial = 1

while contador > 1:
    fatorial = fatorial * numero
    contador = contador - 1

print('O fatorial de {} é {}.'.format(numero, fatorial))