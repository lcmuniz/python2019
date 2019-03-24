# Escreva um programa que receba um número inteiro na entrada,
# calcule e imprima a soma dos dígitos deste número na saída
# Exemplo:
# Digite um número inteiro: 123
# 6
# Dica: Para separar os dígitos, lembre-se: o operador "//" faz
# uma divisão inteira jogando fora o resto, ou seja, aquilo que
# é menor que o divisor; O operador "%" devolve apenas o resto
# da divisão inteira jogando fora o resultado, ou seja, tudo
# que é maior ou igual ao divisor.

numero = input('Digite um número inteiro: ')

soma = 0

num_digitos = len(numero)

num = int(numero)

while num_digitos > 0:
    digito = num % 10
    num = num // 10
    soma = soma + digito
    num_digitos = num_digitos - 1

print(soma)