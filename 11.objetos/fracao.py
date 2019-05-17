def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

# Classe Fracao.
# Uma fração é definida por um numerador e um denominador
class Fracao:

    # executado ao se criar um objeto da classe Fracao.
    # seta os valores iniciais do numerador e denominador
    # a partir dos valores passador como parâmetros
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # método utilizado pela função print para imprimir um
    # objeto da classe Fracao
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # método utilizado pelo operador + para somar dois objetos da classe Fracao
    # retorna um novo objeto do tipo Fracao
    def __add__(f1, f2):
        d = f1.den * f2.den
        n = (d / f1.den * f1.num) + (d / f2.den * f2.num)

        divisor = gcd(n, d)
        return Fracao(n // divisor, d // divisor)

    # método utilizado pelo operador - para subtrair dois objetos da classe Fracao
    # retorna um novo objeto do tipo Fracao
    def __sub__(f1, f2):
        d = f1.den * f2.den
        n = (d / f1.den * f1.num) - (d / f2.den * f2.num)
        divisor = gcd(n, d)
        return Fracao(n // divisor, d // divisor)

    # método utilizado pelo operador * para multiplicar dois objetos da classe Fracao
    # retorna um novo objeto do tipo Fracao
    def __mul__(f1, f2):
        d = f1.den * f2.den
        n = f1.num * f2.num
        divisor = gcd(n, d)
        return Fracao(n // divisor, d // divisor)


    # método utilizado pelo operador / para dividir dois objetos da classe Fracao
    # retorna um novo objeto do tipo Fracao
    def __truediv__(f1, f2):
        d = f1.num * f2.den
        n = f1.den * f2.num
        divisor = gcd(n, d)
        return Fracao(n // divisor, d // divisor)


# Pede os dados da primeira fração
print("Fração 1")
num1 = int(input("Numerador: "))
den1 = int(input("Denominador: "))

print()

# Pede os dados da segunda fração
print("Fração 2")
num2 = int(input("Numerador: "))
den2 = int(input("Denominador: "))

# cria as frações f1 e f2
f1 = Fracao(num1, den1)
f2 = Fracao(num2, den2)

# faz operações com as frações f1 w f2
# e mostra o resultado na tela
print()
print("Soma:", f1+f2)
print("Subtração:", f1-f2)
print("Multiplicação:", f1*f2)
print("Divisão:", f1/f2)

