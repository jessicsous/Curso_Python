'''
criar exceções
'''

# criar a exceção
class ErradoError(Exception):  #criando um erro personalizado
    pass

# levantar a exceção
def testar():
    raise ErradoError('Errado')

# tratar a exceção
try:
    testar()
except ErradoError as error:
    print(f'Error:{error}')