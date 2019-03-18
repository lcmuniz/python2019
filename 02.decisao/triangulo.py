print('Digite os valores dos lados do triângulo.')

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if (lado1 >= lado2 + lado3) or (lado2 >= lado1 + lado3) or (lado3 >= lado1 + lado2):
    print('Valores informados não formam um triângulo')
elif lado1 == lado2 == lado3:
    print('Triângulo equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')