# Faça um programa em Python que receba (entrada de dados)
# o valor correspondente ao lado de um quadrado, calcule e
# imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"
# Abaixo um exemplo de como deve ser a entrada e saída de dados
# do programa:
# Entrada de Dados:
# Digite o valor correspondente ao lado de um quadrado: 3
# Saída de Dados:
# Perímetro: 12 - Área: 9

lado = float(input('Digite o valor correspondente ao lado de um quadrado: '))

perimetro = lado * 4

area = lado ** 2

print('Perímetro: {} - Área: {}'.format(perimetro, area))
