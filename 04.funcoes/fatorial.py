def fatorial(numero):
    if numero < 0:
        return None

    contador = numero
    fatorial = 1

    while contador > 1:
        fatorial = fatorial * numero
        contador = contador - 1

    return fatorial


numero = int(input('Digite um número inteiro: '))

fatorial = fatorial(numero)

if fatorial == None:
    print('Não existe fatorial de número negativo.')
else:
    print('O fatorial de {} é {}.'.format(numero, fatorial))