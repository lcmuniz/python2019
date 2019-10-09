
linha0 = input().split('-')

cd1 = int(linha0[0])
np1 = int(linha0[1])
valor1 = float(linha0[2])

linha1 = input().split()

cd2 = int(linha1[0])
np2 = int(linha1[1])
valor2 = float(linha1[2])

valortotal = np1 * valor1 + np2 * valor2

print('valor a pagar: r$', '{:.2f}'.format(valortotal))