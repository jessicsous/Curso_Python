'''
Funções - def em python
'''

# exemplo
def funcao():
    print('Hello world!')

funcao()
funcao()
funcao()
funcao()

# exemplo aplicável prático / diferença entre as funções
def funcao2():
    print('olá mundo')

funcao2()
funcao2()
funcao2()
funcao2()

print('Hello world!')
print('Hello world!')
print('Hello world!')
print('Hello world!')

# criar parametro dentro da função
def funcao3(msg):
    print('Olá mundo!')

funcao3('mensagem')  # criando o valor do parametro
funcao3('mensagem')
funcao3('mensagem')
funcao3(' ')

# mudando o parâmetro
def saudacao(msg2, nome):
    print(msg2, nome)

saudacao('olá', 'Jéssica')
saudacao('hello', 'visitante')

# sem mandar valores
def saudacao2(msg3='olá', nome2='usuário'):
    print(msg3, nome2)

saudacao2()

# trocando os nomes das variáveis
def saudacao3(msg4='Olá', nome3='Usuário'):  # segue a ordem da função criada
    print(msg4, nome3)

saudacao3(nome3='zezinho', msg4='hi')

# mudando a letra das variáveis
def saudacao4(msg5='Olá', nome4='Usuário'):
    nome4 = nome4.replace('a', '4')  # quando encontrar a letra 'a' vai mudar para '4'
    msg5 = msg5.replace('a', '4')
    print(msg5, nome4)

saudacao4('hi', 'Jéssica')
saudacao4('hello', 'Mário')
saudacao4('olá', 'Lucas')
saudacao4('oi', 'usuário')

# as formas anteriores não são usuais
# forma abaixo de como fazer o msm processo anterior
def saudacao5(msg6='Olá', nome5='Usuário'):
    nome5 = nome5.replace('a', '4')
    msg6 = msg6.replace('a', '4')
    return f' {msg6} {nome5}'

variavel = saudacao5()
print(variavel)





