# imprime a tabuada multiplicacao de de 1 a 10
linha = 1
while linha <= 10:
    coluna = 1
    while coluna <= 10:
        print(linha*coluna, end = "\t")
        coluna = coluna + 1
    print()
    linha = linha + 1
