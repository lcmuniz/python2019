

import sys

nome_arquivo = sys.argv[1]

n_linhas = 0
n_palavras = 0
n_caracteres = 0

try:
    arquivo = open(nome_arquivo)

    linhas = arquivo.readlines()
    n_lin

    for linha in linhas:
        print(linha.upper(), end="")

except FileNotFoundError:
    print('Arquivo não encontrado')

