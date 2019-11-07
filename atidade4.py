# crie uma função que receba um valor e um percentual de desconto e retorne o valor final com desconto


def valor_final_desconto(valor, desconto):
    desconto = valor - (valor * desconto/100)
    return desconto

print(valor_final_desconto(90, 15))