import os

categorias = []

def menu_produtos():
    os.system('clr')
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
        elif opcao == 4:
            listar_categorias()
        
        os.system('clr')
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

    return opcao

def cadastrar_categoria():
    nome = input("Nome da nova categoria: ")
    categorias.append(nome)
    
def listar_categorias():
    print("-------------------")
    print("--- Categorias ----")
    print("-------------------")
    for i in range(0, len(categorias)):
        print('--- %d - %s ---' %(i+1, categorias[i]))

def editar_categoria():
    listar_categorias()


