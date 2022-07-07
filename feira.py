import produtos

import os

precos = []
itens_p = []

itens = []

feira = {}



def menu_feira():
    os.system('clear')
    print('#########################################')
    print('############ Menu Feria ##############')
    print('#########################################')
    print('\n \t1 - Cadastrar Feira')
    print('\n \t2 - Editar Feira')
    print('\n \t3 - Remover Feira ou \n\tItens da Ultima feira')
    print("\n \t4 - Listar Feira")
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = input()

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

        os.system('clear')
        print('#########################################')
        print('############ Menu Feria ##############')
        print('#########################################')
        print('\n \t1 - Cadastrar Feira')
        print('\n \t2 - Editar Feira')
        print('\n \t3 - Remover Feira ou \n\tItens da Ultima feira')
        print("\n \t4 - Listar Feira")
        print("\n \t0 - Sair")
        print('#########################################')
        opcao = input()
            
    return

def cadastrar_feira():
    mais_um = True
    print('Comece cadatrando os itens por categoria')
    produtos.listar_categorias()
    vf = input('A categoria quer voce deseja cadastrar está na lista?\n\t Sim ou Nao')
    if vf !='Sim' and vf !='sim':
        produtos.cadastrar_categoria()
        produtos.listar_categorias()
    
    chavef = int(input('Deseja Cadatrar itens em qual categoria?')) -1
    while mais_um != False:
        item = input('informe o nome do produto')
        itens.append(item)
        itens_p.append(item)
        preco = input('informe o preço do produo')
        precos.append(preco)
        feira.update({chavef:itens})
        feira.update({'Preços':precos})
        feira.update({'Itens':itens_p})
        sair = input('Deseja cadastrar mais um produto?')
        if sair !='sim':
            mais_um = False
    return

print(feira)

def listar_feira():
    print(hehe)
    