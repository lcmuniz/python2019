# Soma os dígitos do número digitado pelo usuário

original = input('Digite um número inteiro: ')

soma = 0

num_digitos = len(original)

num = int(original)

while num_digitos > 0:
    digito = num % 10
    num = num // 10
    soma = soma + digito
    num_digitos = num_digitos - 1

print('A soma dos dígitos do número {} é {}.'
      .format(original, soma))