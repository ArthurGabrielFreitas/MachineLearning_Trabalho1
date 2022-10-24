from Contato import Contato


def consultar(dict_contatos):
    from csv import DictReader
    with open('contatos.csv', 'r') as arquivo:
        leitor_csv = DictReader(arquivo, delimiter=',')
        for linha in leitor_csv:
            dict_contatos[linha['Nome']] = Contato(linha['Nome'], linha['Telefone'], linha['Twitter'],
                                                   linha['Facebook'], linha['Instagram'])
    arquivo.close()
    imprimir_todos(dict_contatos)
    print()
    return dict_contatos


def inserir(dict_contatos):
    nome = input("Digite o nome do contato: ")
    if nome in dict_contatos.keys():
        print("Contato já existente. Para modificá-lo, selecione a opção de alterar.")
    else:
        telefone = input("Digite o telefone do contato: ")
        twitter = input("Digite o usuário de Twitter do contato: ")
        facebook = input("Digite o usuário de Facebook do contato: ")
        instagram = input("Digite o usuário de Instagram do contato: ")
        dict_contatos[nome] = Contato(nome, telefone, twitter, facebook, instagram)
    return dict_contatos


def imprimir(contato):
    print(contato)


def imprimir_todos(dict_contatos):
    if not dict_contatos:
        print("A lista de contatos está vazia.")
    else:
        for contato in dict_contatos.values():
            imprimir(contato)


def imprimir_um(dict_contatos, nome):
    if not dict_contatos:
        print("A lista de contatos está vazia.")
    elif nome in dict_contatos.keys():
        contato = dict_contatos[nome]
        imprimir(contato)
    else:
        print("Nome não encontrado na lista de contatos. Tente novamente.")


def alterar(dict_contatos, nome):
    if nome in dict_contatos.keys():
        print('Alterar contato: ', dict_contatos[nome])
        contato = dict_contatos[nome]
        nome_novo = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        twitter = input("Digite o usuário de Twitter do contato: ")
        facebook = input("Digite o usuário de Facebook do contato: ")
        instagram = input("Digite o usuário de Instagram do contato: ")
        contato.nome = nome_novo
        contato.telefone = telefone
        contato.user_twitter = twitter
        contato.user_facebook = facebook
        contato.user_instagram = instagram
        if nome != nome_novo:
            del dict_contatos[nome]
            dict_contatos[nome_novo] = contato
    else:
        print("Nome não encontrado na lista de contatos. Tente novamente.")
    return dict_contatos


def excluir(dict_contatos, nome):
    print("Excluindo o contato:")
    imprimir_um(dict_contatos, nome)
    del dict_contatos[nome]
    return dict_contatos


def salvar(dict_contatos):
    arquivo = open('contatos.csv', 'w')
    arquivo.write('Nome,Telefone,Twitter,Facebook,Instagram')
    if len(dict_contatos) != 0:
        for contato in dict_contatos:
            arquivo.write(dict_contatos[contato].escrever_csv())
        print(f"{len(dict_contatos)} contatos salvos com sucesso!")
    else:
        print("Não existem dados para serem salvos.")
    arquivo.close()
