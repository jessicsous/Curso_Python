'''
Dictionary comprehension
'''

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]
lista1 = [
    ('chave', 2),
    ('chave2',8),
]
d1 = {x: y for x, y in lista}  # que é o mesmo que...
d2 = dict(lista)  # tranformando lista em lista
d3 = {x: y*2 for x, y in lista}
d4 = {x: y*2 for x, y in lista1}
d5 = {x: y.upper() for x, y in lista}  # pra deixar maiúsculo
d6 = {x.upper(): y.upper() for x, y in lista}  # chave e valor maiúsculo
d7 = {x: y for x, y in enumerate(range(5))}
d8 = {x for x in range(5)}
d9 = {f'chave_{x}':  x**2 for x in range(5)}  #agora é um dicionário
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8, type(d8))  # compreensão de conjuntos
print(d9, type(d9))
