print('Digite números para somar ou zero para terminar.')

numero = 1
soma = 0

while numero != 0:
    numero = float(input('Digite um número: '))
    soma = soma + numero

print('A soma dos números digitados é', soma)

