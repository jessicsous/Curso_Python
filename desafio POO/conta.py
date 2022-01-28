from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia} '
              f'Conta: {self._numero_conta} '
              f'Saldo: {self._saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite=100):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()