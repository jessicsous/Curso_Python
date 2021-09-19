'''
while em python
utilizado para realizar ações enquanto
uma condição for verdadeira.

requisitos: Entender condições e operadores
'''

# while condicao:  # enquanto essa condição for verdadeira faça oq ta dentro do codigo
    # pass

# while True:  # loop infinito. executa infinitamente até achar a expressão falsa (fica preso aqui)
    #nome = input('qual o seu nome?: ')
    #print(f'olá {nome}!')

# print('não será executada.')

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('acabou!')  # executado quando o laço anterior terminar

x = 10
while x < 20:
    if x == 13:
        x = x + 1
        break
    print(x)
    x = x + 1
print('acabou')


