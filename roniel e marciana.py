# Problema 3

# Dica: Use dicionário e tupla
#
# Dado um valor em reais e inteiro. Crie uma função que exiba a quantidade de cédulas
# de cada valor (100, 50, 20, 10, 5 e 2),
# para efetuar um saque, visando sempre entregar o menor número de cédulas possível. (APENAS CÉDULAS)


saque = int(input("Digite o valor do saque: "))
total = saque
nota = 100
total_notas = 0

while True:
    if total >= nota:
        total -= nota
        total_notas += 1
    else:
        if total_notas > 0:
            print(f'total de {total_notas} notas de R$ {nota}')
        if nota == 100:
            nota = 50
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
            total_notas = 0
        if total == 0:
            break
