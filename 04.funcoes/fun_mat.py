# Módulo fun_mat com diversas funções matemáticas

from math import sqrt

def fatorial(numero):

    if numero < 0:
        return None

    contador = 1
    fat = 1

    while contador <= numero:
        fat = fat * contador
        contador = contador + 1

    return fat

def calcular_combinacoes(n, k):

    fat_n = fatorial(n)
    fat_k = fatorial(k)
    fat_n_menos_k = fatorial(n-k)

    combinacoes = fat_n // (fat_k * fat_n_menos_k)

    return combinacoes



def soma(numero):
    contador = 1
    soma = 0

    while contador <= numero:
        soma = soma + contador
        contador = contador + 1

    return soma

def delta(a, b, c):
    return (b**2)-(4*a*c)

def eq2grau(a, b, c):
    d = delta(a,b, c)

    if d < 0:
        return None
    elif d == 0:
        return -b / (2*a)
    else:
        r1 = (-b + sqrt(d)) / (2*a)
        r2 = (-b - sqrt(d)) / (2*a)
        return r1, r2
