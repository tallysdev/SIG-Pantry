import datetime
import feira

cx = {}
cp =[]
z = []
tt = []

for i in feira.feira.keys():
    for j in feira.datasdecompras:
        if feira.feira[i][8] == j:
            cp.append(i)
            tam = len(cp)
            tamaux = (tam -2)
            v = []
            for v in cp:
                z.append(v)
            t = z[tamaux]
            u = z[tamaux+1]
            if tamaux >= -1 and (feira.feira[v][8] == feira.feira[t][8] or feira.feira[v][8] == feira.feira[u][8]):
                tt.append(i)
                cx[j] = [tt,'somapreco']
                print('aaa')
            else:
                cx[j] = [i,'somapreco']

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