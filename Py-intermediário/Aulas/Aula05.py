# List Comprehension

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

listaEx1 = [var for var in lista1]

listaEx2 = [v * 2 for v in lista1]

listaEx3 = [(v, v2) for v in lista1 for v2 in range(3)]

# print(listaEx1, listaEx2, listaEx3)

lista2 = ['Luiz', 'Eduardo', 'Maria']

listaEx4 = [v.replace('a', '@') for v in lista2]

print(listaEx4)
