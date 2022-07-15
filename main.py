#modulo de controle produto.
#modulo de estoque de itens.
#modulo de itens.
import os
import feira
import compra
import controle

def infos_projeto():
    print('''
    Dupla: Thomas Almeida(20220034970) e Tallys Aureliano(20220034890)
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
        op = controle.menu_dispensa()

    elif opcao == 9:
        infos_projeto()

    opcao = menu_principal()
