'''
count - itertools
'''
# o zip retorna um iterador
from types import GeneratorType
# lista
variavel = zip('alo', 'blu')  # 'alo' e 'blu' é um iterável
print(list(variavel))

# dicionário
variavel = zip('alo', 'blu')
print(dict(variavel))

iteracao = zip('alo', 'alo')
print(next(iteracao))
print(next(iteracao))
print(next(iteracao))

# checar
variavel = zip('alo', 'blu')
print(isinstance(variavel, GeneratorType))  # é uma pergunta: 'a variável é uma instância de um gerador?'

# transformar em um gerador
variavel = ((x, y) for x, y in zip('alo', 'blu'))
#print(isinstance(variavel, GeneratorType)
print(next(variavel))
print(next(variavel))
print(next(variavel))

from itertools import count

contador = count()  # iterador sem fim
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

# modificar o contador
contador = count(start=5, step=2)
# loop infinito
for valor in contador:
    print(valor)

# excessão
    if valor >= 10:
        break

# com número de ponto flutuante
contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor, 2))  # duas casas decimais

    if valor >= 10:
        break

# indexar lista com contador
contador = count()
lista = ['Luiz', 'Jessica', 'george']
lista = zip(contador, lista)
print(list(lista))
