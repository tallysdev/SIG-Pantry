import feira
import category
preco = []
cat = {}

def textovd():
    print('#########################################')
    print('########## Veja sua Dispensa ############')
    print('#########################################')
    print('\n\t 1 - Ver por ordem alfabetica ')
    print('\n\t 2 - Ver por data de validade \n\t "da mais recente a mais antiga" ')
    print('\n\t 3 - Ver por preço \n\t "do mais barato ao mais caro" ')
    print('\n\t 4 - Ver por categoria ')
    print('\n\t 0 - Sair ')
    try:
        opcao = int(input())
    except:
        print("Opção inválida! Tente novamente.")
        opcao = int(input())
    return opcao

def menu_vd():
    opcao = textovd()
    while opcao != 0:
        
        if opcao == 1:
            op = alfabeticav()
        elif opcao == 2:
            op = validadev()
        elif opcao == 3:
            op = precov()
        elif opcao == 4:
            op = categoriav()
        
        opcao = textovd()
    return

def alfabeticav():
    
    for i in sorted(feira.feira, key = feira.feira.get):
        print('\n Nome:',feira.feira[i][0], '\n\t','Categoria:',  feira.feira[i][1],'Quantidade atual:', feira.feira[i][3],'Preço:', feira.feira[i][4],'\n')


    return

def validadev():
    print()
    return

def precov():
    for j in feira.feira.keys():    
        preco.append(feira.feira[j][4])
        
    preco.sort()

    for v in preco:
        for i in feira.feira.keys():
            if v == feira.feira[i][4]:
                print('\n Preço:',v,'\n\t Nome:',feira.feira[i][0],', ','Categoria:',  feira.feira[i][1],', ','Quantidade atual:', feira.feira[i][3],'\n')
    return

def categoriav():
    
    # def get_datas():
    # datas = {}
    # for i in feira.keys():
    #     data = feira[i][6]
    #     if data in datas.keys():
    #         datas[data].append([i , feira[i][3], feira[i][4]])
    #     else:
    #         datas[data] = [[i, feira[i][3], feira[i][4]]]
    # return datas

    # def listartodos():
    # cx = feira.get_datas()
    # print('#########################################')
    # print('##########   Listar Compras  ############')
    # print('#########################################')
    # for i in cx.keys():
    #         print('----------------------\n')
    #         print('Data::\t', i)
    #         for j in range(0, len(cx[i])):
    #             print('\nProduto: \t', cx[i][j][0])
    #             print('Qtd. comprada: \t', cx[i][j][1])
    #             print('Preço: \t', cx[i][j][2])


    for i  in category.categorias.keys():
        cat.append(i)
        for j in feira.feira.values():
            print()
            if j[1] == str(i):
                print(j[1])
    
    return