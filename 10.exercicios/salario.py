numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input('Digite o valor da hora trabalhada: '))

salario = horas_trabalhadas * valor_hora

print("NÚMERO =", numero_funcionario)
print("SALÁRIO = R$ {:.2f}".format(salario))