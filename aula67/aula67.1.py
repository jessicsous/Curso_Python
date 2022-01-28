'''
outra maneira de criar gerenciador de contexto
'''

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando arquivo')
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')