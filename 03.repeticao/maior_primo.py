# funcao que retorna se o número n é primo ou não
def eh_primo(n):
    if n == 1:
        return True
    if n == 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

# funcao que retorna o maior numero primo entre 1 e n
def maior_primo(n):
    i = n
    while i > 0:
        if eh_primo(i):
            return  i
        i = i - 1
