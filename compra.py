import feira

# compras_do_dia_x
cx = {}
# codigosbarras_dos_produtos
cp =[]
z = []
# for i in feira.feira.keys():
#   cp.append(i)  
# print(cp)

for j in feira.datasdecompras:
    for i in feira.feira.keys():
        if feira.feira[i][8] == j:
            cp.append(i)
            cx.update({j:[cp,'somapreco']})


# cx.update({j:[cp,'somapreco']})
print(cx)

def menu_compra():
    print()
    return

def texto():
    
    print('#########################################')
    print('############ Menu Compras ##############')
    print('#########################################')
    print('\n \t1 - Pesquidar nas Compras')
    print('\n \t2 - Editar Compra')
    print('\n \t3 - Remover Remover Compra')
    print('\n \t4 - Acessar Produtos')
    print("\n \t0 - Sair")
    print('#########################################')
    opcao = input()
    return opcao