# Escreva um programa que receba um número inteiro positivo
# na entrada e verifique se é primo. Se o número for primo,
# imprima "primo". Caso contrário, imprima "não primo".
# Exemplos:
# Digite um número inteiro: 13
# primo
# Digite um número inteiro: 12
# não primo

numero = int(input('Digite um número inteiro: '))

contador = 2
eh_primo = True

while contador < (numero / 2 + 1):
    if numero % contador == 0:
        eh_primo = False
        break
    contador = contador + 1

if eh_primo:
    print('primo')
else:
    print('não primo')