# Reduce

from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print('A soma de todos números da lista é: {}'.format(soma_lista))

soma_produtos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print('A média de preço dos produtos é de: {:.2f}'.format(soma_produtos / len(produtos)))

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print('A idade média das pessoas é de: {:.2f}'.format(soma_idade/len(pessoas)))
