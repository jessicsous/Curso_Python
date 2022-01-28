'''
groupby - agrupando valores
'''

from itertools import groupby
# como agrupar elementos em dicionarios
alunos = [
    {'nome': 'jessica', 'nota': 'A'},
    {'nome': 'joao', 'nota': 'C'},
    {'nome': 'maria', 'nota': 'D'},
    {'nome': 'luiz', 'nota': 'B'},
    {'nome': 'marcos', 'nota': 'A'},
    {'nome': 'alessandro', 'nota': 'D'},
    {'nome': 'andre', 'nota': 'A'},
    {'nome': 'jack', 'nota': 'C'},
]

alunos.sort(key=lambda item: item['nota'])
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')

    for aluno in valores_agrupados:
        print(aluno)
    print()