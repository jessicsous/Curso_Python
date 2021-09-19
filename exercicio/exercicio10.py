'''
fizz buzz - se o parametro da função for divisivel por 2, retorne fizz, se o parametro da função for divisivel por 5,
retorne buzz. se o parametro da função for divisivel por 5 e por 3, retorne fizzbuzz, caso contrario, retorne
o número enviado.
'''

def f(numero):
    if numero/2 ** 0:
        return 'fizz'
    elif numero/5 ** 0:
        return 'buzz'
    elif numero/5 and numero/3 ** 0:
        return 'fizzbuzz'
    else:
        return 'tente novamente'
var = f(10)
print(var)