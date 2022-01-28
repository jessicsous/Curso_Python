'''
O que são dataclasses? O módulo fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr(), __eq__(etc)
em classes definidas pelo usuário,
Basicamente, dataclasses são sytax sugar para criar classes normais.
foi originalmente descrito na pep 557.
adicionado na versão 3.7 do python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
'''


from dataclasses import dataclass

@dataclass(eq=False, repr=False, order=False, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    #@property
    #def nome_completo(self):
        #return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('Jéssica', 'Silva')
p2 = Pessoa('Jéssica', 'Silva')

print(p1)
print(p1 == p2)


#print(p1.nome)
#print(p1.sobrenome)
#print(p1.nome_completo)
