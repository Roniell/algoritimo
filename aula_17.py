# def camel_case(texto):
#     camel = []
#     texto_camel = ""
#     for i, l in enumerate(texto):
#         if i % 2 != 0:
#             camel.append(texto[i].upper())
#         else:
#             camel.append(texto[i])
#     texto_camel = ",".join(camel)
#     return texto_camel
#
#
# print(camel_case("asdf"))



def quant_vogais(palvras):
    resultado = {}
    for v in ('a', 'e', 'i', 'o', 'u'):
        resultado[v] = palvras.count(v)
    return resultado
print(quant_vogais('adalamita'))

