# Este programa gera uma lista de temperaturas
# aleatórias e depois imprime a média, a menor e
# a maior temperatura da lista

import random

# Função para gerar as temperaturas
def gera_temperatutas(num_temp, min, max):

    lista = []
    for i in range(num_temp + 1):
        temp = random.randint(min, max + 1)
        lista.append(temp)

    return lista

# Função para encontrar a menor e a maior temperatura
def min_max_temperatura(temperaturas):
    menor = maior = temperaturas[0]
    for t in temperaturas:
        if t < menor:
            menor = t
        if t > maior:
            maior = t
    return [menor, maior]

# Função para encontrar a média das temperaturas
def temperatura_media(temperaturas):
    soma = 0
    for t in temperaturas:
        soma = soma + t
    return soma / len(temperaturas)


temperaturas = gera_temperatutas(10, 30, 40)
min_max = min_max_temperatura(temperaturas)
media = temperatura_media(temperaturas)

print('Temperaturas:', temperaturas)
print('Média:', media)
print('Menor:', min_max[0])
print('Maior:', min_max[1])