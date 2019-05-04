def area_quadrado(lado):
    assert lado > 0, "Lado inválido"
    return lado * lado


def area_quadrado2(lado):
    if lado > 0:
        return lado * lado
    else:
        raise ValueError("Lado inválido")

def area_triangulo(base, altura):
    assert base > 0 and altura > 0, "Base a altura devem ser maior que zero"
    return (base * altura) / 2


def perimetro_triangulo(l1, l2, l3):
    assert l1 + l2 > l3, "Triangulo invalido"
    assert l1 + l3 > l2, "Triangulo invalido"
    assert 12 + l3 > l1, "Triangulo invalido"
    return l1+l2+l3


