import category
import pickle
import datetime

import os

precos = []
itens_p = []

feira = {}

try:
    arqFeira = open('prods.docx', 'rb')
    feira = pickle.load(arqFeira)
    arqFeira.close()
except:
    arqFeira = open('prods.docx', 'wb')
    arqFeira.close()

saidas = feira

codigosdebarra = []

def texto():
    os.system('cls')
    print('#########################################')
    print('############ Menu Produtos ##############')
    print('#########################################')
    print('\n 1 - Cadastrar Produtos')
    print('\n 2 - Editar Produtos')
    print('\n 3 - Remover Produtos')
    print('\n 4 - Pesquisar nos Produtos')
    print('\n 5 - Acessar Categorias')
    print("\n 0 - Sair")
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
        
        arqFeira = open('prods.docx', 'wb')
        pickle.dump(feira, arqFeira)
        arqFeira.close()

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

        arqFeira = open('prods.docx', 'wb')
        pickle.dump(feira, arqFeira)
        arqFeira.close()
    
    else:
       print('\nNão exite produto com esse nome.')

def remover_produto():
    print('#########################################')
    print('########   Remover Produtos  ############')
    print('#########################################')
    chaveaux = int(input('\nInforme o codigo de barras do produto desejado:\t'))
    if chaveaux in feira.keys():
        feira.pop(chaveaux)
        arqFeira = open('prods.docx', 'wb')
        pickle.dump(feira, arqFeira)
        arqFeira.close()
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