def usuario_escolhe_jogada(n, m):
    while True:
        num_pecas = int(input('Quantas peças você vai tirar? '))
        if num_pecas > 0 and num_pecas <= n and num_pecas <= m:
            return num_pecas
        print('Oops! Jogada inválida! Tente de novo.')

def computador_escolhe_jogada(n, m):

    # se tem menos que m peças no tabuleiro, retira todas as n peças
    if n <= m:
        return n

    num_pecas = m
    while num_pecas > 0:
        pecas_restantes = n - num_pecas

        # se, tirando num_pecas, resta múltiplo de (m + 1) peças
        # retira num_pecas
        if pecas_restantes % (m + 1) == 0:
            return num_pecas
        num_pecas = num_pecas - 1

    # não tem como deixar múltiplo de (m + 1) no tabuleiro
    # retira m peças
    return m

