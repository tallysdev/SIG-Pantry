import os
import feira
import category
preco = []
cat = {}

def textovd():
    os.system('cls')
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
    os.system('cls')
    for i in sorted(feira.feira, key = feira.feira.get):
        print('\n Nome: ',feira.feira[i][0])
        print('\t','Categoria:',  feira.feira[i][1])
        print('\t','Quantidade atual:', feira.feira[i][3])
        print('\t','Preço:', feira.feira[i][4],)
        print('\t','Validade: ', feira.feira[i][5],'\n')
    input('Digite Enter para seguir...')

    return

def validadev():
    os.system('cls')    
    dade = feira.get_val()
    for i in dade.keys():
            print('----------------------\n')
            print('Validade: ', i)
            for j in range(0, len(dade[i])):
                print('\t','Produto: ', dade[i][j][0])
                print('\t','Categoria: ', dade[i][j][1])
                print('\t','Quantidade comprada: ', dade[i][j][2])
                print('\t','Preço: ', dade[i][j][3],'\n')
    
    input('Digite Enter para seguir...')
    return

def precov():
    os.system('cls')
    for j in feira.feira.keys():    
        preco.append(feira.feira[j][4])
        
    preco.sort()

    for v in preco:
        for i in feira.feira.keys():
            if v == feira.feira[i][4]:
                print('----------------------\n')
                print('\n Preço: ',v)
                print('\t','Nome:',feira.feira[i][0])
                print('\t','Categoria:',  feira.feira[i][1])
                print('\t','Quantidade atual:', feira.feira[i][3])
                print('\t','Validade:', feira.feira[i][4],'\n')
    
    input('Digite Enter para seguir...')

    return

def categoriav():
    os.system('cls')
    cat = feira.get_cat()
    for i in cat.keys():
            print('----------------------\n')
            print('Categoria: ', i)
            for j in range(0, len(cat[i])):
                print('\t','Produto: ', cat[i][j][0])
                print('\t','Qtd. comprada: ', cat[i][j][1])
                print('\t','Preço: ', cat[i][j][2])
                print('\t','Validade: ', cat[i][j][3],'\n')
    
    input('Digite Enter para seguir...')
    
    return  
