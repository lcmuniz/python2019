def data_por_extenso(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    print('ajsdlas')
    
    meses = ['janeiro', 'fevereiro', 'março', 'abril',
             'maio', 'junho', 'julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro']

    nome_mes = meses[mes - 1]

    return str(dia) + ' de ' + nome_mes + ' de ' + str(ano)
