'''
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
'''


def f():
    variavel = 'valor'
    return variavel

def f2(arg):
    print(arg)

var2 = f()
f2(var2)

# outra forma
def f():
    return 'valor'

def f2(arg):
    return arg()

var = f2(f)
print(var)