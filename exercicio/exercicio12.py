'''
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1
executar duas funções que recebam um número diferente de argumentos.
'''
def f(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def f1(nome):
    return f'oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = f(f1, 'jessica')
executando2 = f(saudacao, 'jessica', 'hello')
print(executando)
print(executando2)