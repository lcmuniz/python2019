from math import sqrt

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

delta = (b**2) - (4*a*c)

if delta < 0:
    print('Não existem raízes reais.')
elif delta == 0:
    raiz = -b / (2*a)
    print('A raiz é', raiz)
else:
    raiz1 = (-b + sqrt(delta) / (2*a))
    raiz2 = (-b - sqrt(delta) / (2*a))
    print('As raizes são {} e {}.'.format(raiz1, raiz2))