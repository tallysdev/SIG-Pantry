import os

categorias = {1: 'Limpeza', 2: 'Alimentação', 3: 'Higiene'}

def menu_produtos():
    os.system('clear')
    print('#########################################')
    print('############ Menu Produtos ##############')
    print('#########################################')
    print('\n \t1 - Cadastrar Categoria dos Produtos')
    print('\n \t2 - Editar Categoria dos Produtos')
    print('\n \t3 - Remover Categoria dos Produto')
    print("\n \t4 - Listar Categorias")
    print("\n \t5 - Sair")
    print('#########################################')
    opcao = int(input())

    while opcao != 5:
        if opcao == 1:
            cadastrar_categoria()
        elif opcao == 2:
            editar_categoria()
        elif opcao == 3:
            remover_categoria()
        elif opcao == 4:
            listar_categorias()
        
        os.system('clear')
        print('#########################################')
        print('############ Menu Produtos ##############')
        print('#########################################')
        print('\n \t1 - Cadastrar Categoria dos Produtos')
        print('\n \t2 - Editar Categoria dos Produtos')
        print('\n \t3 - Remover Categoria dos Produto')
        print("\n \t4 - Listar Categorias")
        print("\n \t5 - Sair")
        print('#########################################')
        opcao = int(input())

    return

def cadastrar_categoria():
    index = len(categorias)
    nome = input("Nome da nova categoria: ")
    categorias[index + 1] = nome
    
def listar_categorias():
    print("-------------------")
    print("--- Categorias ----")
    print("-------------------")
    for key in categorias.keys():
        print('--- %d - %s ---' %(key, categorias[key]))

def editar_categoria():
    listar_categorias()

    escolha = int(input("Qual categoria deseja editar? "))

    if not escolha in categorias.keys():
        print("Categoria inexistente!")
    else:
        novaCat = input("Novo nome da categoria: ")
        categorias[escolha] = novaCat

def remover_categoria():
    listar_categorias()

    escolha = int(input("Qual categoria deseja remover? "))

    if not escolha in categorias.keys():
        print("Categoria inexistente!")
    else:
        categorias.pop(escolha)
