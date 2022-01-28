'''
zip - unindo iteráveis
zip_longest - itertools
'''

# junção das listas abaixo
### código
cidades = ['são paulo', 'manaus', 'belém', 'salvador']

# código
estados = ['SP', 'AM', 'PA', 'BA']

cidades_estados = zip(cidades, estados)
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))

# ou iterar de forma melhor
for valor in cidades_estados:
    print(valor)

# ou criar uma lista
cidades_estados = zip(estados, cidades)  # invertendo a ordem dos valores
print(list(cidades_estados))

# ou criar um dicionário
cidades_estados = zip(estados, cidades)
print(dict(cidades_estados))

# zip_longest é usado para listas com quantidades diferentes, para a menor lista não eliminar os valores da maior
# exemplo
from itertools import zip_longest, count

cidades = ['Rio de Janeiro', 'Sao paulo', 'Manaus']
estados = ['Rj', 'SP']
cidades_estados = zip_longest(estados, cidades)
print(list(cidades_estados))

#renomeando o 'none'
cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidades_estados))
