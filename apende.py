dicionario = {}

def listar_campo():
    print(dicionario.items())

def criar_campo():
    chave = input('Informe o nome da chave: ')
    valor = input('Inforeme o valor da chave: ')
    dicionario[chave] = valor

def buscar_informação():
    if len(dicionario) > 0:
        buscar = input('Qual informação você deseja buscar: ')
        if buscar is dicionario:
            print('Informação não encontrada!')
        else:
            print(dicionario[buscar])

def alterar_informação():
    if len(dicionario) > 0:
        buscar = input('Informe a alteração que você deseja fazer: ')
        if buscar is dicionario:
            print('Informação não encontrada: ')
        else:
            dicionario[buscar] = input('Novo valor: ')
    else:
        print('Informação não encontrada!')

def deletar_campo():
    if len(dicionario) > 0:
        buscar = input('Informe o campo que você quer deletar: ')
        if buscar is dicionario:
            print('Informação não encontrada')
        else:
            del dicionario[buscar]
            print('Informação deletada com sucesso!')
    else:
        print('Não existe nenhuma informação encontrada!')




while True:
    print('#' * 33)
    print('# 1 - Lista campo                       #')
    print('# 2 - Criar um campo                    #')
    print('# 3 - Buscar informação                 #')
    print('# 4 - Alterar valor do campo            #')
    print('# 5 - Deletar campo                     #')
    print('# 0 - Sair                              #')
    print('#' * 33)

    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        listar_campo()
    elif opcao == 2:
        criar_campo()
    elif opcao == 3:
        buscar_informação()
    elif opcao == 4:
        alterar_informação()
    elif opcao == 5:
        deletar_campo()
    elif opcao == 0:
        print('Obrigado por usar nosso garoto de programa')
        break