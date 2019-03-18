valor_hora = float(input('Digite o valor da hora de trabalho: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas;
imposto_renda = salario_bruto * 0.10
inss = salario_bruto * 0.08
salario_liquido = salario_bruto - imposto_renda - inss

print('Salário bruto: ', salario_bruto)
print('Imposto de renda: ', imposto_renda)
print('INSS: ', inss)
print('Salário líquido: ', salario_liquido)