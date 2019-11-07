def numero_primo(numero):
    n = numero
    quantidade_divisores = 0
    resolucao = False
    while n >= 1:
        if numero % n == 0:
            quantidade_divisores += 1
        n -= 1
    if quantidade_divisores > 2:
        resolucao = False
    else:
        resolucao = True
    return resolucao

print(numero_primo(7))

