def maisculas(texto):
    assert type(texto) is str, "parametro deve ser uma string"
    assert len(texto) > 0, "texto tem que ter caracteres"
    return texto.upper()

def minusculas(texto):
    assert type(texto) is str, "parametro deve ser uma string"
    return texto.lower()

def reverso(texto):
    assert type(texto) is str, "parametro deve ser uma string"
    lista = []
    for c in texto:
        lista = [c] + lista

    s = ""
    for e in lista:
       s = s + e

    return s



