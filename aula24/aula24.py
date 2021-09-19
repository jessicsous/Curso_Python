'''
Split, Join, Enumerate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
'''
# string = 'O Brasil é o país do futebol, o Brasil é penta'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
# print(lista_1)
# print(lista_2)
#
# for valor in lista_1:
#     print(valor)
#     break

# for valor in lista_1:
#     print(f' A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd = lista_1.count(valor)
#
#     if qtd > contagem:
#         contagem = qtd
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# for valor in lista_2:
#     print(valor.strip().capitalize())  # remover espaço e mudar a primeira letra p maiúscula
#
# lista = ['o', 'Brasil', 'é', 'penta']
#
# lista_1 = (' ').join(lista)
# print(lista_1)

# outra forma
# string = 'O Brasil é penta'
# lista = string.split(' ')
# string_1 = (' ').join(lista)
# print(string_1)

# enumerate
# string = 'O Brasil é penta'
# lista =  string.split(' ')
#
# for v1, v2 in enumerate(lista):
#     print(v1, v2)

lista = ['Luiz', 'João', 'Maria']
for v1, v2 in enumerate(lista):
    print(v1 , v2)




