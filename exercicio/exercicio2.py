"""
faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
bom dia 0-11, boa tarde 12-17 e boa noite 18-23.
"""
horario = input('digite um horário(0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('digite um horário entre 0 e 23')
    else:
        if horario <= 11:
            print('bom dia!')
        elif horario <=17:
            print('boa tarde!')
        else:
            print('boa noite!')
else:
    print('por favor, digite um horário entre 0-23')