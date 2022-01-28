'''
Associação - uma classe relacionada á outra, porém intependentes
'''

from da_aula55 import Escritor
from da_aula55 import Caneta
from da_aula55 import Maquinadeescrever

escritor = Escritor('jessica')
maquina = Maquinadeescrever()
print(escritor.nome)
maquina.escrever()