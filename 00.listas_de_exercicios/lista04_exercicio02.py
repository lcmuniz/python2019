# Escreva um programa que calcula as raízes de uma equação
# do segundo grau.
# O programa deve receber os parametros a, b, e c da equação
# ax2+bx+c, respectivamente, e imprimir o resultado na saída
# da seguinte maneira:
# Quando não houver raízes reais imprima: esta equação não possui
# raízes reais.
# Quando houver apenas uma raiz real imprima: a raiz desta equação é X,
# onde X é o valor da raiz.
# Quando houver duas raízes reais imprima as raízes da equação são X e Y,
# onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais, elas devem
# ser impressas em ordem crescente, ou seja, X deve ser menor que Y.

from math import sqrt

a = float(input('Digite o coeficente a: '))
b = float(input('Digite o coeficente b: '))
c = float(input('Digite o coeficente c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = -b / (2*a)
    print('a raiz desta equação é', raiz)
else:
    raiz1 = (-b + sqrt(delta)) / (2*a)
    raiz2 = (-b - sqrt(delta)) / (2*a)

    if raiz1 <=  raiz2:
        x = raiz1
        y = raiz2
    else:
        x = raiz2
        y = raiz1

    print('as raízes da equação {} e {}'. format(x, y))