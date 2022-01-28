'''
list comprehension
otimização e usar menos linhas de código
'''

l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]  # iteração sob a lista 1

ex2 = [v * 2 for v in l1]  # multiplicando cada elemento da lista 1 por 2
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['jessica', 'mario', 'lucas']
ex4 = [v.replace('a', '@').upper() for v in l2]  # trocando o 'a' por '@'

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),

)
ex5 = [(x, y) for y, x in tupla]  # invertendo o valor da tupla
ex5 = dict(ex5)  # transfomando em dicionário

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]  # pegando da l3 os números que são divisíveis por 2
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # todos q são divisíveis por 3 e por 8
ex8 = [v if v % 4 == 0 else ' não é divisível' for v in l3]  # todos divisíveis por 4, se não for 'não é divisível'
ex9 = [v if v % 4 == 0 and v % 8 == 0 else 0 for v in l3] # todos os divisíveis por 4 e 8, se não for '0'
print(ex9)