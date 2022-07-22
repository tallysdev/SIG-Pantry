import datetime 
import os
import feira
import lscaegory
import controle

def textoliscom():
    os.system('cls')
    print('#########################################')
    print('########## Lista de Compras ############')
    print('#########################################')
    print('\n\t 1 - Lista de Compras com base em nos produtos que estão acabando ')
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

        opcao = textoliscom()
    
def compras_datadas():
    aux = datetime.date.today()
    aux1 = str(aux)
    datas = []
    cdt = []
    aux = feira.get_datas()
    for i in aux.keys():
        r = datetime.datetime.strptime(i, '%Y-%m-%d').date()
        datas.append(r)    
        for j in datas:  
            ww = 0
            ww = j
            aux2  = datetime.datetime.strptime(aux1,'%Y-%m-%d').date()
            delta = ww - aux2
            if delta.days < -9 and not j in cdt:
                cdt.append(j)
    return cdt

def ls_fal():
    lsfalz = feira.saidas
    dd = {}
    data = compras_datadas()
    datastr = []
    for i in data:
        aux = str(i)
        datastr.append(aux)

    for a in lsfalz.keys():
        for b in datastr:
            if lsfalz[a][6] == b:
                c = int(lsfalz[a][2])
                d = int(lsfalz[a][3])
                df = c - d
                if d < c:
                    dd.update({a:[[lsfalz[a][0]],[lsfalz[a][1]],[lsfalz[a][2]],[lsfalz[a][3]],[lsfalz[a][4]],[lsfalz[a][5]],[lsfalz[a][6]],df]})
    
    print('Precisa Comprar esses Produtos: ')
    for e in dd.keys():
        print('\n Nome: ', dd[e][0])
        print('\t','Em',  dd[e][7],'unidades')
        print()
    
    input('\n digite Enter para sair')


def ls_val():
    print()
    return
def ls_geral():
    print()
    return

def info_m():
    print()
    return