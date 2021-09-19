'''
while / else
contadores
acumuladores
'''

contador = 1
acumulador = 1


while contador <= 10:
    print(contador, acumulador)

    if contador >= 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:  # quando o laço while passar a ser falso
    print('cheguei no else.')

