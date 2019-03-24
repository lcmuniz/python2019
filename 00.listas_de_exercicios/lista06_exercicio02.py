# Escreva a função maior_primo que recebe um número inteiro
# maior ou igual a 2 como parâmetro e devolve o maior número
# primo menor ou igual ao número passado à função
# Exemplos de execução no shell do Python:
# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7
# Dica: escreva uma função eh_primo(k) e faça um laço percorrendo
# os números até o número dado checando se o número é primo ou não;
# se for, guarde numa variável. Ao fim do laço, o valor armazenado
# na variável é o maior primo encontrado.

def eh_primo(k):

    i = 2
    eh_primo = True

    while i < (k / 2 + 1):
        if k % i == 0:
            eh_primo = False
            break
        i = i + 1

    return eh_primo

def maior_primo(n):
    i = n
    while True:
        if eh_primo(i):
            return i
        i = i - 1

print(maior_primo(0))