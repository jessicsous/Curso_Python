'''
No exercício anterior foi feito uma soma de duas listas usando várias soluções diferentes.
uma delas foi usando zip para unir duas listas e utilizar list comprehension para fazer a conta:
'''

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

'''
o problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício)
Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.
'''

from itertools import zip_longest

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)

'''
Nesse caso, é usado o fillvalue como 0, assim conseguimos capturar os valores restantes
da lista maior, realizando contas, sem obter um erro no programa.h
'''
