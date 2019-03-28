import random

def joga_dado():
    dado = random.randint(1,6)
    return dado

pontos_computador = 0
pontos_usuario = 0
rodada = 0

while True:
    rodada = rodada + 1
    print('Rodada:', rodada)
    jogada_computador = joga_dado()
    pontos_computador = pontos_computador + jogada_computador
    print('Computador tirou', jogada_computador, 'pontos e agora tem', pontos_computador, 'pontos.')
    if pontos_computador > 12:
        print()
        print('Fim de jogo. O computador estourou! O usuário venceu!')
        break
    elif pontos_computador  == 12:
        print()
        print('Fim de jogo. O computador venceu!')
        break

    jogada_usuario = joga_dado()
    pontos_usuario = pontos_usuario + jogada_usuario
    print('Usuário tirou', jogada_usuario, 'pontos e agora tem', pontos_usuario, 'pontos.')
    if pontos_usuario > 12:
        print()
        print('Fim de jogo. O usuário estourou! O computador venceu!')
        break
    elif pontos_usuario == 12:
        print()
        print('Fim de jogo. O usuário venceu!')
        break
    print()


