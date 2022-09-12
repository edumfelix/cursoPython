"""
Groupby
"""

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Fernando', 'nota': 'D'},
]

alunos.sort(key=lambda item: item['nota'])
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'{agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
