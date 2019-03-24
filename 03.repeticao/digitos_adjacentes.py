# Este programa informa se o número digitado pelo usuário
# possui dígitos adjacentes iguais.
# Por exemplo: o número 12202 tem o número dois números 2 adjacentes.
# O número 12353 não possui dígitos adjacentes.


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
    anterior = digito

if adjacente:
    print('O número {0} possui dígitos adjacentes iguais.'.format(original))
else:
    print('O número {0} não possui dígitos adjacentes iguais.'.format(original))
