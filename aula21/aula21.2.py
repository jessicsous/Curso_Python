'''
função range(start=0, stop, step=1)
start = inicio, step = quantas casas pular
'''

# usar laço 'for' em conjunto com a função 'range', para criar uma range de numero
for numero in range(0, 10, 1):
    print(numero)

# de trás pra frente
for numero in range(10, 0, -1):
    print(numero)

# multiplos de 8
for n in range(100):
    if n % 8 == 0:
        print(n)

# transformar uma letra para maiúscula usando o for

texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

# usando continue

texto1 = 'python'
nova_string1 = ''

for letra in texto1:
    if letra == 't':
        continue  # se n quiser q apareça a letra t
        nova_string1 = nova_string1 + letra.upper()
    elif letra == 'h':
        nova_string1 += letra.upper()
    else:
        nova_string1 += letra
print(nova_string1)

# usando break:

texto2 = 'python'
nova_string2 = ''

for letra in texto2:
    if letra == 't':
        nova_string2 = nova_string2 + letra.upper()
    elif letra == 'h':
        nova_string2 += letra.upper()
        break  # quebrar o laço
    else:
        nova_string2 += letra
print(nova_string2)




