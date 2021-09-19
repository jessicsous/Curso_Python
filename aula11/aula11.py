'''
Operadores Relacionais
== igualdade,
> maior q
>= maior q ou igual á
< menor q
<= menor q ou igual á
!= diferente
'''
print(2 == 2)  # dois sinais de igual é uma pergunta. (2 é igual a 2?)
print(2 == '2')  # retorna false pq int n é igual str

num_1 = 2
num_2 = 2

expressão = num_1 == num_2  # afirmando q essa expressão é igual a uma pergunta
print(expressão)

expressão1 = num_1 > num_2  # afirmando que essa expressão é a pergunta se num_1 é maior que num_2
print(expressão1)

expressão2 = num_1 >= num_2  # pergunta se a variável da esquerda é maior ou igual a da direita
print(expressão2)

expressão3 = num_1 <= num_2  # pergunta se a variável é menor ou igual
print(expressão3)

expressão4 = num_1 != num_2  # perguntando se a variável num_1 é diferente da num_2, se fordiferente retorna true
print(expressão)

var_1 = 'jessica'
var_2 = 'silva'

expressão = (var_1 != var_2)
print(expressão)

nome = input('qual o seu nome? ')
idade = int(input('qual a sua idade? '))

# limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')


nome = input('qual o seu nome? ')
idade = int(input('qual a sua idade? '))

# limite para pegar o empréstimo
muito_jovem = 20
muito_velho = 30

if idade >= muito_jovem and idade <= muito_velho:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')








