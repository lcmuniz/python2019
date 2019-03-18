from math import sqrt

def delta(a, b, c):
    return (b**2) - (4*a*c)

def calcula_raizes(a, b, c):
    d = delta(a, b, c)

    if d < 0:
        return None
    elif d == 0:
        return -b / (2*a)
    else:
        r1 = (-b + sqrt(d)) / (2 * a)
        r2 = (-b - sqrt(d)) / (2 * a)
        return r1, r2

def main():
    a = float(input('Digite o coeficiente a: '))
    b = float(input('Digite o coeficiente b: '))
    c = float(input('Digite o coeficiente c: '))

    raiz = calcula_raizes(a, b, c)

    if raiz == None:
        print('Não existem raízes reais.')
    elif type(raiz) is float:
        print('A raíz é', raiz)
    else:
        print('As raízes são', raiz[0], 'e', raiz[1])

main()