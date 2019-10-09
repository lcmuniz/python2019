def mdc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

def simplifica(num, den):
    div = mdc(num, den)
    n = num // div
    d = den // div
    return n, d


def fatorial(n):
    assert n >= 0, "Não existe fatorial negativo"
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return  f

def raiz_quadrada(numero):
    assert numero >= 0, "numero deve ser maior ou igual a zero"
    return numero ** 0.5

def exponencial(base, expoente):
    return base ** expoente