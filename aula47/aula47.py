'''
Uso do try e except como condicional
'''

def convert_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = convert_numero(input('Digite um número: '))

    if numero is not None:
        print(numero * 5)
    else:
        print('isso não é número.')