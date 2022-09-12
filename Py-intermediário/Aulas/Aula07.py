# Zip - Unindo iteráveis
# Zip_longest - Itertools
from itertools import zip_longest

cidades = ['Fortaleza', 'São Paulo', 'Belo Horizonte', 'Salvador']

estados = ['CE', 'SP', 'MG']

cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')
for endereco in cidades_estados:
    print(endereco)
