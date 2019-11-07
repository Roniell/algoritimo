# crie uma função que receba um número e retoner true se o número > 0

print("#" * 30)
def is_positivo(numero):

        return numero > 0

print(is_positivo(-5))
print("#" * 30)


# crie uma função que receba um número como arguemnto e imprima todos os impares anteriores a ele

print("#" * 30)
def numero_imapres(numero):
    while numero > 0:
        numero -= 1
        if numero % 2 == 1:
            print(numero)

numero_imapres(5)
print("#" * 30)

# crie uma função que receba um número como argumento e retorne true se o número for primo

print("#" * 30)
def numero_primo(numero):
    cont = numero
    quantidade_divisores = 0
    resolucao = False
    while cont > 0:
        if numero % cont == 0:
            quantidade_divisores += 1
        cont -= 1
    return quantidade_divisores == 2

print(numero_primo(9))
print("#" * 30)


# crie uma função que receba um valor e um percentual de desconto e retorne o valor final com desconto

print("#" * 30)
def valor_final_desconto(valor, desconto):
    valor_total = valor - (valor * desconto/100)
    return valor_total

print(valor_final_desconto(100, 10))
print(valor_final_desconto(valor=100, desconto=10))
print("#" * 30)

