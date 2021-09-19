'''
Funções (def) em Python - return
'''

# sem o 'return', n retorna nunhum valor
def funcao(var):
    print(var)

variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor.')

# retornando o valor da variavel
def funcao(var):
    return var
    print('Isso não será executado')

variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor.')

# conta de divisão
def divisao(n1, n2):
    return n1 / n2

divide = divisao(8,0)
print(divide)

# verificando o erro do zero
def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(8,0)
print(divide)  # retorna o valor 'none', ou 'valor vazio'

# verificando o erro do zero e retornando um valor verdadeiro
def divisao(n1, n2):
    if n2 > 0:
        return n1/n2

divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('conta inválida')

# maneira usual com 'return'
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2
divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('conta inválida')