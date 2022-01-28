'''
Herança Múltipla = herda de uma ou várias aula61
'''

class A:
    def falar(self):
        print('Falando... Estou em A.')

class B(A):
    def falar(self):
        print('Falando... Estou em B.')

class C(A):
    def falar(self):
        print('Falando... Estou em C.')

class D(B, C):
    def falar(self):
        print('Falando... Estou em D.')

d = D()
d.falar()