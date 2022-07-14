#controle de estoque

import feira
import compra
import os

def textocontr():
    os.system('cls')
    print('#########################################')
    print('######### Controle de Dispença ##########')
    print('#########################################')
    print('\n \t1 - Ver Dispença')
    print('\n \t2 - Gerar listas de compras')
    print('\n \t3 - Cadastrar Saídas')
    print('\n \t4 - Informaçoes sobre o Controle de Dispença')
    print("\n \t0 - Sair")
    print('#########################################')
    try:
        opcao = int(input())
    except:
        print("Opção inválida! Tente novamente.")
        opcao = int(input())
    return opcao

def menu_dispenca():
    opcao = textocontr()
    while opcao != '0':

        if opcao == '1':
            print('hehe')
        
        elif opcao == '2':
            print('hehe')
        
        
        elif opcao == '3':
            print('hehe')
        
        
        elif opcao == '4':
            print('hehe')

    return
    