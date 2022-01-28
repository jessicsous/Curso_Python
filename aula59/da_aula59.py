class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print('método falar em Cliente')

class Clientevip(Cliente):
    def falar(self):  # sobrepondo o método falar já existente
        Pessoa.falar(self)  # chamando o método falar da classe (Pessoa)
        Cliente.falar(self)  # chamando o método falar da classe (Cliente)
        super().falar()  # outra forma de chamar o método da classe mais próxima
        print('outro cliente vip falando')

class Clientetop(Clientevip):
    def __init__(self, nome, idade, sobrenome):  # sobrepondo o construtor de Pessoa
        super().__init__(nome, idade)  # chamando o construtor da super classe
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        Clientevip.falar(self)
        print(f'{self.nome} {self.sobrenome}, está falando')