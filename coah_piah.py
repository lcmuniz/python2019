import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e
    devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas
    dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases
    dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras
    dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o
    numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de
    palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):

    wal_a = as_a[0]
    ttr_a = as_a[1]
    hlr_a = as_a[2]
    sal_a = as_a[3]
    sac_a = as_a[4]
    pal_a = as_a[5]

    wal_b = as_b[0]
    ttr_b = as_b[1]
    hlr_b = as_b[2]
    sal_b = as_b[3]
    sac_b = as_b[4]
    pal_b = as_b[5]

    wal = abs(wal_a - wal_b)
    ttr = abs(ttr_a - ttr_b)
    hrl = abs(hlr_a - hlr_b)
    sal = abs(sal_a - sal_b)
    sac = abs(sac_a - sac_b)
    pal = abs(pal_a - pal_b)

    return (wal + ttr + hrl + sal + sac + pal) / 6

def calcula_assinatura(texto):

    total_caracteres = 0
    total_caracteres_frase = 0
    total_caracteres_sentenca = 0
    total_palavras = 0
    todas_palavras = []
    todas_frases = []
    sentencas = separa_sentencas(texto)
    for s in sentencas:
        total_caracteres_sentenca = total_caracteres_sentenca + len(s)
        frases = separa_frases(s)
        todas_frases = todas_frases + frases
        for f in frases:
            total_caracteres_frase = total_caracteres_frase + len(f)
            palavras = separa_palavras(f)
            todas_palavras = todas_palavras + palavras
            total_palavras = total_palavras + len(palavras)
            for p in palavras:
                total_caracteres = total_caracteres + len(p)

    wal = total_caracteres / total_palavras

    ttr = n_palavras_diferentes(todas_palavras) / len(todas_palavras)

    hlr = n_palavras_unicas(todas_palavras) / len(todas_palavras)

    sal = total_caracteres_sentenca / len(sentencas)

    sac = len(todas_frases) / len(sentencas)

    pal = total_caracteres_frase / len(todas_frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e
    deve devolver o numero (1 a n) do texto com maior probabilidade de
    ter sido infectado por COH-PIAH.'''

    ass_t = calcula_assinatura(textos[0])
    menor = compara_assinatura(ass_t, ass_cp)
    index = 0

    for i in range(1, len(textos)):
        ass_t = calcula_assinatura(textos[i])
        comp = compara_assinatura(ass_t, ass_cp)
        if comp < menor:
            menor = comp
            index = i

    return index + 1


