# Escreva um programa que receba um número inteiro na entrada
# e verifique se o número recebido possui ao menos um dígito com
# um dígito adjacente igual a ele. Caso exista, imprima "sim";
# se não existir, imprima "não".
# Exemplos:
# Digite um número inteiro: 12345
# não
# Digite um número inteiro: 1011
# sim

original = input('Digite um número inteiro: ')

num_digitos = len(original)

num = int(original)

anterior = -1

adjacente = False

while num_digitos > 0:
    digito = num % 10
    num = num // 10
    num_digitos = num_digitos - 1
    if anterior == digito:
        adjacente = True
        break
    anterior = digito

if adjacente:
    print('sim')
else:
    print('não')
