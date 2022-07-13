import datetime
import feira
import category
import os

def menu_compra():
    opcao = texto()
    while opcao !='0':

        if opcao == '1':
            pesquisa_compra()
        
        elif opcao == '2':
            editar_compra()

        elif opcao == '3':
            print()
            # remover_produto()

        elif opcao == '4':
            op = category.menu_category()

        opcao = texto()
    return

def texto():
    os.system('cls')
    print('#########################################')
    print('############ Menu Compras ##############')
    print('#########################################')
    print('\n \t1 - Pesquisar nas Compras')
    print('\n \t2 - Editar Compra')
    print('\n \t3 - Remover Compra')
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = input()
    return opcao

def listartodos():
    cx = feira.get_datas()
    print('#########################################')
    print('##########   Listar Compras  ############')
    print('#########################################')
    for i in cx.keys():
            print('----------------------\n')
            print('Data::\t', i)
            for j in range(0, len(cx[i])):
                print('\nProduto: \t', cx[i][j][0])
                print('Qtd. comprada: \t', cx[i][j][1])
                print('Preço: \t', cx[i][j][2])
    input("\nPressione enter para continuar...")
    return

def pesquisa_compra():
    cx = feira.get_datas()
    print('#########################################')
    print('##########   Pesquisar Compra  ##########')
    print('#########################################')
    lembra = input('\nVoce lembra a Data da Compra?\t\n (S/N)\t')
    if lembra =='n' or lembra == 'N':
        print('\nVeja se está na lista abaixo \n')
        listartodos()
    else:
        chaveaux = input('\nInforme a data da compra desejada (AAAA-MM-DD):\t')
        if chaveaux in cx.keys():
            print('Data::\t', chaveaux)
            for j in range(0, len(cx[chaveaux])):
                print('\nProduto: \t', cx[chaveaux][j][0])
                print('Qtd. comprada: \t', cx[chaveaux][j][1])
                print('Preço: \t', cx[chaveaux][j][2])
            input("Pressione enter para continuar...")
        
        else:
            print('\nNão Compra com essa Data.')
            print('Só existe esses produtos:')
            listartodos()

def editar_compra():
    cx = feira.get_datas()
    lembra = input('\nVoce lembra a Data da Compra?\t\n (S/N)\t')
    if lembra =='n' or lembra == 'N':
        print('\nVeja se está na lista abaixo \n')
        listartodos()

    chaveaux = input('\nInforme a data da compra que deseja editar (AAAA-MM-DD):\t')
    if chaveaux in cx.keys():
        print('Data::\t', chaveaux)
        for j in range(0, len(cx[chaveaux])):
            print('\nProduto: \t', cx[chaveaux][j][0])
            print('Qtd. comprada: \t', cx[chaveaux][j][1])
            nova_qtd = input("Nova quantidade: ");
            print('Preço: \t', cx[chaveaux][j][2])
            novo_preco = input("Novo preço: ")
            feira.feira[cx[chaveaux][j][0]][3] = nova_qtd
            feira.feira[cx[chaveaux][j][0]][4] = novo_preco
        input("Pressione enter para continuar...")
    
    else:
        print('\nNão Compra com essa Data.')
        print('Só existe esses produtos:')
        listartodos()

