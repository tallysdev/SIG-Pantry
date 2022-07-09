import produtos

import os

precos = []
itens_p = []

itens = []

feira = {}
codigosdebarra = []

def texto():
    os.system('cls')
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
            print('receba')

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
        codigob = input('informe o codigo de barra do produto\t')
        nome = input('Informe o nome do produto {}\t'.format(1+i))
        itens.append(nome)
        marca = input('Informe a marca do produto f\t')
        itens.append(marca)
        cat = input('Informe a categoria do produto f\t')
        itens.append(cat)
        uni = input('Informe a porção do produto (em kg) \n se o produto não for de alimentação pode reponder com a categoria\t')
        itens.append(uni)
        min = input('Informe a quantidade minima que voce precisa desse produto no mês\t')
        itens.append(min)
        atua = input('Informe a quantitade que voce comprou desse produto\t')
        itens.append(atua)
        preco = input('Informe o preço\t')
        itens.append(preco)
        precos.append(preco)
        data = input('Informe a validade do produto\t')
        itens.append(data)
        feira.update({codigob:itens})

    return


 # mais_um = True
    # print('Comece cadatrando os itens por categoria')
    # produtos.listar_categorias()
    # vf = input('A categoria quer voce deseja cadastrar está na lista?\n\t Sim ou Nao')
    # if vf !='Sim' and vf !='sim':
    #     produtos.cadastrar_categoria()
    #     produtos.listar_categorias()
    
    # chavef = int(input('Deseja Cadatrar itens em qual categoria?')) -1
    # while mais_um != False:
    #     item = input('informe o nome do produto')
    #     itens.append(item)
    #     itens_p.append(item)
    #     preco = input('informe o preço do produo')
    #     precos.append(preco)
    #     feira.update({chavef:itens})
    #     feira.update({'Preços':precos})
    #     feira.update({'Itens':itens_p})
    #     sair = input('Deseja cadastrar mais um produto?')
    #     if sair !='sim':
    #         mais_um = False
    # return
