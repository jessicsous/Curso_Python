'''
Operações ternárias
'''

# logged_user = True
#
# if logged_user:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário precisa logar'
# print(msg)

# outra forma
# logged_user = False  # ou false
# msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
# print(msg)

# idade = 18
#
# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')

# outra forma
# idade = 18
# eh_maior = (idade >= 18)
# msg = 'pode acessar' if eh_maior else 'Não pode acessar'
# print(idade)

# outra forma
idade = input('Qual a sua idade? ')


if not idade.isnumeric():
    print('Você precisa digitar apenas um número')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)
    msg = 'pode acessar' if eh_maior else 'Não pode acessar'
    print(msg)
