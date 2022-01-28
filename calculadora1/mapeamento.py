from dados import produtos, pessoas, lista
from functools import reduce


#nova_lista = map(lambda x: x * 2, lista)  # multiplicando cada elemento da lista vezes 2
#nova_lista1 = [x for x in lista]  # cópia da lista
#nova_lista2 = [x * 2 for x in lista]  # outra forma
#print(nova_lista2)
#print(lista)
#print(list(nova_lista))
#print(nova_lista1)

# acrescentar 5% sob os preços do produtos

# cada linha da lista anterior vai chegar no argumento da função a seguir 'p', desse argumento será acessada a chave preco...
# e após acessdado o valor da chave será modificado
#def aumenta_preco(p):
    #p['preco'] = round(p['preco'] * 1.05, 2)
    #return p

#novos_produtos = map(aumenta_preco, produtos)  # a função map mapea uma função que passa em cada elemento do iterável

#for produto in novos_produtos:
    #print(produto)
#print()
# pegar só o nome das pessoas do dicionário anterior

#nomes = map(lambda p: p['nome'], pessoas)

# for pessoa in nomes:
    # print(pessoa)
# print()
# só as idades

# idades = map(lambda i: i['idade'], pessoas)

# for idade in idades:
    #print(idade)

# map = passar uma função dentro de cada elemento do dicionário

# função filter: filtrar informações

nova_lista = filter(lambda x: x > 5, lista)
nova_lista1 = [x for x in lista if x > 5]
print(nova_lista1)
print(list(nova_lista))

# filtrar produtos com preços acima de 10,00 reais

lista_produto = filter(lambda p: p['preco'] > 10, produtos)

for produto in lista_produto:
    print(produto)
print()

# para operações mais complexas pode-se criar uma função assim como no map

def filtra(produto):
    if produto['preco'] > 10:
        return True

lista_produto1 = filter(filtra, produtos)

for produto in lista_produto1:
    print(produto)

# checar quem é maior de idade

def filtra(pessoas):
    if pessoas['idade'] >= 18:
        return True
    else:
        return False

lista_pessoas = filter(filtra, pessoas)

for pessoa in lista_pessoas:
    print(pessoa)

# reduce = acumuladora compulsiva
# forma aprendida anteriormente
acumula = 0
for item in lista:
    acumula += item

print(acumula)

# usando a função reduce
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))  # media de idades
