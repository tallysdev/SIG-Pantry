import category

import datetime

import os

precos = []
itens_p = []

feira = {   1:['pao','1','10','5',2.5,'2023-07-10','2022-07-10'],
            2:['cebola','2','5','2',5.8,'2023-07-10','2022-07-10'],
            3:['tomate','3','10','3',6.9,'2023-07-10','2022-07-10'],
            4:['aipim','1','10','8',15.1,'2023-07-10','2022-07-11'],
            5:['berinjela','2','10','6',1.0,'2023-07-10','2022-07-12'],
            6:['janela','3','10','5',2.9,'2023-07-10','2022-07-13'],
            7:['alface','1','10','3',3.0,'2023-07-10','2022-07-13'],
            8:['cururu','2','10','5',7.0,'2023-07-10','2022-07-14']
            
            }

saidas = feira

codigosdebarra = []

def texto():
    os.system('cls')
    print('#########################################')
    print('############ Menu Produtos ##############')
    print('#########################################')
    print('\n \t1 - Cadastrar Produtos')
    print('\n \t2 - Editar Produtos')
    print('\n \t3 - Remover Produtos')
    print('\n \t4 - Pesquisar nos Produtos')
    print('\n \t5 - Acessar Categorias')
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = input()
    return opcao

def menu_feira():
    
    opcao = texto()
    while opcao !='0':

        if opcao == '1':
            cadastrar_feira()
        
        elif opcao == '2':
            editar_produtos()

        elif opcao == '3':
            remover_produto()

        elif opcao == '4':
            listar()

        elif opcao == '4':
            op = category.menu_category()

        opcao = texto()
            
    return

def cadastrar_feira():
    os.system('cls')
    print('#########################################')
    print('#######   Cadastrar Produtos  ###########')
    print('#########################################')
    print('\n Comece cadastrando os itens por categoria')
    category.listar_categorias()
    vf = input('A categoria quer voce deseja cadastrar está na lista?\n\t Sim ou Nao')
    if vf !='Sim' and vf !='sim':
        category.cadastrar_categoria()
        category.listar_categorias()
    p=int(input('\n\t Informe quantos produtos deseja cadastrar \t'))
    for i in range(p):
        itens = []
        
        codigob = input('\nInforme o codigo de barra do produto:{}\t'.format(i+1))
        
        nome = input('Informe o nome do produto {}:\t'.format(i+1))
        
        cat = input('Informe a categoria de {}:\t' .format(nome))
        
        qtd_min = input('Informe a quantidade minima que voce precisa de {} no mês\t'.format(nome))
        
        qtd = input('Informe a quantitade que voce comprou de {}:\t' .format(nome))
        
        preco = input('Informe o preço de {}:\t' .format(nome))
        precos.append(preco)
        
        data = input('Informe a validade de {}: (DD-MM-AAAA)\t' .format(nome))

        data_compra = datetime.date.today()

        feira.update({codigob:[nome,cat,qtd_min,qtd,preco,data,data_compra]})

    return

def listartodos():
    for i in feira.keys():
        print('Código de Barras:\t', i)
        print('Nome:\t',feira[i][0])
        print('Categoria:\t', feira[i][1])
        print('Quantidade mínima:\t', feira[i][2])
        print('Quantidade comprada:\t', feira[i][3])
        print('Preço:\t', feira[i][4])
        print('Data de validade:\t', feira[i][5],'\n')
    input("Pressione enter para continuar...")
    return

def listar():
    print('#########################################')
    print('##########   Listar Produtos  ###########')
    print('#########################################')
    lembra = input('\nVoce lembra do Código de barras do produto?\t\n (S/N)')
    if lembra =='n' or lembra == 'N':
        print('\nVeja se está na lista abaixo \n')
        listartodos()
    else:
        chaveaux = input('\nInforme o codigo de barras do produto desejado:\t')
        if chaveaux in feira.keys():
            print('Código de Barras:\t', chaveaux)
            print('Nome:\t',feira[chaveaux][0])
            print('Categoria:\t', feira[chaveaux][1])
            print('Quantidade mínima:\t', feira[chaveaux][2])
            print('Quantidade comprada:\t', feira[chaveaux][3])
            print('Preço:\t', feira[chaveaux][4])
            print('Data de validade:\t', feira[chaveaux][5], '\n')
        
        else:
            print('\nNão exite produto com esse nome.')
            print('Só existe esses produtos:')
            listartodos()

    return

def editar_produtos():
    print('#########################################')
    print('#########   Editar Produtos  ############')
    print('#########################################')
    chaveaux = input('\nInforme o codigo de barras do produto desejado:\t')
    
    if chaveaux in feira.keys():

        nome = input('Informe o nome do produto:\t')
        
        cat = input('Informe a categoria de {}\t' .format(nome))
        
        qtd_min = input('Informe a quantidade minima que voce precisa de {} no mês\t'.format(nome))
        
        qtd = input('Informe a quantitade que voce comprou de {}\t' .format(nome))
        
        preco = input('Informe o preço de {}\t' .format(nome))
        precos.append(preco)
        
        data = input('Informe a validade de {}\t' .format(nome))

        feira.update({chaveaux:[nome,cat,qtd_min,qtd,preco,data,feira[chaveaux][8]]})
    
    else:
       print('\nNão exite produto com esse nome.')

def remover_produto():
    print('#########################################')
    print('########   Remover Produtos  ############')
    print('#########################################')
    chaveaux = input('\nInforme o codigo de barras do produto desejado:\t')
    if chaveaux in feira.keys():
        feira.pop(chaveaux)
        print('Pronto, o produto {} foi removido'.format(chaveaux))
        
        
    else:
       print('\nNão exite produto com esse nome.')

def get_datas():
    datas = {}
    for i in feira.keys():
        data = feira[i][6]
        if data in datas.keys():
            datas[data].append([i , feira[i][3], feira[i][4]])
        else:
            datas[data] = [[i, feira[i][3], feira[i][4]]]
    return datas

def get_cat():
    auxcat = {}
    for i in feira.keys():
        cat = feira[i][1]
        if cat in auxcat.keys():
            auxcat[cat].append([feira[i][0], feira[i][3], feira[i][4], feira[i][5]])
        else:
            auxcat[cat] = [[feira[i][0], feira[i][3], feira[i][4], feira[i][5]]]
    return auxcat

def get_val():
    vali = {}
    for i in feira.keys():
        val = feira[i][5]
        if val in vali.keys():
            vali[val].append([feira[i][0], feira[i][1], feira[i][3], feira[i][4]])
        else:
            vali[val] = [[feira[i][0], feira[i][1], feira[i][3], feira[i][4]]]
    return vali