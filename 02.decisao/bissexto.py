ano = int(input('Digite o ano: '))

bissexto = False

if ano % 4 == 0:
    bissexto = True
    if bissexto % 100 == 0 and bissexto % 400 != 0:
        bissexto = False

if bissexto:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))