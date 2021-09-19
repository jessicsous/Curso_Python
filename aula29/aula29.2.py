'''
continuação. Funções (def) em python - return -
'''
def dumb():  # aqui foi criado uma função 'dumb' sem parametro()
    return 1  # retornado o valor '1'
var = dumb()  # criado uma variável para a função
print(var, type(var))  # imprimido a variável e seu valor 'type'

# retorno vazio
def dumb():
    return  # retorno vazio
print(dumb())  # retorna 'none', que significa 'vazio' ou expressão falsa

# Função retornando outra função
def f(var):
    print(var)

def dumb():
     return f  # retorna a função 'f'

var = dumb()('colocar o valor aqui.')  # iguala 'var' a 'dumb' e atribui valor

# ver o 'id' de 'var' e o 'id' de 'f' o qual retorna o endereço do objeto referenciado
def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual á f')
else:
    ('var é diferente de f')

# usando 'var' como se fosse 'f'
def f(var):
    print(var)
def dumb():
    return f
var = dumb()
var('pode imprimir algo na tela.')





