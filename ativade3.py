# crie uma função que receba um número como argumento e retorne true se o número for primo


def numero_primo(numero):
    cont = 1

    resultado = False

    while cont <= numero:
        if numero % 2 != 0:
            resultado = True
        cont = cont + 1
        return resultado

print(numero_primo(8))


