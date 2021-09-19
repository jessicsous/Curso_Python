
def bem_vindo():
    print('''
    bem vindo à calculadora
    ''')

def calculo():
    operacao = input('''
digite: 
+ para adição 
- para subtração
* para multiplicação
/ para divisão
''')

    numero_1 = int(input('digite o primeiro numero: '))
    numero_2 = int(input('digite o segundo numero: '))



    if operacao == '+':
        print('{} + {} = '. format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operacao == '-':
        print('{} + {} = '. format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operacao == '*':
        print('{} * {} = '. format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operacao == '/':
        def divisao(numero_1, numero_2):
            if numero_2 > 0:
                return numero_1 / numero_2
        divide = divisao(numero_1,numero_2)
        if divide:
            print(divide)
        else:
            print('erro')
        

    else:
        print('tente novamente.')


    novamente()

def novamente():
    calc_novamente = input('''
    Deseja fazer o calculo novamente?
    Por favor digite S para sim ou N para não''')

    if calc_novamente.upper() == 'S':
        calculo()

    elif calc_novamente.upper() == 'N':
        print('Até logo.')

    else:
        novamente()

bem_vindo()
calculo()



