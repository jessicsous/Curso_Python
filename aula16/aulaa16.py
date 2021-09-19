'''
formatando valores com modificadores

:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - centro
'''

numero_1 = 10
numero_2 = 3
divisao = numero_1 / numero_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'jessica  silva'
print(nome. lower())  # tudo minúsculo
print(nome. upper())  # tudo maiúsculo
print(nome. title())  # primeiras letras maiúsculas

sobrenome = 'sousa'
print(f'{nome:s}')  # dizer pro python que é uma string
print(f'{nome:.6s}')
print(f'{nome:#^50}')

nome_formatado = '{:#<88}'.format(nome)
nome_formatado1 = '{0:$^50} {1:#^20}'.format(nome, sobrenome)
print(nome_formatado1)
print(nome_formatado)


num_1 = 1
print(f'{num_1:0>10}')  # 10 casas decimais á esquerda

num_2 = 1150
print(f'{num_2:0>6}')

print(f'{num_2:0^10}')

print(f'{num_2:.2f}')

print(f'{num_2:0>6.2f}')



