'''
calculadora usando o while
'''

while True:
    print()
    num_1 = input('digite um número: ')
    num_2 = input('digite outro número: ')
    operador = input('digite um operador: ')
    sair = input('deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
    

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1+num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '/':
        print(num_1/num_2)
    elif operador == '*':
        print(num_1*num_2)
    else:
        print('operador inválido')