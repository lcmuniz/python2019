nome = input('Digite seu nome: ')

nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')
nota3 = input('Digite a terceira nota: ')

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

media = (nota1 + nota2 + nota3) / 3

print('Olá {}, sua média é {}.'.format(nome, media))