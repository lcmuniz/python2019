nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input('Digite o valor total das vendas efetuadas: '))

salario = salario_fixo + (vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(salario))