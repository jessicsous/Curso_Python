'''
Combinations, Permutations e product - itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
produto - Ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product
# saber todas as combinações possíveis sem importar a ordem e sem repetição
nomes = ['jessica', 'luiz', 'sousa', 'maria']

for grupo in combinations(nomes, 2):
    print(grupo)

# saber todas as combibinações possíveis se importando com a ordem porém sem repetição ex= jessica luiz e luiz jessica
nomes = ['jessica', 'luiz', 'sousa', 'maria']

for grupo in permutations(nomes, 2):
    print(grupo)

# saber todas as combinações possíveis se importando com a ordem e com repetição ex jessica jessica
nomes = ['jessica', 'luiz', 'sousa', 'maria']

for grupo in product(nomes, repeat=2):
    print(grupo)