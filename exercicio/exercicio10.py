'''
fizz buzz - se o parametro da função for divisivel por 3, retorne fizz, se o parametro da função for divisivel por 5,
retorne buzz. se o parametro da função for divisivel por 5 e por 3, retorne fizzbuzz, caso contrario, retorne
o número enviado.
'''

def f(numero):
    if numero % 5 and numero % 3 == 0:
        return 'fizzbuzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'
    return numero

var = f(0)
print(var)

# outra forma

def f(numero):
    if numero % 5 and numero % 3 == 0:
        return f'fizzbuzz, {numero} é divisível por 3 e 5'
    if numero % 3 == 0:
        return f'fizz, {numero} é divisível por 3'
    if numero % 5 == 0:
        return f'buzz, {numero} é divisível por 5'
    return numero

from random import randint
for i in range(100):
    aleatorio = randint(0,100)
    print(f(aleatorio))



