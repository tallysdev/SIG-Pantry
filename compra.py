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
            remover_compra()

        elif opcao == '4':
            get_precototal()

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
    print('\n \t4 - Consultar preços por data')
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
### 
### i = data retirada do dicionário cx
### j = índice dos produtos na data i
###
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
        data = input('\nInforme a data da compra desejada (AAAA-MM-DD):\t')
        if data in cx.keys():
            print('Data::\t', data)
            for j in range(0, len(cx[data])):
                print('\nProduto: \t', cx[data][j][0])
                print('Qtd. comprada: \t', cx[data][j][1])
                print('Preço: \t', cx[data][j][2])
### 
### data = autoexplicativo
### j = índice dos itens comprados na data 'data'
###
            input("Pressione enter para continuar...")

        else:
            print('\nNão existe compra com essa data.')
            print('Só existe esses produtos:')
            listartodos()

def editar_compra():
    cx = feira.get_datas()
    lembra = input('\nVoce lembra a Data da Compra?\t\n (S/N)\t')
    if lembra =='n' or lembra == 'N':
        print('\nVeja se está na lista abaixo \n')
        listartodos()

    data = input('\nInforme a data da compra que deseja editar (AAAA-MM-DD):\t')
    if data in cx.keys():
        print('Data::\t', data)
        for j in range(0, len(cx[data])):
            print('\nProduto: \t', cx[data][j][0])
            print('Qtd. comprada: \t', cx[data][j][1])
            nova_qtd = input("Nova quantidade: ");
            print('Preço: \t', cx[data][j][2])
            novo_preco = input("Novo preço: ")
            feira.feira[cx[data][j][0]][3] = nova_qtd
            feira.feira[cx[data][j][0]][4] = novo_preco
### 
### data = data retirada do dicionário cx
### j = índice dos itens comprados na data 'data'
### cx[data][j][0] = código de barras do produto
### 3, 4 = índices das informações de quantidade e preço na lista de produtos do módulo feira 
###
        input("Pressione enter para continuar...")
    
    else:
        print('\nNão existe compra com essa data.')
        print('Só existe esses produtos:')
        listartodos()

def remover_compra():
    cx = feira.get_datas()
    lembra = input('\nVoce lembra a Data da Compra?\t\n (S/N)\t')
    if lembra =='n' or lembra == 'N':
        print('\nVeja se está na lista abaixo \n')
        listartodos()

    data = input('\nInforme a data da compra que deseja remover (AAAA-MM-DD):\t')
    if data in cx.keys():
        toda = input("Deseja remover todos os produtos dessa compra (S/N)?")
        if toda.lower() == 's':
            for j in range(len(cx[data])):
                feira.feira.pop(cx[data][j][0])
        else:
            prods = []
            qnt = int(input("Quantos produtos deseja remover da compra? "))
            for i in range(qnt):
                prod = int(input("Informe o código do produto %d:" %(i+1)))
                prods.append(prod)
            for j in range(len(cx[data])):
                if cx[data][j][0] in prods:
                    feira.feira.pop(cx[data][j][0])

    else:
        print('\nNão existe compra com essa data.')
        print('Só existe esses produtos:')
        listartodos()

def get_precototal():
    cx = feira.get_datas()
    precos = {'total': 0}
    for i in cx.keys():
        preco_data = 0
        for j in range(0, len(cx[i])):
            try:
                precoUnit = float(cx[i][j][2])
                precos['total'] += precoUnit
                preco_data += precoUnit
            except:
                continue
        precos[i] = preco_data
    for i in precos.keys():
        print("\nData: %s" %i)
        print("Valor gasto: %.2f" %precos[i])
    input("Pressione enter para continuar...")



