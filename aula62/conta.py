from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('o valor precisa ser numérico')

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end= ' ')
        print(f'Saldo: {self._saldo}')

    def sacar(self):
        pass



