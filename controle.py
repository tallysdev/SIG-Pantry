#controle de estoque

import feira
import compra
import os
import verdisp
import liscom



def textocontr():
    os.system('cls')
    print('#########################################')
    print('######### Controle de Dispensa ##########')
    print('#########################################')
    print('\n \t1 - Ver Dispensa')
    print('\n \t2 - Gerar listas de compras')
    print('\n \t3 - Cadastrar Saídas')
    print('\n \t4 - Informaçoes sobre o Controle de Dispensa')
    print("\n \t0 - Sair")
    print('#########################################')
    try:
        opcao = input()
    except:
        print("Opção inválida! Tente novamente.")
        opcao = input()
    
    return opcao

def menu_dispensa():
    opcao = textocontr()
    while opcao != '0':

        if opcao == '1':
            op = verdisp.menu_vd()
        
        elif opcao == '2':
            op = liscom.menu_lc()
            # print('em desenvolvimento')
        
        
        elif opcao == '3':
            op  = saidas()
        
        
        elif opcao == '4':
            op = info()

        opcao = textocontr()

def saidas():
    print(feira.saidas)
    lembra = input('Olá, Você lembra o codigo de barras do produto?')
    if lembra != 'sim' or lembra != 's':
        print('Então veja os produtos logo abaixo:')
        print()
        feira.listartodos()
    p = int(input('Gostaria de cadastrar quantos produtos?\t'))
    for i in range(p):
        x = int(input('Informe o codigo de barras do produto:\t'))
        nova=input('agora informe a quantidade que resta do produto {}'.format(feira.saidas[x][0]))
        if int(nova) > int(feira.saidas[x][3]):
            print('Aqui cadastramos saídas, não entradas, por favor informe a saida correta')
            nova=input('agora informe a quantidade que resta do produto {}'.format(feira.saidas[x][0]))
        else: 
            feira.saidas[x][3]=nova

    print(feira.saidas)
    input('\n\naa')
    return


def info():
    os.system('cls')
    print('\t Olá quem fala é a IA da sua dispensa, vou te mostrar agora como funciona esse modulo,\n A primeira opção é a de ver dispensa, nela você vai ter diversas formas de ver como está o seu estoque, por produtos, datas de validade, quantidade e categorias. \n\n\t A segunda opção é a de gerar lista compras, a função dela é fazer com base nos seus produtos cadastrados uma lista de compras especifica para cada produto que já acabou, está acabando ou necessita de mais compras para o mês ou produtos que já tenham vencido a data de validade. \n\n\t A terceira opção é uma das mais importantes se não a mais importante desse programa, lá você vai cadastrar o produtos você vai usando no decorrer do dia-a-dia, ela é fundamental para o bom funcionaento da gestão do estoque.\n\n\t A quarta sou eu, parabéns por chegar até aqui.\n\n\tA ultima opção é a de voltar para o meu anterior')
    input('\nPressione Enter para prosseguir...\t')

    return