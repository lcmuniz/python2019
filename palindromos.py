
def remover_acentos(texto):
    assert type(texto) is str, 'remover_acentos(): parametro deve ser do tipo texto'
    texto = texto.upper()
    for c in 'ÁÉÍÓÚÂÊÔÃÕ':
        texto = texto.replace(c, '')
    return texto

def remover_pontuacao(texto):
    assert type(texto) is str, 'remover_pontuacao(): parametro deve ser do tipo texto'
    for c in ' .,;?!:-':
        texto = texto.replace(c, '')
    return texto

def eh_palindromo(texto):
    assert type(texto) is str, 'eh_palindromo(): parametro deve ser do tipo texto'
    texto = remover_pontuacao(texto)
    texto = remover_acentos(texto)
    invertido = texto[::-1]

    return texto.upper() == invertido.upper()
