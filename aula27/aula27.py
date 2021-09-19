# espressão condicional
# nome = input('Qual o seu nome? ')
# print(nome or 'você não digitou nada')


a = 0  # retorna falso
b = None  # retorna falso
c = False  # retorna falso
d = []  # retorna falso
e = {}  # retorna falso
f = 22  # retorna verdadeiro
g = 'Luiz'  # retorna verdadeiro

variavel = a or b or c or d or e or f or g  # imprime a primeira expressão verdadeira
print(variavel)