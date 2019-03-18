nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))
nota3 = float(input('Digite a primeira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Aprovado com média {}.'.format(media))
elif media >= 4:
    print('Em recuperação com média {}.'.format(media))
else:
    print('Reprovado com média {}.'.format(media))
