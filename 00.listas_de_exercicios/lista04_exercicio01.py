# Receba 4 números na entrada, um de cada vez. Os dois primeiros
# devem corresponder, respectivamente, às coordenadas x e y
# de um ponto em um plano cartesiano. Os dois últimos devem
# corresponder, respectivamente, às coordenadas x e y de um outro
# ponto no mesmo plano.
# Calcule a distância entre os dois pontos.
# Se a distância for maior ou igual a 10, imprima 'longe' na saída.
# Caso o contrário, quando a distância for menor que 10, imprima 'perto'

from math import sqrt

x1 = float(input('Digite o x da primeira coordenada: '))
y1 = float(input('Digite o y da primeira coordenada: '))

x2 = float(input('Digite o x da segunda coordenada: '))
y2 = float(input('Digite o y da segunda coordenada: '))

dx = x1 - x2
dy = y1 - y2

distancia = sqrt(dx ** 2 + dy ** 2)

if distancia >= 10:
    print('longe')
else:
    print('perto')