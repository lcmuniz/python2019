
import csv

with open("/home/lcmuniz/Documents/sumario.csv", "w") as sumario:
    sumario.write("Nome Completo, Média\n")
    with open("/home/lcmuniz/Documents/grades.csv") as grades:
        conteudo = csv.reader(grades)

        for aluno in conteudo:
            if (aluno[0] == 'Last name'):
                continue
            nome = aluno[1] + " " + aluno[0]
            media = (float(aluno[3]) + float(aluno[4]) + float(aluno[5]) + float(aluno[6])) / 4

            sumario.write(nome +  "," + str(media) + "\n")





