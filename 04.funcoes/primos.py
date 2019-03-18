def eh_primo(numero):

    contador = 2

    while contador < (numero / 2 + 1):
        if numero % contador == 0:
            return False
        contador = contador + 1

    return True

numero = int(input('Digite um número: '))

contador = 1

print('Números primos entre 1 e {}: '.format(numero))

numeros = ""

while contador <= numero:
    if eh_primo(contador):
        numeros = numeros + " " + str(contador)
    contador = contador + 1

print(numeros)