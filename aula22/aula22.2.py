'''
listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

# juntar listas
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

# juntar listas com 'extend'
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
l2.extend('A')

print(l1)
print(l2)

# adicionando valores com 'append'
l1 = [1,2,3]
l2 = [4,5,6]
l1.append('A')
l2.append('B')

print(l1)
print(l2)

# inserir valor em qualquer parte da lista usando 'insert'
l1 = [1,2,3]
l2 = [4,5,6]
l2.insert(0,'B')

print(l2[0])

#deletar elemento do final da lista com 'pop'
l1 = [1,2,3]
l2 = [4,5,6]
l2.pop()
l1.pop()

print(l1)
print(l2)

# excluir elementos de maneira rapida usando 'del'
l1 = [1,2,3,4,5,6,7,8,9]
del(l1[3:5])

print(l1)

# mostrar o maior e o menor valor da lista
l2 = [1,2,3,4,5,6,7,8,9]
print(max(l2))
print(min(l2))

# simplificar a forma de escrever listas usando range
l2 = list(range(1,10))  # porém essa função retorna um objeto range, por isso é usado a função list pra transformar o objeto em uma lista
print(l2)

l3 = list(range(0,100,8))  # de 0 a 100, pulando de 8 em 8 (multiplos de 8)
print(l3)

# usando 'for' em lista
l2 = list(range(1,10))
for elem in l2:
    print(f'o tipo de elem é {type(elem)} e seu valor é {elem}')




