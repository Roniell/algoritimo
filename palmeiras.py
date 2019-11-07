def cabulosa(n1, n2, n3, n4):
    total = (n1 + n2) * n1 + (n2 + n3) * n2 + (n3 + n4) * n3
    return str(total)


print(cabulosa(1, 2, 3, 4))


def is_par(numero):
    return int(numero) % 2 == 0


# print(is_par(3))


def grava_no_arquivo(arquivo, numero):
    txt = open(arquivo, 'w')
    txt.write(numero)
    txt.close()


def main():
    if is_par(cabulosa(1, 2, 3, 4)):
        grava_no_arquivo('par.txt', cabulosa(1, 2, 3, 4))
    else:
        grava_no_arquivo('impar.txt', cabulosa(1, 2, 3, 4))


main()
