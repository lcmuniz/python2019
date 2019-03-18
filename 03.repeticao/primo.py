numero = int(input('Digite um número: '))

contador = 2
eh_primo = True

while contador < (numero / 2 + 1):
    if numero % contador == 0:
        eh_primo = False
        break
    contador = contador + 1

if eh_primo:
    print('O número', numero, 'é primo.')
else:
    print('O número', numero, 'não é primo.')