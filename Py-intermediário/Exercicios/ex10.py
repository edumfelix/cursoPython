listaA = [1, 2, 3, 4, 5]
listaB = [6, 7, 8, 9, 10]

if len(listaA) < len(listaB):
    for x in range(len(listaA)):
        listaA[x] += listaB[x]
    print(listaA)
else:
    for x in range(len(listaB)):
        listaA[x] += listaB[x]
    print(listaB)
