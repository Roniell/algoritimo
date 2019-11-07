# TODO: Dada uma string, imprima essa string inteira em maiuscula
#  exemplo: 'python' -> 'PYTHON. (1 scores)

#
# def maiuscula(palavra):
#     palavra_maiusculo = palavra.upper()
#     return palavra_maiusculo
# print(maiuscula('python'))

# TODO: Dada ums string, retorne a string invertida.
#  Exemplo: 'asdf' -> 'fdsa' (3 scores)
#
# def invertida(text):
#     palavra = list(text)
#     palavra.reverse()
#     return ''.join(palavra)
#
#
# print(invertida('asdf'))


# TODO: Dada uma string, retorne em um dicionário a quantidade de cada uma das
#  vogais contidas na string.
#  Exemplo: 'adalamita' -> {'a': 4, 'e': 0, 'i': 1, 'o': 0, 'u': 0 } (4 scores

# def quant_vogais(palvras):
#     resultado = {}
#     for v in ('a', 'e', 'i', 'o', 'u'):
#         resultado[v] = palvras.count(v)
#     return resultado
# print(quant_vogais('adalamita'))

# TODO: C. fix_start
#  Dada uma string s, retornar uma string
#  onde todas as ocorrências do seu primeiro caractere seja
#  alterado para "*", não alterar
#  o primeiro char em si.
#  por exemplo, "babble" rende "ba**le"; "google" rende "goo*le".
#  Suponha que a corda é de comprimento 1 ou mais.
#  Dica: s.replace(stra, strb) retorna uma versão da string s
#  onde todas as instâncias de stra foram substituídas por strb. (5 scores)
def fix_start(s):

#     char = s[0]
#     length = len(s)
#     s = s.replace(char, '*')
#     s = char + s[1:]

    return s


print(fix_start('roniel'))

# TODO: Dada uma string, retorne um booleano que indique se ela é ou não um número.
#   exemplo: '1243' -> True, 'a12' -> False. (1 scores)
