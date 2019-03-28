import random

def jogada_computador():
    jogada = random.randint(1,3)
    if jogada == 1:
        return 'pedra'
    elif jogada == 2:
        return 'papel'
    else:
        return 'tesoura'

def jogada_usuario():
    while True:
        jogada = input('Digite sua jogada: ')
        if jogada != 'pedra' and jogada != 'papel' and jogada != 'tesoura':
            print('Jogada inválida. Você deve escolher pedra, papel ou tesoura.')
        else:
            return jogada

def partida():

    while True:
        computador = jogada_computador()
        usuario = jogada_usuario()

        print('Computador escolheu', computador)

        if computador == usuario:
            print('Empate. Os dois escolheram', computador, '.')
            print('Vamos tentar novamente.')
            print()
        elif computador == 'pedra' and usuario == 'tesoura':
            print('Pedra quebra tesoura. Computador ganhou.')
            return
        elif computador == 'pedra' and usuario == 'papel':
            print('Papel embrulha pedra. Usuário ganhou.')
            return
        elif computador == 'papel' and usuario == 'tesoura':
            print('Tesoura corta papel. Usuário ganhou.')
            return
        elif computador == 'papel' and usuario == 'pedra':
            print('Papel embrulha pedra. Computador ganhou.')
            return
        elif computador == 'tesoura' and usuario == 'pedra':
            print('Pedra quebra tesoura. Usuário ganhou.')
            return
        elif computador == 'tesoura' and usuario == 'papel':
            print('Tesoura corta papel. Computador ganhou.')
            return

partida()