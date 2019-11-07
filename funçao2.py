# TODO: Criar uma função para excluir um contato da lista
# TODO: Criar uma função para buscar um contato na lista por indece
# TODO: Criar uma função para alterar um contato
# TODO: Crair uma função para buscar um contato pelo nome
# TODO: Modificar para mostrar também o índice


contatos = []


def lista_contatos():
    if len(contatos) > 0:
        for i, cantato in enumerate(contatos):
            print(i, cantato)
    else:
        print('Não existe contatos no cadastrado!')

def criar_contato():
    nome = input("informe o nome do contato: ")
    telefone = input('Informe o número do telefone: ')
    contatos.append([nome, telefone])
    print('Contato cadrastrado com sucesso!')

def buscar_por_indice():
    if len(contatos) > 0:
        buscar = int(input('Informe o indíce do contato: '))
        if buscar >= len(contatos):
            print('Contato não existe!')
        else:
            print(contatos[buscar])
    else:
        print('Não existe nenhum contato cadastrado!')


def buscar_por_nome():
    if len(contatos) > 0:
        buscar = input('Informe o nome do contato: ')
        if buscar not in contatos:
           print('Contato não existente!')
        else:
            nome = buscar
            for i, contato in enumerate(contatos):
                if contato[0] == nome:
                    print(i, contato)
    else:
        print('Não existe contatos para serem pesquisado!')


def alterar_contato():
    if len(contatos) > 0:
        buscar = int(input('Buscar por indíce: '))
        if buscar >= len(contatos):
            print('Contato não existente')
        else:
            alterar_nome = input('Informe o novo nome do cantato: ')
            alterar_telefone = input('Informe o novo número do telefone: ')
            contatos[buscar] = [alterar_nome, alterar_telefone]
            print('Contato alterado com sucesso!')
    else:
        print('Não existe contato para ser alterado!')

def deletar_contato():
    if len(contatos) > 0:
        buscar = int(input('Informe o indíce do contato para ser deletado: '))
        if buscar >= len(contatos):
            print('Contato não existente!')
        else:
            del contatos[buscar]
            print(('Contato deletado com sucesso!'))
    else:
        print(('Não existe nenhum contato cadastrado para realizar a busca!'))



while True:
    print('#' * 33)
    print('# 1 - Lista contato              #')
    print('# 2 - Criar contato              #')
    print('# 3 - Buscar contato por indíce  #')
    print('# 4 - Buscar contato por nome    #')
    print('# 5 - Alterar contato            #')
    print('# 6 - Deletar contato            #')
    print('# 0 - Sair                       #')
    print('#' * 33)

    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        lista_contatos()
    elif opcao == 2:
        criar_contato()
    elif opcao == 3:
        buscar_por_indice()
    elif opcao == 4:
        buscar_por_nome()
    elif opcao == 5:
        alterar_contato()
    elif opcao == 6:
        deletar_contato()
    elif opcao == 0:
        print('Obrigado por usar nosso programa')
        break

