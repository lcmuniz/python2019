valor = int(input("Valor: "))

cem = valor // 100
resto = valor % 100

cinquenta = resto // 50
resto = resto % 50

vinte = resto // 20
resto = resto % 20

dez = resto // 10
resto = resto % 10

cinco = resto // 5
resto = resto % 5

dois = resto // 2
resto = resto % 2

um = resto

print("{} nota(s) de R$ 100,00".format(cem))
print("{} nota(s) de R$ 50,00".format(cinquenta))
print("{} nota(s) de R$ 20,00".format(vinte))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinco))
print("{} nota(s) de R$ 2,00".format(dois))
print("{} nota(s) de R$ 1,00".format(um))