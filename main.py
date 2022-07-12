#modulo de controle produto.
#modulo de estoque de itens.
#modulo de itens.
import os
import feira
import compra

def infos_projeto():
    print('''
    Dupla: Thomas Almeida e Tallys Aureliano
    Projeto: SIG_Pantry
    Versão: 0.01''')
    input("Pressione enter para continuar..")

def menu_principal():
    os.system('cls')
    print('#########################################')
    print('########## Menu Principal ###############')
    print('#########################################')
    print()
    print('\t\t introdução .....')
    print('\n \t1 - Modolo de Produtos')
    print('\n \t2 - Modulo de Compras')
    print('\n \t3 - Modulo de Controle de estoque')
    print('\n \t9 - Informações do projeto')
    print("\n \t0 - Sair")
    print('#########################################')
    try:
        opcao = int(input())
    except:
        print("Opção inválida! Tente novamente.")
        opcao = int(input())
    return opcao

opcao = menu_principal()
while opcao != 0:

    if opcao == 1 :
        op = feira.menu_feira()
    elif opcao == 2 :
        op = compra.menu_compra()

    elif opcao == 3 :
        print('#########################################')
        print('############ Menu de Estoque ##############')
        print('#########################################')
        print()
        print('\n \t1 - Cadastrar Saídas')
        print('\n \t2 - Reposiçaõ de items')
        print('\n \t3 - Estoque por Validade')
        print("\n \t4 - Proxima Compra")
        print("\n \t5 - Criar feria padrão")
        print("\n \t6 - Editar feira padrão")
        print('#########################################')

    elif opcao == 9:
        infos_projeto()

    opcao = menu_principal()
