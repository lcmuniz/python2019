# Função para encontrar o maior elemento de uma lista
def maior_elemento(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior