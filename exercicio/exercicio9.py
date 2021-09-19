'''
Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return)
o valor do primeiro número somado do aumento do percentual do mesmo.
'''

def f(primeiro, segundo):
    vari1 = primeiro * (segundo/100)
    vari2 = primeiro
    return vari1 + vari2

var = f(50, 50)
print(var)
