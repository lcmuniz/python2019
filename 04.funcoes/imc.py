def imc(peso, altura):
    return peso / altura ** 2

def resultado(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau 1"
    elif 35 <= imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obseidade grau 3"

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = imc(peso, altura)
resultado = resultado(imc)

print(imc, resultado)
