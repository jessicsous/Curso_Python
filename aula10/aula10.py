'''
condições IF, ELIF e ELSE
'''

if True: # significa (se), o true e false só funciona com inicial maiuscula
    print('verdadeiro.')  # 4 espaços coloca o codigo na mesma hierarquia anterior

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)

if False:
    print('verdadeiro.')
print('a minha expressão não é verdadeira.')  # essa expressão não depende do if

if True:
    print('verdadeiro.')  # (se isso for verdadeiro faça isso)
else:  # é o mesmo que (se não), usado para checar uma expressão. (se não for verdadeiro executa isso)
    print('não é verdadeiro.')

if False:  # se for verdadeiro exibe a expressão abaixo
    print('verdadeiro.')
elif True:  # se não for exibe a expressão abaixo
    print('agora é verdadeiro.')
else:
    print('não é verdadeiro.')

