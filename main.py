#modulo de controle produto.
#modulo de estoque de itens.
#modulo de itens.
import os
import produtos

def menu_principal():
    os.system('clr')
    print('#########################################')
    print('########## Menu Principal ###############')
    print('#########################################')
    print()
    print('\t\t introdução .....')
    print('\n \t1 - Modolo de Produtos')
    print('\n \t2 - M1odulo de Feira')
    print('\n \t3 - Modulo de Controle de estoque')
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = int(input())
    return opcao

opcao = menu_principal()
while opcao != 0:

    if opcao == 1 :
        op = produtos.menu_produtos()

    elif opcao == 2 :
        print('#########################################')
        print('############ Menu Feira ##############')
        print('#########################################')
        print()
        print('\n \t1 - Cadastrar item da feira')
        print('\n \t2 - Editar editar item da feira')
        print('\n \t3 - Remover item da feira')
        print("\n \t4 - Listar feira")
        print('#########################################')

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

    os.system('clc')
    print('#########################################')
    print('########## Menu Principal ###############')
    print('#########################################')
    print()
    print('\t\t introdução .....')
    print('\n \t1 - Modolo de Produtos')
    print('\n \t2 - Modulo de Feira')
    print('\n \t3 - Modulo de Controle de estoque')
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = int(input())
