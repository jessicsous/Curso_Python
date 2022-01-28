'''
Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
'''

def saudacao(saudar='olá',nome='jessica'):
    print(saudar,nome)

saudacao()

# outra maneira

def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('olá', 'jéssica')
