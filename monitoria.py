def antecessor_impares(numero):
    while numero > 0:
        numero -= 1
        if numero % 2 == 1:
            print(numero)

antecessor_impares(9)