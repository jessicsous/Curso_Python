'''
Getters e setters
'''

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #Getter
    @property
    def nome(self):
        return self._nome

    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.tittle

    # Getter : obtem um valor
    @property
    def preco(self):
        return self._preco

    # setter : configura um valor
    @preco.setter
    def preco(self, valor):
        if isistance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.preco)
