import os
import feira


def textoliscom():
    os.system('cls')
    print('#########################################')
    print('########## Lista de Compras ############')
    print('#########################################')
    print('\n\t 1 - Lista de Compras com base em nos alimentos faltando ')
    print('\n\t 2 - Lista de Compras com base na data de Validade  ')
    print('\n\t 3 - Lista de Compras por categorias ')
    print('\n\t 4 - Lista de Compras Geral ')
    print('\n\t 5 - informações sobre este modulo ')
    print('\n\t 0 - Sair ')
    try:
        opcao = int(input())
    except:
        print("Opção inválida! Tente novamente.")
        opcao = int(input())
    return opcao

def menu_lc():
    opcao = textoliscom()

    while opcao !=0:

        if opcao == 1:
            op = ls_fal()
        elif opcao == 2:
            op = ls_val()
        elif opcao == 3:
            op = lscaegory.menulsc()
        elif opcao == 4:
            op = ls_geral()
        elif opcao == 5:
            op = info_m()
    return

def ls_fal():
    print()

def ls_val():
    print()

def ls_geral():
    print()

def info_m():
    print()