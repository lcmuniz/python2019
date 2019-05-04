def soma_matrizes(m1, m2):
    num_lin_m1 = len(m1)
    num_col_m1 = len(m1[0])
    num_lin_m2 = len(m2)
    num_col_m2 = len(m2[0])

    if num_lin_m1 == num_lin_m2 and num_col_m1 == num_col_m2:
        soma = []
        for i in range(num_lin_m1):
            lin = []
            for j in range(num_col_m1):
                lin.append(m1[i][j] + m2[i][j])
            soma.append(lin)
        return soma
    else:
        return False

