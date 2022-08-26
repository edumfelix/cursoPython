# map - Mapeamento

from dados import produtos, pessoas, lista

# nova_lista = map(lambda x: x * 2, lista)

nova_lista = [x * 2 for x in lista]
for lista1 in nova_lista:
    print(lista1)

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
