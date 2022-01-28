'''
Método de classe
'''

from random import randint

class Pessoa:
    ano_atual = 2021  # atributo relacionado á classe

    def __init__(self, nome, idade):  # atributo relacionado â instância
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # atributo relacionado á instância
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):  # método de classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # Método estático, não precisa da instância nem da classe
    def gera_id():
       rand = randint(10000, 19999)
       return rand

p1 = Pessoa.por_ano_nascimento('Jéssica', 1997)  # do método de classe
p1 = Pessoa('Jéssica', 24)  # do método de classe

p1 = Pessoa('Jéssica', 24)
p1.get_ano_nascimento()
print(Pessoa.ano_atual)

print(Pessoa.gera_id())  # do método estático
print(p1.gera_id())  # do método estático