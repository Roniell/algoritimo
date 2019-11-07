def numero_primo(numero):
    num = numero
    quantidade_divisores = 0
    resolucao = False
    while num >= 1:
        if numero % num == 0:
            quantidade_divisores = quantidade_divisores + 1
        if quantidade_divisores > 2:
            resolucao = False
        else:
            resolucao = True
        return resolucao
print(numero_primo(7))
