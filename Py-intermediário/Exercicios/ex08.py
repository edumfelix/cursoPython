lista = '012345678901234567890123456789012345678901234567890123456789'
n = 10
lista_separada = [lista[i: i+n] for i in range(0, len(lista), n)]

lista_separada = '.'.join(lista_separada)

print(lista_separada)
