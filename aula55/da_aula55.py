'''
Agregação = uma classe usa a outra como parte de si
'''

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta0

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('caneta está escrevendo...')

class Maquinadeescrever:
    def escrever(self):
        print('maquina está escrevendo...')