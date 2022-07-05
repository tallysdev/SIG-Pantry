import os

categorias = ['Limpeza', 'Alimentação', 'Higiene']

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

    escolha = int(input("Qual categoria deseja editar? ")) - 1

    if(escolha >= len(categorias) or escolha <= 0):
        print("Categoria inexistente!")
    else:
        novaCat = input("Novo nome da categoria: ")
        categorias[escolha] = novaCat

def remover_categoria():
    listar_categorias()

    escolha = int(input("Qual categoria deseja remover? ")) - 1

    if(escolha >= len(categorias) or escolha <= 0):
        print("Categoria inexistente!")
    else:
        categorias.pop(escolha);
