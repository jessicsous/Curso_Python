'''
implementando protocolo iterator
'''

# recriando a lista do python - o objetivo é mostrar como as coisas funcionam ocultamente
class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):  # para obter os valores do couxete
        return self.__items[index]

    def __setitem__(self, index, valor):  # setar o valor dos couxetes
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def   __delitem__(self, index):  # deletar os valores da classe
        del self.__items[index]

    def __iter__(self):  # implementar o protocolo do iterator
        return self

    def __next__(self):  # implementar o protocolo do iterator
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):  # print na classe
        return f'{self.__class__.__name__}({self.__items})'

if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('jessica')
    lista.add('sousa')

    lista = list(lista)

    #print(lista)
    #lista[0] = 'joao'
    #lista[2] = 'funciona?'
    #print(lista)

    #del lista[2]

    #print(lista)

    #print(next(lista))
    #print(next(lista))

    #print(lista[0])
    #print(lista[1])


    for valor in lista:
        print(valor)




