usuario = input('Nome do usuário: ')
senha = int(input('senha do usuário: '))

usuario_bd = 'jessica'
senha_bd = 123456

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('usuário ou senha inválidos')