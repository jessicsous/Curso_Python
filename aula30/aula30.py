'''
funções (def) em python - *args **kwargs -
k'''

# revisão das aulas anteriores
def funcao(a, b, c, d, nome, e):
    print(a, b, c, d, nome, e)  # vai dar erro pois o argumento 'e' n foi definidok

funcao(1,2,3,4,5)

# outro erro
def funcao(a, b, c, d, nome=argumento, e):   # a partir do momento q um argumento é definido por valor padrão,
     print(a, b, c, d, nome, e)  # os próximos devem ser definidos também

funcao(1,2,3,4,5,'Jéssica')

# outro erro
def funcao(a, b, c, d, nome=argumento, e=argumento):
    print(a, b, c, d, nome, e)

funcao(1,2,3,4,5, nome='Jéssica', 6)  # erro, pois a partir do momento que a função for chamada com o argumento
# nomeado, os próximos também devem ser nomeados.

# outro erro
def funcao(a, b, c, d, nome=argumento, e=argumento):
    print(a, b, c, d, nome, e)

var = funcao(1,2,3,4,5, 'Jéssica', '6')  # variavel com valor none, pois não está retornando nenhum valor
print(var)

# solução para erro anterior
def funcao(a, b, c, d, nome=None, e=None):
    print(a, b, c, d, nome, e)
    return nome, e

var = funcao(1, 2, 3, 4, 5, nome='Jéssica', e='6')
print(var)

# *args = empacotamento e desempacotamento
# exemplo:
lista = [1,2,3,4,5]
n1, n2, *n = lista  # desempacotando n1=1, n2=2 e empacotando [3,4,5] em '*n'
print(n1, n2, n)

# desempacotando uma lista
lista = [1,2,3,4,5]
print(*lista)

# usando separador no desempacotamento
lista = [1,2,3,4,5]
print(*lista, sep='-')  # sep = separador

# empacotando em uma tupla
def f(*args):
    print(args)

f(1,2,3,4,5)

# acessando valores os valores da tupla (não pode ser alterada)
def f(*args):
    print(args)
    print(args[0])
    print(-1)
    print(len(args))

f(1,2,3,4,5)

# maneira de alterar valor de uma tupla, fazendo um quest
def f(*args):
    args = list(args)  # mudando args para lista
    args[0] = 20
    print(args)

f(1,2,3,4,5)

# desempacotando a lista para adicionar valores
def f(*args):
    print(args)

lista = [1,2,3,4,5]
f(*lista, 10,20,30,40,50)

# desempacotando e mesclando listas dentro da função
def f(*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
f(*lista, *lista2)

# **kwargs = argumentos nomeados
# exemplo
def f(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
f(*lista, *lista2, nome='Jéssica', sobrenome='Sousa')

# descobrir o envio de algum argumento
def f(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')  # melhor utilização, pq quando huver dúvida sobre a existencia do argumento, não da erro
    print(nome)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
f(*lista, *lista2, nome = 'Jéssica', sobrenome = 'Sousa')





