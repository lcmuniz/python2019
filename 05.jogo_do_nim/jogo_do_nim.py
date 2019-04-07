import random

# Pede ao usuário o número de peças que ele quer retirar e retorna este número de peças
def usuario_escolhe_jogada(n, m):
    while True:
        num_pecas = int(input('Quantas peças você vai tirar? '))
        if num_pecas > 0 and num_pecas <= n and num_pecas <= m:
            return num_pecas
        print('Oops! Jogada inválida! Tente de novo.')

# Calcula quantas peças o computador vai tirar e retorna este número de peças
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

# Executa uma partida
def partida():

    # Solicita quantas peças vão estar no tabuleiro e quantas peças pode tirar por vez
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()

    # Testa quem vai começar
    if n % (m + 1) == 0:
       # Se n é múltiplo de m+1, a vez é do jogador
       print('Você começa!')
       vez = 'usuario'
    else:
       # Se n não é múltiplo de m+1, a vez é do computador
       print('O computador começa!')
       vez = 'computador'
    print()

    # gera um número aleatório para decidir quem começa a partida
    # i = random.randint(1,2)
    # if i == 1:
    # print('O computador começa!')
    #     vez = 'computador'
    # else:
    #     print('Você começa!')
    #     vez = 'usuario'
    # print()

    # Enquanto n (número de peças no tabuleiro) for maior que zero, continua jogando
    while n > 0:
        if vez == 'computador':
            # Se a vez é do computador, chama a função computador_escolhe_jogada()
            pecas = computador_escolhe_jogada(n, m)

            if pecas == 1:
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou', pecas, 'peças.')

            # a vez passa a ser do usuário
            vez = 'usuario'
        else:
            # Se a vez é do jogador, chama a função usuario_escolhe_jogada()
            pecas = usuario_escolhe_jogada(n, m)

            if pecas == 1:
                print('Você tirou uma peça.')
            else:
                print('Você tirou', pecas, 'peças.')

            # a vez passa a ser do computador
            vez = 'computador'

        # diminui o número de peças no tabuleiro (n) do número de peças tiradas (pecas)
        n = n - pecas

        if n > 0:
            # Se n > 0, então ainda restam peças no tabuleiro
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            else:
                print('Agora restam', n, 'no tabuleiro.')
        else:
            # Se n é igual a zero, acabou o jogo
            if vez == 'usuario':
                print('Fim do jogo! O computador ganhou!')
                print()
                return 'computador'
            else:
                print('Fim do jogo! Você ganhou!')
                print()
                return 'usuario'
        print()


# Executa um campeonato
def campeonato():

    partidas_usuario = 0
    partidas_computador = 0

    print('Você escolheu um campeonato!')
    print()
    rodada = 1

    num_partidas = int(input('Quantas partidas você quer jogar? '))
    print()
    while rodada <= num_partidas:
        print('***** Rodada {} *****'.format(rodada))
        print()
        vencedor = partida()

        if vencedor == 'usuario':
            partidas_usuario = partidas_usuario + 1
        else:
            partidas_computador = partidas_computador + 1

        rodada = rodada + 1

    print('***** Final do campeonato! *****')

    print('Placar: Você {} x {} Computador'.format(partidas_usuario, partidas_computador))


def main():
    # Início do jogo, menu inicial
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    print()
    tipo = input('> ')

    if tipo == '1':
        # Se o usuário escolher 1, chama a função partida() para executar uma partida
        print()
        print('Você escolheu uma partida isolada!')
        print()
        partida()
    else:
        # Se o usuário escolher 2, chama a função campeonato() para jogar um campeonato
        campeonato()


# inicia a execucao do programa
main()
