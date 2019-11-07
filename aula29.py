from dia29 import *


while True:
    text = "SUPER AGENDA DE CONTATOS PLUS ULTRA"
    print('#' * (len(text)))
    print("SUPER AGENDA DE CONTATOS PLUS ULTRA")
    print("###     1- LISTAR CONTATOS      ###")
    print("###     2- BUSCAR CONTATOS      ###")
    print("###     3- ADD CONTATO          ###")
    print("###     4- EDITAR CONTATO       ###")
    print("###     5- REMOVER CONTATO      ###")
    print("###     6- SAIR                 ###")
    print('#' * (len(text)))

    op = int(input('opção:'))
    if op == 1:
        listar_todos()
    elif op == 2:
        cod = int(input('Informe o codigo do contato:'))
        consultar_por_codigo(cod)
    elif op == 3:
        nome = input('Informe o nome: ')
        email = input('Informe o email: ')
        telefone = input('Informe o telefone: ')
        add_contato(nome, email, telefone)
    elif op == 4:
        cod = int(input('Informe o codigo do contato:'))
        nome = input('Informe o nome: ')
        email = input('Informe o email: ')
        telefone = input('Informe o telefone: ')
        editar_contato(cod, nome, email, telefone)
    elif op == 5:
        cod = int(input('Informe o codigo do contato:'))
        deletar_contato(cod)
    elif op == 6:
        print('Fim do programa')
        break
    else:
        print('Opção invalida')