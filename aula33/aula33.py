'''
Tuplas
'''

# diferença da tupla pra lista : os elementos da tupla não podem ser editados
# como criar uma tupla:
t1 = (1,2,3)  # tupla

g = (1,2,3)

print(type(g))

for v in g:  # interando sobre a tupla
    print(v)

# tuplas também podem ser usadas sem os parênteses
t2 = 1,2,3, 'abc'
print(type(t2))

# tuplas precisam de virgula, senão n são formadas
# exemplo
t3 = 1
print(type(t3))

# concatenação de tuplas
t4 = 1,2,3,4,5
t5 = 6,7,8,9,10
t6 = t4 + t5
print(t6)

# pra mudar uma tupla tem que transformar primeiro pra uma lista
t7 = ('jessica',) * 10  # tupla
t7 =list(t7)  # transformada em lista
t7[1] = 5  # muda o valor do índice [1]
t7 = tuple(t7)  # transforma em tupla novamente
print(t7)

