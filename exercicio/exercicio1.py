"""
faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é número inteiro.
"""
numero_inteiro = input('digite um numero inteiro: ')

if numero_inteiro.isdigit():  # checar se pode converter a string para um inteiro (tem só numero nessa string?)
    numero_inteiro = int(numero_inteiro)


    if  numero_inteiro % 2 == 0:
        print(f' {numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')

else:
    print('não é número inteiro.')

# checagem invertida

numero_interio = input('digite um número: ')

if not numero_inteiro.isdigit():
    print('isso não é um número inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é impar')
    else:
        print(f'{numero_inteiro} é par')




