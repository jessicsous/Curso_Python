'''
Módulos padrão do python:
módulos são arqivos .py (que contém código python) e servem para expandir
as funcionalidades padrão da linguagem
veja todos os  módulos padrão do python em:
https://docs.python.org/3/py-modindex.html
'''
# como utilizar módulos
# qual plataforma o python ta sendo executado
# impotando o módulo sys
import sys
print(sys.platform)
# ou
from sys import platform
print(platform)
# ou adicionando apelido
from sys import platform as so
print(so)

# gerar números aleatórios
import random

for i in range(10):
    print(random.randint(0,10))

# somente randint
from random import randint

for i in range(10):
    print(randint(0,10))

# problemas que podem ocorrer
from random import randint

def randint(*args):
    return 'alguma coisa'

for i in range(10):
    print(randint(0,10))

# resolução do ploblema anterior
from random import randint  as apelido

def randint(*args):
    return 'alguma coisa'

for i in range(10):
    print(apelido(0,10))

