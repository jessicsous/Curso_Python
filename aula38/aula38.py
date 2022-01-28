'''
Iteráveis
Iteradores
Geradores
'''

lista = [1,2,3,4,5,6]
lista1 = 123456
lista2 = 'string'
print(hasattr(lista, '__iter__'))  # verificação se a lista é um objeto iterável
print(hasattr(lista1, '__iter__'))
print(hasattr(lista2, '__iter__'))

# como transformar uma lista em um iterador
lista3 = [10,20,30,40,50,60]
lista3 = iter(lista)

print(next(lista3))
print(next(lista3))
print(next(lista3))
print(next(lista3))
print(next(lista3))
print(next(lista3))

# geradores (servem para evitar o consulmo de memoria)
import sys
lista4 = list(range(1000))
print(lista4)
print(sys.getsizeof(lista4))  # quantos bytes a lista ta consulmindo de memoria

import time  # módulo para vêr oq acontece na tela

def gera():  # criando uma função
    r = []  # cria uma raw
    for n in range(100):  # faz uma ieração da função range de 0 a 99
        r.append(n)  # colocando os valores, a cada iteração do laço, no raw vazio
        time.sleep(0.1)  # dormir 0.1 segundo
    return r  # depois de tudo retorna o valor

g = gera()

for v in g:
    print(v)

# para retornar um valor de cada vez
def gerad():
    for n in range(100):
        yield n
        time.sleep(0.1)

g1 = gerad()

for v in g1:
    print(v)

# código manual sem o laço for
def gerador():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel

g2 = gerador()

print(next(g2))
print(next(g2))

# forma mais simples para criar gerador
l1 = [x for x in range(100)]  # salva todos os valores na memória
print(type(l1))
l2 = (x for x in range(100))  # não salva todos valores na memória, só entrega os valores pedidos. para pedir pode ser utilizado o next ou o for
print(type(l2))

print(sys.getsizeof(l1))  # tamanho da lista
print(sys.getsizeof(l2))  # tamanho da lista / apesar de identicas tem tamanhos diferentes

