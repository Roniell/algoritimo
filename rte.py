def mult_vogais(palavra):
    vogais = []
    texto_lista = ''
    for letras in palavra:
        if letras in 'aeiou':
            vogais.append(letras*2)
        else:
            vogais.append(letras)
        texto_lista = ''.join(vogais)
    return texto_lista
print(mult_vogais('roniel'))


def vagais_maiusculas(palavras):
    vogais = []
    texto_lista = ''
    for letras in palavras:
        if letras in 'aeiou':
            vogais.append(letras.upper())
        else:
            vogais.append(letras)
        texto_lista = ''.join(vogais)
    return texto_lista
print(vagais_maiusculas('roniel'))