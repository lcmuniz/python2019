# Escreva a função vogal que recebe um único caractere como
# parâmetro e devolve True se ele for uma vogal e False se
# for uma consoante.
# Exemplos de execução no shell de Python
# >>> vogal("a")
# True
# >>> vogal("b")
# False
# >>> vogal("E")
# True
# Os valores True e False devolvidos devem ser do tipo bool (booleanos),
# e não strings Dica: Lembre-se que para passar uma vogal como
# parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

def vogal(letra):

    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True

    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        return True

    return False

