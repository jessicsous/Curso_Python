'''
operadores lógicos - usado para comparações
and, or, not
in e not in
'''

# 1

a = 2
b = 2
c = 3

# verdadeiro e falso = falso
# verdadeira e verdadeira = verdadeiro
# comparação1 and comparação2

# verdadeiro ou verdadeiro = verdadeiro
# verdadeiro ou falso = verdadeiro
# comparação1 or coparação2

resultado = a == b and b < c
print(resultado)

resultado1 = a == b or b < c
print(resultado1)

resultado2 = not a == b and not b < c  # inversão da expressão
print(resultado2)

# 2

a = 2
b = 3

if not b > a:  # se 'b' não for maior q 'a', imprime a expressão abaixo, se n for passa pra próxima verificação.
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

# 3

a = ''
b = 0

if not a:
    print('por favor, preencha o valor de A.')

# 4

nome = 'jessica silva'

if 'u' in nome:  # se 'u' está em 'nome', executa o comando abaixo.
    print('existe a letra u no seu nome')
else:
    print('Não existe')

# 5

if 'u' not in nome:  # se 'u' não estiver dentro de 'nome', executa o comando abaixo
    print('não existe')
else:
    print('existe')

