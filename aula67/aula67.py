'''
Criando gerenciadores de contexto
'''

'''
sem gerenciador de contexto = pode acontecer do programador esquecer de fechar
arquivo = open('abc.txt', 'w')
arquivo.write('algo')
arquivo.close()
'''

# o gerenciador de contexto resolva o problema anterior
# with open('abc.txt', 'w') as arquivo:
   # arquivo.write('algo')

# gerenciador de contexto próprio
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):  # os parâmetros aparecem quando há excessão
        print('fechando arquivo')
        self.arquivo.close()
        # excessão tratada
        return True

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('algo')