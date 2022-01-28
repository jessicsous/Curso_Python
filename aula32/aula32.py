'''
funções anônimas ou espressões lambda
'''

def f(arg, arg2):
    return arg * arg2

var = f(2,2)
print(var)

# mesma coisa anterior usando as funções anônimas
a = lambda x,y: x * y
print(a(2,2))

#exemplo:
lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8],
]

# função pra ordenar lista
def f(item):
    return item[1]

lista.sort(key=f)
print(lista)

# reverso
lista1 = [
    ['p1', 5],
    ['p2', 7],
    ['p3', 55],
]

def f1(item):
    return item[1]

lista1.sort(key=f1, reverse=True)
print(lista1)

# esse processo pode ser substituido pelas expressões lambda
lista2 = [
    ['p1', 5],
    ['p2', 4],
    ['p3', 3],
]

lista2.sort(key=lambda item: item[1])
print(lista2)

# reverso
lista3 = [
    ['p1', 5],
    ['p2', 4],
    ['p3', 3],
]

lista3.sort(key=lambda item: item[1], reverse=True)
print(lista3)

# outra forma de ordenar usando 'sorted'
lista4 = [
    ['p1', 1],
    ['p2', 2],
    ['p3', 3],
]
print(sorted(lista, key=lambda i: i[1]))

# reverso
lista5 = [
    ['p1', 3],
    ['p2', 2],
    ['p3', 1],
]
print(sorted(lista, key=lambda i: i[1], reverse=True))

