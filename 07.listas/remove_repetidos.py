# Função que recebe uma lista e retorna uma lista
# sem os elementos repetidos
def remove_repetidos(lista):
    resultado = []
    for n in lista:
        if n not in resultado:
            resultado.append(n)
    resultado.sort()
    return resultado