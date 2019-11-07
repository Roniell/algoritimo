
agenda = []

def add_contato(nome,email,telefone):
    contato = {'nome': nome, 'email': email, 'telefone': telefone}
    agenda.append(contato)


def listar_todos():
    if agenda:
        for cod, contato in enumerate(agenda):
            print('Cod:', cod, '>', contato)
    else:
        print('Nenhum contato existente!')

def deletar_contato(cod):
    if len(agenda) > cod:
        del agenda[cod]
    else:
        print('Código inexistente!')


def consultar_por_codigo(cod):
    if len(agenda) > cod:
        print('Nome:', agenda[cod]['nome'])
        print('Email:', agenda[cod]['email'])
        print('Telefone:', agenda[cod]['telefone'])
    else:
        print('Contato inexistente!')

def editar_contato(cod, nome, email, telefone):
    if len(agenda) > cod:
        if nome:
            agenda[cod]['nome'] = nome
        if email:
            agenda[cod]['email'] = email
        if telefone:
            agenda[cod]['telefone'] = telefone
    else:
        print('Contato inexistente! ')
