from contato_controller import consultar, inserir, imprimir_todos, imprimir_um, alterar, excluir, salvar


def menu():
    dict_contatos = {}
    dict_contatos = consultar(dict_contatos)
    while True:
        action = input("Escolha uma ação para a lista de contatos usando a letra entre parênteses:\n"
                       "Consultar Todos (C)\nConsultar Um (U)\nInserir (I)\nAlterar (A)\nRemover (R)\n"
                       "Gravar (G)\nSair (S)\n").upper()
        if action == 'I':
            print("Inserir um contato novo na lista")
            dict_contatos = inserir(dict_contatos)
        elif action == 'C':
            print("Consultar todos os contatos da lista")
            imprimir_todos(dict_contatos)
        elif action == 'U':
            print("Consultar um contato da lista")
            nome = input("Digite o nome do contato a ser consultado: ")
            imprimir_um(dict_contatos, nome)
        elif action == 'A':
            print("Alterar um contato existente na lista")
            nome = input("Digite o nome do contato a ser alterado: ")
            dict_contatos = alterar(dict_contatos, nome)
        elif action == 'R':
            print("Remover um contato da lista")
            nome = input("Digite o nome do contato a ser removido: ")
            dict_contatos = excluir(dict_contatos, nome)
        elif action == 'G':
            print("Gravar alterações")
            salvar(dict_contatos)
        elif action == 'S':
            print("Sair do menu")
            resp = input("Deseja salvar os dados da sessão? S ou N: ").upper()
            if resp == 'S':
                salvar(dict_contatos)
            break
        else:
            print("Comando inválido. Digite um novo comando")


menu()
