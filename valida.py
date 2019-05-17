def valida_data(data):

    cond1 = len(data) == 10
    cond2 = data[2] == '/' and data[5] == '/'

    try:
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:])
    except ValueError:
        return False

    cond3 = dia >= 1 and dia <= 31
    cond4 = mes >= 1 and mes <= 12

    return cond1 and cond2 and cond3 and cond4
