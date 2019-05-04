tempo = int(input("Tempo gasto na viagem (em horas): "))
velocidade = float(input("Velocidade média (km/h): "))

distancia = tempo * velocidade

litros = distancia / 12

print("{:.3f}".format(litros))