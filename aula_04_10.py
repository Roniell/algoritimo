def escreve_arquivo(texto, arquivo):
    arq = open(arquivo, 'w')
    arq.write(texto)
    arq.close()



def encripta(palavra, deslocamento):
    lista = []
    for l in palavra:
        lista.append(chr(ord(l) + deslocamento))
    texto_cifrado = "".join(lista)
    escreve_arquivo(texto_cifrado, 'criptografado.txt')
    return texto_cifrado

def decripta(palavra, deslocamento):
    lista = []
    for l in palavra:
        lista.append(chr(ord(l) - deslocamento))
    texto_descriptografado = "".join(lista)
    escreve_arquivo(texto_descriptografado, 'descriptografado.txt')
    return texto_descriptografado

def run():
    nome = input('Informe o texto para cifrar: ')
    deslocamento = int(input('Informe o deslocamento: '))
    cifrado = encripta(nome, deslocamento)
    decifrado = decripta(cifrado, deslocamento)
    print(f'Texto cifrado: {cifrado}')
    print(f'Texto descifrado: {decifrado}')

run()