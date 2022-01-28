'''
Dicionários: esrutura de dados que suporta um par de chave e valor
semelhante a lista porém quem determina o indice n é o python
'''
a1 = {'chave':'valor da chave'}
print(a1)

# criando nova chave
a2 = {'chave':'valor da chave'}
a2['nova_chave'] = 'valor da nova chave'
print(a2)
print(a2['chave'])  # acessar a chave

# outra maneira de criar dicionários
a3 = dict(chave1='valor da chave', chave2='valor da outra chave')
print(a3)

# para criar varias chaves num dicionario seus valores tem q ser diferentes
# exemplo
a4 = {1: 'valor', 2: 'valor', 3: 'valor real da chave'}
print(a4)

# do contrário o valor da ultima chave prevalece sobre os demais
# exemplo
a5 = {1: 'valor', 1: 'valor', 1: 'valor real da chave'}
print(a5)

# em python qualquer tipo de dados imultáveis podem ser usados para as chaves
# exemplo de tipos
a6 = {
    'str' : 'valor',
    123: 'outro valor',
    (1,2,3,4) : 'tupla',
}
print(a6[(1,2,3,4)])

# se for chamado para ser impresso uma chave inexistente no dicionário, o programa dá erro e todos os dados abaixo
# param de funcionar
# exemplo
# print(a6['nao existe'])

# a6['naoexiste'] = 'agora existe.'
# uma solção seria colocar dentro de uma verificação if
# exemplo
if 'naoexiste' in a6:  # se a chave 'não existe' estiver no dicionário 'a6' ...
    print(a6['naoexiste'])  # imprimir a chave

# se a chave da verificação anterior for criada ela passa a ser exibida no print. precisa ser criada antes da verificação

# outra maneira de acessa chave no dicionário:
print(a6.get('nomedachave'))  # como essa chave não existe no dicionário vai aparecer o valor none...
#... a vantagem é que o código não para de funcionar.

# chacagem
if a6.get('nomedachave') is not None:  # se a chave estiver dentro do dicionario...
    print(a6.get('nomedachave'))  #... imprime a chave

# mudar valores que ja existem
a6['str'] = 'novo valor'
print(a6[('str')])

# como excluir chave ('str')
del a6['str']
print(a6)

# checagens
print('str' in a6)  # se str existe em a6
print('str' in a6.keys())  # se str existe em a6
print('valor' in a6.values())  # se valor  existe em a6
print(len(a6))  # informa quantos pares de chave

# iteração sobre dicionários
# chaves
for k in a6:
    print(k)

# valores
for v in a6.values():
    print(v)

# chaves e valores
# for v in a6.items():
   # print(v)

# desempacotando para acessar chave e valor
for k, v in a6.items():
    print(k, v)

# exemplo de dicionário dentro de dicionário
clientes = {
    'cliente1' : {
        'nome' : 'Jessica',
        'sobrenome' : 'Sousa',
    },
    'cliente2' : {
        'nome' : 'Lucas',
        'sobrenome' : 'viamonte',
    },
}
# iteração em dicionários com filhos dicionários
for clientes_k, clientes_v in clientes.items():  # iterando o loop inteiro
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():  # iterando sobre o valor
        print(f'\t{dados_k} = {dados_v}')

# como criar uma copia rasa de um dicionario em uma variável
a7 = {1: 'a', 2: 'b', 3: 'c'}
v = a7
print(a7)
print(v)  # os valores são identicos porém n podem mais ser alterados sem um influenciar o valor do outro...
#... uma solução seria a seguinte:
a8 = {1: 'a', 2: 'b', 3: 'c'}
v = a8.copy()
v[1] = 'Jessica'  # agora pode trocar o índice 1, somente na variável

print(a8)
print(v)

# para criar dicioários independentes usando módulos
# um módulo pode criar uma cópia real cujos muja cópia é independente da matriz
# exemplo
import copy

a9 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Jessica', 'Sousa']}  # a chave 'd' é uma lista dentro do dicionário
v = copy.deepcopy(a9)  # ao invés de utilizar o .copy(), utiliza-se o módulo 'copy'
v[1] = 'Jessica'  # alteração da chave '1' para 'Jéssica'
v['d'][0] = 'Silva'  # alteração do índice '0' da lista localizada na chave 'd'

print(a9)
print(v)

# converter lista em dicionário
lista = [
    ['a1', 1],
    ['a2', 2],
    ['a3', 3],
]

a10 = dict(lista)
print(a10)

# converter tuplas dentro de uma lista para dicionário
lista = [
    ('a1', 1),
    ('a2', 2),
    ('a3', 3),
]

a11 = dict(lista)
print(a11)


