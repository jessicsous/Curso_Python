# add (adiciona), update (atualiza), clear, discard
# union (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elemento apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
# sets só suportam elementos únicos
# sets não tem índice, então não tem como acessar um valor do set.

s1 = {1,2,3,4,5,6}  # os sets suportam somente elementos imultáveis (strings, tuplas...)
print(s1)

# é possível iterar sobre o set
for v in s1:
    print(v)

# set vazio:
s2 = set()
# adicionar elementos:
s2.add(1)
# adicionar tupla:
s2.add((1,2,3))
print(s2)
# remover valor do set
s2.discard(1)
print(s2)
# "adiciona elementos" e itera sobre os elementos / não respeita ordem
s2.update('python')
print(s2)
s2.update([1,2,3], {1,2,3,4})  # set não aceita elementos duplicados
print(s2)

# usando um set para remover elementos duplicados de uma lista
l1 = [1,1,1,1,6,6,6,7,7,7,7,7,8,8,8]
l1 = set(l1)
l1 = list(l1)
print(l1)

# união de sets
s3 = {1,2,3,4,5,11}
s4 = {1,2,3,4,5,6,7,8,9,10}
s5 = s3 | s4
print(s5)
s6 = s3 & s4  # intercessão entre os sets (fica os elementos comuns)
print(s6)
s7 = s4 - s3 # a ordem importa
print(s7)
s8 = s3 ^ s4
print(s8)

l1 = ['jessica', 'silva']
l2 = ['jessica', 'jessica', 'silva', 'silva']

if set(l1) == set(l2):
    print('l1 é igual à l2')
else:
    print('l1 é diferente de l2')
