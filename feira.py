import produtos

import os

precos = []
itens_p = []



feira = {1:['','','','','','','','','',]}
codigosdebarra = []

def texto():
    
    print('#########################################')
    print('############ Menu Produtos ##############')
    print('#########################################')
    print('\n \t1 - Cadastrar Produtos')
    print('\n \t2 - Editar Produtos')
    print('\n \t3 - Remover Produtos')
    print("\n \t4 - Pesquisar nos Produtos")
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

        opcao = texto()
            
    return

def cadastrar_feira():
    os.system('cls')
    print('#########################################')
    print('#######   Cadastras Produtos  ###########')
    print('#########################################')
    print('\n Comece cadastrando os itens por categoria')
    produtos.listar_categorias()
    vf = input('A categoria quer voce deseja cadastrar está na lista?\n\t Sim ou Nao')
    if vf !='Sim' and vf !='sim':
        produtos.cadastrar_categoria()
        produtos.listar_categorias()
    p=int(input('\n\t Informe quantos produtos deseja cadastrar \t'))
    for i in range(p):
        itens = []
        
        codigob = input('\ninforme o codigo de barra do produto {}\t'.format(i+1))
        
        nome = input('Informe o nome do produto {}\t'.format(i+1))
        
        marca = input('Informe a marca de {}\t' .format(nome))
        
        cat = input('Informe a categoria de {}\t' .format(nome))
        
        uni = input('Informe a porção de {} (em kg)\n se o produto não for de alimentação pode reponder com a categoria\t'.format(nome))
        
        min = input('Informe a quantidade minima que voce precisa de {} no mês\t'.format(nome))
        
        atua = input('Informe a quantitade que voce comprou de {}\t' .format(nome))
        
        preco = input('Informe o preço de {}\t' .format(nome))
        precos.append(preco)
        
        data = input('Informe a validade de {}\t' .format(nome))

        feira.update({codigob:[nome,marca,cat,uni,min,atua,preco,data]})

    return

def listartodos():
    for i in feira.keys():
            print('\nCódigo de Barras:\t', i)
            print('Nome:\t', feira[i][0])
            print('Marca:\t', feira[i][1])
            print('Categoria:\t', feira[i][2])
            print('Unidade de medida:\t', feira[i][3])
            print('Quantidade mínima necessária:\t', feira[i][4])
            print('Quantidade comprada:\t', feira[i][5])
            print('Preço:\t', feira[i][6])
            print('Data de validade:\t', feira[i][7])
    return

def listar():
    lembra = input('Voce lembra do Código de barras do produto?\t\n (S/N)')
    if lembra =='nao':
        print('\nVeja se está na lista abaixo \n')
        listartodos()

    else:
        chaveaux = input('\nInforme o codigo de barras do produto desejado:\t')
        if chaveaux in feira:
            print('Código de Barras:\t', chaveaux)
            print('Nome:\t',feira([chaveaux][0]))
            print('Marca:\t', feira[chaveaux][1])
            print('Categoria:\t', feira[chaveaux][2])
            print('Unidade de medida:\t', feira[chaveaux][3])
            print('Quantidade mínima necessária:\t', feira[chaveaux][4])
            print('Quantidade comprada:\t', feira[chaveaux][5])
            print('Preço:\t', feira[chaveaux][6])
            print('Data de validade:\t', feira[chaveaux][7])
        
        else:
            print('\nNão exite produto com esse nome.')


    return

def editar_produtos():
    chaveaux = input('\nInforme o codigo de barras do produto desejado:\t')
    
    if chaveaux in feira:

        nome = input('Informe o nome do produto:\t')
        
        marca = input('Informe a marca de {}\t' .format(nome))
        
        cat = input('Informe a categoria de {}\t' .format(nome))
        
        uni = input('Informe a porção de {} (em kg)\n se o produto não for de alimentação pode reponder com a categoria\t'.format(nome))
        
        min = input('Informe a quantidade minima que voce precisa de {} no mês\t'.format(nome))
        
        atua = input('Informe a quantitade que voce comprou de {}\t' .format(nome))
        
        preco = input('Informe o preço de {}\t' .format(nome))
        precos.append(preco)
        
        data = input('Informe a validade de {}\t' .format(nome))

        feira.update({chaveaux:[nome,marca,cat,uni,min,atua,preco,data]})
    
    else:
       print('\nNão exite produto com esse nome.')

def remover_produto():
    chaveaux = input('\nInforme o codigo de barras do produto desejado:\t')
    if chaveaux in feira:
        print('Pronto, o produto {} foi removido'.format(chaveaux))
        print(feira.pop([chaveaux]))
    else:
       print('\nNão exite produto com esse nome.')
