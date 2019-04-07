# Este programa recebe números pelo teclado
# (até o usuário digitar 0) e imprime
# os números em ordem inversa do digitado
lista = []
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    lista = [n] + lista

for n in lista:
    print(n)