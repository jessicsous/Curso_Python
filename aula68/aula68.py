'''
Em python tudo é um objeto: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse
'''

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não um atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'valor'
    pass
    b_fala = 'atributo n método'
    #def b_fala(self):
        #print('oi')
    def bla(self):
        pass
b = B()
