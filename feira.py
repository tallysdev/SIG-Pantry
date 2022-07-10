import produtos

import os

precos = []
itens_p = []



feira = {1:['fabs totosa','1','2','3','4','5','6','7','8',]}
codigosdebarra = []

def texto():
    
    print('#########################################')
    print('############ Menu Produtos ##############')
    print('#########################################')
    print('\n \t1 - Cadastrar Produtos')
    print('\n \t2 - Editar Produtos')
    print('\n \t3 - Remover Produtos')
    print("\n \t4 - Listar Produtos")
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = input()
    return opcao

def menu_feira():
    
    opcao = texto()
    while opcao !='0':

        if opcao == '1':
            # def algo()
            cadastrar_feira()
        
        elif opcao == '2':
            # def algo()
            print('receba')

        elif opcao == '3':
            # def algo()
            print('receba')

        elif opcao == '4':
            # def algo()
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
        itens.append(nome)
        
        marca = input('Informe a marca de {}\t' .format(nome))
        itens.append(marca)
        
        cat = input('Informe a categoria de {}\t' .format(nome))
        itens.append(cat)
        
        uni = input('Informe a porção de {} (em kg)\n se o produto não for de alimentação pode reponder com a categoria\t'.format(nome))
        itens.append(uni)
        
        min = input('Informe a quantidade minima que voce precisa de {} no mês\t'.format(nome))
        itens.append(min)
        
        atua = input('Informe a quantitade que voce comprou de {}\t' .format(nome))
        itens.append(atua)
        
        preco = input('Informe o preço de {}\t' .format(nome))
        itens.append(preco)
        precos.append(preco)
        
        data = input('Informe a validade de {}\t' .format(nome))
        itens.append(data)
        feira.update({codigob:itens})

    return

def listar():
    chaveaux = int(input('Informe o codigo de barras/t'))
    print('nome', feira[chaveaux][0])
    print('nome é', feira[chaveaux][1])
    print('nome é', feira[chaveaux][2])
    print('nome é', feira[chaveaux][3])
    print('nome é', feira[chaveaux][4])
    print('nome é', feira[chaveaux][5])
    print('nome é', feira[chaveaux][6])
    print('nome é', feira[chaveaux][7])
    print('nome é', feira[chaveaux][8])

    return
