'''
Escopo de variáveis
'''

variavel = 'valor'  # está em escopo global (está acessível em todos os locais na aplicação)
# exemplo
def f():
    print(variavel)

def f2():
    print(variavel)

f()
f2()

# variavel criada dentro do escopo local
def f():
    variavel = 'escopo local'
    print(variavel)
f()

# print fora do def, n reproduz a variavel local, reproduz a global
# exemplo
def f():
    variavel = 'escopo local'
    print(variavel)

f()
print(variavel)  # imprime a variável que está no escopo global

# alterar valor da variável local pelo valor da variável global / não recomendado pode gerar valores estranhos
# exemplo
def f():
    global variavel
    variavel = 'escopo local'
    print(variavel)

f()
print(variavel)  # ficou com o msm valor da variavel de escopo local

# melhor maneira de executar o script anterior sem mexer na variável global
def f2(arg=None):
    arg = arg.replace('c', 'v')
    return arg

f()
variavel2 = f2(arg=variavel)
print(variavel2)

# conectando duas funções / passando valor de uma pra outra
def f():
    variavel2 = 'valor'
    return variavel2

def f2(arg):
    print(arg)

var = f()
f2(var)

