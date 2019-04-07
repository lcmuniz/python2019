import random

numeros = []

for i in range(11):
    n = random.randint(1, 101)
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)

ordenada = numeros.copy()
ordenada.sort()

print("Na lista {}, ".format(numeros))
print("o menor número é {} e".format(menor))
print("o maior número é {}.".format(maior))
print("A lista ordenada é {}.".format(ordenada))