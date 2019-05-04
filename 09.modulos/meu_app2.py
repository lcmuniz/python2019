from geometria import area_quadrado
from geometria import area_triangulo
from strings import reverso

lista = [10,20,30]

for e in lista:
    print(area_quadrado(e))

for e in lista:
    print(area_triangulo(e, e))

texto = "a base do teto desaba"

print(reverso(texto))

