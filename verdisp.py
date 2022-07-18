def textovd():
    print('#########################################')
    print('########## Veja sua Dispensa ############')
    print('#########################################')
    print()
    print('\t 1 - Ver por ordem alfabetica ')
    print('\t 2 - Ver por data de validade \n\t "da mais recente a mais antiga" ')
    print('\t 3 - Ver por preço \n\t "do mais barato ao mais caro" ')
    print('\t 4 - Ver por categoria ')
    try:
        opcao = int(input())
    except:
        print("Opção inválida! Tente novamente.")
        opcao = int(input())
    return opcao

def menu_vd():
    opcao = textovd
    while opcao != 0:
        
        if opcao == 1:
            print()
        elif opcao == 2:
            print()
        elif opcao == 3:
            print()
        elif opcao == 4:
            print()
    return

def alfabeticav():
    print()
    return

def validadev():
    print()
    return

def precov():
    print()
    return

def categoriav():
    print()
    return