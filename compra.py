import datetime
import feira
import category

# compras do dia x
cx = {}

cp2 =[]

z = []

tt = []



tam = len(feira.datasdecompras)
auxtam = tam - 1
for i in feira.feira.keys():
    auxtam = auxtam - 1
    if feira.datasdecompras[auxtam] == feira.feira[i][8]:
        tt.append(i)
        cx[feira.feira[i][8]] = [tt,'preços']
    else:
        cx[feira.feira[i][8]] = [i,'preços']
    
print(cx)

def menu_compra():
    opcao = texto()
    while opcao !='0':

        if opcao == '1':
            pesquisa_compra()
        
        elif opcao == '2':
            print()
            # editar_produtos()

        elif opcao == '3':
            print()
            # remover_produto()

        elif opcao == '4':
            print()
            # listar()

        elif opcao == '4':
            op = category.menu_category()

        opcao = texto()
    return

def texto():
    
    print('#########################################')
    print('############ Menu Compras ##############')
    print('#########################################')
    print('\n \t1 - Pesquisar nas Compras')
    print('\n \t3 - Remover Remover Compra')
    print('\n \t4 - Acessar Produtos')
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = input()
    return opcao

def listartodos():
    for i in cx.keys():
            print('\nData::\t', i)
            print('Produtos por codigo de barra\t', cx[i][0])
            print('Preço\t', cx[i][1])
    return

def pesquisa_compra():

    print('#########################################')
    print('##########   Listar Compras  ###########')
    print('#########################################')
    lembra = input('\nVoce lembra a Data da Compra?\t\n (S/N)\t')
    if lembra =='n' or lembra == 'N':
        print('\nVeja se está na lista abaixo \n')
        listartodos()

    else:
        chaveaux = datetime.date(input('\nInforme a data da compra desejada:\t'))
        if chaveaux in feira.keys():
            print('\nData::\t', chaveaux)
            print('Produtos por codigo de barra\t', cx[chaveaux][0])
            print('Preço\t', cx[chaveaux][1])
        
        else:
            print('\nNão Compra com essa Data.')
            print('Só existe esses produtos:')
            listartodos()