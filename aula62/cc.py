from aula62.conta import Conta

class Contacorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__int__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self._saldo + self._limite < valor:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()
