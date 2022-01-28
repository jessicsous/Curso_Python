'''
https://rszalski.github.io/magicmethods/  <--- link que fala sobre os métodos mágicos
métodos mágicos = começam e terminam com dois anderlaies e
modificam o comportamento da classe
'''

class A:
    def __new__(cls, *args, **kwargs):  # método construtor
        cls.nome = 'jessica silva'

        def haha(*args, **kwargs):
            print('oi')

        cls.haha = haha

        print('executando o new')


        if not hasattr(cls, 'existe'):
            cls._existe = object.__new__(cls)

        return cls._existe



    def __init__(self):
        print('executando init')

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'você não pode fazer isso'
        else:
            self.__dict__[key] = value

    def __del__(self):  # nem sempre esse método é chamado
        print('objeto coletado.')

    def __str__(self):
        return "<class 'A'>"

    def __len__(self):
        return 24

a = A()
print(len(a))
a.nome = 'Jéssica Silva'
a.qualquer = 'agora sim'
print(a.nome, a.qualquer)


