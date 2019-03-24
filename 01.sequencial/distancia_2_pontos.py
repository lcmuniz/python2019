# Calcula a distância entre dois pontos

from math import sqrt

print('Digite as coordenadas do ponto A: ')
xa = float(input('x: '))
ya = float(input('y: '))

print('Digite as coordenadas do ponto B: ')
xb = float(input('x: '))
yb = float(input('y: '))

dx = xa - xb
dy = ya - yb

distancia = sqrt(dx ** 2 + dy ** 2)

print('A distância entre os pontos A({},{}) e B({},{}) é {}.'
      .format(xa,ya,xb,yb,distancia))