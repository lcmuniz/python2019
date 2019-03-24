# Reescreva o programa visto na aula que calcula o número de horas,
# minutos e segundos, para imprimir também a quantidade de dias,
# ou seja, faça um programa em Python que, dada a quantidade de
# segundos, "quebre" esse valor em dias, horas, minutos e segundos.
# A saída deve estar no formato: a dias, b horas, c minutos e d segundos.
# Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando
# ou outras diferenças são considerados erro.
# Abaixo um exemplo de como deve ser a entrada e saída de dados do
# programa:
# Exemplo:
# Entrada de Dados:
# Por favor, entre com o número de segundos que deseja converter: 178615
# Saída de Dados:
# 2 dias, 1 horas, 36 minutos e 55 segundos.

segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // (60 * 60 * 24)
resto = segundos % (60 * 60 * 24)

horas = resto // (60 * 60)
resto = resto % (60 * 60)

minutos = resto // 60
resto = resto % 60

print('{} dias, {} horas, {} minutos e {} segundos.'
      .format(dias, horas, minutos, resto))

