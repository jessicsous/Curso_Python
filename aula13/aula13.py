'''
contar a quantidade de caracteres usando a função 'len',
'''

usuario = input('digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('você precisa digitar pelo menos 5 caracteres.')
else:
    print('você está cadastrado no sistema.')



